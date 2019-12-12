import Universal_Orbit_Map as UOM

orbit_lst = [line.rstrip('\n') for line in open('.\\Day_6_Inputs.txt','r')]

#orbit_lst = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
#orbit_lst2 = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']

orbit_lst = orbit_lst[::-1]

links = UOM.MakeLinks(orbit_lst)

chains = []
chains2 = []

for i,lnk in enumerate(links):
    chain = []
    chains.append(UOM.FormOrbitChain(lnk,links,chain))
    print(str(i) + ':' + str(len(links)))

count = 0

for chain in chains:
    count += len(chain)

count2 = 0

for chain in chains:
    if chain[0] == 'YOU':
        you = chain
    if chain[0] == 'SAN':
        san = chain

count2 = UOM.CalculateOrbitTransfers(you,san)

print('Part 1: ' + str(count))
print('Part 2: ' + str(count2))