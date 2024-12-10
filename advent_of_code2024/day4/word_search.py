from __future__ import annotations
from typing import List

from advent_of_code2024.day4.xmas import XMASFinder


class WordSearch:
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

