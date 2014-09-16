'''
Minimal network

The following undirected network consists of seven vertices and twelve edges with a total weight of 243.
The same network can be represented by the matrix below.
However, it is possible to optimise the network by removing some edges and still ensure that all points on the network remain connected. The network which achieves the maximum saving is shown below. It has a weight of 93, representing a saving of 243 - 93 = 150 from the original network.

Using network.txt (right click and 'Save Link/Target As...'), a 6K text file containing a network with forty vertices, and given in matrix form, find the maximum saving which can be achieved by removing redundant edges whilst ensuring that the network remains connected.

'''
import collections

def bfs(matrix):
    '''
    traverse matrix, start from node 0,
    breadth first search
    '''
    visitedNodes = []
    searchQueue = collections.deque()
    searchQueue.appendleft(0)
    width = len(matrix[0])
    while len(searchQueue) > 0:
        # print('')
        # print('visited: ', visitedNodes)
        currentNode = searchQueue.pop()
        # print('visiting: {c}, searchQueue {q}'.format(c=currentNode, q=searchQueue))
        visitedNodes.append(currentNode)
        # print('connected to: ', matrix[currentNode])
        for i in xrange(width):
            if matrix[currentNode][i] != 0 and i not in visitedNodes and i not in searchQueue:
                searchQueue.appendleft(i)
        # print('seachQueue updated: {q}'.format(q=searchQueue))
    return visitedNodes


def getMaxValPos(matrix):
    maxVal, i, j = max((item, i, j)  for i, row in enumerate(matrix)
                                 for j, item in enumerate(row))
    return maxVal, i, j


def getMatrixWeight(matrix):
    return sum(sum(i for i in row) for row in matrix)

def removeEdge(matrix):
    '''
    find max edge to remove from matrix
    if break the network, find the next max edge to remove
    '''
    toAddBack = []
    while True:
        maxVal, maxi, maxj = getMaxValPos(matrix)
        # print('remove from matrix: ', maxVal, maxi, maxj)
        matrix[maxi][maxj] = 0
        matrix[maxj][maxi] = 0
        for (val, i, j) in toAddBack:
            matrix[i][j] = val
            matrix[j][i] = val
        if connected(matrix):
            break
        else:
            for (val, i, j) in toAddBack:
                matrix[i][j] = 0
                matrix[j][i] = 0
            toAddBack.append((maxVal, maxi, maxj))
            
    return matrix


def loadMatrix():
    matrix = []
    f = open('problem107.txt')
    for line in f:
        matrix.append([int(e) if e != '-' else 0 for e in line.strip().split(',')])
    f.close()
    return matrix


def connected(matrix):
    size = len(matrix[0])
    visitedNodes = bfs(matrix)
    return len(visitedNodes) == size


def isMinimised(matrix):
    size = len(matrix[0])
    numEdges = sum(sum(1 for i in row if i) for row in matrix)
    print('remaining edge: ', numEdges / 2)
    return numEdges == (size - 1) * 2


def minimise(matrix):
    while not isMinimised(matrix):
        matrix = removeEdge(matrix)
        print('remaining weight: ', getMatrixWeight(matrix))
    return matrix


def solution():
    matrix = loadMatrix()
    before = getMatrixWeight(matrix)
    matrix = minimise(matrix)
    after = getMatrixWeight(matrix)
    return (before - after) / 2


if __name__ == '__main__':
    result = solution()
    print 'Result: ', result