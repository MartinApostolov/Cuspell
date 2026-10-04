from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from cuspell.data_validation import validate_language_data
from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ParameterizedOldNameTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_give_old_name_expands_to_frozen_parameterized_event(self):
        self.assertIsNone(self.language.entry("Give"))
        parameterized = [
            entry
            for entries in self.language.old_names_by_sign.values()
            for entry in entries
            if entry.get("meaning", {}).get("kind") == "expression"
            and entry.get("meaning", {}).get("parameters")
        ]
        self.assertEqual([entry["id"] for entry in parameterized], ["old.core.give"])

        named = self.parser.check("«TransferHave» Self This You!")
        direct = self.parser.check(
            "Concurrent EndHave Self This BeginHave You This!"
        )
        self.assertTrue(named.valid, named.diagnostics)
        self.assertTrue(direct.valid, direct.diagnostics)
        self.assertEqual(
            named.ast.children[0].canonical(),
            direct.ast.children[0].canonical(),
        )

    def test_give_old_name_has_frozen_historical_cost(self):
        self.assertEqual(self.language.old_name_cost("TransferHave"), 2)
        self.assertEqual(
            self.parser.mana_cost("«TransferHave» Self This You!"),
            5,
        )
        self.assertEqual(
            self.parser.mana_cost(
                "Concurrent EndHave Self This BeginHave You This!"
            ),
            9,
        )

    def test_parameterized_old_name_arguments_are_typed(self):
        result = self.parser.check("«TransferHave» Here This You!")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(d.code == "TypeMismatch" for d in result.diagnostics),
            result.diagnostics,
        )

    def test_parameterized_old_name_parameters_cannot_be_omitted(self):
        result = self.parser.check("«TransferHave» Self _ You!")
        self.assertFalse(result.valid)
        self.assertTrue(
            any(d.code == "InvalidOmission" for d in result.diagnostics),
            result.diagnostics,
        )

    def test_unregistered_new_name_never_becomes_callable_macro(self):
        result = self.parser.check("«TransferHaveLater» Self This You!")
        self.assertFalse(result.valid)

    def test_caller_binder_can_be_passed_as_explicit_argument(self):
        result = self.parser.check(
            "x:Entity Happen «TransferHave» $x This You?"
        )
        self.assertTrue(result.valid, result.diagnostics)

    def test_parameterized_old_name_rejects_extra_argument(self):
        result = self.parser.check("«TransferHave» Self This You That!")
        self.assertFalse(result.valid)

    def test_registry_validation_rejects_invalid_frozen_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "language", root / "language")
            shutil.copytree(ROOT / "world", root / "world")
            old_path = root / "language" / "names" / "old_names.json"
            data = json.loads(old_path.read_text(encoding="utf-8"))
            give = next(
                entry for entry in data["entries"]
                if entry["id"] == "old.core.give"
            )
            give["meaning"]["source"] = (
                "Concurrent EndHave $giver $theme "
                "BeginHave $recipient $hidden"
            )
            old_path.write_text(
                json.dumps(data, indent=2) + "\n",
                encoding="utf-8",
            )

            errors = validate_language_data(root)
            self.assertTrue(
                any(
                    "old.core.give: invalid frozen expression: FreeVariable"
                    in error
                    for error in errors
                ),
                errors,
            )

    def test_registry_validation_rejects_unused_parameter(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "language", root / "language")
            shutil.copytree(ROOT / "world", root / "world")
            old_path = root / "language" / "names" / "old_names.json"
            data = json.loads(old_path.read_text(encoding="utf-8"))
            give = next(
                entry for entry in data["entries"]
                if entry["id"] == "old.core.give"
            )
            give["meaning"]["parameters"].append(
                {"name": "witness", "type": "Entity"}
            )
            old_path.write_text(
                json.dumps(data, indent=2) + "\n",
                encoding="utf-8",
            )

            errors = validate_language_data(root)
            self.assertIn(
                "old.core.give: Old Name parameter 'witness' is unused by "
                "the frozen expression",
                errors,
            )

    def test_registry_validation_rejects_hidden_parameter_defaults(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            shutil.copytree(ROOT / "language", root / "language")
            shutil.copytree(ROOT / "world", root / "world")
            old_path = root / "language" / "names" / "old_names.json"
            data = json.loads(old_path.read_text(encoding="utf-8"))
            give = next(
                entry for entry in data["entries"]
                if entry["id"] == "old.core.give"
            )
            give["meaning"]["parameters"][0]["default"] = "Self"
            old_path.write_text(
                json.dumps(data, indent=2) + "\n",
                encoding="utf-8",
            )

            errors = validate_language_data(root)
            self.assertTrue(
                any(
                    "old.core.give: Old Name parameter has unsupported fields"
                    in error
                    and "default" in error
                    for error in errors
                ),
                errors,
            )

    def test_template_cannot_capture_caller_binder(self):
        injected = {
            "id": "old.test.capture",
            "sign": "CaptureTest",
            "gloss": "capture-test",
            "established_before_magic": True,
            "name_units": [{"root": "Cause"}],
            "meaning": {
                "kind": "expression",
                "type": "EventSpec",
                "parameters": [
                    {"name": "target", "type": "Entity"},
                ],
                "source": "Cause $hidden EndLife $target",
            },
        }
        self.language.old_names_by_sign.setdefault("CaptureTest", []).append(injected)
        self.language.old_names_by_id["old.test.capture"] = injected
        try:
            result = self.parser.check(
                "? hidden:Entity Happen «CaptureTest» This."
            )
            self.assertFalse(result.valid)
            self.assertTrue(
                any(d.code == "InvalidOldName" for d in result.diagnostics),
                result.diagnostics,
            )
        finally:
            self.language.old_names_by_sign["CaptureTest"].remove(injected)
            if not self.language.old_names_by_sign["CaptureTest"]:
                del self.language.old_names_by_sign["CaptureTest"]
            del self.language.old_names_by_id["old.test.capture"]


if __name__ == "__main__":
    unittest.main()
