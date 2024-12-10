from __future__ import annotations

import re
from abc import ABC, abstractmethod
from typing import List



class XMASFinder(ABC):

    @abstractmethod
    def count_xmas(self):
        raise NotImplemented

    def register_a_word_search_grid(self, word_search_grid: List[str]) -> None:
        self._word_search = word_search_grid
        self._size_of_a_row = len(self._word_search[0])
        self._nb_rows = len(self._word_search)


class HorizontalXMAS(XMASFinder):

    def __init__(self, word_to_search="XMAS"):
        self._word_search = []
        self._word_to_search = word_to_search

    def count_xmas(self) -> int:
        count = 0
        for row in self._word_search:
            count += self._find_occurrences_from(a_string=row)
        return count

    def _find_occurrences_from(self, a_string: str):
        return len(re.findall(self._word_to_search, a_string)) + len(re.findall(self._word_to_search[::-1], a_string))


class VerticalXMAS(XMASFinder):

    def __init__(self, word_to_search="XMAS"):
        self._word_search = []
        self._word_to_search = word_to_search
        self._size_of_a_row = 0
        self._nb_rows = 0

    def count_xmas(self) -> int:
        count = 0
        for col_index in range(self._size_of_a_row):
            all_letters = self._get_all_letters_at(col_index=col_index)
            count += self._find_occurrences_from(a_string=all_letters)
        return count

    def _get_all_letters_at(self, col_index: int) -> str:
        all_letters = ""
        for row_index in range(self._nb_rows):
            all_letters += self._word_search[row_index][col_index]
        return all_letters

    def _find_occurrences_from(self, a_string: str):
        return len(re.findall(self._word_to_search, a_string)) + len(re.findall(self._word_to_search[::-1], a_string))


class DiagonalXMAS(XMASFinder):

    def __init__(self, word_to_search="XMAS"):
        self._word_search = []
        self._word_to_search = word_to_search
        self._nb_rows = 0

    def count_xmas(self) -> int:
        count = 0
        for index_row, row in enumerate(self._word_search):
            for index_column, letter in enumerate(row):
                count += self._right_diagonal(index_column, index_row, letter)
                count += self._left_diagonal(index_column, index_row, letter)
                count += self._upper_right_diagonal(index_column, index_row, letter)
                count += self._upper_left_diagonal(index_column, index_row, letter)

        return count

    def _right_diagonal(self, index_column: int, index_row: int, letter: str):
        diagonal = letter
        try:
            diagonal += self._word_search[index_row + 1][index_column + 1]
            diagonal += self._word_search[index_row + 2][index_column + 2]
            diagonal += self._word_search[index_row + 3][index_column + 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _left_diagonal(self, index_column: int, index_row: int, letter: str):
        diagonal = letter
        if self._out_of_bounds(index=index_column):
            return 0
        try:
            diagonal += self._word_search[index_row + 1][index_column - 1]
            diagonal += self._word_search[index_row + 2][index_column - 2]
            diagonal += self._word_search[index_row + 3][index_column - 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _upper_right_diagonal(self, index_column: int, index_row: int, letter: str):
        diagonal = letter
        if self._out_of_bounds(index=index_row):
            return 0
        try:
            diagonal += self._word_search[index_row - 1][index_column + 1]
            diagonal += self._word_search[index_row - 2][index_column + 2]
            diagonal += self._word_search[index_row - 3][index_column + 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _upper_left_diagonal(self, index_column: int, index_row: int, letter: str):
        diagonal = letter
        if self._out_of_bounds(index=index_row) or self._out_of_bounds(index=index_column):
            return 0
        try:
            diagonal += self._word_search[index_row - 1][index_column - 1]
            diagonal += self._word_search[index_row - 2][index_column - 2]
            diagonal += self._word_search[index_row - 3][index_column - 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _out_of_bounds(self, index: int):
        return index - 3 < 0
