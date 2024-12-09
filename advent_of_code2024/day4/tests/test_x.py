import unittest

from advent_of_code2024.day4.positon import Position
from advent_of_code2024.day4.word_search import WordSearch, OneRowOfLetters, SearchZone, Neighbours


class MyTestCase(unittest.TestCase):
    def read_input(self, input):
        word_search = WordSearch()
        for row in input:
            one_row = OneRowOfLetters()
            for a_letter in row:
                one_row.append_letter(letter=a_letter)
            word_search.register_row(a_row_of_letter=one_row)
        return word_search

    def test_easiest_case(self):
        input = ["XMAS"]
        word_search = self.read_input(input=input)
        search_zone = SearchZone(word_search=word_search)

        sut = search_zone.find_neighbours(position=Position(0, 0))

        self.assertEqual({Position(row_index=0, column_index=1): 'M'}, sut)
