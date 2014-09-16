'''
Permuted multiples

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

analysis:
1) first digit must be 1 (because of 6X)

'''

import math

def numDigits(a):
    return len(list(str(a)))

def sameDigits(a, b):
    countA = [0]*10
    countB = [0]*10
    for ea, eb in zip(list(str(a)), list(str(b))):
        countA[int(ea)] += 1
        countB[int(eb)] += 1
    same = True
    for i in xrange(10):
        if countA[i] != countB[i]: 
            same = False
            break
    # print(a, b, same)
    return same

def findPermutedMultiples(a):
    if sameDigits(a, a*2) and sameDigits(a, a*3) and sameDigits(a, a*4) and sameDigits(a, a*5) and sameDigits(a, a*6):
        return True
    else:
        return False
    
def solve():
    found = False
    i = 9
    while not found:
        i += 1
        n = numDigits(i)
        if i == 2 * math.pow(10, n-1):
            i = int(math.pow(10, n))
        found = findPermutedMultiples(i)
    return i

if __name__ == '__main__':
    result = solve()
    print 'Result: ', result