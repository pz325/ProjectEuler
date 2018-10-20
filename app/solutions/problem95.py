# coding=utf-8
'''
Amicable chains

The proper divisors of a number are all the divisors excluding the number itself. For example, the proper divisors of 28 are 1, 2, 4, 7, and 14. As the sum of these divisors is equal to 28, we call it a perfect number.

Interestingly the sum of the proper divisors of 220 is 284 and the sum of the proper divisors of 284 is 220, forming a chain of two numbers. For this reason, 220 and 284 are called an amicable pair.

Perhaps less well known are longer chains. For example, starting with 12496, we form a chain of five numbers:

12496 → 14288 → 15472 → 14536 → 14264 (→ 12496 → ...)

Since this chain returns to its starting point, it is called an amicable chain.

Find the smallest member of the longest amicable chain with no element exceeding one million.
'''

import util

LIMIT = 1000000
checked = []

def sum_proper_divisor(n):
    return sum(util.proper_divisors(n))

def find_amicable_chail(n):
    chain = [n]
    # checked.append(n)
    sp = sum_proper_divisor(n)
    while sp not in chain and sp <= LIMIT :
        chain.append(sp)
        # checked.append(sp)
        sp = sum_proper_divisor(sp)
        if sp > LIMIT or sp == 0:
            # print(chain)
            chain = [n]
            break
        
        if sp in chain and sp != chain[0]:
            # print(chain)
            chain = [n]
            break
        
        # if sp in checked:
        #     chain = [n]
        #     break
    
    if (len(chain) > 1):
        print(chain)
    return chain

def brute_force():
    N = 1000000
    longest_chain = []
    for i in range(12500, N):
        amicable_chain = find_amicable_chail(i)
        if len(amicable_chain) > len(longest_chain):
            longest_chain = amicable_chain

    return min(longest_chain)

@util.timeit
def solution():
    return brute_force()

if __name__ == '__main__':
    result = solution()
    print('Result: {result}'.format(result=result))