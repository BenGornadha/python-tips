import re
from typing import List


def read_input(filename: str):
    with open(filename, 'r') as fd:
        res = fd.read()
    return res


class MulFinder:

    def find_all_part_1(self, a_string: str):
        pattern = r"mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, a_string)
        return matches

    def find_all_part_2(self, a_string: str):
        pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
        matches = re.findall(pattern, a_string)

        return matches


class MulCalculator:
    def __init__(self, muls: List[str]):
        self._muls = muls
        self._pattern_digits = r"\d{1,3}"

    def _get_first_number(self, a_mul: str):
        return int(re.search(self._pattern_digits, a_mul.split(',')[0]).group())

    def _get_second_number(self, a_mul: str):
        return int(re.search(self._pattern_digits, a_mul.split(',')[1]).group())

    def compute(self):
        sum = 0
        current_is_to_do = True
        for a_mul in self._muls:
            if a_mul == "don't()":
                current_is_to_do = False
                continue
            if a_mul == "do()":
                current_is_to_do = True
                continue
            if current_is_to_do:
                sum += self._get_first_number(a_mul) * self._get_second_number(a_mul)
        return sum


if __name__ == '__main__':
    res = read_input(filename="input.txt")
    all_mul = MulFinder().find_all_part_2(a_string=res)
    # all_mul2 = MulFinder().find_all2(a_string=res)
    muc = MulCalculator(muls=all_mul)
    print(muc.compute())
