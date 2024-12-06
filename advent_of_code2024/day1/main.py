from typing import List, Tuple


def read_input(filename: str) -> Tuple[List[str]]:
    first_col = []
    second_col = []
    input_file = open(filename, "r")
    for a_line in input_file:
        num1, num2 = a_line.split()
        first_col.append(num1)
        second_col.append(num2)
    return first_col, second_col


if __name__ == '__main__':
    first_col, second_col = read_input(filename="input.txt")
    first_col = sorted(first_col)
    second_col = sorted(second_col)
    res = 0
    nb_val = len(first_col)

    for i, first_element in enumerate(first_col):
        # res += abs(int(first_element) - int(second_col[i]))
        current_value = int(first_element)
        nb_time_found = 0
        for second_element in second_col:
            if int(second_element) == current_value:
                nb_time_found += 1
        res = res + (current_value * nb_time_found)

    print(res)
