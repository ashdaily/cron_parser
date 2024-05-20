import unittest
from parameterized import parameterized

from src.cron_fields import HourField


class TestHourField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(24))),
        ("*/5", [0, 5, 10, 15, 20]),
        ("0-5", [0, 1, 2, 3, 4, 5]),
        ("0-12/2", [0, 2, 4, 6, 8, 10, 12]),
        ("13-23/4", [13, 17, 21]),
        ("0-12/2,13-23/4", [0, 2, 4, 6, 8, 10, 12, 13, 17, 21]),
        ("0-12/2,13-23/4,9", [0, 2, 4, 6, 8, 9, 10, 12, 13, 17, 21]),
        ("0-12/2,13-23/4,9,21-23", [0, 2, 4, 6, 8, 9, 10, 12, 13, 17, 21, 22, 23]),
    ])
    def test_hour_field(self, cron_string, expected_output):
        field = HourField(cron_string)
        self.assertEqual(expected_output, field.parse())
