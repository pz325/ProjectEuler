number = [''] * 1001
number[1] = 'one'
number[2] = 'two'
number[3] = 'three'
number[4] = 'four'
number[5] = 'five'
number[6] = 'six'
number[7] = 'seven'
number[8] = 'eight'
number[9] = 'nine'
number[10] = 'ten'
number[11] = 'eleven'
number[12] = 'twelve'
number[13] = 'thirteen'
number[14] = 'fourteen'
number[15] = 'fifteen'
number[16] = 'sixteen'
number[17] = 'seventeen'
number[18] = 'eighteen'
number[19] = 'nineteen'
number[20] = 'twenty'
number[30] = 'thirty'
number[40] = 'forty'
number[50] = 'fifty'
number[60] = 'sixty'
number[70] = 'seventy'
number[80] = 'eighty'
number[90] = 'ninety'
# #1 ~ #9
for i in xrange(1, 10):
    for j in xrange(2, 10):
        number[j * 10 + i] = number[j * 10] + number[i]
# #00
for i in xrange(1, 10):
    number[i * 100] = number[i] + 'hundred'
# ###
for i in xrange(1, 10):
    for j in xrange(1, 100):
        number[i * 100 + j] = number[i] + 'hundredand' + number[j]
number[1000] = 'onethousand'

total = 0
for i in xrange(1, 1001):
    print i, number[i]
    total += len(number[i])
print total

