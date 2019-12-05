import Secure_Container as Cracker

minRange = 367479
maxRange = 893698
password = []

#password = [8,9,9,9,9,9]

password = Cracker.InitPassword(password,minRange)

Part1Count = 0
Part2Count = 0

while Cracker.Combinelst(password) <= maxRange:
    if Cracker.CheckPassword(password,minRange,maxRange):
        Part1Count += 1
    if Cracker.CheckPassword_2(password,minRange,maxRange):
        Part2Count += 1
    password = Cracker.IncrementPassword(password)

print('Part 1: ' + str(Part1Count))
print('Part 2: ' + str(Part2Count))