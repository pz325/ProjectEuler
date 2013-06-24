'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a  b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''
from problem3 import prime_factors

'''
divisor generator idea copied from
http://stackoverflow.com/questions/171765/what-is-the-best-way-to-get-all-the-divisors-of-a-number
'''


def appendEs2Sequences(sequences, es):
    result = []
    if not sequences:
        for e in es:
            result.append([e])
    else:
        for e in es:
            result += [seq+[e] for seq in sequences]
    return result


def cartesianproduct(lists):
    """
    given a list of lists,
    returns all the possible combinations taking one element from each list
    The list does not have to be of equal length
    """
    return reduce(appendEs2Sequences, lists, [])


def factorGenerator(n):
    p = prime_factors(n)
    factors = {}
    for p1 in p:
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors


def divisors(n):
    if n == 0:
        return [0]
    factors = factorGenerator(n)
    divisors = []
    listexponents = [map(lambda x:k**x, range(0, factors[k]+1)) for k in factors.keys()]
    listfactors = cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors


def amicables(d):
    a = []
    for i in range(1, len(d)-1):
        if d[i] < len(d) and d[i] != i:
            if d[d[i]] == i:
                a.append(i)
    return a


N = 10000
d = map(lambda x: sum(divisors(x))-x, range(0, N))
a = amicables(d)
o = map(lambda x: '{0}: {1}'.format(x, d[x]), a)
print a
print o
print '==result=='
print sum(a)
