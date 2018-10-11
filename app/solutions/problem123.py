'''
Prime square remainders

Follow the problem 123.py

R = 2 * n * p > 10 ^ 9
'''

import util
import itertools

def calculateR(p, n):
    a = ((p - 1) ** n + (p + 1) ** n)
    b = p**2
    r = ((p - 1) ** n + (p + 1) ** n) % (p ** 2)
    # print(n, p, a, b, r)
    print(n, r)
    return r

def calculateR_v2(p, n):
    return 2 * n * p

def bruteForce(target):
    n = 1
    for p in util.prime_start():
        # reminder is always 2 when n is even number
        if n % 2 == 0:
            n += 1
            continue

        r = calculateR_v2(p, n)
        if r > target:
            break

        n += 1
    
    return n

def solution():
    target = 10 ** 10
    n = bruteForce(target)
    return n

if __name__ == '__main__':
    print('Result: ', solution())
