'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2 * 1^2
15 = 7 + 2 * 2^2
21 = 3 + 2 * 3^2
25 = 7 + 2 * 3^2
27 = 19 + 2 * 2^2
33 = 31 + 2 * 1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
from util import is_prime

x = 35
found = False
while(not found):
    if not is_prime(x):
        n = 1
        has_prime = False
        while(2 * n * n < x - 2):
            t = x - 2 * n * n
            if is_prime(t):
                has_prime = True
                break
            n += 1
        if not has_prime:
            found = True
            print 'result: ', x
    x += 2
