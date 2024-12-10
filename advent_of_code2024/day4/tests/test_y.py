import unittest

from advent_of_code2024.day4.word_search import WordSearch
from advent_of_code2024.day4.xmas import HorizontalXMAS, VerticalXMAS, DiagonalXMAS, CrossXMAS


class MyTestCase(unittest.TestCase):
    def test_easiest_case_with_horizontal(self):
        input = ["XMAS"]

        word_search = WordSearch(input=input)
        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)

        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_easiest_case(self):
        input = ["X"]

        word_search = WordSearch(input=input)
        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(0, sut)

    def test_found_multiple_in_horizontal(self):
        input = ["XMASXMAS"]

        word_search = WordSearch(input=input)
        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(2, sut)

    def test_column_xmas(self):
        input = ["X", "M", "A", "S"]

        word_search = WordSearch(input=input)
        horizontal_search = VerticalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_diagnoal_xmas(self):
        input = ["XXXS",
                 "MMXS",
                 "XXAS",
                 "SSSS"]

        word_search = WordSearch(input=input)
        horizontal_search = DiagonalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_diagonal_but_in_the_other_direction(self):
        input = ["SSSX",
                 "AAMA",
                 "AAAA",
                 "SSSS"]

        word_search = WordSearch(input=input)
        horizontal_search = DiagonalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_diagonal_but_backwards(self):
        input = ["SSSS",
                 "AAAA",
                 "AAMA",
                 "SSSX"]

        word_search = WordSearch(input=input)
        horizontal_search = DiagonalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_partie_1_enonce(self):
        input = ["MMMSXXMASM",
                 "MSAMXMSMSA",
                 "AMXSXMAAMM",
                 "MSAMASMSMX",
                 "XMASAMXAMM",
                 "XXAMMXXAMA",
                 "SMSMSASXSS",
                 "SAXAMASAAA",
                 "MAMMMXMMMM",
                 "MXMXAXMASX"
                 ]

        word_search = WordSearch(input=input)
        word_search.register_a_xmas_finder(a_finder=VerticalXMAS())
        word_search.register_a_xmas_finder(a_finder=HorizontalXMAS())
        word_search.register_a_xmas_finder(a_finder=DiagonalXMAS())

        sut = word_search.count_xmas()

        self.assertEqual(18, sut)

    def test_partie_2_easiest_case(self):
        input = ["MXS",
                 "XAX",
                 "MXS"]

        word_search = WordSearch(input=input)
        word_search.register_a_xmas_finder(a_finder=CrossXMAS())

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)

    def test_partie_2_enonce(self):
        input = [".M.S......",
                 "..A..MSMS.",
                 ".M.S.MAA..",
                 "..A.ASMSM.",
                 ".M.S.M....",
                 "..........",
                 "S.S.S.S.S.",
                 ".A.A.A.A..",
                 "M.M.M.M.M.",
                 ".........."]

        word_search = WordSearch(input=input)
        word_search.register_a_xmas_finder(a_finder=CrossXMAS())
        sut = word_search.count_xmas()

        self.assertEqual(9, sut)
