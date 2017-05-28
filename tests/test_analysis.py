import unittest
import analysis

class TestStats(unittest.TestCase):
    def test_arpeggios(self):
        stats = analysis.Stats()

        stats.analyse("arpeggios.log")

        # arpeggios are expected, power chords are not
        self.assertEquals(['CEG', 'EGB', 'GBD'], stats.arpeggios)
        self.assertEquals([], stats.power_chords)

    def test_power_chords(self):
        stats = analysis.Stats()

        stats.analyse("arpeggios.log")

        # arpeggios are not expected, power chords are
        self.assertEquals([], stats.arpeggios)
        self.assertEquals(['CG', 'GD', 'DA', 'AD'], stats.power_chords)

    def test_diagonals(self):
        stats = analysis.Stats()

        stats.analyse("arpeggios.log")

        # there are two diagonal moves in arpeggios.log
        self.assertEquals(2, len(stats.diagonals))

        # the diagonal moves are:
        expected_diagonals = [
            {'from': (5, 5), 'to': (4, 4)},
            {'from': (2, 4), 'to': (1, 5)}
        ]

        self.assertEquals(expected_diagonals, stats.diagonals)

if __name__ == '__main__':
    unittest.main()
