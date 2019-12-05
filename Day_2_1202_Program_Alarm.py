import re, IntMachine

intcode = open('.\\Day_2_Inputs.txt','r')

opCodes = re.split(r',',intcode.readline())

opCodes = list(map(int,opCodes))

opCodes2 = opCodes[:]

opcode = 0
iter = 0
valToFind = 19690720

print('Part 1: ' + str(IntMachine.Compute(opCodes)))

print('Part 2: ' + str(IntMachine.ComputeNounVerb(opCodes2,valToFind)))