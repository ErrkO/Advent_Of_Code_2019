import math

def Calculate(val):
    return math.floor(float(val)/3) - 2

def FuelForModule(fuel):
    totalForModule = 0
    while (fuel > 0):
        fuel = Calculate(fuel)
        if fuel > 0:
            totalForModule += fuel

    return totalForModule

inputs = open("F:\\Users\\erico\\Code_Projects\\Advent_Of_Code\\Day_1\\Problem_1\\Inputs.txt","r")

totalFuel = 0

for i in inputs:
    fuelForModule = FuelForModule(int(i))
    totalFuel += fuelForModule

print('Actual fuel is: 50346')
print('Estimated fuel is: ' + str(totalFuel))