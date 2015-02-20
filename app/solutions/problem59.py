'''
XOR decryption

'''

upperCases = range(65, 92)
lowerCases = range(97, 123)
others = [ord(' '), ord('"')]
validChars = upperCases + lowerCases + others

unlikely = [ord(c) for c in 'defghlpqrsw']

def getString(chars):
    return ''.join([chr(c) for c in chars])

def decrypt(text, key):
    i = 0
    keyChars = [ord(c) for c in key]
    result = []
    print('key', key)
    while i < len(text):
        result.append(text[i] ^ keyChars[i % len(key)])
        i += 1
    return result

def solution():
    chars = [int(c) for c in open('problem59.txt').read().strip().split(',')]
    candidate = []
    for c in xrange(97, 123):
        # if c in unlikely: continue
        candidate.append(chr(c))
        print(chr(c), getString([x ^ c for x in chars]))# if c ^ x not in xrange(65, 91) and c ^ x not in xrange(97, 122)]))
    print(candidate)
    # for c in candidate:
        # key = ''.join(['o', c, 'o'])
        # result = decrypt(chars, key)
        # print(getString(result))

    # key = 'm'
    # print(getString(chars))
    # print(len(chars))
    return 0

if __name__ == '__main__':
    result = solution()
    print 'Result: ', result