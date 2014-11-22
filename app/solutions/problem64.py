'''
Odd period square roots

ref: http://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

answer: 1322
'''

import math

def sqrtContinuedFraction(S):
    a0 = math.floor(math.sqrt(S))
    m0 = 0
    d0 = 1

    fractions = []
    a, m, d = a0, m0, d0
    while a != 2 * a0:
        m = d * a - m
        d = (S  - m * m) / d
        a = math.floor((a0 + m) / d) 
        fractions.append(a)

    return a0, fractions


def solution():
    oddResults = 0
    N = 10000
    for S in range(2, N+1):
        if math.sqrt(S) == math.floor(math.sqrt(S)): continue
        a0, fractions = sqrtContinuedFraction(S)
        if len(fractions) % 2 != 0: oddResults += 1

    return oddResults

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
