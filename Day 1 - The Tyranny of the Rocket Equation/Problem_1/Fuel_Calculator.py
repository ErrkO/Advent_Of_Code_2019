import math

inputs = open("F:\\Users\\erico\\Code_Projects\\Advent_Of_Code\\Day_1\\Problem_1\\Inputs.txt","r")

totalFuel = 0

for i in inputs:
    totalFuel += math.floor(float(i)/3) - 2

print(totalFuel)