#!/usr/bin/python

import random
import pacmaze

SILENCE = 0;
A = 1;
B = 2;
C = 3;
D = 4;
E = 5;
F = 6;
G = 7;

def random_walk(logFileName):
    world = pacmaze.PacMaze(None)

    block = world._world

    currentPos = [5, 5];

    #logFileName = "data/log";
    
    logFile = open(logFileName,"w");

    size = 12;

    nextX = 0;
    nextY = 0;

    for steps in range(240):
        randomVariable = random.random();

        oldPos = [currentPos[0], currentPos[1]];

        key = SILENCE;

        if (randomVariable < 0.2): # stand
            nextX = 0;
            nextY = 0;

        if (randomVariable >= 0.2 and randomVariable < 0.4): # right
            nextX = 1;
            nextY = 0;

        if (randomVariable >= 0.4 and randomVariable < 0.6): # left
            nextX = -1;
            nextY = 0;

        if (randomVariable >= 0.6 and randomVariable < 0.8): # up
            nextX = 0;
            nextY = 1;

        if (randomVariable >= 0.8): # down
            nextX = 0;
            nextY = -1;


        currentPos[0] = currentPos[0] + nextX;
        currentPos[1] = currentPos[1] + nextY;

        # makes the 'wall teleport'
        if (currentPos[0] < 0):
            currentPos[0] = size-1

        elif (currentPos[0] > size-1):
            currentPos[0] = 0;

        if (currentPos[1] < 0):
            currentPos[1] = size-1;

        elif (currentPos[1] > size-1):
            currentPos[1] = 0;

        if (currentPos[0] == oldPos[0] and currentPos[1] == oldPos[1]):
            key = SILENCE;
        else:
            key = block[currentPos[0]][currentPos[1]];

        logFile.write("%d, %d, %d\n" % (currentPos[0], currentPos[1], key))
    logFile.close();


if __name__ == '__main__':
    begin = 0

    for n in range(1000):
        random_walk("data/log%d.log" % n);
