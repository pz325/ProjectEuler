'''
Combinatoric selections
'''

import math
import operator


def combination(n, r):
    if r > n/2:
        return combination(n, n-r)
    maxNumerator = n-r
    minDenominator = r+1

    numerator = xrange(maxNumerator+1, n+1)
    denominator = xrange(1, minDenominator) 

    # print(numerator)
    # print(numerator)
    return reduce(operator.mul, numerator, 1) / reduce(operator.mul, denominator, 1)


def solution():
    count = 0
    for n in xrange(1, 101):
        for r in xrange(0, n):
            c = combination(n, r)
            if c > 1000000:
                count += n-2*r+1
                break
    return count


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result


# print(combination(6, 0))
# print('='*23)
# print(combination(6, 1))
# print('='*23)
# print(combination(6, 2))
# print('='*23)
# print(combination(6, 3))
# print('='*23)
# print(combination(6, 4))
# print('='*23)
# print(combination(6, 5))
# print('='*23)
# print(combination(23, 10))
