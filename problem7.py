from problem3 import prime_factors

count = 1
i = 3
target = 10001
while(True):
    pfs = prime_factors(i)
    if len(pfs) == 1:
        count += 1
        print count, i
    if count == target:
        break
    i += 2
