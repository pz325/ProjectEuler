'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
from util import is_prime
from util import digits


def is_pandigital(n):
    [num, ds] = digits(n)
    p = [True] * num
    for d in ds:
        if d == 0 or d > num:
            break
        else:
            p[d-1] = False
    # print n, p
    if len(filter(lambda x: x, p)) == 0:
        return True
    else:
        return False

N = 1000000000
pandigital_prime = []
for i in xrange(1, N):
    if is_prime(i) and is_pandigital(i):
        print i
        pandigital_prime.append(i)
# pandigital_prime = filter(lambda x: is_prime(x) and is_pandigital(x), range(1, N))
print '==result=='
print pandigital_prime
