'''
Totient maximum

ref http://en.wikipedia.org/wiki/Euler%27s_totient_function

it is easy to calculate phi(n)

http://www.mathblog.dk/project-euler-69-find-the-value-of-n-%E2%89%A4-1000000-for-which-n%CF%86n-is-a-maximum/
has a very quick solution! (no need to try every number!)

answer: 510510
'''

import time
from util import prime_factors


def phi(n):
    r = 1.0
    for p in prime_factors(n):
        r *= (1.0 - 1.0/float(p))
    r *= n
    return r


def solution():
    N = 1000000

    maxResult = 0
    index = 0
    for i in range(2, N+1):
        current = float(i) / float(phi(i))
        if current > maxResult: 
            maxResult = current
            index = i

    return index


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
