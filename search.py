import pacmaze
import fringe
import sys


def graph_search(maze, initial_state, fringe):
    explored = {}
    fringe.insert(pacmaze.Node(initial_state))
    
    while True:
        if fringe.is_empty():
            return None

        node = fringe.remove()
        
        #print "%d, %d, %d" % (node.state[0], node.state[1], maze.query(node.state[0], node.state[1]))
        #print maze

        if maze.is_goal(node.state):
            return pacmaze.PacMaze.solution(node)

        if node.state not in explored:
            explored[node.state] = True
            fringe.insert_list(maze.expand(node))

        #sys.stdout.write('\rFringe size: %8d' % len(fronteira.elementos))
        #print 'expandiu', node.estado, 'len(fechados)', len(fechados)


def bfs(input_file, initial_state):
    sol = graph_search(pacmaze.PacMaze(input_file), initial_state, fringe.BFSFringe())
    #print ' '.join(sol)
    return sol


def dfs(input_file, initial_state):
    sol = graph_search(pacmaze.PacMaze(input_file), initial_state, fringe.DFSFringe())
    #print ' '.join(sol)
    return sol


def astar(world, initial_state):
    manhattan = lambda node: manhattan_distance(node.state, world.goal_position())
    sol = graph_search(world, initial_state, fringe.AStarFringe(manhattan))
    #print ' '.join(sol)
    return sol


def is_optimal_solution(input_file, initial_state, actions):
    """
    Retorna se o conjunto de acoes a partir de estado_inicial leva ao estado final
     e e' o menor possivel
    :param initial_state:
    :param actions:
    :return: bool
    """

    maze = pacmaze.PacMaze(input_file)
    if maze.is_solution(initial_state, actions):
        # bfs is guaranteed to be optimal since costs are unitary:
        return len(bfs(input_file, initial_state)) == len(actions)

    return False

def manhattan_distance(state1, state2):
     return abs(state1[0] - state2[0]) + abs(state1[1] - state1[1])