'''
Prime pair sets
'''
from util import prime_start
from util import is_prime
import time

def concatenate(a, b):
    c = b
    while c > 0:
        a *= 10
        c /= 10
    return a + b
    # return int(str(a)+str(b))

def findPairs(i, primes):
    '''
    @param i Index of primes
    '''
    pairs = set()
    # startTime = time.time() 
    for j in range(i, len(primes)):
        if is_prime(concatenate(primes[i], primes[j])) and is_prime(concatenate(primes[j], primes[i])):
            pairs.add(primes[j])    
    # print('calculate pair[{0}] takes {1} seconds'.format(primes[i], time.time()-startTime))
    return pairs

def solution():
    N = 10000
    primes = []
    for p in prime_start():
        primes.append(p)
        if p > N:
            break

    print(len(primes), 'primes generated')
    lowSum = 5 * primes[-1]

    pairs = {}

    startTime = time.time()
    # a, b, c, d, e are primes array index
    for a in range(1, len(primes)):
        if primes[a] * 5 > lowSum: break
        if primes[a] not in pairs:
            pairs[primes[a]] = findPairs(a, primes)

        for b in range(a+1, len(primes)):
            if primes[a] + primes[b] * 4 > lowSum: break
            if primes[b] not in pairs[primes[a]]: 
                # print(primes[a], primes[b], 'no match found')
                continue
            if primes[b] not in pairs:
                pairs[primes[b]] = findPairs(b, primes)

            for c in range(b+1, len(primes)):
                if primes[a] + primes[b] + primes[c] * 3 > lowSum: break
                if primes[c] not in pairs[primes[a]] or primes[c] not in pairs[primes[b]]: 
                    continue
                if primes[c] not in pairs:
                    pairs[primes[c]] = findPairs(c, primes)

                for d in range(c+1, len(primes)):
                    if primes[a] + primes[b] + primes[c] + primes[d] * 2 > lowSum: break
                    if primes[d] not in pairs[primes[a]] or primes[d] not in pairs[primes[b]] or primes[d] not in pairs[primes[c]]: 
                        continue
                    if primes[d] not in pairs:
                        pairs[primes[d]] = findPairs(d, primes)

                    for e in range(d+1, len(primes)):
                        if primes[a] + primes[b] + primes[c] + primes[d] + primes[e] > lowSum: break
                        if primes[e] not in pairs[primes[a]] or primes[e] not in pairs[primes[b]] or primes[e] not in pairs[primes[c]] or primes[e] not in pairs[primes[d]]: continue
                        if lowSum > primes[a] + primes[b] + primes[c] + primes[d] + primes[e]:
                            lowSum = primes[a] + primes[b] + primes[c] + primes[d] + primes[e]                        
                        print('found', primes[a], primes[b], primes[c], primes[d], primes[e])

    print('search accomplished in {0} seconds'.format(time.time() - startTime))
    return lowSum


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
