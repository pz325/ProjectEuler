'''
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
'''
from problem3 import prime_factors


def is_circular_prime(n):
    ret = True
    s = str(n)
    s_cycle = s + s  # double string to generate circular number
    if len(s) > 1:
        for i in xrange(0, len(s)):
            tmp = s_cycle[i:i+len(s)]
            if len(prime_factors(int(tmp))) > 1:
                ret = False
                break
    return ret

N = 1000000
count = 0
for i in xrange(2, N+1):
    if len(prime_factors(i)) == 1:
        if is_circular_prime(i):
            count += 1
            print i, count

print '==result=='
print count
