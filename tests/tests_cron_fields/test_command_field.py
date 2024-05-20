import unittest

from src.cron_fields import CommandField


class TestCommandField(unittest.TestCase):
    def test_command_field(self):
        field = CommandField("/usr/bin/find")
        self.assertEqual("/usr/bin/find", field.parse())
