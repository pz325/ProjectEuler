'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''
from util import is_prime

N = 1000000
p = []
for i in xrange(2, N):
    if is_prime(i):
        p.append(i)

limit_reached = False
max_w = 0
for w in xrange(21, len(p)):
    for i in xrange(0, len(p)-w):
        total = sum(p[i:i+w])
        if i == 0 and total >= N:
            limit_reached = True
        if total < N:
            if is_prime(total):
                if w > max_w:
                    max_w = w
                    print 'max w: {w}, total: {total}'.format(w=w, total=total)
        else:
            break
    if limit_reached:
        break
