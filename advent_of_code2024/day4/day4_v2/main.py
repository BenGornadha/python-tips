from advent_of_code2024.day4.day4_v2.word_search import WordSearch
from advent_of_code2024.day4.main import read_input

if __name__ == '__main__':
    data = read_input(filename="input.txt")
    print(data)

    word_search = WordSearch(input=data)

    res =  word_search.count_xmas()
    res2 = word_search.count_x_mas()
    print(res)
    print(res2)