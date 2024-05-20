import unittest
from parameterized import parameterized

from src.cron_fields import MinuteField


class TestMinuteField(unittest.TestCase):
    @parameterized.expand([
        ("*", list(range(0, 60))),
        ("*/15", [0, 15, 30, 45]),
        ("*/5", list(range(0, 60, 5))),
        ("0-5", list(range(6))),
        ("0-15/5", list(range(0, 16, 5))),
        ("1-15/2", list(range(1, 16, 2))),
        ("0-59/5,1-15/2", sorted(set(list(range(0, 60, 5)) + list(range(1, 15, 2))))),
    ])
    def test_minute_field(self, cron_string, expected_output):
        field = MinuteField(cron_string)
        self.assertEqual(expected_output, field.parse())

    @parameterized.expand([
        ("60", ValueError),
        ("-1", ValueError),
        ("*/70", ValueError),
        ("*/-5", ValueError),
        ("0-70/5", ValueError),
        ("1-80/2", ValueError),
    ])
    def test_minute_field_invalid(self, cron_str, expected_exception):
        field = MinuteField(cron_str)
        with self.assertRaises(expected_exception):
            field.parse()
