'''
Coin partitions

http://en.wikipedia.org/wiki/Partition_(number_theory)

generating function -- def partition

had big integer issue

Inspired by http://www.mathblog.dk/project-euler-78-coin-piles/
so to only save modulo N

'''
N = 1000000

def partition(n, p):  
    '''
    partition generating function
    ''' 
    result = 0
    k = 1
    while True:
        g = k * (3 * k - 1) / 2
        i = n - g
        # print('accumulating: k={k}, g={g}, i={i}'.format(k=k, g=g, i=i))
        if i < 0:
            break
        result += (-1) ** (k-1) * p[i]
        if k > 0:
            k *= -1
        else:
            k *= -1
            k += 1
    return int(result % N)

def solution():
    p = []
    p.append(1)  # p(0) = 1
    n = 1
    while True:
        p.append(partition(n, p))
        if p[n] % N == 0:
            break
        n += 1
    return n

if __name__ == '__main__':
    print('Result', solution())