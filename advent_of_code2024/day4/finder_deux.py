import re


class VerticalXMAS:

    def __init__(self, word_to_search="XMAS"):
        self._puzzle = []
        self._word_to_search = word_to_search

    def register_a_word_search_puzzle(self, word_search_puzzle: List[str]) -> None:
        self._puzzle = word_search_puzzle
        self._size_of_a_row = len(self._puzzle[0])
        self._nb_rows = len(self._puzzle)

    def count_xmas(self) -> int:
        count = 0
        for col_index in range(self._size_of_a_row):
            all_letters = self._get_all_letters_at(col_index=col_index)
            count += self._find_occurrences_from(a_string=all_letters)
        return count

    def _get_all_letters_at(self, col_index: int) -> str:
        all_letters = ""
        for row_index in range(self._nb_rows):
            all_letters += self._puzzle[row_index][col_index]
        return all_letters

    def _find_occurrences_from(self, a_string: str):
        return (len(re.findall(self._word_to_search, a_string)) +
                len(re.findall(self._word_to_search[::-1], a_string)))
