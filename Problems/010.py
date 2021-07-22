"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from typing import List


def find_prime_number(from_number: int = 2, to_number: int = 1000) -> List[int]:
    result = list()
    for i in range(from_number, to_number):
        prime_flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime_flag = False
                break

        if prime_flag:
            print(f"Prime number is: {i}")
            result.append(i)

    return result


if __name__ == '__main__':
    print(sum(find_prime_number(2, 2_000_000)))