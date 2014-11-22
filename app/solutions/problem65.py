'''
Convergents of e

answer: 272
'''

def f(x, m, n):
    '''
    return x + 1 / (m/n), in (m_, n_)
    '''
    return (x * m + n, m)


def fraction(a, N):
    '''
    @param a continuous fractions of a irrational number
        first is a0,
        the rest repeats
        e.g. sqrt(2): [1, 2]
        e.g. sqrt(23): [4, 1, 3, 1, 8]
    @param N
    @param return N_th fraction in the format of (numerator, denominator)
    '''
    if len(a) < N:
        cf = [a[0]]
        cfLength = len(a) - 1
        for i in range(1, n):
            cf.append(a[i%cfLength])
    else:
        cf = a
    # print('    cf to calculate: {0}'.format(cf))
    m = cf[-1]
    n = 1
    for i in range(N-1, 0, -1):
        x = cf[i-1]
        # print('    calculate: {x} + 1 / ({m} / {n})'.format(x=x, m=m, n=n))
        m, n = f(x, m, n)
    return m, n


def getEContinuousFractions(n):
    '''
    e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...]
    '''
    a = [2]
    k = 1
    for i in range(1, n):
        if i%3 == 1: a.append(1)
        elif i%3 == 0: 
            a.append(1)
            k += 1
        else: a.append(2*k)
    return a


def test():
    N = 10
    for i in range(1, N+1):
        eContinuousFractions = getEContinuousFractions(i)
        print('{0} th continuous fractions: {1}'.format(i, eContinuousFractions))
        numerator, denominator = fraction(eContinuousFractions, i)
        print(numerator, denominator)


def solution():
    N = 100
    eContinuousFractions = getEContinuousFractions(N)
    numerator, denominator = fraction(eContinuousFractions, N)
    return sum([int(x) for x in str(numerator)])

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
