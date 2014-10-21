'''
Powerful digit sum

'''

def solution():
    maxSum = 0
    for a in xrange(1, 101):
        for b in xrange(1, 101):
            c = a ** b
            d = sum([int(s) for s in str(c)])
            if d > maxSum:
                maxSum = d
    return maxSum

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
