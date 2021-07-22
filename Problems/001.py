"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. T
he sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_multiple_values(input_values: int):
    return sum([i for i in range(input_values) if (i % 3 == 0 or i % 5 == 0)])


if __name__ == '__main__':
    x = 1000
    print(sum_multiple_values(x))
