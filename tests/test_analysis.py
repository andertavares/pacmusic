import unittest
import analysis

class TestStats(unittest.TestCase):
    def test_arpeggios(self):
        stats = analysis.Stats()
        stats.analyse("arpeggios.log")
        # arpeggios are expected, power chords are not
        self.assertEquals(['CEG', 'EGB', 'GBD'], stats.arpeggios)
        self.assertEquals([], stats.power_chords)

    def test_diagonals(self):
        stats = analysis.Stats()
        stats.analyse("arpeggios.log")
        # arpeggios are expected, power chords are not
        self.assertEquals([{'from': (5, 5),'to': (4, 4)}, {'from': (2, 4),'to': (1, 5)}], stats.diagonals)
        self.assertEquals([], stats.power_chords)

    def test_power_chords(self):
        stats = analysis.Stats()
        stats.analyse("power_chords.log")
        # arpeggios are not expected, power chords are
        self.assertEquals([], stats.arpeggios)
        self.assertEquals(['CG', 'GD', 'DA', 'AD'], stats.power_chords)


if __name__ == '__main__':
    unittest.main()
