import ply.lex as lex


class Lexer(object):
    # List of token names.   This is always required
    tokens = (
       'ARPEGGIOS',
       'POWER_CHORDS',
       'NOTES'
    )

    #Arpegios Token
    def t_ARPEGGIOS(self,token):
        r'(ECG|EGC|CEG|CGE|GEC|GCE|DFA|DAF|FDA|FAD|ADF|AFD|EGB|EBG|GEB|GBE|BEG|BGE|FAC|FCA|AFC|ACF|CFA|CAF|GBD|GDB|BGD|BDG|DGB|DBG|ACE|AEC|CAE|CEA|EAC|ECA|BDF|BFD|DBF|DFB|FBD|FDB)'
        return token

    #Power Chords Token
    def t_POWER_CHORDS(self,token):
        r'(CG|GC|DA|AD|EB|BE|FC|CF|GD|DG|AE|EA|BF|FB)'
        return token
    #Notes Token
    def t_NOTES(self,token):
        r'(C|D|E|F|G|A|B)'
        return token
    # whatever error
    def t_error(self,t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    # Build the lexer
    def build(self,**kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

    def getArpeggios(self,data):
        self.lexer.input(data)
        arp = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            if(tok.type=='ARPEGGIOS'):
                arp.append(tok.value)
        return arp;

    def getPowerChords(self,data):
        self.lexer.input(data)
        arp = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            if(tok.type=='POWER_CHORDS'):
                arp.append(tok.value)
        return arp;

    def getNotes(self,data):
        self.lexer.input(data)
        arp = []
        while True:
            tok = self.lexer.token()
            if not tok:
                break      # No more input
            if(tok.type=='NOTES'):
                arp.append(tok.value)
        return arp;

     # Test it output
    def test(self,data):
        self.lexer.input(data)
        while True:
             tok = self.lexer.token()
             if not tok:
                 break
             print(tok)
