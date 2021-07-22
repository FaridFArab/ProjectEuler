"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math


if __name__ == '__main__':
    total: int = 1000
    find_flag = False
    for a in range(1, total // 3):
        for b in range(a, total // 2):
            c = total - a - b
            if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                find_flag = True
                break
        if find_flag:
            break
    print(f"a: {a}, b: {b}, c:{c}")
    print(a * b * c)