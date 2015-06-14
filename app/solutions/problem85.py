'''
Counting rectangles

rectangle:
a * b

sub-rectangle:
1 * 1
1 * 2
...
1 * a
2 * 1
2 * 2
...
2 * a
...
b * 1
b * 2
b * a

number of sub rectangle x * y = (a-x+1) * (b-y+1)

2772
'''

def countSubRectangle(a, b):
    count = 0
    for x in range(1, a+1):
        for y in range(1, b+1):
            count += (a - x + 1) * (b - y + 1)
    return count


def solution():
    target = 2000000
    minDiff = target
    resultA, resultB = 0, 0
    for a in range(30, 2000):
        for b in range(30, 2000):
            rects = countSubRectangle(a, b)
            diff = abs(rects - target)
            if diff < minDiff:
                minDiff = diff
                resultA, resultB = a, b
                print(resultA, resultB, minDiff)
            if rects > target:
                break
    print(resultA, resultB, countSubRectangle(resultA, resultB))

    return resultA * resultB


if __name__ == '__main__':
    print('Result:', solution())
