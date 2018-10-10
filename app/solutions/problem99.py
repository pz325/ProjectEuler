'''
problem 99

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

709
'''
import math

def compare_exp(x, y):
    '''
    @param x = (a, b)
    @param y = (m, n)
    @return True if a**b > m**n
    affected by precision: e.g. (894483, 504959) v.s. (619415, 518874) (should be lesser, but compare_exp returns True)
    '''
    a = float(x[0])/float(y[1])
    b = math.log(y[0], x[1])
    # print(x[0]**x[1]>y[0]**y[1], a>b)
    return a > b


def solution():
    with open('problem99.txt') as f:
        lines = f.readlines()
    index, m, m_index = 1, 0, 1
    for l in lines:
        a, b = [int(i) for i in l.strip().split(',')]
        t = b * math.log10(a)
        if t > m:
            m = t
            max_index = index
        
        index += 1
    
    return max_index

if __name__ == '__main__':
    print 'Result: ', solution()
