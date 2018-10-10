'''
Prime square remainders

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

def bruteForce(target):
    n = 1
    for p in util.prime_start():
        # reminder is always 2 when n is even number
        if n % 2 == 0:
            n += 1
            continue

        r = calculateR(p, n)
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
