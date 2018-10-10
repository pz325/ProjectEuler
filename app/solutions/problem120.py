'''
Square remainders

ref: https://www.mathblog.dk/project-euler-120-maximum-remainder/

n = (a-1)/2 when r is max

max_r = 2 * a * ((a-1)/2)

or 

max_r = a * (a - 2), when a is even
max_r = a * (a - 1), when a is odd
'''

def calculateR(a, n):
    x = (a - 1) ** n + (a + 1) ** n
    y = a * a
    r = x % y
    return r

def maxR(a):
    return 2 * a * ((a - 1) / 2)


def solution():
    r = sum(maxR(a) for a in range(3, 1001))
    return r


if __name__ == '__main__':
    print('Result: ', solution())