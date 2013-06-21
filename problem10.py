'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from problem3 import prime_factors

target = 2e6
i = 3
total = 2
while True:
    pfs = prime_factors(i)
    if len(pfs) == 1:
        print i
        total += i
    i += 2
    if i > target:
        break
print '==total=='
print total