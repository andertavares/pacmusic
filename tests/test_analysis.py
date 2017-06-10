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

        self.assertEquals([{'from': (5, 5),'to': (4, 4)}, {'from': (2, 4),'to': (1, 5)}], stats.diagonals)
        self.assertEquals([], stats.power_chords)

    def test_power_chords(self):
        stats = analysis.Stats()
        stats.analyse("power_chords.log")
        # arpeggios are not expected, power chords are
        self.assertEquals([], stats.arpeggios)
        self.assertEquals(['CG', 'GD', 'DA', 'AD'], stats.power_chords)

    def test_positions(self):
        stats = analysis.Stats()
        stats.analyse("power_chords.log")

        # there are 5 positions in power_chords.log
        self.assertEquals(5, len(stats.positions))

        # compares the coordinates
        self.assertEquals(
            [
                (5, 5),
                (4, 4),
                (3, 4),
                (2, 4),
                (1, 5)
            ],
            stats.positions
        )

    def test_num_moves(self):
        stats = analysis.Stats()
        stats.analyse("arpeggios.log")

        # 4 moves are performed in arpeggios.log
        self.assertEquals(4, stats.num_moves())

    def test_occurrences(self):
        stats = analysis.Stats()
        stats.analyse("intervals.log")

        # intervals.log has CEG twice and BF 4 times

        self.assertEquals(2, stats.occurrences('CEG'))
        self.assertEquals(4, stats.occurrences('BF'))
        self.assertEquals(0, stats.occurrences('GBD'))

    def test_intervals(self):
        stats = analysis.Stats()
        stats.analyse("intervals.log")

        # CEG is separated by two notes
        self.assertEquals([2], stats.intervals('CEG'))

        # BF occurrences are separated by 3, 0 and 1 notes
        # [3, 0, 0, 1] ??? 
        self.assertEquals([3, 0, 1], stats.intervals('BF'))

        # GBD does not occur, so empty list of intervals
        self.assertEquals([], stats.intervals('GBD'))


if __name__ == '__main__':
    unittest.main()
