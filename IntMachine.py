import re

def Add(lst, index):
    pos1 = lst[index + 1]
    pos2 = lst[index + 2]
    pos3 = lst[index + 3]
    valToBePlaced = lst[pos1] + lst[pos2]
    lst[pos3] = valToBePlaced

    return lst

def Multiply(lst,index):
    pos1 = lst[index + 1]
    pos2 = lst[index + 2]
    pos3 = lst[index + 3]
    valToBePlaced = lst[pos1] * lst[pos2]
    lst[pos3] = valToBePlaced

    return lst

def Compute(lst):
    opcode = 0
    iter = 0

    while opcode != 99:
        if lst[iter] == 1:
            lst = Add(lst,iter)
            iter += 4
        elif lst[iter] == 2:
            lst = Multiply(lst,iter)
            iter += 4
        elif lst[iter] == 99:
            opcode = 99

    return lst[0]

def ComputeAnswer(noun,verb):
    return (100 * noun) + verb

def ComputeNounVerb(lst,valToFind):
    noun = 0
    verb = 0
    finalval = 0

    for i in range(0,99):
        for j in range(0,99):
            opCopy = lst[:]
            noun = i
            verb = j
            opCopy[1] = noun
            opCopy[2] = verb
            finalval = Compute(opCopy)
            if finalval == valToFind:
                break
        if finalval == valToFind:
                break

    return ComputeAnswer(noun,verb)
