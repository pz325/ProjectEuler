'''
Cubic permutations

The cube, 41063625 (345^3), can be permuted to produce two other cubes: 
56623104 (384^3) and 66430125 (405^3). 

In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''

def solution():
    count = {}
    # search 100 ~ 9999
    for x in xrange(100, 10000):
        cube = x*x*x
        key = ''.join(sorted(str(cube)))
        if key not in count:
            count[key] = [cube]
        else:
            count[key].append(cube)

    minCube = 99999*99999*99999
    for k, v in count.items():
        if len(count[k]) == 5 and min(count[k]) < minCube:
            minCube = min(count[k])
    return minCube

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
