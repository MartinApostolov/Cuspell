from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class CraftTransportVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "knife": ("LowLength«Sharp«EndJoinedMatter«UseThing»»»", "core.artifacts.knife", 8),
            "axe": ("«MatterPart«HighExtentHard«ChangeExtentLifeMatter»»»«EndJoinedMatter«UseThing»»", "core.artifacts.axe", 14),
            "saw": ("Repeat«EndJoinedMatter«UseThing»»", "core.artifacts.saw", 6),
            "pot/cooking vessel": ("Heat«InThing»", "core.artifacts.pot", 3),
            "needle": ("SharpBeginJoined«UseThing»", "core.artifacts.needle", 5),
            "wheel": ("RotatePartThing", "core.artifacts.wheel", 3),
            "cart/wagon": ("Have«RotatePartThing»MoveThing", "core.transport.cart", 6),
            "plow": ("Change««ChangeExtentLifeMatter»HaveMatter»«UseThing»", "core.artifacts.plow", 9),
            "loom": ("BeginExist«JoinedLowExtentMatter»«UseThing»", "core.artifacts.loom", 8),
            "furnace/kiln": ("HighHeat«InThing»", "core.artifacts.furnace", 4),
            "anvil": ("HardChange«HeatChangeHardMatter»«UseThing»", "core.artifacts.anvil", 8),
            "sail": ("«Move«LifeGasMatter»Thing»Part«MoveInLiquidThing»", "core.transport.sail", 10),
            "oar": ("Move«MoveInLiquidThing»«UseThing»", "core.transport.oar", 7),
            "anchor": ("PreventMove«MoveInLiquidThing»Thing", "core.transport.anchor", 7),
            "port/harbor facility": ("Have«MoveInLiquidThing»Region", "core.transport.port", 6),
            "building/constructed structure": ("JoinedInThing", "core.built_environment.building", 3),
            "roof": ("Prevent«Fall«LiquidMatter»Thing»Part«JoinedInThing»", "core.built_environment.roof", 9),
            "room": ("In«JoinedInThing»Region", "core.built_environment.room", 5),
            "floor": ("MoveSurfacePart«JoinedInThing»", "core.built_environment.floor", 6),
            "workshop": ("Use«UseThing»«JoinedInThing»", "core.built_environment.workshop", 6),
            "mill": ("Change««BeginLifePart«ChangeExtentLifeMatter»»«TransferLifeMatter»»«JoinedInThing»", "core.built_environment.mill", 14),
            "fortification": ("PreventAttack«JoinedInThing»", "core.built_environment.fortification", 5),
        }

    def test_craft_transport_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                surface = gloss.split("/", 1)[0].split()[0].capitalize()
                self.assertIsNone(self.language.entry(surface))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_craft_transport_old_names_resolve_as_world_kinds(self):
        for gloss, (sign, concept_id, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                result = self.parser.check(f"«{sign}» This.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_craft_transport_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(
                    self.language.old_name_cost(sign),
                    expected_cost,
                )

    def test_wheel_history_uses_productive_rotation_without_making_wheel_a_root(self):
        self.assertIsNotNone(self.language.entry("Rotate"))
        self.assertIsNone(self.language.entry("Wheel"))
        self.assertEqual(self.language.old_name_cost("RotatePartThing"), 3)

    def test_rotate_is_explicit_rigid_axis_motion_not_move(self):
        rotate = self.parser.check("Rotate This Here Toward This @!")
        move = self.parser.check("Move This Here!")
        self.assertTrue(rotate.valid, rotate.diagnostics)
        self.assertTrue(move.valid, move.diagnostics)
        rotate_node = rotate.ast.children[0]
        move_node = move.ast.children[0]
        self.assertEqual(rotate_node.type, "EventSpec")
        self.assertEqual(move_node.type, "EventSpec")
        self.assertNotEqual(rotate_node.canonical(), move_node.canonical())

    def test_batch_does_not_fake_manufacturing_or_vehicle_manner_roots(self):
        for surface in ("Build", "Make", "Cook", "Weave", "Sew", "Drive", "Ride"):
            with self.subTest(surface=surface):
                self.assertIsNone(self.language.entry(surface))
        self.assertEqual(len(self.language.entries), 216)


if __name__ == "__main__":
    unittest.main()
