'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from problem3 import prime_factors

count = 1
i = 3
target = 10001
while(True):
    pfs = prime_factors(i)
    if len(pfs) == 1:
        count += 1
        print count, i
    if count == target:
        break
    i += 2
