import argparse
import pacmaze
import search
import sys
import os


def run(params):
    """
    Runs the program with parameters specified from command line
    :param params:
    :return:
    """
    
    # creates data directory
    outdir = params['output_dir']
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    worldfile = None
    if 'world' in params:
        worldfile = params['world']

    maze = pacmaze.PacMaze(worldfile)

    goals = [(9, 9), (11, 11), (0, 0), (11, 5)]  # for 12x12 world
    #goals = [(6, 6), (0, 0), (0, 6), (6, 0)]  # for 7x7 world
    
    for num, goal in enumerate(goals):

        outfile = open(os.path.join(outdir, 'log%d.log' % num), 'w')

        print 'Current goal: (%d,%d)' % goal

        maze.set_goal(goal[0], goal[1])
        directions = search.astar(maze, maze.pacman_position())
        #print 'Directions:', directions #pacmaze.PacMaze.solution(goal)
        
        path = maze.walk(maze.pacman_position(), directions)
        print 'PM at', maze.pacman_position()

        outfile.write('\n'.join(['%d, %d, %s' % (x[0], x[1], x[2]) for x in path]))
        print '\n'.join(['%d, %d, %s' % (x[0], x[1], x[2]) for x in path])

        print 'File written.'
        outfile.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='PacMusic - A PacMan-like world with music.')
    parser.add_argument('-w', '--world', type=str, help='Path to the world file')
    parser.add_argument('-d', '--with-diagonals', action='store_true', help='Allow diagonal moves')
    parser.add_argument(
        '-o', '--output-dir', type=str, help='Directory where output is generated',
        default='data'
    )
    args = vars(parser.parse_args())

    run(args)
    print 'Done'
