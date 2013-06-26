'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2 =   0.5
1/3 =   0.(3)
1/4 =   0.25
1/5 =   0.2
1/6 =   0.1(6)
1/7 =   0.(142857)
1/8 =   0.125
1/9 =   0.(1)
1/10    =   0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d  1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''


def unit_fraction(n):
    results = []
    numerator = 1
    found = False
    while not found:
        while numerator < n:
            numerator *= 10
            quotient = numerator / n
            remainder = numerator % n
            if quotient == 0 and remainder == 0:
                found = True
                break
            key = (quotient, remainder)
            try:
                index = results.index(key)
            except ValueError, e:
                index = -1
            
            if index >= 0:
                found = True
                break
            else:
                results.append(key)
        numerator = remainder
    return index, results

N = 1000
max_run = 0
d = 0
for i in xrange(7, N):
    [index, results] = unit_fraction(i)
    result = len(results) - index
    if result > max_run:
        max_run = result
        d = i

print '==result=='
print d
