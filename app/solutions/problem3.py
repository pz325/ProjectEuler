'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

from util import prime_factors

def solution():
    N = 600851475143
    pfs = prime_factors(N)
    result = pfs[-1]
    return result

if __name__ == '__main__':
    print 'Result: ', solution()
