def is_prime(n):
    if len(prime_factors(n)) == 1:
        return True
    else:
        return False


def prime_factors(x):
    '''
    give prime factors of x
    '''
    if x <= 0:
        return [0]
    if x == 1:
        return [1]
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
