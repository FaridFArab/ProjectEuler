"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""


def divisible_by(min_number: int, max_number: int) -> int:
    divisible_flag = True
    minimum_acceptable_value = max_number

    while divisible_flag:
        for i in range(min_number, max_number+1):
            if minimum_acceptable_value % i != 0:
                minimum_acceptable_value += 1
                divisible_flag = True
                break
            else:
                divisible_flag = False
    else:
        return minimum_acceptable_value


if __name__ == '__main__':
    print(divisible_by(1, 20))
