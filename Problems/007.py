"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""


def find_prime_numbers(prime_count: int):
    result = list()
    prime_list_completed_flag = True
    start_number = 2
    while prime_list_completed_flag:
        for j in range(2, start_number // 2 + 1):
            if start_number % j == 0:
                prime_list_completed_flag = False
                break

        if prime_list_completed_flag:
            result.append(start_number)
            if len(result) == prime_count:
                return result

        start_number += 1
        prime_list_completed_flag = True


if __name__ == '__main__':
    print(find_prime_numbers(10001)[-1])