'''
Poker hands

In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

Consider the following five hands dealt to two players:

Hand        Player 1        Player 2        Winner
1       5H 5C 6S 7S KD
Pair of Fives
    2C 3S 8S 8D TD
Pair of Eights
    Player 2
2       5D 8C 9S JS AC
Highest card Ace
    2C 5C 7D 8S QH
Highest card Queen
    Player 1
3       2D 9C AS AH AC
Three Aces
    3D 6D 7D TD QD
Flush with Diamonds
    Player 2
4       4D 6S 9H QH QC
Pair of Queens
Highest card Nine
    3D 6D 7H QD QS
Pair of Queens
Highest card Seven
    Player 1
5       2H 2D 4C 4D 4S
Full House
With Three Fours
    3C 3D 3S 9S 9D
Full House
with Three Threes
    Player 1
The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''




def organise(hand):
    values = []
    suits = []
    for c in hand:
        value, suit = list(c)
        if value == 'T': 
            value = 10
        elif value == 'J':
            value = 11
        elif value == 'Q':
            value = 12
        elif value == 'K':
            value = 13
        elif value == 'A':
            value = 14
        else:
            value = int(value) 
        values.append(value)
        suits.append(suit)
    repeatValues = countRepeats(values)
    repeatSuits = countRepeats(suits)
    return repeatValues, repeatSuits



def isFlush(repeatSuits):
    return len(repeatSuits) == 1

def isStraight(repeatValues):
    return len(repeatValues) == 5 and repeatValues[0][0] - repeatValues[4][0] == 4

def isStraightFlush(repeatValues, repeatSuits):
    return isFlush(repeatSuits) and isStraight(repeatValues)

def isRoyalStraight(repeatValues, repeatSuits):
    return isFlush(repeatSuits) and isStraight(repeatValues) and repeatValues[0][0] == 14

def isFourAKind(repeatValues):
    return len(repeatValues) == 2 and (repeatValues[0][1] == 4 or repeatValues[1][1] == 4)

def isFullHouse(repeatValues):
    return len(repeatValues) == 2 and (repeatValues[0][1] == 3 or repeatValues[1][1] == 3)

def isThreeAKind(repeatValues):
    return len(repeatValues) == 3 and (repeatValues[0][1] == 3 or repeatValues[1][1] == 3 or repeatValues[2][1] == 3)

def isTwoPairs(repeatValues):
    return len(repeatValues) == 3 and (repeatValues[0][1] == 2 or repeatValues[1][1] == 2 or repeatValues[2][1] == 2)

def isOnePair(repeatValues):
    return len(repeatValues) == 4

def countRepeats(values):
    '''
    
    check in sequence, for repeats
    '''
    values = sorted(values, reverse=True)
    repeats = []
    curr = values[0]
    count = 1
    for i in xrange(1, 5):
        if values[i] == curr:
            count += 1
        else:
            repeats.append((curr, count))
            curr = values[i]
            count = 1
    repeats.append((curr, count))
    return repeats


'''
0 - high card
1 - one pair
2 - two pairs
3 - three a kind
4 - straight
5 - flush            -- same suit
6 - full house
7 - four a kind
8 - straight Flush   -- same suit
9 - Royal flush      -- same suit
'''
def score(repeatValues, repeatSuits):
    if isRoyalStraight(repeatValues, repeatSuits): return 9  # royal flush
    if isStraightFlush(repeatValues, repeatSuits): return 8  # straight flush
    if isFourAKind(repeatValues): return 7                   # four a kind
    if isFullHouse(repeatValues): return 6                   # full house
    if isFlush(repeatValues): return 5                       # flush
    if isStraight(repeatValues): return 4                    # straight
    if isThreeAKind(repeatValues): return 3                  # three a kind
    if isTwoPairs(repeatValues): return 2                    # two pairs
    if isOnePair(repeatValues): return 1                     # one pair
    return 0


def judgeHighCard(hand1, hand2):
    v1 = [i[0] for i in hand1]
    v2 = [i[0] for i in hand2]
    return compare(v1, v2)

def compare(v1, v2):
    for i, j in zip(v1, v2):
        if i < j: return False
        if i > j: return True
    return None

def judgeOnePair(hand1, hand2):
    pairV1 = [i[0] for i in hand1 if i[1] == 2]
    pairV2 = [i[0] for i in hand2 if i[1] == 2]
    comparePair = compare(pairV1, pairV2)
    if comparePair != None: return comparePair

    singleV1 = [i[0] for i in hand1 if i[1] == 1]
    singleV2 = [i[0] for i in hand2 if i[1] == 1]
    return compare(singleV1, singleV2)

def judgeTwoPairs(hand1, hand2):
    pairV1 = [i[0] for i in hand1 if i[1] == 2]
    pairV2 = [i[0] for i in hand2 if i[1] == 2]
    comparePair = compare(pairV1, pairV2)
    if comparePair != None: return comparePair

    singleV1 = [i[0] for i in hand1 if i[1] == 1]
    singleV2 = [i[0] for i in hand2 if i[1] == 1]
    return compare(singleV1, singleV2)

def judgeThreeAKind(hand1, hand2):
    threeV1 = [i[0] for i in hand1 if i[1] == 3]
    threeV2 = [i[0] for i in hand2 if i[1] == 3]
    comparePair = compare(threeV1, threeV2)
    if comparePair != None: return comparePair

    singleV1 = [i[0] for i in hand1 if i[1] == 1]
    singleV2 = [i[0] for i in hand2 if i[1] == 1]
    return compare(singleV1, singleV2)


def judgeStraight(hand1, hand2):
    return hand1[4][0] > hand2[4][0]


def judgeFlush(hand1, hand2):
    return judgeHighCard(hand1, hand2)

def judgeFullHouse(hand1, hand2):
    threeV1 = [i[0] for i in hand1 if i[1] == 3]
    threeV2 = [i[0] for i in hand2 if i[1] == 3]
    compareThree = compare(threeV1, threeV2)
    if compareThree != None: return compareThree

    pairV1 = [i[0] for i in hand1 if i[1] == 2]
    pairV2 = [i[0] for i in hand2 if i[1] == 2]
    return compare(pairV1, pairV2)

def judgeFourAKind(hand1, hand2):
    fourV1 = [i[0] for i in hand1 if i[1] == 4]
    fourV2 = [i[0] for i in hand2 if i[1] == 4]
    return compare(fourV1, fourV2)

def judgeStraightFlush(hand1, hand2):
    return judgeStraight(hand1, hand2)

def judge(hand1, hand2, score):
    if score == 0: return judgeHighCard(hand1, hand2)
    if score == 1: return judgeOnePair(hand1, hand2)
    if score == 2: return judgeTwoPairs(hand1, hand2)
    if score == 3: return judgeThreeAKind(hand1, hand2)
    if score == 4: return judgeStraight(hand1, hand2)
    if score == 5: return judgeFlush(hand1, hand2)
    if score == 6: return judgeFullHouse(hand1, hand2)
    if score == 7: return judgeFourAKind(hand1, hand2)
    if score == 8: return judgeStraightFlush(hand1, hand2)

def pokerHands(hand):
    '''
    return True if player 1 wins
    '''
    tokens = hand.split(' ')
    player1 = tokens[0:5]
    player2 = tokens[5:]
    v1, s1 = organise(player1)
    v2, s2 = organise(player2)
    score1 = score(v1, s1)
    score2 = score(v2, s2)
    

    player1Win = None
    if score1 < score2:
        player1Win = False
    if score1 > score2:
        player1Win = True

    if player1Win == None:
        player1Win = judge(v1, v2, score1)
    
    if player1Win:
        print('player1', player1, v1, s1, score1)
        print('player2', player2, v2, s2, score2)
        print(player1Win)
        print('='*10)

    return player1Win


hand1 = '5H 5C 6S 7S KD 2C 3S 8S 8D TD'
hand2 = '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'
hand3 = '2D 9C AS AH AC 3D 6D 7D TD QD'
hand4 = '4D 6S 9H QH QC 3D 6D 7H QD QS'
hand5 = '2H 2D 4C 4D 4S 3C 3D 3S 9S 9D'

def test():
    print pokerHands(hand1)
    print pokerHands(hand2)
    print pokerHands(hand3)
    print pokerHands(hand4)
    print pokerHands(hand5)


def solution():
    result = 0
    f = open('problem54.txt')
    for l in f:
        if pokerHands(l.strip()): result += 1     
    return result


if __name__ == '__main__':
    # test()
    result = solution()
    print 'Result: ', result

