import Lexer.lexer as lx
import re

class Stats(object):

    def __init__(self):
        self._arpeggios = []
        self._power_chords = []
        self._notes = []
        # a list of dicts [{'from':(row,col), 'to':(row,col)}, ...]
        self._diagonal_moves = []
        self._positions = []

    def analyse(self, input_file):
        """
        Analyse a file, storing arpeggios and power chords
        :param input_file:
        :return:
        """
        seq_notes = []
        f = open(input_file,'r')
        rw = []
        cl = []
        for line in f:
            line = line.replace(" ", "").replace("\n", "") #Remove whitespace
            rw.append(int(line.split(',')[0]))
            cl.append(int(line.split(',')[1]))
            seq_notes.append(line.split(',')[2])

            # stores the visited positions
            self._positions.append((int(line.split(',')[0]), int(line.split(',')[1])) )

        self._diagonal_moves = lx.getDiagonalMoves(rw, cl)
        self._arpeggios = lx.getArpeggios("".join(seq_notes))
        self._power_chords = lx.getPowerChords("".join(seq_notes))
        self._notes = lx.getNotes("".join(seq_notes))
        # m.test("".join(seq_notes))# Test it

    @property
    def arpeggios(self):
        """
        Returns the arpeggios encountered
        :return:
        """
        return [x['seq'] for x in self._arpeggios]

    @property
    def notes(self):
        """
        Returns the power chords encountered
        :return:
        """
        return [x['seq'] for x in self._notes]

    @property
    def power_chords(self):
        """
        Returns the power chords encountered
        :return:
        """
        return  [x['seq'] for x in self._power_chords]

    @property
    def diagonals(self):
        """
        Returns the number of diagonal moves encountered
        :return: list
        """
        return self._diagonal_moves

    @property
    def positions(self):
        """
        Returns a list of tuples with the traveled coordinates
        :return:
        """
        return self._positions

    def num_moves(self):
        """
        Returns the number of moves performed
        :return:
        """
        return max(0, len(self._positions) - 1)

    @staticmethod
    def typeOfnote(x):
        tipo = 8
        if(len(x)==3):
            rex = []
            rex.append(r'(ECG|EGC|CEG|CGE|GEC|GCE)')
            rex.append(r'(DFA|DAF|FDA|FAD|ADF|AFD)')
            rex.append(r'(EGB|EBG|GEB|GBE|BEG|BGE)')
            rex.append(r'(FAC|FCA|AFC|ACF|CFA|CAF)')
            rex.append(r'(GBD|GDB|BGD|BDG|DGB|DBG)')
            rex.append(r'(ACE|AEC|CAE|CEA|EAC|ECA)')
            rex.append(r'(BDF|BFD|DBF|DFB|FBD|FDB)')
            for t in range(len(rex)):
                if(re.match(rex[t],x)):
                    tipo = t
                    break;
            return tipo;
        elif(len(x)==2):
            rex = []
            tipo = 8
            rex.append(r'(CG|GC)')
            rex.append(r'(DA|AD)')
            rex.append(r'(EB|BE)')
            rex.append(r'(FC|CF)')
            rex.append(r'(GD|DG)')
            rex.append(r'(AE|EA)')
            rex.append(r'(BF|FB)')
            for t in range(len(rex)):
                if(re.match(rex[t],x)):
                    tipo = t
                    break;
            return tipo;

    def occurrences(self, sequence,typ=0):
        """
        Returns the number of times a given sequence
        (chord or power chord) has occurred
        :param sequence: str
        :return: int
        """
        if(typ==1):
            if((len(sequence) <=3) and (len(sequence)>=2)):
                tipo = self.typeOfnote(sequence)
                a = {2: self._power_chords, 3: self._arpeggios}
                return len([i for i in a[len(sequence)] if i['typ']==tipo])
            else:
                return 0;
        else:
            if((len(sequence) <=3) and (len(sequence)>=2)):
                a = {2: self._power_chords, 3: self._arpeggios}
                return len([i for i in a[len(sequence)] if i['seq']==sequence])
            else:
                return 0;

    def intervals(self, sequence,typ=0):
        """
        Returns a list with the intervals (number of
        other notes) between occurrences of the given
        chord or power chord
        :param sequence: str
        :return: list of int
        """
        if(typ==1):
            if((len(sequence) <=3) and (len(sequence)>=2)):
                a = {2: self._power_chords, 3: self._arpeggios}
                mstipo = []
                intervals = []
                tipo = self.typeOfnote(sequence)
                for i in a[len(sequence)]:
                    if(i['typ']==tipo):
                        mstipo.append(i)
                for i in range(len(mstipo)-1):
                    if(0 <= (mstipo[i+1]['pos'] - ((mstipo[i]['pos'])+len(sequence)))):
                        intervals.append(max(0,mstipo[i+1]['pos'] - ((mstipo[i]['pos'])+len(sequence))))
                return intervals
            else:
                return [0];
        else:
            if(len(sequence) <=3 and len(sequence)>=2):
                a = {2: self._power_chords, 3: self._arpeggios}
                intervals = []
                msmarp = []
                for i in a[len(sequence)]:
                    if(i['seq']==sequence):
                        msmarp.append(i)
                for i in range(len(msmarp)-1):
                    if(0 <= (msmarp[i+1]['pos'] - ((msmarp[i]['pos'])+len(sequence)))):
                        intervals.append((msmarp[i+1]['pos'] - ((msmarp[i]['pos'])+len(sequence))))
                return intervals;
            else:
                return [0]
