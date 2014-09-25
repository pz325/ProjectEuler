'''

Spiral primes

answer: 26241
'''

from util import is_prime


def solution():
	ratio = 1.0
	start = 1
	step = 2
	count = 1
	countPrime = 0
	side = 1
	while ratio > 0.1:
		diagonals = [start + i * step for i in xrange(1, 5)]
		# print(diagonals)
		for n in diagonals:
			if is_prime(n): countPrime += 1
		count += 4
		
		ratio = float(countPrime) / float(count)
		# print(countPrime, count, ratio)
		# print(start, step, side)
		start = diagonals[3]
		step += 2
		side += 1
	return (side - 1) * 2 + 1


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result