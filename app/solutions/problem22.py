'''
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938  53 = 49714.

What is the total of all the name scores in the file?
'''
f = open('problem22.txt')
r = f.readlines()[0]
names = r.split(',')
names = [name[1:-1] for name in names]
names.sort()

index = 1
total = 0
for name in names:
    value = sum([ord(ch)-64 for ch in name])
    score = index * value
    total += score
    index += 1
print '==total=='
print total
