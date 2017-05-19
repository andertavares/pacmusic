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

    currentPos = initial_position

    moves = []

    #logFileName = "data/log";
    
    #logFile = open(logFileName,"w");

    #size = 12;

    for steps in range(240):
        randomVariable = random.random()

        oldPos = [currentPos[0], currentPos[1]]

        key = pacmaze.CHORDS['SILENCE']

        direction = random.choice(world.STRAIGHT.keys())

        '''
        if randomVariable < 0.2:  # stand
            nextX = 0
            nextY = 0

        if (randomVariable >= 0.2 and randomVariable < 0.4):  # right
            nextX = 1
            nextY = 0

        if (randomVariable >= 0.4 and randomVariable < 0.6):  # left
            nextX = -1;
            nextY = 0;

        if (randomVariable >= 0.6 and randomVariable < 0.8):  # up
            nextX = 0;
            nextY = 1;

        if (randomVariable >= 0.8):  # down
            nextX = 0;
            nextY = -1;
        '''
        # applies the move in current direction
        currentPos = world.apply_move(currentPos, world.STRAIGHT[direction])

        #currentPos[0] = currentPos[0] + move[0]
        #currentPos[1] = currentPos[1] + move[1]

        '''
        # makes the 'wall teleport'
        if (currentPos[0] < 0):
            currentPos[0] = size-1

        elif (currentPos[0] > size-1):
            currentPos[0] = 0;

        if (currentPos[1] < 0):
            currentPos[1] = size-1;

        elif (currentPos[1] > size-1):
            currentPos[1] = 0;
        '''

        '''
        # checks if PacMan has stood still
        if currentPos == oldPos: #(currentPos[0] == oldPos[0] and currentPos[1] == oldPos[1]):
            key = pacmaze.CHORDS['SILENCE']
        else:
            key = world.query(currentPos) #block[currentPos[0]][currentPos[1]];

        logFile.write("%d, %d, %d\n" % (currentPos[0], currentPos[1], key))
        '''

        # adds current direction
        moves.append(direction)

        # checks whether goal was reached
        if currentPos == world.goal_position():
            break

    # sets pac man position and returns
    world.set_pacman_position(currentPos[0], currentPos[1])
    return moves
'''
if __name__ == '__main__':
    begin = 0

    for n in range(1000):
        random_walk("data/log%d.log" % n);
'''