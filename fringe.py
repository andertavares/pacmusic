import abc
import heapq  # for astar
from abc import abstractmethod
import collections


class Fringe(object):
    """
    Represents the frontier in graph search.
    Cannot be directly instantiated.
    """

    __metaclass__ = abc.ABCMeta

    def __init__(self):
        self.elements = []

    @abstractmethod
    def insert(self, node):
        """
        Inserts node in fringe
        :param node:
        :return:
        """
        pass

    def insert_list(self, the_list):
        """
        Insere all list nodes in fringe
        :param the_list:
        :return:
        """
        for node in the_list:
            self.insert(node)

    @abstractmethod
    def remove(self):
        """
        Removes a node from fringe and returns it
        :return: Node
        """
        pass

    def is_empty(self):
        """
        Whether the fringe is empty
        :return: bool
        """
        return len(self.elements) == 0


class DFSFringe(Fringe):
    """
    Behaves as a stack
    """
    def insert(self, node):
        self.elements.append(node)

    def remove(self):
        return self.elements.pop()


class BFSFringe(Fringe):
    """
    Behaves as a queue
    """
    def __init__(self):
        super(BFSFringe, self).__init__()
        self.elements = collections.deque()

    def insert(self, node):
        self.elements.append(node)

    def remove(self):
        return self.elements.popleft()


class AStarFringe(Fringe):
    """
    Implements the fringe of A*
    """
    def __init__(self, heuristic):
        super(AStarFringe, self).__init__()
        self.heur = heuristic

    def insert(self, node):
        heapq.heappush(self.elements, (self.cost(node), node))

    def remove(self):
        #speeds up with a heap
        cost, to_remove = heapq.heappop(self.elements)
        return to_remove

    def cost(self, node):
        return node.cost + self.heur(node)
