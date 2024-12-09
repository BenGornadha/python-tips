import re
import unittest
from typing import List


class WordSearch:
    WORD_SEARCHING = "XMAS"

    def __init__(self, input: List[str]) -> None:
        self._rows = input
        self._size_of_a_row = len(self._rows[0])

    def count_xmas(self) -> int:
        count_horizontal = self._count_horizontal_xmas()
        count_vertical = self._count_vertical_xmas()
        count_diagonal = self._count_diagnoal_xmas()
        return count_horizontal + count_vertical + count_diagonal

    def _count_horizontal_xmas(self):
        count = 0
        for row in self._rows:
            count += self._find_occurences_from(a_string=row)
        return count

    def _count_vertical_xmas(self):
        count = 0
        for col_index in range(self._size_of_a_row):
            column = ""
            for row_index in range(len(self._rows)):
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
        return len(re.findall(WordSearch.WORD_SEARCHING, a_string))


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = ["XMAS"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something2(self):
        input = ["X"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(0, sut)

    def test_something3(self):
        input = ["XMASXMAS"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(2, sut)

    def test_something4(self):
        input = ["X", "M", "A", "S"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something5(self):
        input = ["XXXS",
                 "MMXS",
                 "XXAS",
                 "SSSS"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something7(self):
        input = ["SSSX",
                 "AAMA",
                 "AAAA",
                 "SSSS"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something8(self):
        input = ["SSSS",
                 "AAAA",
                 "AAMA",
                 "SSSX"]

        word_search = WordSearch(input=input)

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)
