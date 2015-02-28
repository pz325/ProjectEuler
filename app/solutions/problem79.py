'''
Passcode derivation

read in 'problem79.txt'

sequence maintained permutation
=> generate possible combination
=> shortest length
'''

def sequenceMaintainedPermutation(password, key):
    '''
    generate new passwords using sequence maintaned permutation
    '''
    # print('==== start sequence maintained permutation ====')
    # print('{k} against {p}'.format(k=key, p=password))
    passwords = set()
    passwords.add(password)
    previousKeyIndex = -1
    for i in range(0, len(key)):
        newPasswords = set()
        for password in passwords:
            if key[i] in password:
                # print('{c} of {k} found in {p}'.format(c=key[i], k=key, p=password))
                newPasswords.add(password)
                continue
            if i > 0:
                previousKeyIndex = password.find(key[i-1])
                # print('prev char: {c} at {index} in {p}'.format(c=key[i-1], index=previousKeyIndex, p=password))
            # 0
            if previousKeyIndex < 0:
                newPasswords.add(key[i]+password)
            # middle
            for j in range(0, len(password)):
                if j > previousKeyIndex:
                    p = password[0:j] + key[i] + password[j:]
                    newPasswords.add(p)    
            # last
            newPasswords.add(password+key[i])
            
            # print('added {c}, so passwords are {p}'.format(c=key[i], p=newPasswords))
        passwords = newPasswords
    # print('permutation:', key, passwords)
    return newPasswords

def allIn(key, password):
    '''
    check whether all key in password
    '''
    isAllIn = True
    for c in key:
        if password.find(c) == -1:
            isAllIn = False
            break
    return isAllIn

def inSequence(key, password):
    '''
    check whether key is in sequence for the given password
    '''
    # print('check {k} in {p}'.format(k=key, p=password))
    isInSequence = True
    for i in range(0, len(key)-1):
        # print('find {c} at {index} in {p}'.format(c=key[i], index=password.find(key[i]), p=password))
        if password.find(key[i]) > password.find(key[i+1]):
            isInSequence = False;
            break
    # print('return {t}'.format(t=isInSequence))
    return isInSequence


def solution():
    passwords = set()
    for key in open('problem79.txt'):
        key = key.strip()
        
        # print('password:', passwords)
        # print('key:', key)

        newPasswords = set()
        if len(passwords) == 0:
            passwords.add(key)
            continue
        for password in passwords:
            if allIn(key, password):
                if inSequence(key, password):
                    newPasswords.add(password)
            else:
                newPasswords.update(sequenceMaintainedPermutation(password, key))
                
        passwords = newPasswords
        
    minLength = 1000000
    result = ''
    for password in passwords:
        if len(password) < minLength:
            result = password
    return result

if __name__ == '__main__':
    print('Result', solution())