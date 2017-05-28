from Lexer.lexer import Lexer

class Stats(object):
    def __init__(self):
        self._arpeggios = []
        self._power_chords = []
        # a list of dicts [{'from':(row,col), 'to':(row,col)}, ...]
        self._diagonal_moves = []

    def analyse(self, input_file):
        """
        Analyse a file, storing arpeggios and power chords
        :param input_file:
        :return:
        """
	m = Lexer()
        m.build()           # Build the lexer
        self._arpeggios = m.getArpeggios(input_file)
        self._power_chords = m.getPowerChords(input_file)
        self._notes = m.getNotes(input_file)
        pass

    @property
    def arpeggios(self):
        """
        Returns the arpeggios encountered
        :return:
        """
        return self._arpeggios

    @property
    def power_chords(self):
        """
        Returns the power chords encountered
        :return:
        """
        return self._power_chords

    @property
    def diagonals(self):
        """
        Returns the number of diagonal moves encountered
        :return: list
        """
        return self._diagonal_moves
