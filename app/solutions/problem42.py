'''
The nth term of the sequence of triangle numbers is given by, tn = 1/2 * n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
'''

base = 64;
triangleNumber = [1, 3, 6, 10, 15, 21, 28, 
    36, 45, 55, 66, 78, 91, 105, 120, 136, 153, 171, 190, 210, 
    231, 253, 276, 300, 325, 351, 378, 406, 435, 465, 496, 528, 
    561, 595, 630, 666, 703, 741, 780, 820, 861, 903, 946, 990, 
    1035, 1081, 1128, 1176, 1225, 1275]

def main():
    count = 0
    words = [w[1:len(w)-1] for w in open('problem42.txt').read().split(',')]
    for w in words:
        score = sum([ord(ch) - base for ch in w])
        if score in triangleNumber:
            count += 1

    print 'result: ', count


if __name__ == '__main__':
    main()
