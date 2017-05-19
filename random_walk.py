#!/usr/bin/python

import random
import pacmaze


def random_walk(world, initial_position):
    """
    Performs a uniformly random walk in the world, if it reaches the goal, it's by chance
    :param world: pacmaze.PacMaze
    :param initial_position: tuple (row, col)
    :return: list with moves (e.g.: ['acima', 'imovel', 'esquerda']
    """

    current_pos = initial_position

    moves = []

    for steps in range(240):

        direction = random.choice(world.STRAIGHT.keys())

        # applies the move in current direction
        current_pos = world.apply_move(current_pos, world.STRAIGHT[direction])

        # adds current direction
        moves.append(direction)

        # checks whether goal was reached
        if current_pos == world.goal_position():
            break

    # sets pac man position and returns
    world.set_pacman_position(current_pos[0], current_pos[1])
    return moves
