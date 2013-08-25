'''
The following iterative sequence is defined for the set of positive integers:

n  n/2 (n is even)
n  3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13  40  20  10  5  16  8  4  2  1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

def next_in_Collatz_sequence(n):
    if n % 2 == 0:
        return n / 2
    else:
        return 3 * n + 1

def Collatz_sequence(n):
    sequence = []
    sequence.append(n)
    while n != 1:
        n = next_in_Collatz_sequence(n)
        sequence.append(n)
    return sequence

seed = 0
max_num_sequence = 0
for i in xrange(999999, 0, -1):
    sequence = Collatz_sequence(i)
    print i, len(sequence)
    if len(sequence) > max_num_sequence:
        max_num_sequence = len(sequence)
        seed = i

print seed, max_num_sequence
