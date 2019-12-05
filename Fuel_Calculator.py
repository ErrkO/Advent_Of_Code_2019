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

def CalculateFuel(lst):
    totalFuel = 0

    for i in lst:
        totalFuel += Calculate(i)

    return totalFuel

def CalculateTotalFuel(lst):
    totalFuel = 0

    for i in lst:
        fuelForModule = FuelForModule(int(i))
        totalFuel += fuelForModule

    return totalFuel