'''
Starting in the top left corner of a 22 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 2020 grid?
'''

import copy

n = [1]

for i in xrange(0, 19):
    last = copy.deepcopy(n)
    n.append(0)
    n[0] = 1
    for j in xrange(1, len(last)):
        n[j] = n[j-1] + last[j]
    n[len(last)] = 2 * n[len(last)-1]
print '==result=='
print 2 * sum(n)
