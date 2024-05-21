import unittest
from parameterized import parameterized

from src.cron_fields import DayOfWeekField


class TestDayOfWeekField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(1, 8))),
        ("*/2", [1, 3, 5, 7]),
        ("1-5", [1, 2, 3, 4, 5]),
        ("2-6/2", [2, 4, 6]),
        ("1-2/1,3-7/2", [1, 2, 3, 5, 7]),
        ("mon-fri", [2, 3, 4, 5, 6]),
    ])
    def test_day_of_week_field(self, cron_string, expected_output):
        field = DayOfWeekField(cron_string)
        self.assertEqual(expected_output, field.parse())
