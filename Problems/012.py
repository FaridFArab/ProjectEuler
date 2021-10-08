"""


The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 +
2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

     1: 1
     3: 1,3
     6: 1,2,3,6
    10: 1,2,5,10
    15: 1,3,5,15
    21: 1,3,7,21
    28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

"""

import time


def numdivisors(triangle):
    factors = 0
    for i in range(1, int((triangle ** 0.5)) + 1):
        if triangle % i == 0:
            factors += 1
    return factors * 2


def maxtriangledivisors(max):
    i = 1
    triangle = 0
    while i > 0:
        triangle += i
        if numdivisors(triangle) >= max:
            print('it was found number', triangle, 'triangle', i, 'with total of ', numdivisors(triangle), 'factors')
            return triangle
        i += 1


# startTime = time.time()
maxtriangledivisors(500)
# print(time.time() - startTime)