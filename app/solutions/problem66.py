'''
Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 - D*y^2 = 1

For example, when D=13, the minimal solution in x is 649^2 - 13x180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 - 2x2^2 = 1
2^2 - 3x1^2 = 1
9^2 - 5x4^2 = 1
5^2 - 6x2^2 = 1
8^2 - 7x3^2 = 1

Hence, by considering minimal solutions in x for D <=7, the largest x is obtained when D=5.

Find the value of D <= 1000 in minimal solutions of x for which the largest value of x is obtained.

'''


'''
possible ending digits:

  D    y        x
* 0    [0-9]    [1,9]
* 1    [2,8]    5
* 1    [5]      [4,6]
* 1    [0]      [1,9]
* 2    [2,3,7,8] [3,7]
* 2    [5,0]     [1,9]
* 3    [1,9]    [2,8]
* 3    [4,6]    [3,7]
* 3    5         [4,6]
* 3    0         [1,9]
* 4    [1,4,6,9] 5
* 4    [5,0]     [1,9]
* 5    [1,3,5,7,9] [4,6]
* 5    [0,2,3,4,8] [1,9]
* 6    [2,3,7,8,] 5
* 6    [5,0]     [1,9]
* 7    [2,8]       [3,7]
* 7    [3,7]     [2,8]
* 7    [5]       [4,6]
* 7    [0]       [1,9]
* 8    [1,4,6,9]  [3,7]
* 8    [5,0]     [1,9]
* 9    [4,6]     5
* 9    5         [4,6]
* 9    0         [1,9]
'''

from itertools import product
import math

def genPossibleEndings():
    possible_Dyx_Endings = []
    possible_Dy_Endings = []
    D_y_x = [
    ([0], range(10), [1, 9]),
    ([1], [2, 8], [5]),
    ([1], [5], [4, 6]),
    ([1, 3, 7, 9], [0], [1, 9]),
    ([2, 4, 6, 8], [5, 0], [1, 9]),
    ([2], [2,3,7,8], [3,7]),
    ([3], [1, 9], [2,8]),
    ([3], [4,6],[3,7]),
    ([3], [5], [4,6]),
    ([4], [1,4,6,9], [5]),
    ([5], [1,3,5,7,9], [4,6]),
    ([5], [0,2,4,6,8], [1,9]),
    ([6], [2,3,7,8], [5]),
    ([7], [2,8], [3,7]),
    ([7], [3,7], [2,8]),
    ([7], [5], [4,6]),
    ([8], [1,4,6,9], [3,7]),
    ([9], [4,6], [5]),
    ([9], [5], [4,6]),
    ]
    for (D, y, x) in D_y_x:
        possible_Dyx_Endings.extend(list(product(D, y, x)))
        possible_Dy_Endings.extend(list(product(D, y)))
    
    return possible_Dyx_Endings, possible_Dy_Endings


def isSquare(n):
    sqrtn = math.sqrt(n)
    return int(sqrtn) == sqrtn


def solution():
    MAX_D = 1000
    possible_Dyx_Endings, possible_Dy_Endings = genPossibleEndings()
    minD, minx = 2, 1
    for D in xrange(2, MAX_D):
        if isSquare(D): continue
        y = 1
        while (D%10, y%10) not in possible_Dy_Endings:
            y += 1
        while True:
            oneDyy = 1 + D * y * y
            x = int(math.sqrt(oneDyy))-1
            while (D%10, y%10, x%10) not in possible_Dyx_Endings:
                x += 1
                # print(D, y, x, x*x, oneDyy, x*x-oneDyy)
                if x*x < oneDyy:
                    break
                # raw_input("[x+=1] Press Enter to continue...")
            if x * x == oneDyy:
                print(D, x)
                if x > minx:
                    minx, minD = x, D
                break
            else:
                while True:
                    y += 1
                    # raw_input("[y+=1] Press Enter to continue...")
                    # print(D, y, x, x*x, oneDyy, x*x-oneDyy)
                    if (D%10, y%10) in possible_Dy_Endings: break
            # if y > 5:
            #     break
        # break
    return minx

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
