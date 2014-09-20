'''
Powerful digit counts

The 5-digit number, 16807=7^5, is also a fifth power. 
Similarly, the 9-digit number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

'''

import math
from util import digits_2

def test():
    x = 8   # try 2, 8, 9, 10
    for y in xrange(1, 24):
        p = int(math.pow(x, y))
        l = digits_2(p)
        print(l, y)

def solution():
    count = 0
    x = 2
    while True:
        y = 1
        if digits_2(int(math.pow(x, y))) > y:
            break
        while True:
            p = int(math.pow(x, y))
            l = digits_2(p)
            if l == y:
                count += 1
                print(x, y, l)
            if l < y: break
            y += 1
        x += 1

    return count + 1  # 1^1

def solution_2():
    count = 0
    for x in xrange(2, 100):
        for y in xrange(1, 100):
            p = int(math.pow(x, y))
            l = digits_2(p)
            # print(x, y, l)
            if l == y:
                count += 1
                print(x, y, p)
            if l > y: break
    return count + 1  # 1^1

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
