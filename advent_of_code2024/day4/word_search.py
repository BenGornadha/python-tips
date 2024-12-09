import dataclasses


@dataclasses.dataclass(frozen=True)
class Letter:
    value: str


@dataclasses.dataclass(frozen=True)
class NoLetter:
    pass


class OneRowOfLetters:

    def __init__(self, size_row=140):
        self._letters = []
        self._size_row = size_row

    def append_letter(self, letter=Letter):
        self._letters.append(letter)

    def find_cell_at(self, column_index: int) -> Letter | NoLetter:
        if self._is_out_of_bounds(column_index=column_index):
            return NoLetter()
        return self._letters[column_index]

    def _is_out_of_bounds(self, column_index: int) -> bool:
        return self._size_row < column_index and column_index >= 0

class WordSearch:

    def __init__(self):
        self._rows = []

    def register_row(self, a_row_of_letter : OneRowOfLetters) -> None:
        self._rows.append(a_row_of_letter)

    def tick(self):
        for row_of_letter in self._rows:
            for letter in row_of_letter:
                print(letter)


