'''
coin sums

refer to http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
dynamic probramming

1p
0 1 2 3 4 5
1 1 1 1 1 1

2p
0 1 2 3 4 5
1 1 2 2 3 3

5p
0 1 2 3 4 5
1 1 2 2 3 4

'''


def solution():
    coins = (1, 2, 5, 10, 20, 50, 100, 200)
    target = 200

    ways = [0] * (target + 1)
    ways[0] = 1

    for i in coins:
        for j in range(i, target + 1):
            ways[j] += ways[j - i]
    return ways[target]


if __name__ == '__main__':
    print('Result:', solution())    