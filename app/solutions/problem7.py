'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
'''
from util import is_prime

def solution():
    count = 1
    i = 3
    target = 10001
    while(True):
        if is_prime(i):
            count += 1
        if count == target:
            break
        i += 2
    return i

if __name__ == '__main__':
    print 'Result: ', solution()