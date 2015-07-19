'''
Monopoly odds


Monte Carlo simulation....

101524
'''

from random import randint


board = [
    'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
    'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
    'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
    'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
]

CC_target = [0, 10]   # 2/16
CH_target = [0, 10, 11, 24, 39, 5, '+R', '+R', '+U', '-3']        # 10/16


def roll():
    MAX_DICE = 4
    return randint(1, MAX_DICE), randint(1, MAX_DICE)


def move(pos, dice1, dice2):
    return (pos + dice1 + dice2) % 40


def moveToNextSpecialSlot(pos, specialSlot):
    '''
    @specialSlot  'R' or 'U'
    '''
    targetPos = pos
    while specialSlot not in board[targetPos]:
        targetPos += 1
        if targetPos == 40:
            targetPos = 0
    return targetPos


def applyCCRule(pos):
    targetPos = pos
    if randint(1, 8) == 1:
        ccCard = randint(0, 1)
        targetPos = CC_target[ccCard]
    return targetPos


def applyCHRule(pos):
    targetPos = pos
    if randint(1, 16) <= 10:
        chCard = randint(0, 9)
        if isinstance(CH_target[chCard], int):
            targetPos = CH_target[chCard]
        else:
            if '+R' == CH_target[chCard]:
                targetPos = moveToNextSpecialSlot(pos, 'R')
            if '+U' == CH_target[chCard]:
                targetPos = moveToNextSpecialSlot(pos, 'U')
            if '-3' == CH_target[chCard]:
                targetPos -= 3
    return targetPos


def applyRule(pos):
    targetPos = pos
    if board[pos] == 'G2J':
        targetPos = 10     # JAIL
    if 'CC' in board[pos]:
        targetPos = applyCCRule(pos)
    if 'CH' in board[pos]:
        targetPos = applyCHRule(pos)

    return targetPos


def topThreeIndex(posCount):
    sortedPosCount = sorted(enumerate(posCount), key=lambda p: p[1], reverse=True)
    return sortedPosCount[0:3]


def solution():
    pos = 0
    N = 1000000
    countConsecutiveDouble = 0
    posCount = [0] * 40
    for _ in range(0, N):
        dice1, dice2 = roll()
        if dice1 == dice2:
            countConsecutiveDouble += 1
        else:
            countConsecutiveDouble = 0
        if countConsecutiveDouble == 3:
            pos = 10    # JAIL
            countConsecutiveDouble = 0
        else:
            pos = move(pos, dice1, dice2)
            targetPos = applyRule(pos)
            while targetPos != pos:
                pos = targetPos
                targetPos = applyRule(pos)
            pos = targetPos

        posCount[pos] += 1

    return topThreeIndex(posCount)
    # return 0


if __name__ == '__main__':
    print('Result: ', solution())
