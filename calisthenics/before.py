class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total += grade
        return total / len(self.grades)

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
