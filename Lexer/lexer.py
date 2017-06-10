import re



def getArpeggios(data):
    arp = []
    rex = []
    rex.append(r'(ECG|EGC|CEG|CGE|GEC|GCE)')
    rex.append(r'(DFA|DAF|FDA|FAD|ADF|AFD)')
    rex.append(r'(EGB|EBG|GEB|GBE|BEG|BGE)')
    rex.append(r'(FAC|FCA|AFC|ACF|CFA|CAF)')
    rex.append(r'(GBD|GDB|BGD|BDG|DGB|DBG)')
    rex.append(r'(ACE|AEC|CAE|CEA|EAC|ECA)')
    rex.append(r'(BDF|BFD|DBF|DFB|FBD|FDB)')
    i=0
    while True:
        for t in range(len(rex)):
            sobj = re.match(rex[t], data[i:])
            if(sobj):
                arp.append({'arp':sobj.group(),'pos':i,'typ':t})
        i=i+1
        if(i==len(data)):
            break
    return arp;


def getPowerChords(data):
    chd = []
    rex = []
    rex.append(r'(CG|GC)')
    rex.append(r'(DA|AD)')
    rex.append(r'(EB|BE)')
    rex.append(r'(FC|CF)')
    rex.append(r'(GD|DG)')
    rex.append(r'(AE|EA)')
    rex.append(r'(BF|FB)')
    i=0
    while True:
        for t in range(len(rex)):
            sobj = re.match(rex[t], data[i:])
            if(sobj):
                chd.append({'chd':sobj.group(),'pos':i,'typ':t})
        i=i+1
        if(i==len(data)):
            break
    return chd;

def getNotes(data):
    notes = []
    rex = r'(C|D|E|F|G|A|B)'
    i=0
    while True:
        sobj = re.match(rex, data[i:])
        if(sobj):
            notes.append({'notes':sobj.group(),'pos':i})
        i=i+1
        if(i==len(data)):
            break
    return notes;


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
