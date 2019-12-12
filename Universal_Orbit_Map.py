class Link:
    well = ''
    orbital = ''

    def __init__(self,well,orbital):
        self.well = well
        self.orbital = orbital

    def __str__(self):
        return self.orbital + ' orbits ' + self.well

    def __eq__(self,lnk):
        if self.well == lnk.well:
            return True
        return False

def MakeLinks(lst):
    links = []
    for pair in lst:
        tup = pair.split(')')
        links.append(Link(tup[0],tup[1]))

    return links

def FormOrbitChain(link,linklst,chain):

    chain.append(link.orbital)

    for lnk in linklst:
        if link.well == lnk.orbital:
            return FormOrbitChain(lnk,linklst,chain)

    return chain

def CalculateOrbitTransfers(you,san):
    del you[0]
    del san[0]

    for i,y in enumerate(you):
        for j,s in enumerate(san):
            if y == s:
                del you[i:]
                del san[j:]

    return len(you) + len(san)
