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

    # sets target radius
    target_radius = params['target_radius']

    # sets max targets
    max_targets = params['max_targets']


    maze = pacmaze.PacMaze(worldfile)

    # sets diagonal moves as specified by user
    maze.set_diagonal_moves(args['diagonals'])

    for num in range(args['number_trials']): #, goal in enumerate(goals):

        cont_steps = 0

        for i in range(args['max_targets']):
            col, row = create_target(maze, target_radius)
            goal = (row, col)
            maze.add_goal(goal[0], goal[1])

        # print(maze._goals) #print list goals


        outfile = open(os.path.join(outdir, 'log%d.log' % num), 'w')
        outfile.write('%d, %d, %s' % (maze.pacman_position()[0], maze.pacman_position()[1], maze.query(maze.pacman_position()[0],maze.pacman_position()[1])))
        outfile.write('\n')
        while cont_steps < args['max_steps']:

            # print(maze._goals) #print list remaining
            # print maze.__str__() # print world

            if len(maze._goals) == 0:
                break

            possible_directions = []
            # determines which method will be used for walking
            if params['method'] == 'astar':
                possible_directions = search.astar(maze, maze.pacman_position())

            elif params['method'] == 'random':
                possible_directions = random_walk.random_walk(maze, maze.pacman_position())

            real_directions = []
            for i in possible_directions:
                print cont_steps
                if cont_steps < args['max_steps']:
                    real_directions.append(i)
                    cont_steps = cont_steps + 1
                else:
                    break
            path = maze.walk(maze.pacman_position(), real_directions)
            # agent might have reached some goals, let's re-add them
            while len(maze._goals) < args['max_targets']:
                col, row = create_target(maze, target_radius)
                goal = (row, col)
                maze.add_goal(goal[0], goal[1])

            # print 'PM at', maze.pacman_position()
            outfile.write('\n'.join(['%d, %d, %s' % (x[0], x[1], x[2]) for x in path]))
            outfile.write('\n')
            # print '\n'.join(['%d, %d, %s' % (x[0], x[1], pacmaze.NOTE_TO_INT[x[2]]) for x in path])
        print 'File ' + str(num) + ' written.'
        outfile.close()


def create_target(maze, target_radius, taboo=None):
    """
    Returns a coordinate (row, col) with a target within a radius from the player
    It also returns a coordinate outside a taboo list
    :param maze:pacmaze.PacMaze
    :param target_radius:int
    :param taboo:list(tuple(int,int))
    :return:tuple(int,int)
    """

    if taboo is None:
        taboo = []

    player_pos = maze.pacman_position()

    # initializes selected coordinates as player's position
    row, col = player_pos

    # adds player position to taboo to activate the loop at least once
    taboo.append(player_pos)

    # randomly selects the goal within target radius
    # repeats until coordinates are not in taboo list
    while (row, col) in taboo:
        row = random.randint(player_pos[0] - target_radius, player_pos[0] + target_radius)
        col = random.randint(player_pos[1] - target_radius, player_pos[1] + target_radius)

    return col, row


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='PacMusic - A PacMan-like world with music.')

    parser.add_argument('-w', '--world', type=str, help='Path to the world file')
    parser.add_argument(
        '-n', '--number-trials', type=int, default=100,
        help='Number of trials (can be seen as repetitions)'
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

    parser.add_argument(
        '-r', '--target-radius', type=int,
        help='Maximum distance from player (in each axis) that a target will appear',
        default=7
    )

    parser.add_argument(
        '-t', '--max-targets', type=int, default=3,
        help='Maximum number of simultaneous targets',

    )

    parser.add_argument(
        '--max-steps', type=int, default=120,
        help='Maximum number of steps per trial.',
    )

    args = vars(parser.parse_args())

    run(args)
    print 'Done'
