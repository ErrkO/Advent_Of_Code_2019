import os
import IntMachine

def GetFile(filename):
    cwd = os.getcwd()
    path = os.path.join(cwd,filename)
    return open(path)

