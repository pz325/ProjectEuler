'''
digit power sum

248155780267521
'''

from util import digits


def isPowerSum_s(s, x):
    _, d = digits(s ** x)
    if sum(d) == s:
        print(s, x, s**x)
        return True
    else:
        return False


def solution():
    results = []
    for s in range(2, 99):
        for x in range(2, 9):
            if isPowerSum_s(s, x):
                results.append(s**x)
    print(len(results))
    return(max(results))


if __name__ == '__main__':
    print('Result: ', solution())
