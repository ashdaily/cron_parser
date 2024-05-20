import unittest
from parameterized import parameterized

from src.cron_parser import CronParser


class TestCronParser(unittest.TestCase):
    @parameterized.expand([
        ("*/15 * * * * /path/to/command",
         [list(range(0, 60, 15)), list(range(24)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)),
          "/path/to/command"]),
        ("*/5 * * * * /path/to/command",
         [list(range(0, 60, 5)), list(range(24)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)),
          "/path/to/command"]),
        ("15 * * * * /path/to/command",
         [[15], list(range(24)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("0 0 * * * /path/to/command",
         [[0], [0], list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("30 14 * * * /path/to/command",
         [[30], [14], list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("0 3 * * 1 /path/to/command",
         [[0], [3], list(range(1, 32)), list(range(1, 13)), [1], "/path/to/command"]),
        ("0 9 * * 1-5 /path/to/command",
         [[0], [9], list(range(1, 32)), list(range(1, 13)), [1, 2, 3, 4, 5], "/path/to/command"]),
        ("*/10 9-17 * * 1-5 /path/to/command",
         [list(range(0, 60, 10)), list(range(9, 18)), list(range(1, 32)), list(range(1, 13)), [1, 2, 3, 4, 5],
          "/path/to/command"]),
        ("0 0 1,15 * * /path/to/command",
         [[0], [0], [1, 15], list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("0 0 L * * /path/to/command",
         [[0], [0], [31], list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("0 9 15W * * /path/to/command",
         [[0], [9], [15], list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
        ("0 8 * * 5#2 /path/to/command",
         [[0], [8], list(range(1, 32)), list(range(1, 13)), [(5, 2)], "/path/to/command"]),
        ("0 0 1 1 * /path/to/command",
         [[0], [0], [1], [1], list(range(1, 8)), "/path/to/command"]),
        ("*/5 * * * 1-5 /path/to/command",
         [list(range(0, 60, 5)), list(range(24)), list(range(1, 32)), list(range(1, 13)), [1, 2, 3, 4, 5],
          "/path/to/command"]),
        ("0 */6 * * * /path/to/command",
         [[0], list(range(0, 24, 6)), list(range(1, 32)), list(range(1, 13)), list(range(1, 8)), "/path/to/command"]),
    ])
    def test_special_cases(self, cron_str, expected):
        parser = CronParser(cron_str)
        parsed = parser.parse()
        self.assertEqual(parsed["minute"], expected[0])
        self.assertEqual(parsed["hour"], expected[1])
        self.assertEqual(parsed["day of month"], expected[2])
        self.assertEqual(parsed["month"], expected[3])
        self.assertEqual(parsed["day of week"], expected[4])
        self.assertEqual(parsed["command"], expected[5])
