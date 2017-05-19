import os
import pacmaze
import search


def run():
    
    # creates data directory
    if not os.path.exists('data'):
        os.mkdir('data')

    maze = pacmaze.PacMaze(None)
    goals = [(9, 9), (11, 11), (0, 0), (11, 5)]
    
    for num, goal in enumerate(goals):

        outfile = open('data/log%d.log' % num, 'w')

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
    run()
    print 'Done'
