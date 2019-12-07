import re, math

class Point:

    X = 0
    Y = 0

    def __init__(self, x, y):
        self.X = x
        self.Y = y

    def __eq__(self,p2):
        if self.X == p2.X and self.Y == p2.Y:
            return True
        else:
            return False

    def __str__(self):
        return '(' + str(self.X) + ',' + str(self.Y) + ')'

def AddPoint(point,x,y):
    return Point(point.X + x,point.Y + y)

def GetSmallest(lst):
    smallest = lst[1]
    for item in lst:
        if item != 0:
            if item < smallest:
                smallest = item
    return smallest

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

    return path[1:]

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

def StepCounter(p1,p2,directions,index):
    steps = 0
    for i in range(0,index + 1):
        if i == index:
            steps += ManhattenDistance(p1,p2)
        else:
            magnitude = int(re.split(r'(R|U|D|L)',directions[i])[2])
            steps += magnitude

    return steps
