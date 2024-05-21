from cron_fields import (
    MinuteField, HourField, DayOfMonthField,
    MonthField, DayOfWeekField, CommandField, YearField)


class CronFieldFactory:
    @staticmethod
    def create_field(name, field_str):
        if name == "minute":
            return MinuteField(field_str)
        elif name == "hour":
            return HourField(field_str)
        elif name == "day of month":
            return DayOfMonthField(field_str)
        elif name == "month":
            return MonthField(field_str)
        elif name == "day of week":
            return DayOfWeekField(field_str)
        elif name == "year":
            return YearField(field_str)
        elif name == "command":
            return CommandField(field_str)
        else:
            raise ValueError(f"Unknown field name: {name}")
