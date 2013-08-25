'''
Euler discovered the remarkable quadratic formula:

n*n + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41 * 41 + 41 + 41 is clearly divisible by 41.
The incredible formula  n*n - 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, 79 and 1601, is 126479.

Considering quadratics of the form:

n*n + an + b, where |a|  1000 and |b|  1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.
'''

from util import is_prime


def quad(n, a, b):
    return n * n + a * n + b


def quadratic_formula(a, b):
    n = 0
    while is_prime(quad(n, a, b)):
        # print 'n: {n} makes {r} is prime'.format(n=n, r=quad(n, a, b))
        n += 1
    return n

# print quadratic_formula(1, 41)

max_n = 0
for a in xrange(-1000, 1001):
    for b in xrange(-1000, 1001):
        n = quadratic_formula(a, b)
        if n > max_n:
            max_n = n
            product = a * b
        if n > 10:
            print '{a} and {b} makes {n} primes'.format(a=a, b=b, n=n)
print max_n, product
