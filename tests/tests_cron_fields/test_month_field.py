import unittest
from parameterized import parameterized

from src.cron_fields import MonthField


class TestMonthField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(1, 13))),
        ("*/5", [1, 6, 11]),
        ("1-5", [1, 2, 3, 4, 5]),
        ("1-12/2", [1, 3, 5, 7, 9, 11]),
        ("1-3/1,6-12/2", [1, 2, 3, 6, 8, 10, 12]),
    ])
    def test_month_field(self, cron_string, expected_output):
        field = MonthField(cron_string)
        self.assertEqual(expected_output, field.parse())
