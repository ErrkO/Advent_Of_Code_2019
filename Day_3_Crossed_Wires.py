import re, math
import Crossed_Wires as cwires

#wires = open('.\\Day_3_Wires.txt','r')

#wire1 = re.split(r',',wires.readline())
#wire2 = re.split(r',',wires.readline())

wire1 = re.split(r',','R75,D30,R83,U83,L12,D49,R71,U7,L72')
wire2 = re.split(r',','U62,R66,U55,R34,D71,R55,D58,R83')

wire1path = []
wire2path = []

wire1path.append(cwires.Point(0,0))
wire2path.append(cwires.Point(0,0))

intersectionDist = []
steps = []

wire1path = cwires.MapPath(wire1,wire1path)
wire2path = cwires.MapPath(wire2,wire2path)

for i in range(1,len(wire1path)):
    for j in range(1,len(wire2path)):
        if cwires.Intersection(wire1path[i-1],wire1path[i],wire2path[j-1],wire2path[j]):
            point = cwires.IntersectionPoint(wire1path[i-1],wire1path[i],wire2path[j-1],wire2path[j])

            wire1Steps = cwires.StepCounter(wire1path[i-1],point,wire1,i)
            wire2Steps = cwires.StepCounter(wire2path[j-1],point,wire2,j)

            steps.append(wire1Steps + wire2Steps)
            intersectionDist.append(cwires.ManhattenDistance(wire1path[0],point))

closepoint = cwires.GetSmallest(intersectionDist)
smallstep = cwires.GetSmallest(steps)

print('PART 1: Closest Point distance ' + str(closepoint))
print('PART 2: Shortest step ' + str(smallstep))
