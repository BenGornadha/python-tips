import unittest

from advent_of_code2024.day4.word_search import WordSearch
from advent_of_code2024.day4.xmas_finders import HorizontalXMAS, VerticalXMAS, DiagonalXMAS, CrossXMAS


class MyTestCase(unittest.TestCase):
    def test_easiest_case_with_horizontal(self):
        input = ["XMAS"]

        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_puzzle(word_search_puzzle=input)

        sut = horizontal_search.count_xmas()

        self.assertEqual(1, sut)

    def test_easiest_case(self):
        input = ["X"]

        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_puzzle(word_search_puzzle=input)

        sut = horizontal_search.count_xmas()

        self.assertEqual(0, sut)

    def test_found_multiple_in_horizontal(self):
        input = ["XMASXMAS"]

        horizontal_search = HorizontalXMAS()
        horizontal_search.register_a_word_search_puzzle(word_search_puzzle=input)
        sut = horizontal_search.count_xmas()

        self.assertEqual(2, sut)
