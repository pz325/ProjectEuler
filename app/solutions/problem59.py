'''
XOR decryption

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

solution:
    encrypt "common english words"
        we used 'the, and, this, that, but, was'
    
    encrypt pattern, e.g. key is 'key'
        'the'
         key
         eyk
         yke

    find occurance in the decrpyted text then guess key

occurance and key guessing:
    ----
    the
    [('odg', 18), ('god', 18), ('dgo', 18)]
    ----
    was
    [('odg', 10), ('god', 10), ('dgo', 10)]
    ----
    and
    [('odg', 7), ('god', 7), ('dgo', 7)]
    ----
    this
    [('odg', 2), ('god', 2), ('dgo', 2)]
    ----
    that
    [('odg', 2), ('god', 2), ('dgo', 2)]
    ----
    but
    [('pyu', 0), ('xmf', 0), ('xtw', 0)]

use 'god' as key, so we get:

(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.

'''

UPPER_CASES = range(65, 92)
LOWER_CASES = range(97, 123)
OTHERS = [ord(' '), ord('"')]
VALID_CHARS = UPPER_CASES + LOWER_CASES + OTHERS
COMMON_WORDS = [' the ', ' was ', ' and ', ' this ', ' that ', ' but ']

def key_rotator(key_chars):
    '''
    generate rotated key
    '''
    for i in range(len(key_chars)):
        yield key_chars[i:]+key_chars[:i]

def key_generator():
    '''
    generate all keys with 3 lower case letters
    '''
    for a in LOWER_CASES:
        for b in LOWER_CASES:
            for c in LOWER_CASES:
                yield [a, b, c]


def get_string(chars):
    '''
    convert char array to string
    '''
    return ''.join([chr(c) for c in chars])


def get_chars(text):
    '''
    convert string to char array
    '''
    return [ord(c) for c in text]


def xor(text, key):
    '''
    XOR text with key
    @text in char array
    @key in char array
    @return result in char array
    '''
    i = 0
    xor_result = []
    while i < len(text):
        xor_result.append(text[i] ^ key[i % len(key)])
        i += 1
    return xor_result

def compare_array(a1, a2):
    '''
    compare two array with the same length
    @return index where element not equal
    '''
    i = 0
    while i < len(a1):
        if a1[i] != a2[i]:
            return i
        i += 1
    return i


def count_occurance(text, segment):
    '''
    count occurance of segment in text
    @text in char array
    @segment in char array
    @return num occurance
    '''
    num_occuranace = 0
    if len(text) < len(segment):
        return num_occuranace
    
    len_segment = len(segment)
    i = 0
    while i <= len(text)-len_segment:
        j = compare_array(text[i : i+len_segment], segment)
        if j == len(segment):
            # found a match
            num_occuranace += 1
        i = i+1 if j == 0 else i+j

    return num_occuranace


def test_compare_array():
    a1 = [1, 2, 3]
    a2 = [1, 3, 4]
    print(compare_array(a1, a2))

def test_count_occurance():
    text = [1, 2, 3, 1, 2, 1, 2, 1]
    segment = [1, 2]
    print(count_occurance(text, segment))

def test_key_rotator():
    key = [1, 2, 3]
    for k in key_rotator(key):
        print(k)

def find_keys_with_max_hit(key_hit):
    import operator
    sorted_by_hit = sorted(key_hit.items(), key=operator.itemgetter(1), reverse=True)
    return sorted_by_hit

def get_key():
    for w in COMMON_WORDS:
        print('----')
        print(w)
        w_chars = get_chars(w)
        key_hit = {}
        for key_chars in key_generator():
            key = get_string(key_chars)
            for k in key_rotator(key_chars):
                encrypted_w = xor(w_chars, k)
                num_occuranace = count_occurance(encrypted_chars, encrypted_w)
                if key not in key_hit:
                    key_hit[key] = num_occuranace
                else:
                    key_hit[key] += num_occuranace
        max_key = find_keys_with_max_hit(key_hit)
        print(max_key[0:3])


def solution():
    '''
    problem solution
    '''

    # guess_key()

    encrypted_chars = [int(c) for c in open('problem59.txt').read().strip().split(',')]
    key = 'god'
    decrypted = xor(encrypted_chars, get_chars(key))
    print(get_string(decrypted))
    return sum(decrypted)


if __name__ == '__main__':
    result = solution()
    print('Result: ', result)
