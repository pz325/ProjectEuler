import math
import operator
from functools import reduce


def reverse(n):
    '''
    reverse a number, e.g. 123 -> 321
    '''
    return int(str(n)[::-1])


def isPalindromic(n):
    '''
    Check whether a number is palindromic, e.g. 515 is palindromic
    '''
    return str(n) == str(n)[::-1]


def primes_less_than(n):
    '''
    Find all primes less than a number, n >= 2
    '''
    if n <= 1:
        return []
    if n == 2:
        return [2]
    p = [2]
    for i in range(3, n+1, 2):
        if is_prime(i):
            p.append(i)
    return p


def n_digit_prime(n=2):
    '''
    Generator for primes having n digits
    '''
    start = int(math.pow(10, n-1))
    end = int(math.pow(10, n) - 1)
    for i in prime_start(start):
        if i > end:
            break
        yield i


def prime_start(start=2):
    '''
    Generator for primes, starting from a number
    '''
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
    '''
    Check wether a number is a prime
    '''
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
            factors.append(int(i))
        i += 2
    if x > 1:
        factors.append(int(x))
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


def proper_divisors(n):
    '''
    The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.
    '''
    return divisors(n)[0:-1]


def factors(n):
    factors = []
    sqrt = int(math.sqrt(n))
    if sqrt * sqrt == n:
        factors.append(sqrt)
        sqrt = sqrt - 1

    for i in range(1, sqrt):
        if n % i == 0:
            factors.append(i)
            factors.append(n / i)

    return factors


def divisors(n):
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    factors = factorGenerator(n)
    divisors = []
    listexponents = [map(lambda x:k**x, range(0, factors[k]+1))
                     for k in factors.keys()]
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

    numerator = range(maxNumerator+1, n+1)
    denominator = range(1, minDenominator)

    # print(numerator)
    # print(numerator)
    return reduce(operator.mul, numerator, 1) / reduce(operator.mul, denominator, 1)


def gcd(m, n):
    """Return the greatest common divisor of m and n."""
    while n != 0:
        m, n = n, m % n
    return m


def array_add(a1, a2):
    '''
    addition of two arrays, for dealing with large integer addition
    [1, 2, 3] + [4, 5] <=> 123+45
      => [1, 6, 8]
    @param a1 
    @param a2 
    @return
    '''

    def get_carrier(addition):
        if addition > 9:
            carrier = 1
            addition = addition - 10
        else:
            carrier = 0
        return addition, carrier

    if len(a2) > len(a1):
        return array_add(a2, a1)

    r1 = a1[::-1]
    r2 = a2[::-1]

    carrier = 0
    i = 0
    while i < len(r2):
        addition = r1[i] + r2[i] + carrier
        addition, carrier = get_carrier(addition)
        r1[i] = addition
        i += 1

    while carrier > 0:
        if i < len(r1):
            addition = r1[i] + carrier
            addition, carrier = get_carrier(addition)
            r1[i] = addition
            i += 1
        else:
            r1.append(carrier)
            carrier = 0

    return r1[::-1]


def timeit(func):
    '''
    Decorator for timing the func
    '''
    def wrapper(*args, **kwargs):
        import time
        start_time = time.time()
        func(*args, **kwargs)
        print(
            "--- {duration} seconds ---".format(duration=(time.time() - start_time)))

    return wrapper


def rad(n):
    '''
    The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.
    '''
    if n == 1:
        return 1
    return reduce((lambda x, y: x * y), set(prime_factors(n)))
