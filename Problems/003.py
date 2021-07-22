"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
import time


def find_max_prime_factors_optimized(number: int) -> int:
    for i in range(number - 1, 1, -1):
        prime_flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime_flag = False
                break

        if prime_flag:
            return i


def find_max_prime_factors(number: int) -> int:
    result = list()
    for i in range(number, 2, -1):
        prime_flag = True
        for j in range(2, i // 2 + 1):
            if i % j == 0:
                prime_flag = False
                break

        if prime_flag:
            result.append(i)
            break

    return result[0]


if __name__ == '__main__':
    number = 600851475143
    print('Optimized Method:')
    start_time = time.time()
    # print(divmod(number,  2))
    # print(find_max_prime_factors_optimized(600851475143))
    print("--- %s seconds ---" % (time.time() - start_time))
