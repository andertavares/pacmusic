

class Stats(object):
    def __init__(self):
        self._arpeggios = []
        self._power_chords = []

    def analyse(self, input_file):
        """
        Analyse a file, storing arpeggios and power chords
        :param input_file:
        :return:
        """
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
