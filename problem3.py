def prime_factors(x):
    '''
    give prime factors of x
    '''
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

N = 600851475143
print prime_factors(N)
