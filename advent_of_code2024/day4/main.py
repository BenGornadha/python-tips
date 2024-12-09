from typing import List

from advent_of_code2024.day4.word_search import OneRowOfLetters


def read_input(filename: str) -> List[str]:
    with open(filename, "r") as fd:
        data = fd.readlines()
    return [line.replace('\n', '') for line in data]


if __name__ == '__main__':
    data = read_input(filename="input.txt")
    print(data)
    rows = []
    for row in data:
        one_row = OneRowOfLetters(size_row=140)
        for a_letter in row:
            one_row.append_letter(letter=a_letter)
        rows.append(one_row)
    print(rows)