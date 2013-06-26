'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
from util import is_prime
from util import digits


def permutable(x, y):
    [num, dx] = digits(x)
    [num, dy] = digits(y)
    strx = reduce(lambda x, y: ''.join([str(x), str(y)]), sorted(dx), '')
    stry = reduce(lambda x, y: ''.join([str(x), str(y)]), sorted(dy), '')
    return strx == stry


def has_increasing_sequence(s):
    for i in xrange(0, len(s)-2):
        tmp_s = s[i:]
        d = [x - tmp_s[0] for x in tmp_s]
        for j in xrange(1, len(d)):
            for k in xrange(j+1, len(d)):
                if d[k] == 2 * d[j]:
                    return True, i, j, k
    return False, 0, 0, 0

p = []
for i in xrange(1000, 10000):
    if is_prime(i):
        p.append(i)

for i in xrange(0, len(p)):
    permutable_sequence = [p[i]]
    for j in xrange(i+1, len(p)):
        if permutable(p[i], p[j]):
            permutable_sequence.append(p[j])
    if len(permutable_sequence) > 3:
        # print permutable_sequence
        his, l, m, n = has_increasing_sequence(permutable_sequence)
        if his:
            print permutable_sequence, l, m, n
