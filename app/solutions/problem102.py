'''
Triangle containment

refer to:

http://stackoverflow.com/questions/2049582/how-to-determine-a-point-in-a-triangle

s = 1/(2*Area)*(p0y*p2x - p0x*p2y + (p2y - p0y)*px + (p0x - p2x)*py);
t = 1/(2*Area)*(p0x*p1y - p0y*p1x + (p0y - p1y)*px + (p1x - p0x)*py);

Area = 1/2*(-p1y*p2x + p0y*(-p1x + p2x) + p0x*(p1y - p2y) + p1x*p2y);


p0 is inside the triangle if only if 
s, t, and 1-s-t all positive

228
'''

A = '-340,495,-153,-910,835,-947'
B = '-175,41,-421,-714,574,-645'

class Point(object):
    """docstring for Point"""
    def __init__(self, x, y):
        super(Point, self).__init__()
        self.x = x
        self.y = y

def isInsideTriangle(p, p0, p1, p2):
    Area = 0.5*(-1.0 * p1.y*p2.x + p0.y*(-1.0 * p1.x + p2.x) + p0.x*(p1.y - p2.y) + p1.x*p2.y);
    s = 1.0/(2.0*Area)*(p0.y*p2.x - p0.x*p2.y + (p2.y - p0.y)*p.x + (p0.x - p2.x)*p.y);
    t = 1.0/(2.0*Area)*(p0.x*p1.y - p0.y*p1.x + (p0.y - p1.y)*p.x + (p1.x - p0.x)*p.y);
    return s > 0 and t > 0 and (1-s-t) > 0

def loadPoints(coordinations):
    points = [int(x) for x in coordinations.split(',')]
    p0 = Point(points[0], points[1])
    p1 = Point(points[2], points[3])
    p2 = Point(points[4], points[5])
    return p0, p1, p2


def solution():
    count = 0
    p = Point(0, 0)
    for l in open('problem102.txt'):
        p0, p1, p2 = loadPoints(l.strip())
        if isInsideTriangle(p, p0, p1, p2): 
            count += 1
    return count


if __name__ == '__main__':
    print('Result', solution())
