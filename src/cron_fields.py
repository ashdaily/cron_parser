from logging_config import logger
from strategies import RangeStepStrategy, RangeStrategy, AsteriskStrategy, LastDayOfMonthStrategy, \
    NearestWeekdayStrategy, NthDayOfWeekStrategy, SingleValueStrategy


class CronField:
    def __init__(self, name, field_str, min_val, max_val):
        self.name = name
        self.field_str = field_str
        self.min_val = min_val
        self.max_val = max_val
        logger.debug(f"Initializing {name} field with string: {field_str}")

    def parse(self):
        logger.debug(f"Parsing cron_field of type {self.name} with value: {self.field_str}")
        _parse_result = self.expand(self.field_str)
        logger.debug(f"Parsed cron_field of type {self.name} {self.field_str} to {_parse_result}")
        return _parse_result

    def expand(self, field_str):
        result = set()
        parts = field_str.split(',')
        for part in parts:
            part = part.lower()
            if '/' in part:
                strategy = RangeStepStrategy()
            elif '-' in part:
                strategy = RangeStrategy()
            elif part == '*':
                strategy = AsteriskStrategy()
            elif part == 'l' and self.name == "day of month":
                strategy = LastDayOfMonthStrategy()
            elif part.endswith('w') and self.name == "day of month":
                strategy = NearestWeekdayStrategy()
            elif '#' in part and self.name == "day of week":
                strategy = NthDayOfWeekStrategy()
            else:
                strategy = SingleValueStrategy()

            result.update(strategy.expand(part, self.min_val, self.max_val))

        return sorted(result)


class MinuteField(CronField):
    def __init__(self, field_str):
        super().__init__("minute", field_str, 0, 59)


class HourField(CronField):
    def __init__(self, field_str):
        super().__init__("hour", field_str, 0, 23)


class DayOfMonthField(CronField):
    def __init__(self, field_str):
        super().__init__("day of month", field_str, 1, 31)


class MonthField(CronField):
    def __init__(self, field_str):
        super().__init__("month", field_str, 1, 12)


class DayOfWeekField(CronField):
    def __init__(self, field_str):
        super().__init__("day of week", field_str, 1, 7)


class CommandField:
    def __init__(self, command):
        self.command = command

    def parse(self):
        logger.debug(f"Parsing command field: {self.command}")
        return self.command
