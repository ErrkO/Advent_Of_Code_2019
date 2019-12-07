import re, math
import Crossed_Wires as cwires

wires = open('.\\Day_3_Wires.txt','r')

wire1 = re.split(r',',wires.readline())
wire2 = re.split(r',',wires.readline())

#wire1 = re.split(r',','R8,U5,L5,D3')
#wire2 = re.split(r',','U7,R6,D4,L4')

wire1path = []
wire2path = []

wire1path.append(cwires.Point(0,0))
wire2path.append(cwires.Point(0,0))

intersectionDist = []
steps = []

wire1path = cwires.MapPath(wire1,wire1path)
wire2path = cwires.MapPath(wire2,wire2path)

origin = cwires.Point(0,0)

for i in range(1,len(wire1path)):
    for j in range(1,len(wire2path)):
        if cwires.Intersection(wire1path[i-1],wire1path[i],wire2path[j-1],wire2path[j]):

            point = cwires.IntersectionPoint(wire1path[i-1],wire1path[i],wire2path[j-1],wire2path[j])

            if wire1path[i-1] == origin or wire2path[j-1] == origin:
                pass
            else:
                wire1Steps = cwires.StepCounter(wire1path[i-1],point,wire1,i)
                wire2Steps = cwires.StepCounter(wire2path[j-1],point,wire2,j)

                steps.append(wire1Steps + wire2Steps)

            intersectionDist.append(cwires.ManhattenDistance(origin,point))

closepoint = cwires.GetSmallest(intersectionDist)
smallstep = cwires.GetSmallest(steps)

print('PART 1: Closest Point distance ' + str(closepoint))
print('PART 2: Shortest step ' + str(smallstep))
