pow10 = [1, 10, 100, 1000, 10000, 100000, 1000000]


def isPalindromic(n):
    digits = []
    tmp = n
    while tmp > 0:
        digits.append(tmp % 10)
        tmp /= 10
    length = len(digits)
    revert = 0
    for i in xrange(0, length):
        revert += digits[i] * pow10[length - 1 - i]
    if revert == n:
        return True
    else:
        return False

max_result = 0
for i in xrange(999, 100, -1):
    for j in xrange(999, i - 1, -1):
        result = i * j
        if isPalindromic(result):
            print i, j, result
            if result > max_result:
                max_result = result

print max_result
