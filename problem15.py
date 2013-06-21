x = pow(2, 1000)
total = 0
while x > 0:
    digit = x % 10
    total += digit
    x /= 10
print total
