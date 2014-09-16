'''

Pandigital products

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

analysis:

xx * xxx = xxxx
pattern 1:
	x2 - xx[3,4,7,8,9]
	x3 - xx[2,4,6,7,8,9]
	x4 - xx[2,3,7,8,9]
	x6 - xx[3,7,9]
	x7 - xx[2,3,4,6,8,9]
	x8 - xx[2,3,4,7,9]
	x9 - xx[2,3,4,5,6,7,8]

x * xxxx = xxxx
pattern 2:
	2 - [1-4]xx[3,4,7,8,9]
	3 - [1-3]xx[2,4,6,7,8,9]
	4 - [1-2]xx[2,3,7,8,9]
	6 - 1xx[3,7,9]
	7 - 1xx[2,3,4,6,8,9]
	8 - 1xx[2,3,4,7,9]
	9 - 1xx[2,3,4,5,6,7,8]
'''

def getPattern1():
	r = set()
	ends = [
		[],
		[],
		[3,4,7,8,9],  # 2
		[2,4,6,7,8,9], # 3
		[2,3,7,8,9], # 4
		[],
		[3,7,9], # 6
		[2,3,4,6,8,9], # 7
		[2,3,4,7,9], # 8
		[2,3,4,5,6,7,8] #9
	]
	for end1 in xrange(10):  
		for end2 in ends[end1]:
			for i in xrange(1, 10):
				if i == end1 or i == end2: continue
				for j in xrange(1, 10):
					if j == end1 or j == end2 or j == i: continue
					for k in xrange(1, 10):
						if k == end1 or k == end2 or k == j or k == i: continue
						p1 = i * 10 + end1
						p2 = j * 100 + k * 10 + end2
						prod = p1 * p2

						digits = [int(d) for d in list(str(prod))]
						if 0 in digits: continue
						if len(digits) != 4: continue
						uniqueDigits = set(digits)
						if len(uniqueDigits) != 4: continue
						if end1 not in digits and end2 not in digits and i not in digits and j not in digits and k not in digits:
							r.add((p1, p2, prod))
	print(r)
	return r


def getPattern2():
	r = set()
	ends = [
		([], []),
		([], []),
		([1,2,3,4], [3,4,7,8,9]),  # 2
		([1,2,3], [2,4,6,7,8,9]), # 3
		([1,2], [2,3,7,8,9]), # 4
		([],[]),
		([1], [3,7,9]), # 6
		([1], [2,3,4,6,8,9]), # 7
		([1], [2,3,4,7,9]), # 8
		([1], [2,3,4,5,6,7,8]) #9
	]
	for end1 in xrange(10):
		for start2 in ends[end1][0]:
			if start2 == end1: continue
			for end2 in ends[end1][1]:
				if end2 == start2: continue
				for i in xrange(1, 10):
					if i == end1 or i == start2 or i == end2: continue
					for j in xrange(1, 10):
						if j == end1 or j == start2 or j == end2 or j == i: continue
						p1 = end1
						p2 = start2 * 1000 + i * 100 + j * 10 + end2
						prod = p1 * p2

						digits = [int(d) for d in list(str(prod))]
						if 0 in digits: continue
						if len(digits) != 4: continue
						uniqueDigits = set(digits)
						if len(uniqueDigits) != 4: continue
						if end1 not in digits and start2 not in digits and end2 not in digits and i not in digits and j not in digits:
							r.add((p1, p2, prod))
	print(r)
	return r

def solution():
    p1 = getPattern1()
    p2 = getPattern2()
    result = set()
    for p in p1:
    	result.add(p[2])
    for p in p2:
    	result.add(p[2])
    return sum(result)


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result
