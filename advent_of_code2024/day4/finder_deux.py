import re


class HorizontalXMAS:

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
