from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
import heapq as pq
import numpy as np
import numpy.typing as NDarray
from typing import Set

class AStarStrategy_man(SearchStrategyInterface):
    def __init__(self, initial_state):
        super().__init__(initial_state)

    def __get_man_diff(self, state: NDarray, num: int)-> int:
        # get manhattan distance of num from the goal state
        goal_state = np.array([[0,1,2],[3,4,5],[6,7,8]])
        goal_pos = np.where(goal_state == num)
        state_pos = np.where(state == num)
        return abs(goal_pos[0] - state_pos[0]) + abs(goal_pos[1] - state_pos[1])

    def __get_Hypo(self, state: NDarray, num: int)-> int:
        # get hypo distance of num from the goal state
        goal_state = np.array([[0,1,2],[3,4,5],[6,7,8]])
        goal_pos = np.where(goal_state == num)
        state_pos = np.where(state == num)
        return (goal_pos[0] - state_pos[0])**2 + (goal_pos[1] - state_pos[1])**2

    def heuristic(self, initial_state: StateNode , funct)-> int:
        # get the heuristic value of the initial state
        state = initial_state.get_state()
        h = 0
        for i in range(9):
            h = h + self.funct(state, i)
        return 

    def create_frontier(self, initial_state: StateNode ):
        self.frontier = []
        pq.heapify(self.frontier)
        pq.heappush(self.frontier, (self.heuristic(initial_state, self), initial_state))


    def get_next_state(self) -> StateNode:
        return pq.heappop(self.frontier)
        
    def is_frontier_empty(self) -> bool:
        return len(self.frontier) == 0
    
    def check_neighbor_state(self, neighbor: StateNode, explored_set: Set[StateNode], cost: int):
        if not (neighbor in self.frontier or neighbor in explored_set):
            pq.heappush(self.frontier, (self.heuristic(neighbor, self) + cost , neighbor))

    
## many errors
