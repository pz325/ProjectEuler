found = False
for c in xrange(1, 1000):
    for b in xrange(1, c):
        for a in xrange(1, b):
            if a * a + b * b == c * c:
                print a, b, c
                if a + b + c == 1000:
                    print a * b * c
                    found = True
                    break
        if found:
            break
    if found:
        break
