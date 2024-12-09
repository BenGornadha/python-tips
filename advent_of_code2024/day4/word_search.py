from __future__ import annotations
import dataclasses
from typing import List

from advent_of_code2024.day4.directions import Direction, Directions
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

    def __init__(self, size_row=1):
        self._letters = []
        self._size_row = size_row

    def append_letter(self, letter=Letter):
        self._letters.append(letter)

    def find_letter_at(self, column_index: int) -> Letter:
        if self._is_out_of_bounds(column_index=column_index):
            return NoLetter()
        return self._letters[column_index]

    def _is_out_of_bounds(self, column_index: int) -> bool:
        return self._size_row < column_index and column_index >= 0


class Neighbours:

    def __init__(self, a_letter):
        self.a_letter = a_letter
        self._result = {0: {}}

    def register_a_neighbour(self, distance_from_origin, letter, position):
        self._result[distance_from_origin][letter] = position


class SearchZone:

    def __init__(self, word_search: WordSearch):
        self.word_search = word_search

    def find_neighbours(self, position: Position):
        all_neighbours_letter = []
        letter = self.word_search.find_letter_at(position=position)
        for direction in Directions():
            all_neighbours_letter.append((letter,
                                          self.word_search.find_neighbour_for(position=position,
                                                                              direction=direction),
                                          direction))
        return all_neighbours_letter
        # if letter.next not in [neighbour[1] for neighbour in all_neighbours_letter]:
        #     return 0


class WordSearch:

    def __init__(self):
        self._rows: List[OneRowOfLetters] = []

    def register_row(self, a_row_of_letter: OneRowOfLetters) -> None:
        self._rows.append(a_row_of_letter)

    def find_letter_at(self, position: Position) -> Letter | NoLetter:
        if self._is_out_of_bounds(position.row_index):
            return NoLetter()
        return self._rows[position.row_index].find_letter_at(column_index=position.column_index)

    def find_neighbour_for(self, position: Position, direction: Direction) -> Letter | NoLetter:
        return self._rows[position.neighbour_at(direction=direction).row_index].find_letter_at(
            column_index=position.neighbour_at(direction=direction).column_index)

    def _is_out_of_bounds(self, row_index: int) -> bool:
        return row_index < 0 or row_index > len(self._rows)
