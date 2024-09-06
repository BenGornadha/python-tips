from __future__ import annotations


def calculate_area(shape_type: str, dimensions: tuple) -> float:
    if shape_type == 'circle':
        radius = dimensions[0]
        return 3.14 * radius ** 2

    elif shape_type == 'rectangle':
        length, width = dimensions
        return length * width

    elif shape_type == 'triangle':
        base, height = dimensions
        return (base * height) / 2

    else:
        raise ValueError("Shape not supported")


if __name__ == '__main__':
    print(calculate_area('circle', (5,)))
    print(calculate_area('rectangle', (4, 6)))
    print(calculate_area('triangle', (4, 5)))
