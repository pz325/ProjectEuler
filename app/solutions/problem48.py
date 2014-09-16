'''

Self powers

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.


analysis:

define a product operation, return only the last 10 digits

(a * b) % c = ((a % c) * (b % c)) % c
(a + b) % c = ((a % c) + (b % c)) % c

'''

MOD = 10000000000
def modProduct(a, b):
    return ((a % MOD) * (b % MOD)) % MOD

def modPow(a, b):
    p = 1
    for i in xrange(b):
        p = modProduct(p, a)
    return p

def modAdd(a, b):
    return ((a % MOD) + (b % MOD)) % MOD


def solution():
    result = 0
    for i in xrange(1, 1001):
        result = modAdd(result, modPow(i, i))
    return result


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result