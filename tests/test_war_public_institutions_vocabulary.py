from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class WarPublicInstitutionVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)
        cls.entries = {
            "soldier": ("AttackObligated«Know«MoveLifeThing»»", "core.roles.soldier", 6),
            "army": ("Group«AttackObligated«Know«MoveLifeThing»»»", "core.social.army", 7),
            "armor": ("PreventAttack««Know«MoveLifeThing»»SurfaceThing»", "core.artifacts.armor", 8),
            "shield": ("PreventAttack«UseThing»", "core.artifacts.shield", 4),
            "spear": ("HighLengthSharp«EndLife«UseThing»»", "core.artifacts.spear", 7),
            "bow": ("DistanceAttack«EndLife«UseThing»»", "core.artifacts.bow", 6),
            "arrow": ("SharpMoveAttackThing", "core.artifacts.arrow", 4),
            "prison": ("PreventMove«Know«MoveLifeThing»»«JoinedInThing»", "core.institutions.prison", 9),
            "prisoner": ("In«PreventMove«Know«MoveLifeThing»»«JoinedInThing»»«Know«MoveLifeThing»»", "core.roles.prisoner", 14),
            "judge": ("Authority«EvaluateObligatedGroup»«Know«MoveLifeThing»»", "core.roles.judge", 8),
            "polity/state": ("Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»", "core.institutions.polity", 9),
            "government": ("Authority«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»Group", "core.institutions.government", 11),
            "citizen/member of polity": ("Member«Authority«ObligatedPermittedRule»Group«Know«MoveLifeThing»»»«Know«MoveLifeThing»»", "core.roles.citizen", 14),
        }

    def test_war_public_words_are_old_names_not_base_roots(self):
        for gloss, (sign, _, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                surface = gloss.split("/", 1)[0].split()[0].capitalize()
                self.assertIsNone(self.language.entry(surface))
                matches = self.language.old_name_entries(sign)
                self.assertEqual(len(matches), 1)
                self.assertEqual(matches[0]["gloss"], gloss)

    def test_war_public_old_names_resolve_as_world_kinds(self):
        for gloss, (sign, concept_id, _) in self.entries.items():
            with self.subTest(gloss=gloss):
                result = self.parser.check(f"«{sign}» This.")
                self.assertTrue(result.valid, result.diagnostics)
                self.assertIn(
                    f"Concept({concept_id})",
                    result.ast.children[0].canonical(),
                )

    def test_war_public_historical_costs_are_recursive_and_frozen(self):
        for gloss, (sign, _, expected_cost) in self.entries.items():
            with self.subTest(gloss=gloss):
                self.assertEqual(
                    self.language.old_name_cost(sign),
                    expected_cost,
                )

    def test_market_is_persistent_institution_or_site_not_event_union(self):
        market = self.language.world_concepts["core.institutions.market"]
        self.assertIn("persistent trading site Entity", market["description"])
        self.assertIn("events are modeled separately", market["description"])

    def test_event_categories_are_not_faked_as_entity_kinds(self):
        self.assertNotIn("core.events.trial", self.language.world_concepts)
        self.assertNotIn("core.events.war", self.language.world_concepts)
        self.assertNotIn("core.events.battle", self.language.world_concepts)
        self.assertEqual(len(self.language.entries), 215)


if __name__ == "__main__":
    unittest.main()
