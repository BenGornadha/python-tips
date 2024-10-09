from __future__ import annotations


class Name:
    def __init__(self, name: str) -> None:
        self.value = name

    def __str__(self) -> str:
        return self.value


class Grade:
    def __init__(self, score: float):
        self.value = score

    def __add__(self, other: Grade):
        return Grade(self.value + other.value)

    def __truediv__(self, divisor: int) -> Grade:
        return Grade(self.value / divisor)

    def __str__(self) -> str:
        return f"{self.value:.2f}"


class Grades:
    def __init__(self) -> None:
        self.grades_list = []

    def add(self, grade: Grade) -> None:
        self.grades_list.append(grade)

    def average(self) -> Grade:
        if not self.grades_list:
            return Grade(0)
        total = Grade(0)
        for grade in self.grades_list:
            total += grade
        return total / len(self.grades_list)

    def __str__(self) -> str:
        return ', '.join(str(grade) for grade in self.grades_list)


class Student:
    def __init__(self, name: str):
        self.name = Name(name)
        self.grades = Grades()

    def add_grade(self, grade: int):
        self.grades.add(Grade(grade))

    def average_grade(self) -> Grade:
        return self.grades.average()

    def print_details(self):
        print(f"Student: {self.name}")
        print(f"Grades: {self.grades}")
        print(f"Average: {self.average_grade()}")


if __name__ == '__main__':
    student = Student("Alice")
    student.add_grade(85)
    student.add_grade(92)
    student.add_grade(78)
    student.print_details()
