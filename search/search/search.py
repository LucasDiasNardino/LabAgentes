# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """

        util.raiseNotDefined()

        searchAgents = __import__('searchAgents')

        return searchAgents.getStartState()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

        searchAgents = __import__('searchAgents')

        if(searchAgents.isGoalState(state)):
            return True
        else:
            return False

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

        searchAgents = __import__('searchAgents')

        return searchAgents.getSuccessors(state)

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()

        searchAgents = __import__('searchAgents')

        return searchAgents.getCostOfActions(actions)


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    searchAgents = __import__('searchAgents')

    startState = searchAgents.getStartState()

    visited = set()

    visited.add(startState)

    while True:
        if(problem.isGoalState(startState)):
            return True
        else:
            for successor, _, _ in problem.getSuccessors(startState):
                if(successor not in visited):
                    visited.add(successor)
                    startState = successor
                    break
                else:
                    return False           
    


def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    searchAgents = __import__('searchAgents')


    startState = searchAgents.getStartState()

    visited = set()  
    queue = __import__('util').Queue()  

    visited.add(startState)
    queue.push(startState)

    while not queue.isEmpty(): 
        m = queue.pop()

        if problem.isGoalState(m):
            return True

        for neighbor, _, _ in problem.getSuccessors(m):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.push(neighbor)

    return False  


def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

    searchAgents = __import__('searchAgents')

    startState = searchAgents.getStartState()

    #uniform cost search algorithm
    visited = set()
    queue = __import__('util').PriorityQueue()

    visited.add(startState)
    queue.push(startState, 0)

    while queue:
        queue.sort() 
        cost, state = queue.pop(0)  

        if state not in visited:
            visited.add(state)

            if problem.isGoalState(state):
                return True

            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    total_cost = cost + step_cost
                    queue.append((total_cost, successor))

    return False 

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    util.raiseNotDefined()

    searchAgents = __import__('searchAgents')

    if problem is None:
        return 0
    
    x1, y1 = state
    x2, y2 = problem.goal

    return abs(x1 - x2) + abs(y1 - y2)


def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


    searchAgents = __import__('searchAgents')

    startState = searchAgents.getStartState()


    visited = set()
    visited.add(startState)

    queue = __import__('util').PriorityQueue()
    queue.push(startState, 0)

    while queue:
        queue.sort() 
        cost, state = queue.pop(0)  

        if state not in visited:
            visited.add(state)

            if problem.isGoalState(state):
                return True

            for successor, action, step_cost in problem.getSuccessors(state):
                if successor not in visited:
                    total_cost = cost + step_cost
                    queue.append((total_cost, successor))

    return False

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
