'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.

update: refer to Problem75

Find the product abc.
'''

def solution():
    N = 1000
    max_n = int((N/2) ** 0.5)

    for n in range(2, max_n):
        for m in range(1, n):
            a = n * n - m * m
            b = 2 * n * m
            c = n * n + m * m
            l = a + b + c
            if l == N:
                return a * b * c

if __name__ == '__main__':
    print 'Result: ', solution()
