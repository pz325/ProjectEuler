'''
Digit factorial chains

answer: 402
'''
fractorials = {}
fractorials[0] = 1
fractorials[1] = 1
fractorials[2] = 2
fractorials[3] = 2 * 3
fractorials[4] = 2 * 3 * 4
fractorials[5] = 2 * 3 * 4 * 5
fractorials[6] = 2 * 3 * 4 * 5 * 6
fractorials[7] = 2 * 3 * 4 * 5 * 6 * 7
fractorials[8] = 2 * 3 * 4 * 5 * 6 * 7 * 8
fractorials[9] = 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9

def factorialChain(n):
    chain = set([n])
    while True:
        digits = [int(c) for c in str(n)]
        n = sum([fractorials[i] for i in digits])
        if n not in chain:
            chain.add(n)
        else:
            break
    return chain

def solution():
    N = 1000000
    count = 0
    for i in range(2, N):
        if len(factorialChain(i)) == 60:
            count += 1
            print(i)
    return count

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
