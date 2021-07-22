"""
By considering the terms in the Fibonacci sequence whose values do not exceed four million,
    find the sum of the even-valued terms.
"""
from typing import List


def make_odd_fibo_numbers(values: List[int]) -> int:
    result = [i for i in values if i % 2 == 0]
    return sum(result)


def make_fibo(number: int) -> int:
    result = [1, 1]
    if number in [1, 2]:
        return 1
    else:
        for i in range(2, number):
            last_fibo_item = result[len(result) - 2] + result[len(result) - 1]
            if last_fibo_item >= 4_000_000:
                break
            else:
                result.append(last_fibo_item)
    return make_odd_fibo_numbers(result)


if __name__ == '__main__':
    print(make_fibo(10000))
