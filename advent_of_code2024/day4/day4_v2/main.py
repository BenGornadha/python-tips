from advent_of_code2024.day4.day4_v2.tests.test_x import WordSearch
from advent_of_code2024.day4.main import read_input

if __name__ == '__main__':
    data = read_input(filename="input.txt")
    print(data)

    word_search = WordSearch(input=data)

    res =  word_search.count_xmas()
    print(res)