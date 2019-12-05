import re

def Compute(list):
    opcode = 0
    iter = 0

    while opcode != 99:
        if list[iter] == 1:
            pos1 = list[iter + 1]
            pos2 = list[iter + 2]
            pos3 = list[iter + 3]
            valToBePlaced = list[pos1] + list[pos2]
            list[pos3] = valToBePlaced
            iter += 4
        elif list[iter] == 2:
            pos1 = list[iter + 1]
            pos2 = list[iter + 2]
            pos3 = list[iter + 3]
            valToBePlaced = list[pos1] * list[pos2]
            list[pos3] = valToBePlaced
            iter += 4
        elif list[iter] == 99:
            opcode = 99
        else:
            print('Something is wrong at iter = ' + str(iter) + ' which is: ' + str(list[iter]))

    return list[0]

def ComputeAnswer(noun,verb):
    return (100 * noun) + verb

def main():

    intcode = open('C:\\Users\\eoliver\\OneDrive - inBusiness Services, Inc\\Documents\\Scripts\\AdventCode\\inputs.txt','r')

    opCodes = re.split(r',',intcode.readline())

    opCodes = list(map(int,opCodes))

    noun = 0
    verb = 0
    finalval = 0

    for i in range(0,99):
        for j in range(0,99):
            opCopy = opCodes[:]
            noun = i
            verb = j
            opCopy[1] = noun
            opCopy[2] = verb
            finalval = Compute(opCopy)
            if finalval == 19690720:
                break
        if finalval == 19690720:
                break

    print(str(ComputeAnswer(noun,verb)))

main()