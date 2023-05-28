import math
from typing import Iterable


def take_integer_input(prompt="", num: int = 1) -> Iterable[int]:
    """
    take `num` element and return iterable
    E.g:
    ```
    >>> object = take_integer_input(3)
    Enter 3 number(s): 1 2 3
    >>> tuple(object)
    (1, 2, 3)
    ```
    """
    print(prompt, end=", ")
    return map(int, input(f"enter {num} number(s): ").split())


def int_input_less_than_five():
    number = int(input("Type your number greater than 5: "))
    return number if number > 5 else int_input_less_than_five()


def s1(number):
    return sum(range(1, number + 1))


def s2(number):
    return math.factorial(number)


def s3(number):
    return sum((1 / n for n in range(1, number + 1)))


def isprime(number):
    """Returns True if number is prime."""
    if number == 2 or number == 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= number:
        if number % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def common_prime_divisors(a, b):
    return (
        i
        for i in range(1, min(a, b) + 1)
        if a % i == b % i == 0 and isprime(i) and i != 1
    )


def palindrome(m, n):
    """
    Display all palindrome in the range of [m, n] where m < n
    """
    return [number for number in range(m, n + 1) if str(number) == str(number)[::-1]]


def q1(prompt=""):
    print(prompt)
    number1 = int_input_less_than_five()
    print("S1: ", s1(number1))
    print("S2: ", s2(number1))
    print("S3: ", s3(number1))
    number1 = int_input_less_than_five()
    print(f"{number1} {'is prime' if isprime(number1) else 'is not prime' }")


def q2(prompt=""):
    print(prompt)
    a, b = take_integer_input("Type 2 integer numbers m and n", 2)
    print(
        f"All common prime divisors of {a} and {b}: ",
        list(common_prime_divisors(a, b)),
    )
    print(f"The GCD of {a} and {b} is", math.gcd(a, b))
    print(f"The LCM of {a} and {b} is", math.lcm(a, b))


def q3(prompt=""):
    print(prompt)
    while True:
        try:
            (number3,) = take_integer_input(
                "Input an integer number n (will check input validation)"
            )
            break
        except ValueError:
            print("Invalid input. Please type one integer!!!")
            continue
    print(f"n in binary format: {format(number3, 'b')}")
    (number3,) = take_integer_input(
        "Input an integer number n (will not check input validation)"
    )
    print(
        f"The sum of all digits of {number3} is:",
        sum(map(int, tuple(str(number3)))),
    )

    print(f"The reverse version of {number3} is:", int(str(number3)[::-1]))


def q4(prompt=""):
    print(prompt)
    m, n = take_integer_input("Type 2 number m and n where m < n", 2)
    print(f"All palindrome in [m, n]:", palindrome(m, n))
