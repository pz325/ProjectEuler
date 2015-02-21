'''
Prime summations

refer to http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
dynamic programming

see problem 76 and problem 31
'''
from util import prime_start

def solution():
    N = 5000
    primes = []
    for p in prime_start():
        primes.append(p)
        target = p

        ways = [0] * (target + 1)
        ways[0] = 1

        for i in primes:
            for j in range(i, target + 1):
                ways[j] += ways[j - i]
                if ways[j] > N:
                    return j

if __name__ == '__main__':
    print('Result', solution())
