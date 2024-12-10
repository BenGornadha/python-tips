import unittest

from advent_of_code2024.day4.day4_v2.word_search import WordSearch, WordSearch2
from advent_of_code2024.day4.day4_v2.xmas import HorizontalXMAS, VerticalXMAS, DiagonalXMAS, CrossXMAS


class MyTestCase(unittest.TestCase):
    def test_something(self):
        input = ["XMAS"]

        word_search = WordSearch2(input=input)
        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)

        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something2(self):
        input = ["X"]

        word_search = WordSearch2(input=input)
        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(0, sut)

    def test_something3(self):
        input = ["XMASXMAS"]

        word_search = WordSearch2(input=input)
        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(2, sut)

    def test_something4(self):
        input = ["X", "M", "A", "S"]

        word_search = WordSearch2(input=input)
        horizontal_search = VerticalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something5(self):
        input = ["XXXS",
                 "MMXS",
                 "XXAS",
                 "SSSS"]

        word_search = WordSearch2(input=input)
        horizontal_search = DiagonalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something7(self):
        input = ["SSSX",
                 "AAMA",
                 "AAAA",
                 "SSSS"]

        word_search = WordSearch2(input=input)
        horizontal_search = DiagonalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_something8(self):
        input = ["SSSS",
                 "AAAA",
                 "AAMA",
                 "SSSX"]

        word_search = WordSearch2(input=input)
        horizontal_search = DiagonalXMAS()
        horizontal_search.register_a_word_search_grid(word_search_grid=word_search.grid)
        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_max(self):
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

        word_search = WordSearch2(input=input)
        word_search.register_a_xmas_finder(a_finder=VerticalXMAS())
        word_search.register_a_xmas_finder(a_finder=HorizontalXMAS())
        word_search.register_a_xmas_finder(a_finder=DiagonalXMAS())

        sut = word_search.count_xmas()

        self.assertEqual(18, sut)

    def test_x_max_part2(self):
        input = ["MXS",
                 "XAX",
                 "MXS"]

        word_search = WordSearch2(input=input)
        word_search.register_a_xmas_finder(a_finder=CrossXMAS())

        sut = word_search.count_xmas()

        self.assertEqual(1, sut)

    def test_x_max_part2_finale(self):
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

        word_search = WordSearch2(input=input)
        word_search.register_a_xmas_finder(a_finder=CrossXMAS())
        sut = word_search.count_xmas()

        self.assertEqual(9, sut)
