'''
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?
'''
from util import primes_less_than

N = 50000000
# N = 50
upper_square = int(N ** 0.5) + 50
upper_cube = int(N ** 0.33) + 50
upper_fourth = int(N ** 0.25) + 50

primes_for_square = primes_less_than(upper_square)
primes_for_cube = primes_less_than(upper_cube)
primes_for_fourth = primes_less_than(upper_fourth)

p = set()
for s in primes_for_square:
    for c in primes_for_cube:
        for f in primes_for_fourth:
            r = s ** 2 + c ** 3 + f ** 4
            if r < N:
                p.add(r)

print '==result=='
print len(p)
