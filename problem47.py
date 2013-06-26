'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2  7
15 = 3  5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2  7  23
645 = 3  5  43
646 = 2  17  19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
'''
from util import prime_factors


def check_consecutive_numbers_having_distinct_prime_factors(start, n):
    for i in xrange(start, start+n):
        distinct_pf = set()
        pf = prime_factors(i)
        for p in pf:
            distinct_pf.add(p)
        if len(distinct_pf) != n:
            return False
    return True

x = 600
N = 4
while not check_consecutive_numbers_having_distinct_prime_factors(x, N):
    x += 1
print x
