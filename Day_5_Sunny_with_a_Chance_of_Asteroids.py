import IntMachine, re

input = 1
input2 = 5

print('Input 1: ' + str(input))
print('Input 2: ' + str(input2))

intcode = open('.\\Day_5_Inputs.txt','r')

opCodes = re.split(r',',intcode.readline())

opCodes = list(map(int,opCodes))

#opCodes = [1002,4,3,4,33]

opCodes2 = opCodes[:]

#opCodes2 = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,
#1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,
#999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]

print('Part 1: ')
IntMachine.Compute(opCodes,input)

print('Part 2: ')
IntMachine.Compute(opCodes2,input2)
