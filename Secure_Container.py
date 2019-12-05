def Combinelst(lst):
    s = ''.join(map(str,lst))
    return int(s)

def IncrementPassword(lst):
    pos = len(lst) - 1

    return IncrementRecursion(lst,pos)

def IncrementRecursion(lst,pos):
    lst[pos] += 1

    if pos == 0:
        return lst

    if lst[pos] > 9:
        lst[pos] = 0
        return IncrementRecursion(lst,pos-1)
    else:
        return lst

def GetFirstDigit(num):
    n = str(num)

    return int(n[0])

def CheckForDoubleDigit(lst):
    for i in range(0,len(lst)-1):
        if lst[i] == lst[i+1]:
            return True

    return False

def CheckForDoubleDigit_2(lst):
    digit = -1
    match = False

    for i in range(0,len(lst)-1):
        if match and lst[i+1] != digit:
            return True
        if lst[i] == lst[i+1]:
            if lst[i+1] == digit:
                match = False
            else:
                digit = lst[i]
                match = True
    
    return match

def CheckForAscending(lst):
    for i in range(0,len(lst)-1):
        if lst[i] > lst[i+1]:
            return False

    return True

def CheckBounds(lst,min,max):
    password = Combinelst(lst)
    
    if password > min and password < max:
        return True

    return False

def CheckPassword(lst,min,max):
    if CheckForDoubleDigit(lst) and CheckForAscending(lst) and lst[0] < 10:
        if CheckBounds(lst,min,max):
            return True
    return False

def CheckPassword_2(lst,min,max):
    if CheckForDoubleDigit_2(lst) and CheckForAscending(lst) and lst[0] < 10:
        if CheckBounds(lst,min,max):
            return True
    return False

def InitPassword(pword,min):
    digit = GetFirstDigit(min)

    pword.append(digit)

    for i in range(0,5):
        pword.append(digit)

    return pword
