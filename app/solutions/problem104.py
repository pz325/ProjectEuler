# -*- coding: utf-8 -*-
'''
Pandigital Fibonacci ends

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

329468
'''
import math
from util import digits


def is_pandigital(a):
    _, d = digits(a)
    return (0 not in d) and (len(set(a)) == 9)


def solution():
    '''
    problem solution
    '''
    n1 = 1
    n2 = 1
    k = 3
    while True:
        n = n1 + n2
        num_digits = int(math.ceil(math.log10(n)))
        if num_digits < 9:
            n1, n2 = n2, n
            k += 1
            continue
        last_9_digits = n % (10 ** 9)
        first_9_digits = n / (10 ** (num_digits - 9))
        # print(k, n, num_digits, last_9_digits, first_9_digits)
        # if is_pandigital(last_9_digits):
        #     print(k, num_digits, last_9_digits, first_9_digits)
        #     break
        # if is_pandigital(first_9_digits):
        #     print(k, num_digits, last_9_digits, first_9_digits)
        #     break
        if is_pandigital(last_9_digits) and is_pandigital(first_9_digits):
            print(k, num_digits, last_9_digits, first_9_digits)
            break
        n1, n2 = n2, n
        k += 1
        if 0 == k%2000:
            print('searching at: ', k, num_digits)
 
    return k



if __name__ == '__main__':
    result = solution()
    print('Result: ', result)
