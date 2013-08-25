'''
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn1 + Fn2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?
'''


def fibonacci(n1, n2):
    return n1+n2


def digits(n):
    num = 0
    d = []
    while n > 0:
        d.append(n % 10)
        num += 1
        n /= 10
    return num, d[::-1]

[num, d] = digits(109)

n1 = 1
n2 = 1
num = 1
count = 2
while num < 1000:
    n = fibonacci(n1, n2)
    [num, d] = digits(n)
    count += 1
    n1 = n2
    n2 = n
print '==result=='
print count
