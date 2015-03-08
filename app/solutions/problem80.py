'''
Square root digital expansion


http://en.wikipedia.org/wiki/Methods_of_computing_square_roots

Digit-by-digit calculation


digital sum of the first one hundred decimal digits
    include 1 before the decimal point!!!

http://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil
    1st 1m digits of sqrt 2
    help to verify

40886
'''

from util import digits_2
import math

def digitByDigitSqrt(bringDown, reminder, p):
    # print('[digitByDigitSqrt]: bringDown={b}, reminder={r}, p={p}'.format(b=bringDown, r=reminder, p=p))
    # append to reminder
    c = reminder * 100 + bringDown
    # find greatest x so that x * (20 * p + x ) <= c
    x = 0
    while True:
        z = x + 1
        if z * (20 * p + z) > c:
            break
        x = z 
    y = x * (20 * p + x)
    reminder = c - y
    p = 10 * p + x
    # print('[digitByDigitSqrt]: x={x}, reminder={r}, p={p}'.format(x=x, r=reminder, p=p))
    return x, reminder, p


def sqrt_z(i, ndigits=4):
    '''
    calculate sqrt of i, which is an integer
    digit by digit calculation

    @param i
    @param ndigits precision after decimal point. 4 by default
    '''
    p = 0
    reminder = 0
    sqrtRoot = 0
    numAfterDecimal = 0
    digitBeforeDecimal = []
    digitAfterDecimal = []
    #before decimal
    while True:
        numDigits = digits_2(i)
        if i == 0:
            break
        elif numDigits == 1 or numDigits == 2:
            bringDown = i
            i = 0
        else:
            if numDigits % 2 == 1:
                k = 10 ** (numDigits - 1)
            else:
                k = 10 ** (numDigits - 2)
            bringDown = i / k
            i = i - bringDown * k
        

        l = math.ceil(numDigits / 2.0)
        x, reminder, p = digitByDigitSqrt(bringDown, reminder, p)
        if (ndigits < 10):
            sqrtRoot += x * 10 ** (l-1)
        digitBeforeDecimal.append(x)
        if reminder == 0 and i == 0:
            break

    #after decimal
    while True:
        if reminder == 0:
            break
        bringDown = 0
        x, reminder, p = digitByDigitSqrt(bringDown, reminder, p)
        numAfterDecimal += 1
        if (ndigits < 10):
            sqrtRoot += x * 10 ** (-1 * numAfterDecimal)
        digitAfterDecimal.append(x)
        if numAfterDecimal >= ndigits:
            break
    
    return sqrtRoot, digitBeforeDecimal, digitAfterDecimal


def solution():
    result = 0
    for x in range(1, 101):
        _, digitBeforeDecimal, digitAfterDecimal = sqrt_z(x, 99)
        s = 0
        if len(digitAfterDecimal) > 0:
            s = sum(digitBeforeDecimal) + sum(digitAfterDecimal)
        result += s
        # print(x, s)
        # print(digitBeforeDecimal)
        # print(digitAfterDecimal)

    return result


if __name__ == '__main__':
    print('Result', solution())