'''
abc-hits

The radical of n, rad(n), is the product of distinct prime factors of n. For example, 504 = 2^3 × 3^2 × 7, so rad(504) = 2 × 3 × 7 = 42.

We shall define the triplet of positive integers (a, b, c) to be an abc-hit if:

GCD(a, b) = GCD(a, c) = GCD(b, c) = 1
a < b
a + b = c
rad(abc) < c
For example, (5, 27, 32) is an abc-hit, because:

GCD(5, 27) = GCD(5, 32) = GCD(27, 32) = 1
5 < 27
5 + 27 = 32
rad(4320) = 30 < 32
It turns out that abc-hits are quite rare and there are only thirty-one abc-hits for c < 1000, with ∑c = 12523.

Find ∑c for c < 120000.

rad(abc) = rad(a) * rad(b) * rad(c)
'''
import util

ANSWER = 18407904


def solution():
    # N = 1000
    N = 120000
    rads = [0] * N
    for i in range(1, N):
        rads[i] = util.rad(i)

    abc_hit = []
    for c in range(3, N):
        for a in range(1, int(c/2)):
            b = c - a
            if rads[a] * rads[b] * rads[c] < c and util.gcd(a, b) == 1:
                print('found abc hit: [{a}, {b}, {c}]'.format(a=a, b=b, c=c))
                abc_hit.append(c)

    result = sum(abc_hit)
    return result


if __name__ == '__main__':
    import time
    start_time = time.time()
    result = solution()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Result: %s" % result)
