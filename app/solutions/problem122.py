'''
Efficient exponentiation

x[n+1] = x[n] + x[0]
       = x[n] + x[1]
       = ...
       = x[n] + x[n-1]
       = x[n] + x[n]

x[0] = 1

expand branches and then prune to keep unique adding pairs

1582
'''        


def printLevel(level):
    for coefficients in level:
        print(coefficients)


def newNumberInLevel(level):
    newNumbers = set()
    for coefficients in level:
        newNumbers.add(coefficients[-1])
    return newNumbers


def generateNextLevel(prevLevel):
    '''
    prevLevel is a list of list
    [
        [2, 3]
        [2, 4]
    ]

    nextLevel is also a list of list
    [
        [2, 3, 5]
        [2, 3, 6]
        [2, 4, 6]
        [2, 4, 8]
    ]
    prune, keep only unique pairs
    [
        [2, 3, 5]
        [2, 3, 6]
        [4, 6]
        [2, 4, 8]
    ]
    '''
    nextLevel = []
    # expand
    for coefficients in prevLevel:
        for x in range(0, len(coefficients)):
            newCoefficients = coefficients[:]    
            newCoefficients.append(coefficients[-1] + coefficients[x])
            nextLevel.append(newCoefficients)
    
    # prune step 1, keep only unique pairs
    uniqueAddingPair = set()
    for coefficients in nextLevel:
        toDelete = []
        for x in range(0, len(coefficients)-1):
            addingPair = (coefficients[x], coefficients[-1])
            if addingPair not in uniqueAddingPair:
                uniqueAddingPair.add(addingPair)
            else:
                toDelete.append(coefficients[x])
        for x in toDelete:
            coefficients.remove(x)

    return nextLevel


def solution():
    currentLevel = []
    currentLevel.append([1, 2])

    k = 200
    n = 2

    result = {1:0, 2:1}
    cont = True
    while cont:
        currentLevel = generateNextLevel(currentLevel)
        newNumbers = newNumberInLevel(currentLevel)
        for x in newNumbers:
            if x not in result:
                result[x] = n
        # check result
        cont = False
        for x in range(1, k+1):
            if x not in result:
                cont = True
                break
        n += 1
        # print(result)

    sumResult = 0
    for x in range(1, k+1):
        sumResult += result[x]
    return sumResult



if __name__ == '__main__':
    print('Result', solution())
