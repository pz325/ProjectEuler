'''
Pentagonal numbers are generated by the formula, Pn=n(3n-1)/2. The first ten pentagonal numbers are:
1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...
It can be seen that P4 + P7 = 22 + 70 = 92 = P8. However, their difference, 70 - 22 = 48, is not pentagonal.
Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk - Pj| is minimised; what is the value of D?
'''

import math


def get_pentagonal_number(n):
    return n * (3 * n - 1) / 2


def is_pentagonal_number(x):
    n = (1.0 + math.sqrt(1 + 24 * x)) / 6.0
    return n == int(n)

n = 1
pentagonal_numbers = [get_pentagonal_number(n)]
found = False
while(not found):
    n += 1
    new_number = get_pentagonal_number(n)
    for number in pentagonal_numbers[::-1]:
        if is_pentagonal_number(new_number - number):
            if is_pentagonal_number(new_number + number):
                print 'result: ', new_number, number, new_number - number
                found = True
                break
    pentagonal_numbers.append(new_number)
