'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

1 3 13 31 ...
  5 17 31 ...
  7 21 43 ...
  9 25 49 ...
x_0 = 1, x_n = x_n-1 + 2 + (n - 1) * 8
         x_n = x_n-1 + 4 + (n - 1) * 8
         x_n = x_n-1 + 6 + (n - 1) * 8
         x_n = x_n-1 + 8 + (n - 1) * 8
'''


def total_diag(N, a):
    # print ''
    total = 0
    last = 1
    for n in xrange(1, N+1):
        current = last + a + (n - 1) * 8
        total += current
        last = current
        # print current
    return total

N = 500
total = 1
total += total_diag(N, 2)
total += total_diag(N, 4)
total += total_diag(N, 6)
total += total_diag(N, 8)
print '==result=='
print total
