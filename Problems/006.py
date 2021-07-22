"""
The sum of the squares of the first ten natural numbers is,
                                                        1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                                                        (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
                                                        3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""


def sum_square(first_number: int, last_number: int) -> int:
    return sum([i**2 for i in range(first_number, last_number + 1)])


def square_sum(first_number: int, last_number: int) -> int:
    return sum([i for i in range(first_number, last_number + 1)]) ** 2


if __name__ == '__main__':
    first_number, last_number = 1, 100
    print(square_sum(first_number, last_number) - sum_square(first_number, last_number))
