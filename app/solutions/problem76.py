'''
counting summations

only 1
0 1 2 3 4 5
1 1 1 1 1 1

use 2
0 1 2 3 4 5
1 1 2 2 3 3

use 3
0 1 2 3 4 5
1 1 2 3 4 5

use 4
0 1 2 3 4 5
1 1 2 3 5 6

refer to http://www.mathblog.dk/project-euler-31-combinations-english-currency-denominations/
dynamic programming

'''


def solution():
    target = 100
    ways = [0] * (target + 1)
    ways[0] = 1

    for i in range(1, target):
        for j in range(i, target+1):
            ways[j] += ways[j - i]
    #         print(ways)
    # print(ways)
    return ways[target]


if __name__ == '__main__':
    print('Result', solution())
