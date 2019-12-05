import re

#intcode = '2,3,0,3,99'

intcode = open('C:\\Users\\eoliver\\OneDrive - inBusiness Services, Inc\\Documents\\Scripts\\AdventCode\\inputs.txt','r')

opCodes = re.split(r',',intcode.readline())

opCodes = list(map(int,opCodes))

opcode = 0
iter = 0

while opcode != 99:
    if opCodes[iter] == 1:
        pos1 = opCodes[iter + 1]
        pos2 = opCodes[iter + 2]
        pos3 = opCodes[iter + 3]
        valToBePlaced = opCodes[pos1] + opCodes[pos2]
        opCodes[pos3] = valToBePlaced
        iter += 4
    elif opCodes[iter] == 2:
        pos1 = opCodes[iter + 1]
        pos2 = opCodes[iter + 2]
        pos3 = opCodes[iter + 3]
        valToBePlaced = opCodes[pos1] * opCodes[pos2]
        opCodes[pos3] = valToBePlaced
        iter += 4
    elif opCodes[iter] == 99:
        opcode = 99
    else:
        print('Something is wrong at iter = ' + str(iter) + 'which is: ' + str(opCodes[iter]))

for i, val in enumerate(opCodes):
    print('Value at pos ' + str(i) + ' is: ' + str(val))