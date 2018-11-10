'''
Palindromic sums

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 6^2 + 7^2 + 8^2 + 9^2 + 10^2 + 11^2 + 12^2.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 0^2 + 1^2 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 10^8 that are both palindromic and can be written as the sum of consecutive squares.

'''
import util

ANSWER = 2906969179


def solution():
    N = 10 ** 8
    p = set()
    start = 1
    while True:
        end = start + 1
        sum_square = start ** 2
        while True:
            sum_square += end ** 2
            if sum_square > N:
                break
            if util.isPalindromic(sum_square):
                # print(sum_square, range(start, end))
                p.add(sum_square)
            end += 1
        if start**2 > N:
            break
        else:
            start += 1

    result = sum(p)
    return result


if __name__ == '__main__':
    import time
    start_time = time.time()
    result = solution()
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Result: %s" % result)
