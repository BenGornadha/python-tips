from advent_of_code2024.day4.day4_v2.word_search import WordSearch2
from advent_of_code2024.day4.day4_v2.xmas import HorizontalXMAS, VerticalXMAS, DiagonalXMAS, CrossXMAS
from advent_of_code2024.day4.main import read_input

if __name__ == '__main__':
    data = read_input(filename="input.txt")

    # -------------------- PARTIE 1 --------------------
    word_search = WordSearch2(input=data)
    word_search.register_a_xmas_finder(HorizontalXMAS())
    word_search.register_a_xmas_finder(VerticalXMAS())
    word_search.register_a_xmas_finder(DiagonalXMAS())

    res = word_search.count_xmas()
    print(f"Résultat puzzle Partie 1 : {res}")

    # -------------------- PARTIE 2 --------------------
    word_search2 = WordSearch2(input=data)
    word_search2.register_a_xmas_finder(CrossXMAS())

    res2 = word_search2.count_xmas()
    print(f"Résultat puzzle Partie 2 : {res2}")
