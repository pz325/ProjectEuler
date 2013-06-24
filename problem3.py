'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''


def is_prime(n):
    if len(prime_factors(n)) == 1:
        return True
    else:
        return False


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

# N = 13
# print prime_factors(N)
