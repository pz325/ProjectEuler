'''
Bouncy numbers

1587000
'''

from util import digits

def isBouncyNumber(n):
    numDigits, digitList = digits(n)
    if numDigits < 2:
        return False
    index = 0
    trend = 0
    while trend == 0 and index < numDigits-1:
        trend = digitList[index] - digitList[index+1]
        index += 1
    # print(trend, index)
    for i in range(index, numDigits-1):
        t = digitList[i] - digitList[i+1]
        if t * trend < 0: 
            return True
    return False


def solution():
    percentage = 0
    n = 100
    numBouncyNumber = 0
    while True:
        if isBouncyNumber(n):
            numBouncyNumber += 1
            percentage = float(numBouncyNumber) / float(n)
            if percentage == 0.99:
                break;
        n += 1
        if n % 100000 == 0:
            print(n, percentage)
    print(n, percentage)
    return n

if __name__ == '__main__':
    print('Result', solution())