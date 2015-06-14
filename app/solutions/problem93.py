'''
Arithmetic expressions

brute force:

expression combination:
(0, 1), 2, 3
(0, 1), (2, 3)
(1, 2), 0, 3
(1, 2), 3, 0
(2, 3), 1, 0

1258
'''
from itertools import permutations, product

def opAdd(a, b):
    return a + b
def opSub(a, b):
    return a - b
def opMul(a, b):
    return a * b
def opDiv(a, b):
    return float(a) / float(b)

def printOp(op):
    if op == opAdd:
        return '+'
    elif op == opSub:
        return '-'
    elif op == opMul:
        return '*'
    elif op == opDiv:
        return '/'

def printExpression(numbers, ops, cal):
    if cal == calExpression1:
        expression = '((' + str(numbers[0]) \
            + printOp(ops[0]) \
            + str(numbers[1]) + ')' \
            + printOp(ops[1]) \
            + str(numbers[2]) + ')' \
            + printOp(ops[2]) \
            + str(numbers[3])
    elif cal == calExpression2:
        expression = '(' + str(numbers[0]) \
        + printOp(ops[0]) \
        + str(numbers[1]) + ')' \
        + printOp(ops[1]) \
        + '(' + str(numbers[2]) \
        + printOp(ops[2]) \
        + str(numbers[3]) + ')'

    elif cal == calExpression3:
        expression = '(' + str(numbers[0]) \
        + printOp(ops[0]) \
        + '(' + str(numbers[1]) \
        + printOp(ops[1]) \
        + str(numbers[2]) + '))' \
        + printOp(ops[2]) \
        + str(numbers[3])

    elif cal == calExpression4:
        expression = str(numbers[0]) \
        + printOp(ops[0]) \
        + '((' + str(numbers[1]) \
        + printOp(ops[1]) \
        + str(numbers[2]) + ')'\
        + printOp(ops[2]) \
        + str(numbers[3]) + ')'

    else:
        expression = str(numbers[0]) \
        + printOp(ops[0]) \
        + '(' + str(numbers[1]) \
        + printOp(ops[1]) \
        + '(' + str(numbers[2]) \
        + printOp(ops[2]) \
        + str(numbers[3]) + '))'

    return expression

def calExpression1(numbers, ops):
    '''
    (0, 1), 2, 3
    '''
    r = ops[0](numbers[0], numbers[1])
    r = ops[1](r, numbers[2])
    r = ops[2](r, numbers[3])
    return r

def calExpression2(numbers, ops):
    '''
    (0, 1), (2, 3)
    '''
    r = ops[0](numbers[0], numbers[1])
    p = ops[2](numbers[2], numbers[3])
    r = ops[1](r, p)
    return r
def calExpression3(numbers, ops):
    '''
    (1, 2), 0, 3
    '''
    r = ops[1](numbers[1], numbers[2])
    r = ops[0](numbers[0], r)
    r = ops[2](r, numbers[3])
    return r
def calExpression4(numbers, ops):
    '''
    (1, 2), 3, 0
    '''
    r = ops[1](numbers[1], numbers[2])
    r = ops[2](r, numbers[3])
    r = ops[0](numbers[0],r)
    return r
def calExpression5(numbers, ops):
    '''
    (2, 3), 1, 0
    '''
    r = ops[2](numbers[2], numbers[3])
    r = ops[1](numbers[1], r)
    r = ops[0](numbers[0], r)
    return r 

def findLargestConsecutive(a, b, c, d):
    numbers = [a, b, c, d]
    ops = [opAdd, opSub, opMul, opDiv]
    cals = [calExpression1, calExpression2, calExpression3, calExpression4, calExpression5]
    results = set()
    for n in permutations(numbers):
        for o in product(ops, repeat=3):
            for c in cals:
                try:
                    r = c(n, o)
                    # print(printExpression(n, o, c))
                    if r > 0 and float(r).is_integer():
                        (n, o, c)
                        results.add(r)
                except ZeroDivisionError, e:
                    continue
    largestConsecutive = 1
    for x in range(1, max(results)):
        if x not in results:
            largestConsecutive = x - 1
            break
    return largestConsecutive

def solution():
    largestConsecutive = 28
    ra, rb, rc, rd = 1, 2, 3, 4
    for a in range(1, 10):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    r = findLargestConsecutive(a, b, c, d)
                    if r > largestConsecutive:
                        largestConsecutive = r
                        ra, rb, rc, rd = a, b, c, d
    return ''.join([str(ra), str(rb), str(rc), str(rd)])

if __name__ == '__main__':
    print('Result:', solution())
