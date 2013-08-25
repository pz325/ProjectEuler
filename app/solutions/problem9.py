'''
A Pythagorean triplet is a set of three natural numbers, a  b  c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def solution():
    found = False
    for c in xrange(1, 1000):
        for b in xrange(1, c):
            for a in xrange(1, b):
                if a * a + b * b == c * c:
                    # print a, b, c
                    if a + b + c == 1000:
                        result = a * b * c
                        found = True
                        break
            if found:
                break
        if found:
            break
    return result

if __name__ == '__main__':
    print 'Result: ', solution()