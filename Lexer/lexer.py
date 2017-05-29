import re



def getArpeggios(data):
    arp = []
    rex = r'(ECG|EGC|CEG|CGE|GEC|GCE|DFA|DAF|FDA|FAD|ADF|AFD|EGB|EBG|GEB|GBE|BEG|BGE|FAC|FCA|AFC|ACF|CFA|CAF|GBD|GDB|BGD|BDG|DGB|DBG|ACE|AEC|CAE|CEA|EAC|ECA|BDF|BFD|DBF|DFB|FBD|FDB)'
    i=0
    while True:
        sobj = re.match(rex, data[i:])
        if(sobj):
            arp.append(sobj.group())
            i=i+1
        else:
            break
    return arp;


def getPowerChords(data):
    arp = []
    rex = r'(CG|GC|DA|AD|EB|BE|FC|CF|GD|DG|AE|EA|BF|FB)'
    i=0
    while True:
        sobj = re.match(rex, data[i:])
        if(sobj):
            arp.append(sobj.group())
            i=i+1
        else:
            break
    return arp;

def getNotes(data):
    arp = []
    rex = r'(C|D|E|F|G|A|B)'
    i=0
    while True:
        sobj = re.match(rex, data[i:])
        if(sobj):
            arp.append(sobj.group())
            i=i+1
        else:
            break
    return arp;


def getDiagonalMoves(row,col):
    arp = []
    for i in range(len(row)):
        if(i==(len(row)-1)):
            break
        else:
            if((abs(row[i+1] - row[i])!=0) and (abs(col[i+1] - col[i])!=0)):
                arp.append({'from':(row[i],col[i]), 'to':(row[i+1],col[i+1])})
            else:
                pass
    return arp;
