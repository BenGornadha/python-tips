from __future__ import annotations
import dataclasses

from advent_of_code2024.day4.directions import Direction


@dataclasses.dataclass(frozen=True)
class Position:
    row_index: int
    column_index: int

    def neighbour_at(self, direction: Direction) -> Position:
        return Position(row_index=self.row_index + direction.relative_x,
                        column_index=self.column_index + direction.relative_y)
