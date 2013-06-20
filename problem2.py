def fibonacci(n1, n2):
    return n1 + n2

N = 4e6
x1 = 1
x2 = 2
total = 2
while(True):
    x = fibonacci(x1, x2)
    print x
    x1 = x2
    x2 = x
    if x % 2 == 0 and x < N:
        total += x
    elif x > N:
        break

print '== total =='
print total
