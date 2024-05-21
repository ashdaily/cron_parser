from abc import ABC, abstractmethod


class ExpandStrategy(ABC):
    @abstractmethod
    def expand(self, part, min_val, max_val):
        pass

    def validate(self, value, min_val, max_val):
        if not (min_val <= value <= max_val):
            raise ValueError(f"Value {value} out of range [{min_val}, {max_val}]")


class AsteriskStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        return set(range(min_val, max_val + 1))


class RangeStepStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        range_part, step = part.split('/')
        step = int(step)
        self.validate(step, min_val, max_val)

        result = set()
        if range_part == '*':
            result.update(list(range(min_val, max_val + 1, step)))
        elif '-' in range_part:
            start, end = map(int, range_part.split('-'))
            self.validate(start, min_val, max_val)
            self.validate(end, min_val, max_val)
            result.update(list(range(start, end + 1, step)))
        else:
            start = int(range_part)
            self.validate(start, min_val, max_val)
            result.update(list(range(start, max_val + 1, step)))
        return result


class RangeStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        start, end = map(int, part.split('-'))
        self.validate(start, min_val, max_val)
        self.validate(end, min_val, max_val)
        return set(range(start, end + 1))


class SingleValueStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        value = int(part)
        self.validate(value, min_val, max_val)
        return {value}


class LastDayOfMonthOrWeekStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        return {max_val}


class NearestWeekdayStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        day = int(part[:-1])
        self.validate(day, min_val, max_val)
        return {day}  # Simplification, nearest weekday logic can be complex


class NthDayOfWeekStrategy(ExpandStrategy):
    def expand(self, part, min_val, max_val):
        day, nth = map(int, part.split('#'))
        self.validate(day, min_val, max_val)
        return {(day, nth)}  # Simplification, calculating actual dates needs calendar logic
