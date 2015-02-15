'''
Singlular integer right triangles

how many values of L <= 1,500,000 can exactly one integer sided right angle triangle be formed?

(3, 4, 5) is called 'Pythagorean Triples'

for any positive integer m, n, m < n, 
we have 
    a = n^2 - m^2
    b = 2nm
    c = n^2 + m^2
(a, b, c) is a 'Pythagorean Triples'

L = a + b + c

'''


from util import gcd


def solution():
    N = 1500000
    N = 50
    result = 0
    counts = [0] * (N+1)
    max_n = int((N / 2) ** 0.5)
    for n in range(2, max_n):
        for m in range(1, n):
            if (n + m) % 2 == 1 and gcd(n, m) == 1:  # get primary pythagorean triples
                a = n ** 2 - m ** 2
                b = 2 * n * m
                c = n ** 2 + m ** 2
                abc = a + b + c
                l = abc
                while(l <= N):
                    print('{a} {b} {c} -- {l}'.format(a=a, b=b, c=c, l=l))
                    counts[l] += 1
                    if counts[l] == 1:
                        result += 1
                    if counts[l] == 2:
                        result -= 1
                    l += abc
    return result


if __name__ == '__main__':
    print 'Result: ', solution()
