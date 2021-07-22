"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9779 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""


def find_biggest_digit(digit_num: int) -> int:
    number = '9'
    for i in range(digit_num-1):
        number += '9'
    return int(number)


def find_lowest_digit(digit_num: int) -> int:
    number = '1'
    for i in range(digit_num-1):
        number += '0'
    return int(number)


def is_palindrom(number: int) -> bool:
    return list(str(number)) == list(str(number))[::-1]


def find_biggest_palindrome(digit_number: int) -> int:
    # min = find_lowest_digit(digit_number) * find_lowest_digit(digit_number)
    # max = find_biggest_digit(digit_number) * find_biggest_digit(digit_number)
    # for i in range(max, min - 1, -1):
    #     if list(str(i)) == list(str(i))[::-1]:
    #         return i

    lower_bound = find_lowest_digit(digit_number)
    upper_bound = find_biggest_digit(digit_number)
    for i in range(upper_bound, lower_bound - 1, -1):
        for j in range(i, lower_bound - 1, -1):
            if is_palindrom(i * j):
                return i * j


if __name__ == '__main__':
    # TODO: Wrong answer ! correct is: 906609
    print(find_biggest_palindrome(4))