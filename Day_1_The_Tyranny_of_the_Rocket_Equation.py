import Fuel_Calculator

inputs = open(".\\Day_1_Inputs.txt","r")

fcalc = Fuel_Calculator

print('Part 1: ' + str(fcalc.CalculateFuel(inputs)))

inputs = open(".\\Day_1_Inputs.txt","r")

print('Part 2: ' + str(fcalc.CalculateTotalFuel(inputs)))