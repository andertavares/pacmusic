import unittest
import pacmaze


class TestPacMaze(unittest.TestCase):

    def test_successors(self):
        world = pacmaze.PacMaze('worlds/7x7_paper.txt')

        # without diagonals:
        world.set_diagonal_moves(False)

        # expected successors of 6, 6
        expected_successors = [
            ('imovel', (6, 6)),
            ('acima', (5, 6)),
            ('abaixo', (7, 6)),
            ('esquerda', (6, 5)),
            ('direita', (6, 7)),
        ]

        # converts to set 'coz order does not matter
        self.assertEquals(set(expected_successors), set(world.successors(6, 6)))

        # allow diagonals:
        world.set_diagonal_moves(True)

        # add the diagonals
        expected_successors += [
            ('nordeste', (5, 7)),
            ('noroeste', (5, 5)),
            ('sudeste', (7, 7)),
            ('sudoeste', (7, 5)),
        ]

        # converts to set 'coz order does not matter
        self.assertEquals(set(expected_successors), set(world.successors(6, 6)))

    def test_query_7x7paper_world(self):
        world = pacmaze.PacMaze('worlds/7x7_paper.txt')

        self.assertEquals('E', world.query(5, 5))

        # coordinate mod 7 should give the same note
        self.assertEquals('E', world.query(12, 12))
        self.assertEquals('E', world.query(19, 19))
        self.assertEquals('E', world.query(-2, -2))

    def test_move_7x7paper_world(self):
        world = pacmaze.PacMaze('worlds/7x7_paper.txt')

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
