from __future__ import annotations

import dataclasses
from enum import auto, Enum
from typing import List


def read_input(filename: str):
    input_file = open(filename, "r")
    res = []
    for a_line in input_file:
        levels = a_line.split(" ")
        levels = [int(level.replace("\n", "")) for level in levels]
        res.append(levels)
    return res


@dataclasses.dataclass(frozen=True)
class Level:
    value: int

    def __sub__(self, other):
        return self.value - other.value

    def __gt__(self, other: Level):
        return self.value > other.value

    def __lt__(self, other: Level):
        return self.value < other.value

    def __repr__(self):
        return f"{self.value}"


class Levels:
    def __init__(self):
        self._levels: List[Level] = []

    def append(self, a_level: Level):
        self._levels.append(a_level)

    def __getitem__(self, index):
        if index < len(self._levels):
            return self._levels[index]

    def __iter__(self):
        return iter(self._levels)

    def __len__(self):
        return len(self._levels)

    def __repr__(self):
        return ",".join([str(level) for level in self._levels])


class Direction(str, Enum):
    UP = auto()
    DOWN = auto()


class Report:
    def __init__(self):
        self._levels = Levels()
        self._direction = Direction.UP
        self._is_safe = True

    def add_level(self, level: Level):
        self._levels.append(level)

    def _find_direction(self):
        if self._levels[0] < self._levels[1]:
            self._direction = Direction.UP
            return
        if self._levels[0] == self._levels[1]:
            self._is_safe = False
            return
        self._direction = Direction.DOWN

    def is_safe(self):
        self._find_direction()
        if self._is_safe is False:
            return False
        for current_index, level in enumerate(self._levels):
            next_index = current_index + 1
            if self._no_next_value(next_index=next_index):
                break
            if self._direction == Direction.UP:
                if self._increasing_distance_is_acceptable(level=level, next_index=next_index):
                    continue
                return False
            if self._decreasing_distance_is_acceptable(level, next_index):
                continue
            return False
        return True

    def _decreasing_distance_is_acceptable(self, level: Level, next_index: int) -> bool:
        return 1 <= level - self._levels[next_index] <= 3

    def _increasing_distance_is_acceptable(self, level: Level, next_index: int) -> bool:
        return 1 <= self._levels[next_index] - level <= 3

    def _no_next_value(self, next_index: int) -> bool:
        return next_index == len(self._levels)

    def __repr__(self):
        return repr(self._levels)


if __name__ == '__main__':
    reports = read_input(filename="input.txt")

    count_safe_report = 0
    for report in reports:
        a_report = Report()
        for a_level in report:
            a_report.add_level(level=Level(value=a_level))
        count_safe_report += a_report.is_safe()
        # break
    print(count_safe_report)
