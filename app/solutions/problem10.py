'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from util import is_prime

def solution():
    target = 2e6
    i = 3
    total = 2
    while True:
        if is_prime(i):
            total += i
        i += 2
        if i > target:
            break
    return total

if __name__ == '__main__':
    print 'Result: ', solution()