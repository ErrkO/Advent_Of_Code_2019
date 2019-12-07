import re

def Split(word):
    return [char for char in word]

def Add(lst,index,params):
    val1 = InterperateMode(lst,index+1,params[1])
    val2 = InterperateMode(lst,index+2,params[2])
    pos = lst[index+3]
    valToBePlaced = val1 + val2
    lst[pos] = valToBePlaced

    return lst

def Multiply(lst,index,params):
    val1 = InterperateMode(lst,index+1,params[1])
    val2 = InterperateMode(lst,index+2,params[2])
    pos = lst[index+3]
    valToBePlaced = val1 * val2
    lst[pos] = valToBePlaced

    return lst

def Input(lst,index,inval):
    pos1 = lst[index + 1]
    lst[pos1] = inval

    return lst

def Output(lst,index):
    pos1 = lst[index+1]

    return str(lst[pos1])

def JumpIfTrue(lst,index,params):
    val1 = InterperateMode(lst,index+1,params[1])
    pos = InterperateMode(lst,index+2,params[2])
    
    if val1 != 0:
        return pos
    else:
        return index

def JumpIfFalse(lst,index,params):
    val1 = InterperateMode(lst,index+1,params[1])
    pos = InterperateMode(lst,index+2,params[2])
    
    if val1 == 0:
        return pos
    else:
        return index

def LessThan(lst,index,params):
    val1 = InterperateMode(lst,index+1,params[1])
    val2 = InterperateMode(lst,index+2,params[2])
    pos = lst[index+3]
    
    if val1 < val2:
        valToBePlaced = 1
    else:
        valToBePlaced = 0

    lst[pos] = valToBePlaced

    return lst

def EqualTo(lst,index,params):
    val1 = InterperateMode(lst,index+1,params[1])
    val2 = InterperateMode(lst,index+2,params[2])
    pos = lst[index+3]
    
    if val1 == val2:
        valToBePlaced = 1
    else:
        valToBePlaced = 0
        
    lst[pos] = valToBePlaced

    return lst

def Parameterize(instruction):
    instruction = str(instruction)
    parameters = Split(instruction)
    parameters = parameters[::-1]
    parameters = list(map(int,parameters))

    if len(parameters) == 1:
        parameters.extend([0,0,0])
    elif len(parameters) == 2:
        del parameters[1]
        parameters.extend([0,0,0])
    elif len(parameters) == 3:
        del parameters[1]
        parameters.extend([0,0])
    elif len(parameters) == 4:
        del parameters[1]
        parameters.append(0)

    return parameters

def InterperateMode(lst,index,param):
    if param == 0:
        pos = lst[index]
        val = lst[pos]
    elif param == 1:
        val = lst[index]

    return val

def Compute(lst,input):
    opcode = 0
    iter = 0
    diag = 1
    jump = False
    para = 0

    while opcode != 99:
        print(iter)
        if jump:
            params = Parameterize(para)
            jump = False
        else:
            params = Parameterize(lst[iter])

        if params[0] == 1:
            lst = Add(lst,iter,params)
            iter += 4
        elif params[0] == 2:
            lst = Multiply(lst,iter,params)
            iter += 4
        elif params[0] == 3:
            lst = Input(lst,iter,input)
            iter += 2
        elif params[0] == 4:
            print('Diag Code ' + str(diag) + ': ' + Output(lst,iter))
            diag += 1
            iter += 2
        elif params[0] == 5:
            paraPtr = JumpIfTrue(lst,iter,params)
            if paraPtr == iter:
                iter += 3
            else:
                para = lst[paraPtr]
                jump = True
        elif params[0] == 6:
            paraPtr = JumpIfFalse(lst,iter,params)
            if paraPtr == iter:
                iter += 3
            else:
                para = lst[paraPtr]
                jump = True
        elif params[0] == 7:
            lst = LessThan(lst,iter,params)
            iter += 4
        elif params[0] == 8:
            lst = EqualTo(lst,iter,params)
            iter += 4
        elif lst[iter] == 99:
            print('HALT')
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
            finalval = Compute(opCopy,1)
            if finalval == valToFind:
                break
        if finalval == valToFind:
                break

    return ComputeAnswer(noun,verb)
