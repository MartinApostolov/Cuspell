from __future__ import annotations

import unittest
from pathlib import Path

from cuspell.language import Language
from cuspell.model import Diagnostic
from cuspell.parser import Parser

ROOT = Path(__file__).resolve().parents[1]


class SpaceTimeCompletionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.language = Language.load(ROOT)
        cls.parser = Parser(cls.language)

    def valid(self, source: str):
        result = self.parser.check(source)
        self.assertTrue(result.valid, result.diagnostics)
        return result

    def test_extent_length_and_area(self):
        self.assertEqual(
            self.parser.parse_phrase("Extent This", expected_type="Region").type,
            "Region",
        )
        self.assertEqual(
            self.parser.parse_phrase("Length ThisPath", expected_type="Quantity").type,
            "Quantity:Length",
        )
        self.assertEqual(
            self.parser.parse_phrase("Area ThisRegion", expected_type="Quantity").type,
            "Quantity:Area",
        )

    def test_height_and_width_require_explicit_frame(self):
        self.valid(
            "?[f:CoordinateFrame] Equal Height This $f Width This $f."
        )
        result = self.parser.parse_phrase("Height This", expected_type="Quantity")
        self.assertIsInstance(result, Diagnostic)

    def test_offset_with_explicit_direction(self):
        node = self.parser.parse_phrase(
            "Offset Here Toward Self «LengthUnit» @",
            expected_type="Location",
        )
        self.assertNotIsInstance(node, Diagnostic, node)
        self.assertEqual(node.type, "Location")

    def test_spatial_field_helpers(self):
        edges = self.parser.parse_phrase(
            "Edge ThisRegion",
            expected_type="Collection:Region",
        )
        self.assertNotIsInstance(edges, Diagnostic, edges)
        self.valid("Through ThisPath ThisRegion.")

    def test_ball_and_tube_are_objective_regions(self):
        ball = self.parser.parse_phrase(
            "Ball Here «LengthUnit» @",
            expected_type="Region",
        )
        tube = self.parser.parse_phrase(
            "Tube ThisPath «LengthUnit» @",
            expected_type="Region",
        )
        self.assertNotIsInstance(ball, Diagnostic, ball)
        self.assertNotIsInstance(tube, Diagnostic, tube)

    def test_negative_radius_is_rejected(self):
        result = self.parser.parse_phrase(
            "Ball Here Opposite «LengthUnit» @",
            expected_type="Region",
        )
        self.assertIsInstance(result, Diagnostic)
        self.assertEqual(result.code, "ValueDomainMismatch")

    def test_end_event_is_typed_by_expected_result(self):
        endpoint = self.parser.parse_phrase("End ThisEvent", expected_type="TimePoint")
        self.assertNotIsInstance(endpoint, Diagnostic, endpoint)
        self.assertEqual(endpoint.type, "TimePoint")

        stop = self.parser.parse_phrase("End ThisEvent", expected_type="EventSpec")
        self.assertNotIsInstance(stop, Diagnostic, stop)
        self.assertEqual(stop.type, "EventSpec")

    def test_event_boundaries_return_time_points(self):
        begin = self.parser.parse_phrase("Begin ThisEvent", expected_type="TimePoint")
        end = self.parser.parse_phrase("End ThisEvent", expected_type="TimePoint")
        self.assertNotIsInstance(begin, Diagnostic, begin)
        self.assertNotIsInstance(end, Diagnostic, end)

    def test_interval_constructors(self):
        self.assertEqual(
            self.parser.parse_phrase(
                "Interval Begin ThisEvent End ThisEvent",
                expected_type="TimeInterval",
            ).type,
            "TimeInterval",
        )
        self.assertEqual(
            self.parser.parse_phrase(
                "IntervalFor Now «DurationUnit» @@",
                expected_type="TimeInterval",
            ).type,
            "TimeInterval",
        )

    def test_temporal_relations_cover_points_and_intervals(self):
        self.valid("Before Begin ThisEvent End ThisEvent.")
        self.valid("Before Begin ThisEvent End ThisEvent.")
        self.valid("During Now ThisInterval.")
        self.valid("Simultaneous Begin ThisEvent Begin ThatEvent.")
        self.valid("Overlap ThisInterval ThisInterval.")

    def test_always_and_compositional_never_require_explicit_interval(self):
        self.valid("Always Life This ThisInterval.")
        self.valid("Always Not Life This ThisInterval.")
        missing = self.parser.parse_phrase("Always Life This", expected_type="Proposition")
        self.assertIsInstance(missing, Diagnostic)

    def test_period_is_reciprocal_occurrence_rate(self):
        period = self.parser.parse_phrase(
            "Divide @ OccurrenceRate Move This Here",
            expected_type="Quantity:Time",
        )
        self.assertNotIsInstance(period, Diagnostic, period)
        self.assertEqual(
            self.language.quantity_dimension_vector(period.type),
            {"Time": 1},
        )

    def test_teleport_is_distinct_from_continuous_move(self):
        teleport = self.valid("!Teleport This Here.").ast.children[0].canonical()
        move = self.valid("!Move This Here.").ast.children[0].canonical()
        self.assertNotEqual(teleport, move)


if __name__ == "__main__":
    unittest.main()
