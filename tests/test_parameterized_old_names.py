from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class ParameterizedOldNameTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def test_give_old_name_expands_to_frozen_parameterized_event(self):
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
        self.assertLess(
            self.parser.mana_cost("«TransferHave» Self This You!"),
            self.parser.mana_cost(
                "Concurrent EndHave Self This BeginHave You This!"
            ),
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
