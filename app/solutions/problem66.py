'''
Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 - D*y^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2x2^2 = 1
2^2 - 3x1^2 = 1
9^2 - 5x4^2 = 1
5^2 - 6x2^2 = 1
8^2 - 7x3^2 = 1

Hence, by considering minimal solutions in x for D <=7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

'''
import math


def continued_fraction(x, max_k=100):
    '''
    Find continued fraction of x
    reference https://en.wikipedia.org/wiki/Continued_fraction
    @return (terms, convergents_numerator, convertents_denominator)
    '''
    eps = 10e-9
    terms = []
    convergents_numerator = []
    convergents_denominator = []
    pm2, qm2 = 1, 0
    pm1, qm1 = 0, 1
    real_number = x
    k = 0
    while True:
        a = int(math.floor(real_number))
        r = real_number - a
        terms.append(a)
        # print('real', real_number, 'integer: ', a, 'remain', r)
        if k == 0:
            convergents_numerator.append(a)
            convergents_denominator.append(1)
            # print('p', a, 'q', 1, r'p/q', float(a)/float(1))
            pm1 = a
            qm1 = 1
        else:
            p = a * pm1 + pm2
            q = a * qm1 + qm2
            convergents_numerator.append(p)
            convergents_denominator.append(q)
            # print('p', p, 'q', q, r'p/q', float(p)/float(q))
            pm2, qm2 = pm1, qm1
            pm1, qm1 = p, q

        # print('k', k, 'r', r)
        if k > max_k or r < eps:
            break
        
        real_number = 1.0 / r
        k += 1
        
    
    return terms, convergents_numerator, convergents_denominator


def test_continued_fraction():
    a, p, q = continued_fraction(math.pi, 100)
    print(a)
    print(p)
    print(q)


from decimal import *
getcontext().prec = 100

def solve_diophantine(D):
    '''
    '''
    MAX_K = 1000
    pm2, qm2 = 1, 0
    pm1, qm1 = 0, 1
    real_number = Decimal(D).sqrt()
    k = 0
    while True:
        a = int(math.floor(real_number))
        r = real_number - Decimal(a)
        # print('real', real_number, 'integer: ', a, 'remain', r)
        if k == 0:
            p = a
            q = 1
            # print('p', a, 'q', 1, r'p/q', float(a)/float(1))
            pm1 = a
            qm1 = 1
        else:
            p = a * pm1 + pm2
            q = a * qm1 + qm2
            # print('p', p, 'q', q, r'p/q', float(p)/float(q))
            pm2, qm2 = pm1, qm1
            pm1, qm1 = p, q
        
        if diophantine_equation_match(p, q, D):
            return p, q
        # print('k', k, 'r', r)
        if k > MAX_K:
            break
        
        real_number = Decimal(1.0) / r
        k += 1
    
    print('NOT FOUND -- increase MAX_K', D)
    return 0, 0


def diophantine_equation_match(x, y, D):
    return x*x-D*y*y == 1

def is_sqrt_root(x):
    y = math.sqrt(x)
    return math.floor(y) == y

def solution():
    x_max = 0
    D_max = 0
    for D in range(2, 1001):
        if is_sqrt_root(D):
            continue
        x, y = solve_diophantine(D)
        if x > x_max:
            x_max, D_max = x, D
        # print(D, x, y)
    
    return D_max

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
