'''
Ordered radicals
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).

'''
import util
from functools import reduce

ANSWER = 21417


def rad(n):
    if n == 1:
        return 1
    return reduce((lambda x, y: x * y), set(util.prime_factors(n)))


def solution():
    N = 100001
    target = 10000
    r = [0] * N
    for i in range(1, N):
        r[i] = (i, rad(i))
    r = r[1:]

    r.sort(key=lambda tup: tup[1])
    # print(r)
    result = r[target-1][0]
    return result


if __name__ == '__main__':
    import time
    start_time = time.time()
    result = solution()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Result: %s" % str(result))
