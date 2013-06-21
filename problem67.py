'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
'''
f = open('problem67.txt')
triangle = f.readlines()

# dynamic programming
import copy
total = [int(triangle[0])]
for i in xrange(1, len(triangle)):
    last = copy.deepcopy(total)
    total.append(0)
    n = triangle[i].split(' ')
    total[0] = last[0] + int(n[0])
    total[-1] = last[-1] + int(n[-1])
    for j in xrange(1, len(n)-1):
        t1 = last[j-1] + int(n[j])
        t2 = last[j] + int(n[j])
        total[j] = max(t1, t2)
    # print '===='
    # print last
    # print n
    # print total
print max(total)
