from __future__ import annotations
import dataclasses
from typing import List, Any

from advent_of_code2024.day4.directions import Direction, Directions, West
from advent_of_code2024.day4.letters import Letter, NoLetter
from advent_of_code2024.day4.positon import Position


# @dataclasses.dataclass(frozen=True)
# class Letter:
#     value: str
#
#
# @dataclasses.dataclass(frozen=True)
# class NoLetter:
#     pass


class OneRowOfLetters:

    def __init__(self, ):
        self._letters = []

    def append_letter(self, letter=Letter):
        self._letters.append(letter)

    def find_letter_at(self, column_index: int) -> Letter:
        if self._is_out_of_bounds(column_index=column_index):
            return NoLetter()
        return self._letters[column_index]

    def _is_out_of_bounds(self, column_index: int) -> bool:
        return column_index >= len(self._letters) or column_index < 0


class Neighbours:

    def __init__(self, a_letter: Letter) -> None:
        self.a_letter = a_letter
        self._result = {}

    def register_a_neighbour(self, letter: Letter, position: Position, direction: Direction) -> None:
        self._result[position, direction] = letter

    def __repr__(self) -> str:
        return f"{self._result}"

    def __eq__(self, other: Any) -> bool:
        return self._result == other


class SearchZone:

    def __init__(self, word_search: WordSearch) -> None:
        self.word_search = word_search

    def find_neighbours(self, position: Position) -> Neighbours:
        letter = self.word_search.find_letter_at(position=position)
        neighbours = Neighbours(a_letter=letter)
        for direction in Directions():
            neighbour_letter = self.word_search.find_neighbour_for(position=position, direction=direction)
            if neighbour_letter:
                neighbours.register_a_neighbour(letter=neighbour_letter,
                                                position=Position(row_index=position.row_index + direction.relative_x,
                                                                  column_index=position.column_index + direction.relative_y),
                                                direction=direction)
        return neighbours


class WordSearch:

    def __init__(self) -> None:
        self._rows: List[OneRowOfLetters] = []

    def register_row(self, a_row_of_letter: OneRowOfLetters) -> None:
        self._rows.append(a_row_of_letter)

    def find_letter_at(self, position: Position) -> Letter | NoLetter:
        if self._is_out_of_bounds(position.row_index):
            return NoLetter()
        return self._rows[position.row_index].find_letter_at(column_index=position.column_index)

    def find_neighbour_for(self, position: Position, direction: Direction) -> Letter | NoLetter:
        row_index = position.neighbour_at(direction=direction).row_index
        if self._is_out_of_bounds(row_index):
            return NoLetter()
        return self._rows[row_index].find_letter_at(
            column_index=position.neighbour_at(direction=direction).column_index)

    def _is_out_of_bounds(self, row_index: int) -> bool:
        return row_index < 0 or row_index >= len(self._rows)
