import math
class Node:

    def __init__(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost

    def __eq__(self, other):
        if other is None:
            return False

        return self.state == other.state

    def __str__(self):
        parent_state = self.parent.state if self.parent is not None else 'None'
        return 'state: ' + self.state + ', parent: ' \
               + parent_state + ', action: ' + self.action + ', cost: ' + str(self.cost)

    def as_tuple(self):
        """
        Returns a quadruple (action, row, col, cost, parent.row, parent.col) with node's attributes
        :param:
        :return: tuple(str,int,int,int,str)
        """
        prow, pcol = self.parent.state if self.parent is not None else (-1, -1)

        return self.action, self.state[0], self.state[1], self.cost, prow, pcol

# definition of chords
SILENCE = 0
A = 1
B = 2
C = 3
D = 4
E = 5
F = 6
G = 7

"""
Use the note name to retrieve a
corresponding integer
"""
NOTE_TO_INT = {
    'SILENCE': 0,
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
}

"""
Use a integer to retrieve a note
"""
INT_TO_NOTE = ['SILENCE', 'A','B','C','D','E','F','G']


class PacMaze:

    STRAIGHT = {
        'imovel': (0, 0),   # stand still
        'acima': (-1, 0),
        'abaixo': (1, 0),
        'esquerda': (0, -1),
        'direita': (0, 1)
    }

    DIAGONALS = {
        'noroeste': (-1, -1),  # acima + esquerda
        'nordeste': (-1, +1),  # acima + direita
        'sudoeste': (+1, -1),  # abaixo + esquerda
        'sudeste':  (+1, +1),  # abaixo + direita
    }

    WALL = '#'
    PACMAN = 'P'
    GOAL = '*'

    def __init__(self, inputfile):

        # default 12 x 12 grid
        self._world = [
            'CDEFGABAGFED',
            'DEFGABCBAGFE',
            'EFGABCDCBAGF',
            'FGABCDEDCBAG',
            'GABCDEFEFCBA',
            'ABCDEFGFEDCB',
            'BCDEFGAGFEDC',
            'ABCDEFGFEDCB',
            'GABCDEFEDCBA',
            'FGABCDEDCBAG',
            'EFGABCDCBAGF',
            'DEFGABCBAGFE'
        ]

        # loads world from an input file
        if inputfile is not None:
            self._world = [line.strip() for line in open(inputfile).readlines()]

        self._allow_diagonals = False
        self._pacman_pos = (5, 5)
        self._goals = set()
        # self._goals.add((0, 0)) # a default goal

        self._block_rows = len(self._world)
        self._block_cols = len(self._world[0])

    def query(self, row, col):
        """
        Returns what is in the given world coordinates
        :param row:
        :param col:
        :return:
        """
        return self._world[row % self._block_rows][col % self._block_cols]

    def set_diagonal_moves(self, true_or_false):
        """
        Allow or disallow diagonal moves
        :param true_or_false:bool
        :return:
        """
        self._allow_diagonals = true_or_false

    def pacman_position(self):
        return self._pacman_pos

    def set_pacman_position(self, row, col):
        self._pacman_pos = (row, col)

    def add_goal(self, row, col):
        self._goals.add((row, col))

    def remove_goal(self, row,col):
        self._goals.remove((row, col))

    def closest_goal_position(self):
        """
        Returns the next goal position
        :return: tuple (row, col)
        """
        i = self._pacman_pos
        fx = lambda f,i: math.sqrt((f[0] - i[0])**2 + (f[1] - i[1])**2) if self._allow_diagonals else abs(f[0] - i[0]) + abs(f[1] - i[1])
        mf = (float('inf'),float('inf'))
        df = float('inf')
        for f in self._goals:
            di = fx(f,i)
            if(di<df):
                df = di
                mf = (f[0],f[1])
        return mf

    def successors(self, row, col):
        """
        Returns the successors of the state defined
        by the coordinates received
        :param row:
        :param col:
        :return:
        """
        directions = []
        destinations = []

        allowed_moves = self.STRAIGHT.copy()

        # if diagonal moves are allowed, merge move dicts
        if self._allow_diagonals:
            allowed_moves.update(self.DIAGONALS)

        for direction_name, direction in allowed_moves.iteritems():
            new_row, new_col = self.apply_move((row, col), direction)

            directions.append(direction_name)
            destinations.append((new_row, new_col))

        return zip(directions, destinations)

    def expand(self, node):
        """
        Receives a node and returns a list of successor nodes,
        using the successor function
        :param node:
        :return:
        """
        suc = []
        row, col = node.state
        for (action, reached_state) in self.successors(row, col):
            n = Node(reached_state, node, action, node.cost + 1)

            #avoids re-expanding grandpa node:
            if node.parent is None or node.parent.state != n.state:
                suc.append(n)

        return suc

    @staticmethod
    def solution(node):
        """
        Returns the sequence of actions to reach the received node from root
        :param node:
        :return: list
        """
        steps = []
        while node.parent is not None:
            steps.append(node.action)
            node = node.parent

        steps.reverse()
        return steps

    def is_goal(self, state):
        """
        Returns whether the received state is the goal
        :param state: str
        :return: bool
        """
        return state in self._goals

    def is_solution(self, start_state, actions):
        """
        Returns whether the list of actions reaches the goal
        from the initial state
        :param actions: list
        :return: bool
        """
        cur_state = start_state
        for a in actions:
            prev_state = cur_state  # for checking of illegal moves
            for action, new_state in self.successors(cur_state[0], cur_state[1]):
                if a == action:
                    cur_state = new_state
                    break
            # if action is not in successors, state won't change -> illegal move
            if cur_state == prev_state:
                raise RuntimeError('Illegal move %s attempted at %s' % (a, cur_state))

        # after executing all actions, checks whether reached state is the goal
        return self.is_goal(cur_state)

    def walk(self, initial_pos, directions):
        """
        Follows the directions from initial position, changing PacMan location
        :param initial_pos: tuple (row, col)
        :param directions: list (e.g.: ['acima', 'esquerda', ...])
        :return: list of tuples with coordinates and tiles visited [(row, col, tile), ...]
        """
        path = []
        position = initial_pos

        # retrieves the allowed moves
        moves = self.STRAIGHT.copy()
        if self._allow_diagonals:
            moves.update(self.DIAGONALS)

        # adds current position to path
        # path.append((position[0], position[1], self.query(position[0], position[1])))

        for direction in directions:

            # moves in indicated direction
            position = self.apply_move(position, moves[direction])

            # remove goal
            if (position[0], position[1]) in self._goals:
                self.remove_goal(position[0], position[1])

            # then adds the new position to path
            path.append((position[0], position[1], self.query(position[0], position[1])))


        # sets final position after 'walking'
        self._pacman_pos = position

        return path

    def apply_move(self, position, move):
        """
        Returns a new position when moving in 'direction'
        from 'position'. Checks against boundaries and teleports if needed
        :param position: tuple (row,col)
        :param move: typle (row_increment, col_increment)
        :return tuple: (new_row, new_col)
        """
        # move = self.STRAIGHT[move]

        new_row, new_col = position[0] + move[0], position[1] + move[1]

        # boundary check and 'wall teleport'
        # if new_row < 0:
        #     new_row = len(self._world) - 1  # exit from top, appear on bottom
        #     #print 'appear on bottom'
        #
        # elif new_row > len(self._world) - 1:
        #     new_row = 0  # exit from bottom, appear on top
        #     #print 'appear on top'
        #
        # if new_col < 0:
        #     new_col = len(self._world[0]) - 1  # exit from left, appear on right
        #     #print 'appear on right'
        #
        # elif new_col > len(self._world[0]) - 1:
        #     new_col = 0  # exit from right, appear on left
        #     #print 'appear on left'

        return new_row, new_col

    def __str__(self):
        # header
        string = '   ' + ''.join([str(x) for x in range(len(self._world[0]))]) + '\n'

        for i, row in enumerate(self._world):

            string += str(i).zfill(2) + ' '

            for j, cell in enumerate(self._world[i]):
                char = '-' #str(self.query(i,j))
                if (i, j) == self._pacman_pos:
                    char = 'P'
                elif (i, j) in self._goals:
                    char = '*'

                string += char
            # end of line
            string += '\n'

        return string
