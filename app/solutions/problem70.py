'''
Totient permutation

bruteForce() takes 20 minutes

solution is inspired by http://www.mathblog.dk/project-euler-70-investigate-values-of-n-for-which-%CF%86n-is-a-permutation-of-n/
math wins!

answer: 8319823
'''

from util import prime_factors
from util import prime_start
from util import is_prime
import time


def phi(n):
    r = 1.0
    for p in prime_factors(n):
        r *= (1.0 - 1.0/float(p))
    r *= n
    return int(round(r))


def isPermutation(i, j):
    return sorted([c for c in str(i)]) == sorted([c for c in str(j)])

def bruteForce():
    startTime = time.time()
    N = 10000000

    minResult = N
    index = 0
    roundStartTime = time.time()
    for i in range(2, N):
        if i % 100000 == 0: 
            print('{0} done, this round takes {1} seconds, elapsed {2} seconds'.format(i, time.time()-roundStartTime, time.time()-startTime))
            roundStartTime = time.time()
        phi_i = phi(i)
        current = float(i) / float(phi(i))
        if isPermutation(i, phi_i) and current < minResult: 
            minResult = current
            index = i
            print('found {}, phi_i: {}, min: {}, prime factors: {}'.format(i, phi_i, minResult, prime_factors(i)))

    return index


def solution():
    primes = []
    for p in prime_start(2000):
        if p > 4500: break
        primes.append(p)
    
    N = 10000000
    minResult = N
    index = 0
    for i in range(0, len(primes)):
        for j in range(i, len(primes)):
            n = primes[i] * primes[j]
            if n > N: break
            phi_n = (primes[i] - 1) * (primes[j] - 1)
            ratio = float(n) / float(phi_n)

            if isPermutation(n, phi_n) and ratio < minResult:
                minResult = ratio
                index = n
                print('found {}, phi_i: {}, min: {}, prime factors: {}'.format(n, phi_n, minResult, (primes[i], primes[j])))
    return index


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
