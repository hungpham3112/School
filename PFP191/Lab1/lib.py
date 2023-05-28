from typing import Iterable
from math import sqrt


def take_float_input(num: int = 1) -> Iterable[float]:
    """
    take `num` element and return iterable
    E.g:
    ```
    >>> object = take_float_input(3)
    Enter 3 number(s): 1 2 3
    >>> tuple(object)
    (1.0, 2.0, 3.0)
    ```
    """
    return map(float, input(f"Enter {num} number(s): ").split())


def calc_s1(a: float, b: float, c: float, x: float) -> float:
    return a * pow(x, 2) + b * x + c


def calc_s2(a: float, b: float, c: float) -> float:
    delta = pow(b, 2) - 4 * a * c
    return sqrt(delta) if delta > 0 else 0


def is_nondegenerate_triangle(a: float, b: float, c: float) -> bool:
    a, b, c = sorted((a, b, c))
    return a + b > c


def edges_not_zeros(a: float, b: float, c: float) -> bool:
    return a != 0 and b != 0 and c != 0


def is_degenerate_triangle(a: float, b: float, c: float) -> bool:
    return a + b == c or b + c == a or c + a == b


def is_normal_triangle(a: float, b: float, c: float) -> bool:
    return is_nondegenerate_triangle(a, b, c) and edges_not_zeros(a, b, c)


def triangle_area(a: float, b: float, c: float) -> float:
    p = sum((a, b, c)) / 2
    return sqrt(p * (p - a) * (p - b) * (p - c))


def triangle_perimeter(a: float, b: float, c: float) -> float:
    return sum((a, b, c)) if is_normal_triangle(a, b, c) else max(a, b, c)


def q3():
    a, b, c, x = take_float_input(4)
    print("\n")
    print("S1: ", calc_s1(a, b, c, x), end="\n\n-------------------------\n\n")
    print("S2: ", calc_s2(a, b, c), end="\n\n-------------------------\n\n")
    a, b, c = take_float_input(3)
    if is_normal_triangle(a, b, c):
        print("\n")
        print(
            "Perimeter of triangle:",
            triangle_perimeter(a, b, c),
            end="\n\n-------------------------\n",
        )
        print(
            "Area of triangle: ",
            triangle_area(a, b, c),
            end="\n\n-------------------------\n",
        )
    elif is_degenerate_triangle(a, b, c) and edges_not_zeros(a, b, c):
        print("\n")
        print(
            "Perimeter of triangle:",
            triangle_perimeter(a, b, c),
            end="\n\n-------------------------\n\n",
        )
        print("Area of triangle: ", 0, end="\n\n-------------------------\n\n")
    else:
        print("a, b, c are not side of a triangle")


def q4():
    a, b, c = take_float_input(3)
    print(
        "The maximum value is: ", max(a, b, c), end="\n\n-------------------------\n\n"
    )
    print(
        "The minimum value is: ", min(a, b, c), end="\n\n-------------------------\n\n"
    )
    print(
        f"Before sorted: a = {a}, b = {b}, c = {c}",
        end="\n\n-------------------------\n\n",
    )
    print("After sorted: a = {0}, b = {1}, c = {2}".format(*sorted((a, b, c))))
