'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
def fibonacci(n1, n2):
    return n1 + n2

def solution():
    N = 4e6
    x1 = 1
    x2 = 2
    total = 2
    while(True):
        x = fibonacci(x1, x2)
        # print x
        x1 = x2
        x2 = x
        if x % 2 == 0 and x < N:
            total += x
        elif x > N:
            break
    return total

if __name__ == '__main__':
    print 'Result: ', solution()