import unittest
import pacmaze


class TestPacMaze(unittest.TestCase):
    '''def test_query_7x7paper_world(self):
        world = pacmaze.PacMaze('../worlds/7x7_paper.txt')

        self.assertEquals('E', world.query(5, 5))

        # coordinate mod 7 should give the same note
        self.assertEquals('E', world.query(12, 12))
        self.assertEquals('E', world.query(19, 19))
        self.assertEquals('E', world.query(-2, -2))'''

    def test_move_7x7paper_world(self):
        world = pacmaze.PacMaze('../worlds/7x7_paper.txt')

        path = world.walk((5, 5), ['direita', 'direita', 'direita'])

        self.assertEquals([
                (5, 5, 'E'),
                (5, 6, 'B'),
                (5, 0, 'F'),
                (5, 1, 'C'),
            ],
            path
        )

        self.assertEquals((5, 1), world.pacman_position())


if __name__ == '__main__':
    unittest.main()
