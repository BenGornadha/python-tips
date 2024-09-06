from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        raise NotImplemented


class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_area(self) -> float:
        return 3.14 * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, length: float, width: float):
        self.length = length
        self.width = width

    def calculate_area(self) -> float:
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height

    def calculate_area(self) -> float:
        return (self.base * self.height) / 2


def calculate_area(shape: Shape) -> None:
    print(f"The area is: {shape.calculate_area()}")


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(4, 5)

    calculate_area(circle)
    calculate_area(rectangle)
    calculate_area(triangle)
