from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class OldNewNameSystemTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._tmp = tempfile.TemporaryDirectory()
        cls.root = Path(cls._tmp.name)
        shutil.copytree(ROOT / "language", cls.root / "language")
        shutil.copytree(ROOT / "world", cls.root / "world")

        concepts = {
            "version": "0.1",
            "concepts": [
                {
                    "id": "test.kind.life_hand.a",
                    "semantic_type": "Kind",
                    "description": "same illustrative description"
                },
                {
                    "id": "test.kind.life_hand.b",
                    "semantic_type": "Kind",
                    "description": "same illustrative description"
                }
            ]
        }
        old_names = {
            "version": "0.1",
            "language": "Cuspell",
            "entries": [
                {
                    "id": "old.test.life_hand.a",
                    "sign": "LifeHand",
                    "established_before_magic": True,
                    "name_units": [{"root": "Life"}, {"root": "Hand"}],
                    "meaning": {
                        "kind": "concept",
                        "concept_id": "test.kind.life_hand.a",
                        "type": "Kind"
                    }
                },
                {
                    "id": "old.test.life_hand.b",
                    "sign": "Life!Hand",
                    "established_before_magic": True,
                    "name_units": [{"root": "Life"}, {"root": "Hand"}],
                    "meaning": {
                        "kind": "concept",
                        "concept_id": "test.kind.life_hand.b",
                        "type": "Kind"
                    }
                },
                {
                    "id": "old.test.life_move",
                    "sign": "LifeMove",
                    "established_before_magic": True,
                    "name_units": [{"root": "Life"}, {"root": "Move"}],
                    "meaning": {
                        "kind": "expression",
                        "type": "EventSpec",
                        "source": "Move Self Here"
                    }
                }
            ]
        }
        new_names = {
            "version": "0.1",
            "entries": [
                {
                    "id": "new.test.yona",
                    "sign": "Yona",
                    "referent_id": "test.entity.yona",
                    "referent_type": "Entity"
                },
                {
                    "id": "new.test.yona.life_hand",
                    "sign": "Yona's«LifeHand»",
                    "referent_id": "test.entity.yona.life_hand",
                    "referent_type": "Entity"
                }
            ]
        }

        (cls.root / "world" / "core" / "concepts.json").write_text(
            json.dumps(concepts, indent=2) + "\n",
            encoding="utf-8",
        )
        (cls.root / "language" / "names" / "old_names.json").write_text(
            json.dumps(old_names, indent=2) + "\n",
            encoding="utf-8",
        )
        (cls.root / "world" / "core" / "new_names.json").write_text(
            json.dumps(new_names, indent=2) + "\n",
            encoding="utf-8",
        )

        cls.language = Language.load(cls.root)
        cls.parser = Parser(cls.language)

    @classmethod
    def tearDownClass(cls):
        cls._tmp.cleanup()

    def test_name_registry_fixture_is_valid_language_data(self):
        self.assertEqual(validate_language_data(self.root), [])

    def test_nested_quoted_name_is_one_exact_sign(self):
        node = self.parser.parse_phrase(
            "«Yona's«LifeHand»»",
            expected_type="Sign",
        )
        self.assertNotIsInstance(node, Diagnostic)
        self.assertEqual(node.canonical(), "«Yona's«LifeHand»»")

    def test_punctuation_inside_name_is_literal_not_sentence_mood(self):
        node = self.parser.parse_phrase("«Life!Hand»", expected_type="Sign")
        self.assertNotIsInstance(node, Diagnostic)
        self.assertEqual(node.canonical(), "«Life!Hand»")

    def test_old_name_resolves_to_world_kind(self):
        node = self.parser.parse_phrase("«LifeHand»", expected_type="Kind")
        self.assertNotIsInstance(node, Diagnostic)
        self.assertEqual(node.canonical(), "Concept(test.kind.life_hand.a)")

    def test_old_name_kind_can_be_used_predicatively(self):
        result = self.parser.check("«LifeHand» This.")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "InstanceOf(This,Concept(test.kind.life_hand.a))",
        )

    def test_same_description_different_old_names_can_name_distinct_concepts(self):
        a = self.parser.check("«LifeHand» This.")
        b = self.parser.check("«Life!Hand» This.")
        self.assertTrue(a.valid, a.diagnostics)
        self.assertTrue(b.valid, b.diagnostics)
        self.assertNotEqual(
            a.ast.children[0].canonical(),
            b.ast.children[0].canonical(),
        )

    def test_old_name_spell_expands_semantically_but_keeps_name_mana_cost(self):
        result = self.parser.check("«LifeMove»!")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertEqual(
            result.ast.children[0].canonical(),
            "Move(theme=Self,goal=Here)",
        )
        self.assertEqual(result.mana, 2)

    def test_unregistered_quoted_sign_is_not_a_magical_macro(self):
        result = self.parser.check("«MoveLife»!")
        self.assertFalse(result.valid)

    def test_new_name_reference_remains_contextual_name_reference(self):
        result = self.parser.check("Life Name «Yona».")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn("Name(", result.ast.children[0].canonical())

    def test_nested_new_name_reference_is_supported(self):
        result = self.parser.check("Life Name «Yona's«LifeHand»».")
        self.assertTrue(result.valid, result.diagnostics)
        self.assertIn("Yona's«LifeHand»", result.ast.children[0].canonical())

    def test_new_name_reference_does_not_gain_old_name_execution(self):
        result = self.parser.check("«Yona»!")
        self.assertFalse(result.valid)

    def test_old_name_punctuation_does_not_change_mana_units(self):
        result = self.parser.check("«Life!Hand» This.")
        self.assertTrue(result.valid, result.diagnostics)
        # Two historical name units plus This.
        self.assertEqual(result.mana, 3)


if __name__ == "__main__":
    unittest.main()
