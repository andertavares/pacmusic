import Lexer.lexer as lx
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
