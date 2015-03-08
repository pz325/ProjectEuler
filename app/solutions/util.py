import math
import operator

def reverse(n):
    return int(str(n)[::-1])


def isPalindromic(n):
    return str(n) == str(n)[::-1]


def primes_less_than(n):
    if n == 2:
        return [2]
    p = [2]
    for i in xrange(3, n+1, 2):
        if is_prime(i):
            p.append(i)
    return p

def n_digit_prime(n=2):
    start = int(math.pow(10, n-1))
    end = int(math.pow(10, n) - 1)
    for i in prime_start(start):
        if i > end: break
        yield i


def prime_start(start=2):
    if start == 2:
        yield start
        n = 3
    else:
        if start % 2 == 0:
            n = start + 1
        else:
            n = start
    while True:
        if is_prime(n):
            yield n
        n += 2

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


def prime_factors(x):
    '''
    give prime factors of x
    '''
    if x <= 0:
        return []
    if x == 1:
        return []
    factors = []
    while x % 2 == 0:
        factors.append(2)
        x /= 2
    i = 3
    while i * i <= x:
        while x % i == 0:
            x /= i
            factors.append(i)
        i += 2
    if x > 1:
        factors.append(x)
    return factors


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
    if n == 1:
        return [1]
    factors = factorGenerator(n)
    divisors = []
    listexponents = [map(lambda x:k**x, range(0, factors[k]+1)) for k in factors.keys()]
    listfactors = cartesianproduct(listexponents)
    for f in listfactors:
        divisors.append(reduce(lambda x, y: x*y, f, 1))
    divisors.sort()
    return divisors


def digits(n):
    num = 0
    d = []
    while n > 0:
        d.append(n % 10)
        num += 1
        n /= 10
    return num, d[::-1]

def digits_2(n):
    '''
    return number of digits of n, an integer
    '''
    return len(str(n))

def combination(n, r):
    if r > n/2:
        return combination(n, n-r)
    maxNumerator = n-r
    minDenominator = r+1

    numerator = xrange(maxNumerator+1, n+1)
    denominator = xrange(1, minDenominator) 

    # print(numerator)
    # print(numerator)
    return reduce(operator.mul, numerator, 1) / reduce(operator.mul, denominator, 1)


def gcd(m, n):
    """Return the greatest common divisor of m and n."""
    while n != 0:
        m, n = n, m % n
    return m
