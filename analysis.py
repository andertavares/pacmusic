import Lexer.lexer as lx
class Stats(object):

    def __init__(self):
        self._arpeggios = []
        self._power_chords = []
        self._notes = []
    def analyse(self, input_file):
        """
        Analyse a file, storing arpeggios and power chords
        :param input_file:
        :return:
        """
        seq_notes = []
        f = open(input_file,'r')
        for line in f:
            line = line.replace(" ", "").replace("\n", "") #Remove whitespace
            seq_notes.append(line.split(',')[2])
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
        return self._arpeggios

    @property
    def notes(self):
        """
        Returns the power chords encountered
        :return:
        """
        return self._notes

    @property
    def power_chords(self):
        """
        Returns the power chords encountered
        :return:
        """
        return self._power_chords
