'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
from util import is_prime, digits


def is_truncatable_prime(n):
    num, ds = digits(n)
    # remove digits from left to right
    for i in xrange(1, len(ds)):
        tmp_ds = ds[i:]
        tmp_n = int(reduce(lambda x, y: ''.join([str(x), str(y)]), tmp_ds, ''))
        if not is_prime(tmp_n):
            return False
    # remove digits from right to left
    for i in xrange(1, len(ds)):
        tmp_ds = ds[:len(ds)-i]
        tmp_n = int(reduce(lambda x, y: ''.join([str(x), str(y)]), tmp_ds, ''))
        if not is_prime(tmp_n):
            return False
    return True

count = 0
n = 11
total = 0
while count < 11:
    if is_prime(n) and is_truncatable_prime(n):
        count += 1
        total += n
        print n
    n += 2
print '==result=='
print total
