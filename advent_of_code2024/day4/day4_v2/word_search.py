from __future__ import annotations
import re
from typing import List

from advent_of_code2024.day4.day4_v2.xmas import XMASFinder


class WordSearch2:
    def __init__(self, input: List[str]) -> None:
        self._rows = input
        self._xmas_finders: List[XMASFinder] = []

    @property
    def grid(self) -> List[str]:
        return self._rows.copy()

    def register_a_xmas_finder(self, a_finder: XMASFinder):
        a_finder.register_a_word_search_grid(word_search_grid=self.grid)
        self._xmas_finders.append(a_finder)

    def count_xmas(self) -> int:
        xmas_occurrences_found = 0
        for xmas_finder in self._xmas_finders:
            xmas_occurrences_found += xmas_finder.count_xmas()
        return xmas_occurrences_found


class WordSearch:
    WORD_SEARCHING = "XMAS"

    def __init__(self, input: List[str]) -> None:
        self._rows = input
        self._size_of_a_row = len(self._rows[0])
        self._nb_rows = len(self._rows)

    def count_xmas(self) -> int:
        count_horizontal = self._count_horizontal_xmas()
        count_vertical = self._count_vertical_xmas()
        count_diagonal = self._count_diagnoal_xmas()
        return count_horizontal + count_vertical + count_diagonal

    def count_x_mas(self) -> int:
        count = 0
        for index_row, row in enumerate(self._rows):
            for index_column, letter in enumerate(row):
                if letter == "A":
                    if index_row - 1 < 0 or index_column - 1 < 0:
                        continue
                    if index_row + 1 >= self._nb_rows or index_column + 1 >= self._size_of_a_row:
                        continue
                    north_west = self._get_north_west(index_row, index_column)
                    north_east = self._get_north_east(index_row, index_column)
                    south_west = self._get_south_west(index_row, index_column)
                    south_east = self._get_south_east(index_row, index_column)
                    result = north_west + north_east + south_west + south_east
                    count += (result == "MSMS" or result == "SSMM" or result == "MMSS" or result == "SMSM")
        return count

    def _get_north_west(self, index_row, index_column):
        return self._rows[index_row - 1][index_column - 1]

    def _get_north_east(self, index_row, index_column):
        return self._rows[index_row - 1][index_column + 1]

    def _get_south_west(self, index_row, index_column):
        return self._rows[index_row + 1][index_column - 1]

    def _get_south_east(self, index_row, index_column):
        return self._rows[index_row + 1][index_column + 1]

    def _count_horizontal_xmas(self):
        count = 0
        for row in self._rows:
            count += self._find_occurences_from(a_string=row)
        return count

    def _count_vertical_xmas(self):
        count = 0
        for col_index in range(self._size_of_a_row):
            column = ""
            for row_index in range(self._nb_rows):
                column += self._rows[row_index][col_index]
            count += self._find_occurences_from(a_string=column)
        return count

    def _count_diagnoal_xmas(self):
        count = 0
        for index_row, row in enumerate(self._rows):
            for index_column, letter in enumerate(row):
                count += self._right_diagonal(index_column, index_row, letter)
                count += self._left_diagonal(index_column, index_row, letter)
                count += self._upper_right_diagonal(index_column, index_row, letter)
                count += self._upper_left_diagonal(index_column, index_row, letter)

        return count

    def _right_diagonal(self, index_column, index_row, letter):
        diagonal = letter
        try:
            diagonal += self._rows[index_row + 1][index_column + 1]
            diagonal += self._rows[index_row + 2][index_column + 2]
            diagonal += self._rows[index_row + 3][index_column + 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _left_diagonal(self, index_column, index_row, letter):
        diagonal = letter
        if self._out_of_bounds(index=index_column):
            return 0
        try:
            diagonal += self._rows[index_row + 1][index_column - 1]
            diagonal += self._rows[index_row + 2][index_column - 2]
            diagonal += self._rows[index_row + 3][index_column - 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _out_of_bounds(self, index: int):
        return index - 3 < 0

    def _upper_right_diagonal(self, index_column, index_row, letter):
        diagonal = letter
        if self._out_of_bounds(index=index_row):
            return 0
        try:
            diagonal += self._rows[index_row - 1][index_column + 1]
            diagonal += self._rows[index_row - 2][index_column + 2]
            diagonal += self._rows[index_row - 3][index_column + 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _upper_left_diagonal(self, index_column, index_row, letter):
        diagonal = letter
        if self._out_of_bounds(index=index_row) or self._out_of_bounds(index=index_column):
            return 0
        try:
            diagonal += self._rows[index_row - 1][index_column - 1]
            diagonal += self._rows[index_row - 2][index_column - 2]
            diagonal += self._rows[index_row - 3][index_column - 3]
            return 1 if diagonal == "XMAS" else 0
        except IndexError as _:
            return 0

    def _find_occurences_from(self, a_string: str):
        return len(re.findall(WordSearch.WORD_SEARCHING, a_string)) + len(
            re.findall(WordSearch.WORD_SEARCHING[::-1], a_string))
