import unittest
from parameterized import parameterized

from src.cron_fields import DayOfMonthField


class TestDayOfMonthField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(1, 32))),
        ("*/5", [1, 6, 11, 16, 21, 26, 31]),
        ("1-5", [1, 2, 3, 4, 5]),
        ("1-12/2", [1, 3, 5, 7, 9, 11]),
        ("25-31/2", [25, 27, 29, 31]),
        ("1-5/1,25-30/2", [1, 2, 3, 4, 5, 25, 27, 29]),
        ("1-5/1,25-30/2,10", [1, 2, 3, 4, 5, 10, 25, 27, 29]),
        ("1-5/1,25-30/2,10,12-16", [1, 2, 3, 4, 5, 10, 12, 13, 14, 15, 16, 25, 27, 29]),
        ("L", [31]),
        ("5W", [5])
    ])
    def test_day_of_month_field(self, cron_string, expected_output):
        field = DayOfMonthField(cron_string)
        self.assertEqual(expected_output, field.parse())
