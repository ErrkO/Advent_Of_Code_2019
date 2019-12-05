import re, math

class Point:

    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

def AddPoint(point,x,y):
    return Point(point.X + x,point.Y + y)

def ManhattenDistance(p1,p2):
    return abs(p1.X - p2.X) + abs(p1.Y - p2.Y)

def MapPath(directions,path):
    for i in range(0,len(directions)):
        magnitude = int(re.split(r'(R|U|D|L)',directions[i])[2])
        pPrev = path[i]
        
        if 'R' in directions[i]:
            pNext = AddPoint(pPrev,magnitude,0)
        elif 'L' in directions[i]:
            pNext = AddPoint(pPrev,-magnitude,0)
        elif 'U' in directions[i]:
            pNext = AddPoint(pPrev,0,magnitude)
        elif 'D' in directions[i]:
            pNext = AddPoint(pPrev,0,-magnitude)

        path.append(pNext)

    return path

def OnSegment(p1,p2,p3):
    if (p2.X <= max(p1.X,p3.X) and
        p2.X >= min(p1.X,p3.X) and
        p2.Y <= max(p1.Y,p3.Y) and
        p2.Y >= min(p1.Y,p3.Y)):

        return True
    else:
        return False

def Orientation(p1,p2,p3):
    val = ((p2.Y - p1.Y) * (p3.X - p2.X)) - ((p2.X - p1.X) * (p3.Y - p2.Y))

    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

def Intersection(p11,p12,p21,p22):
    o1 = Orientation(p11,p12,p21)
    o2 = Orientation(p11,p12,p22)
    o3 = Orientation(p21,p22,p11)
    o4 = Orientation(p21,p22,p12)

    if o1 != o2 and o3 != o4:
        return True
    
    if o1 == 0 and OnSegment(p11,p21,p12):
        return True
    
    if o2 == 0 and OnSegment(p11,p22,p12):
        return True

    if o3 == 0 and OnSegment(p21,p11,p22):
        return True

    if o4 == 0 and OnSegment(p21,p11,p22):
        return True

    return False

def IntersectionPoint(p11,p12,p21,p22):
    x = 0
    y = 0

    if p11.X == p12.X:
        x = p11.X
    else:
        x = p21.X

    if p11.Y == p12.Y:
        y = p11.Y
    else:
        y = p21.Y

    return Point(x,y)

def main():

    wires = open('C:\\Users\\eoliver\\OneDrive - inBusiness Services, Inc\\Documents\\Scripts\\AdventCode\\Day_3\\wires.txt','r')

    wire1 = re.split(r',',wires.readline())
    wire2 = re.split(r',',wires.readline())

    #wire1 = re.split(r',','R75,D30,R83,U83,L12,D49,R71,U7,L72')
    #wire2 = re.split(r',','U62,R66,U55,R34,D71,R55,D58,R83')

    wire1path = []
    wire2path = []

    wire1path.append(Point(0,0))
    wire2path.append(Point(0,0))

    intersectionDist = []

    wire1path = MapPath(wire1,wire1path)
    wire2path = MapPath(wire2,wire2path)

    for i in range(1,len(wire1path)):
        for j in range(1,len(wire2path)):
            if Intersection(wire1path[i-1],wire1path[i],wire2path[j-1],wire2path[j]):
                point = IntersectionPoint(wire1path[i-1],wire1path[i],wire2path[j-1],wire2path[j])
                intersectionDist.append(ManhattenDistance(wire1path[0],point))

    smallest = intersectionDist[1]

    for dist in intersectionDist:
        if dist != 0:
            if dist < smallest:
                smallest = dist

    print(smallest)

main()