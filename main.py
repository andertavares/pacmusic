import random_walk
import argparse
import pacmaze
import random
import search
import os


def run(params):
    """
    Runs the program with parameters specified from command line
    :param params:
    :return:
    """
    # sets random seed
    if 'random_seed' in params:
        random.seed(params['random_seed'])
    
    # creates output directory
    outdir = params['output_dir']
    if not os.path.exists(outdir):
        os.mkdir(outdir)

    worldfile = None
    if 'world' in params:
        worldfile = params['world']

    maze = pacmaze.PacMaze(worldfile)

    # sets diagonal moves as specified by user
    maze.set_diagonal_moves(args['diagonals'])

    for num in range(args['number_trials']): #, goal in enumerate(goals):

        outfile = open(os.path.join(outdir, 'log%d.log' % num), 'w')

        # randomly selects the goal within world boundaries
        row = random.randint(0, len(maze._world) - 1)
        col = random.randint(0, len(maze._world[0]) - 1)
        goal = (row, col)

        print 'Current goal: (%d, %d)' % goal

        maze.set_goal(goal[0], goal[1])

        directions = []

        # determines which method will be used for walking
        if params['method'] == 'astar':
            directions = search.astar(maze, maze.pacman_position())

        elif params['method'] == 'random':
            directions = random_walk.random_walk(maze, maze.pacman_position())

        # print 'Directions:', directions #pacmaze.PacMaze.solution(goal)
        
        path = maze.walk(maze.pacman_position(), directions)
        # print 'PM at', maze.pacman_position()

        outfile.write('\n'.join(['%d, %d, %d' % (x[0], x[1], pacmaze.CHORDS[x[2]]) for x in path]))
        # print '\n'.join(['%d, %d, %s' % (x[0], x[1], pacmaze.CHORDS[x[2]]) for x in path])

        print 'File written.'
        outfile.close()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='PacMusic - A PacMan-like world with music.')

    parser.add_argument('-w', '--world', type=str, help='Path to the world file')
    parser.add_argument(
        '-n', '--number-trials', type=int, default=100,
        help='Number of goals the agent must seek'
    )
    parser.add_argument(
        '-s', '--random_seed', type=int,
        help='A number to seed the random generator'
    )
    parser.add_argument('-d', '--diagonals', action='store_true', help='Allow diagonal moves')
    parser.add_argument(
        '-o', '--output-dir', type=str, help='Directory where output is generated',
        default='data'
    )
    parser.add_argument(
        '-m', '--method', type=str, help='Method used by PacMan to move.',
        action='store', default='astar', choices=['astar', 'random', 'randombiased']
    )

    args = vars(parser.parse_args())

    run(args)
    print 'Done'
