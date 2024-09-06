from further.shape.shape import Shape, Circle, Rectangle, Triangle


def calculate_area(shape: Shape) -> None:
    print(f"The area is: {shape.calculate_area()}")


if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(4, 5)

    calculate_area(circle)
    calculate_area(rectangle)
    calculate_area(triangle)
