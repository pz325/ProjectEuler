'''
Prime digit replacements

By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

Inspired by http://www.mathblog.dk/project-euler-51-eight-prime-family/

rules:
possible the repeated digit: 0, 1, 2
the last digit cannot be the repeated digit
three repeated digit
5/6 digits prime
'''

from util import n_digit_prime
import itertools

ALL_DIGITS = list('0123456789')

def getSameDigitPos(a, dist):
    '''
    @param dist number of repeated digits
    '''
    aDigits = [int(d) for d in list(str(a))]
    positionSet = []
    checkedPosition = []
    for i in xrange(len(aDigits)-1):
        position = []
        if i in checkedPosition: continue
        if aDigits[i] not in [0, 1, 2]: continue  # repeated digits [0, 1, 2]
        for j in xrange(i+1, len(aDigits)-1):
            if j in checkedPosition: continue
            if aDigits[i] == aDigits[j]:
                position.append(j)
                checkedPosition.append(j)
        if len(position) > 0:
            position.append(i)
            checkedPosition.append(i)
        if len(position) == dist: # only look for curtain repeated digits
            positionSet.append(position)
    return positionSet


def getTransformCombination(a, dist):
    '''
    @param dist number of repeated digits
    '''    
    positionSet = getSameDigitPos(a, dist)
    for p in positionSet:
        for transform in itertools.combinations(p, dist):  # three repeated digits
            yield transform

def getTransform(a, transform, dist):
    # print(transform)
    ori = list(str(a)) # split into chars
    for i in ALL_DIGITS:
        if int(ori[transform[0]]) == i: continue
        new = ori[:]
        for t in transform:
            new[t] = i
        yield int(''.join(new))


def solve(primes, dist, target):
    count = 0
    found = False
    result = []
    primes = list(primes)
    total = len(primes)
    for p in primes:
        count += 1
        # print('Checking: {p}: {count}/{total}'.format(p=p, count=count, total=total))
        if found: break
        for transform in getTransformCombination(p, dist):
            if found: break
            candidates = []
            for t in getTransform(p, transform, dist):
                if t in primes:
                    candidates.append(t)
            if len(candidates) == target:
                result = candidates[:]
                found = True
    return result


def genPrimes(digits):
    primes = n_digit_prime(digits)
    return primes


if __name__ == '__main__':
    digits = 6
    dist = 3
    target = 8
    primes = genPrimes(digits)
    result = solve(primes, dist, target)
    print 'Result: ', result
