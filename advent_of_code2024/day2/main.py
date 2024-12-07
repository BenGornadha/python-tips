from __future__ import annotations

import copy
import dataclasses
from enum import auto, Enum


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

    def __lt__(self, other: Level):
        return self.value < other.value

    def __repr__(self):
        return f"{self.value}"


class Levels:
    def __init__(self):
        self._levels = []

    def append(self, a_level: Level):
        self._levels.append(a_level)

    def copy(self) ->  Levels:
        return copy.deepcopy(self)

    def __getitem__(self, index):
        if index < len(self._levels):
            return self._levels[index]

    def __delitem__(self, key) -> None:
        del self._levels[key]

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

    def _find_direction(self, levels: Levels):
        if levels[0] < levels[1]:
            self._direction = Direction.UP
            return
        self._direction = Direction.DOWN

    def is_safe(self):
        return self._is_safe_strictly(levels=self._levels) or self.is_safe_with_removing()

    def _is_safe_strictly(self, levels : Levels):
        self._find_direction(levels=levels)
        if self._is_safe is False:
            return False
        for i, level in enumerate(levels):
            next_index = i + 1
            if next_index == len(levels):
                break
            if self._direction == Direction.UP:
                if 1 <= levels[next_index] - level <= 3:
                    continue
                return False
            if 1 <= level - levels[next_index] <= 3:
                continue
            return False
        return True

    def is_safe_with_removing(self):
        nb_levels = len(self._levels)
        for index_to_remove in range(nb_levels):
            potential_report = self._levels.copy()
            del potential_report[index_to_remove]
            if self._is_safe_strictly(levels=potential_report):
                return True
        return False

    def __repr__(self):
        return repr(self._levels)



if __name__ == '__main__':
    reports = read_input(filename="input.txt")
    print(reports)

    count_safe_report = 0
    for report in reports:
        a_report = Report()
        for a_level in report:
            a_report.add_level(level=Level(value=a_level))
        if a_report.is_safe():
            print("Found this safe: ", a_report)
            count_safe_report += 1
        # break
    print(count_safe_report)
