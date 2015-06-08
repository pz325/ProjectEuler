
'''
Square digit chains

44 -> 16 + 16 = 32 -> 9 + 4 = 13 -> 1 + 9 = 10 -> 1
85 -> 64 + 25 = 89

How many starting numbers below ten million will arrive at 89?

non-brute-force anlysis:

up to 7 digits, find combination makes 1, count possible permutations, then take away the result from 9999999

8581146
'''

from util import digits
from itertools import combinations_with_replacement
from itertools import permutations

def chainEnds(n):
    # chains = []
    while n != 1 and n != 89:
        _, allDigits = digits(n);
        n = sum([x**2 for x in allDigits])
        # chains.append(n)
    # return chains
    return n

def bruteForceSolution():  # 163.5s
    count = 0
    for x in range(1, 10000000):
        if x % 10000 == 0: print(x)
        if chainEnds(x) == 89:
            count += 1
    return count


def countCombination(c):
    lowerBound = 10 ** (len(c) - 1)
    combs = set()
    count = 0
    for comb in permutations(c):
        x = int(''.join(map(str, comb)))
        if x >= lowerBound:
            combs.add(x)
    return len(combs)

def solution(): # 21s
    DIGITS = [1, 2, 3, 4, 5, 6, 7, 8, 9,0 ]
    excludeCount = 0
    for numDigis in range(1, 8):
        print(numDigis)
        for comb in combinations_with_replacement(DIGITS, numDigis):
            x = int(''.join(map(str, comb)))
            if x == 0 : continue
            chainEnd = chainEnds(x)
            if chainEnd == 1:
                excludeCount += countCombination(comb)
        print(excludeCount)
    return 9999999 - excludeCount

if __name__ == '__main__':
    print('Result', bruteForceSolution())
