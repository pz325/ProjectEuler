'''
Ordered fractions
'''
from util import gcd
import time
import math

def getReducedProperFractions(d, lowerBound, upperBound):
    reducedProperFractions = {}
    # f = 1.0 / float(d)
    # if f > lowerBound and f < upperBound:
    #     reducedProperFractions['1/{}'.format(d)] = 1.0/float(d)
    lower = int(math.floor(float(d)*lowerBound))
    upper = int(math.ceil(float(d)*upperBound))+1
    for i in range(lower, upper):
        f = float(i) / float(d)
        if f > lowerBound and f < upperBound:
            if gcd(i, d) == 1:
                reducedProperFractions['{}/{}'.format(i, d)] = float(i)/float(d)
    return reducedProperFractions

def bruteForce():
    # N = 8
    N = 1000000
    mark = 3.0/7.0
    lowerBound = 3.0/8.0
    step = 1000
    for n in range(0, N, step):
        reducedProperFractions = {}
        resultFraction = '3/7'
        startTime = time.time()
        for d in range(n, n+step):
            if d == 0 or d == 1: continue
            reducedProperFractions.update(getReducedProperFractions(d, lowerBound, mark))
        print('total reduced proper fractions: {} for {}, takes {} seconds'.format(len(reducedProperFractions), n, time.time()-startTime))
        # sort
        sortedReduceProperFractions = sorted(reducedProperFractions.items(), key=lambda x: x[1])
        lowerBound = sortedReduceProperFractions[-1][1]
    
    resultFraction = sortedReduceProperFractions[-1][0]
    print('{} is left to 3/7'.format(resultFraction))
    return resultFraction.split('/')[1]

def solution():
    # N = 8
    N = 10000
    mark = 3.0/7.0
    lowerBound = 3.0/8.0
    step = 1000
    print(range(0, N, step))
    for n in range(0, N, step):
        reducedProperFractions = {}
        resultFraction = '3/7'
        for d in range(n, n+step):
            if d == 0 or d == 1: continue
            reducedProperFractions.update(getReducedProperFractions(d, lowerBound, mark))
        print('total reduced proper fractions: {}'.format(len(reducedProperFractions)))
        # sort
        sortedReduceProperFractions = sorted(reducedProperFractions.items(), key=lambda x: x[1])
        lowerBound = sortedReduceProperFractions[-1][1]
    
    resultFraction = sortedReduceProperFractions[-1][0]
    print('{} is left to 3/7'.format(resultFraction))
    return resultFraction.split('/')[1]

if __name__ == '__main__':
    # result = solution()
    result = bruteForce()
    print 'Result: ', result
