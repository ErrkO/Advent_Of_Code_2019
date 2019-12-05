import os
import Advent_Of_Code_2019.Day_2_1202_Program_Alarm.IntMachine2

def GetFile(filename):
    cwd = os.getcwd()
    path = os.path.join(cwd,filename)
    return open(path)

