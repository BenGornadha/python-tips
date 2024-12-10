from typing import List

from advent_of_code2024.day4.word_search import WordSearch
from advent_of_code2024.day4.xmas import HorizontalXMAS, VerticalXMAS, DiagonalXMAS, CrossXMAS


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as fd:
        data = fd.readlines()
    return [line.replace('\n', '') for line in data]


if __name__ == '__main__':
    data = read_input(filename="input.txt")

    # -------------------- PARTIE 1 --------------------
    word_search = WordSearch(input=data)
    word_search.register_a_xmas_finder(HorizontalXMAS())
    word_search.register_a_xmas_finder(VerticalXMAS())
    word_search.register_a_xmas_finder(DiagonalXMAS())

    res = word_search.count_xmas()
    print(f"Résultat puzzle Partie 1 : {res}")

    # -------------------- PARTIE 2 --------------------
    word_search2 = WordSearch(input=data)
    word_search2.register_a_xmas_finder(CrossXMAS())

    res2 = word_search2.count_xmas()
    print(f"Résultat puzzle Partie 2 : {res2}")
