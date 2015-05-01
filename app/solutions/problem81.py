'''
Path sum: two ways

dynamic programming:
    for each iteration, node n can extend to two possible nodes (right for n_r, and down for n_d)
        l(n_r) = n_r + l(n)
        l(n_d) = n_d + l(n)
    for node n_r and n_d, find and save the minimum length value as l(n_r) and l(n_d) for the next iteration

427337
'''

SMALL_MATRIX = ['131,673,234,103,18','201,96,342,965,150','630,803,746,422,111','537,699,497,121,956','805,732,524,37,331']


def makeMatrix(lines):
    matrix = []
    for line in lines:
        matrix.append([int(x) for x in line.strip().split(',')])
    return matrix


def updateDistanceMatrix(prevNode, node, distanceMatrix, matrix):
    dist = distanceMatrix[prevNode[0]][prevNode[1]] + matrix[node[0]][node[1]]
    if distanceMatrix[node[0]][node[1]] == 0 or dist < distanceMatrix[node[0]][node[1]]:
        distanceMatrix[node[0]][node[1]] = dist

import sys
def findMinNodeInFrontLine(frontLine, distanceMatrix):
    minDist = sys.maxint
    minNode = (0, 0)
    for node in frontLine:
        if distanceMatrix[node[0]][node[1]] < minDist:
            minDist = distanceMatrix[node[0]][node[1]]
            minNode = (node[0], node[1])
    return minNode

def printMatrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])
        print('')

def extendRightward(node, dim):
    return None if node[0] == dim-1 else (node[0]+1, node[1])

def extendDownward(node, dim):
    return None if node[1] == dim-1 else (node[0], node[1]+1)


def solution():
    # matrix = makeMatrix(SMALL_MATRIX)
    matrix = makeMatrix(open('problem81.txt'))
    dim = len(matrix)
    distanceMatrix = [[0] * dim for i in range(dim)]
    distanceMatrix[0][0] = matrix[0][0]
    frontLine = [(0, 0)]
    while len(frontLine) >= 1:
        newFrontLine = []
        for node in frontLine:
            # extend rightward
            newNode = extendRightward(node, dim)
            if newNode is not None:
                updateDistanceMatrix(node, newNode, distanceMatrix, matrix)
                if newNode not in newFrontLine:
                    newFrontLine.append(newNode)
            # extend downward
            newNode = extendDownward(node, dim)
            if newNode is not None:
                updateDistanceMatrix(node, newNode, distanceMatrix, matrix)
                if newNode not in newFrontLine:
                    newFrontLine.append(newNode)
        frontLine = newFrontLine
        # printMatrix(distanceMatrix)
        # print(findMinNodeInFrontLine(frontLine, distanceMatrix))
        # print('========')
    return distanceMatrix[dim-1][dim-1]


if __name__ == '__main__':
    print('Result', solution())
