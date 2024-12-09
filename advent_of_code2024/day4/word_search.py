from __future__ import annotations
import dataclasses
from typing import List

from advent_of_code2024.day4.directions import Direction, Directions


@dataclasses.dataclass(frozen=True)
class Letter:
    value: str


@dataclasses.dataclass(frozen=True)
class NoLetter:
    pass


class OneRowOfLetters:

    def __init__(self, size_row=140):
        self._letters = []
        self._size_row = size_row

    def append_letter(self, letter=Letter):
        self._letters.append(letter)

    def find_letter_at(self, column_index: int) -> Letter | NoLetter:
        if self._is_out_of_bounds(column_index=column_index):
            return NoLetter()
        return self._letters[column_index]

    def _is_out_of_bounds(self, column_index: int) -> bool:
        return self._size_row < column_index and column_index >= 0


class SearchZone:

    def __init__(self, word_search: WordSearch, ):
        self.word_search = word_search

    def find_neighbours(self, letter: Letter, row_index: int, column_index: int):
        all_neighbours_letter = []
        for direction in Directions():
            all_neighbours_letter.append((letter, self.word_search.find_neighbour_for(row_index=row_index,
                                                                                      column_index=column_index,
                                                                                      direction=direction), direction))


class WordSearch:

    def __init__(self):
        self._rows: List[OneRowOfLetters] = []

    def register_row(self, a_row_of_letter: OneRowOfLetters) -> None:
        self._rows.append(a_row_of_letter)

    def find_letter_at(self, row_index: int, column_index: int) -> Letter | NoLetter:
        if self._is_out_of_bounds(row_index):
            return NoLetter()
        return self._rows[row_index].find_letter_at(column_index=column_index)

    def find_neighbour_for(self, row_index: int, column_index: int, direction: Direction) -> Letter | NoLetter:
        return self._rows[row_index + direction.relative_x].find_letter_at(
            column_index=column_index + direction.relative_y)

    def _is_out_of_bounds(self, row_index: int) -> bool:
        return row_index < 0 or row_index > len(self._rows)
