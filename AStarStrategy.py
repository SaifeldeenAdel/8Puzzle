from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
import heapq as pq
from prio_q import PriorityQueue
import numpy as np
import numpy.typing as NDarray
from typing import Set


class AStarStrategy(SearchStrategyInterface):
    def __init__(self, initial_state, heuristic_function):
        self.hf = heuristic_function
        super().__init__(initial_state)

    def heuristic(self, *args, **kwargs):
        return self.hf(*args, **kwargs)

    def create_frontier(self, initial_state: StateNode):
        # self.frontier = []
        # pq.heapify(self.frontier)
        # pq.heappush(self.frontier, (self.heuristic(initial_state), initial_state))
        self.frontier = PriorityQueue()
        self.frontier.push(initial_state, self.heuristic(initial_state) + initial_state.depth)

    def get_next_state(self) -> StateNode:
        return self.frontier.pop()  # returns a tuple, first element is priority and second is the node

    def is_frontier_empty(self) -> bool:
        return len(self.frontier) == 0

    def check_neighbor_state(self, neighbor: StateNode, explored_set: Set[StateNode]):
        if not (neighbor in self.frontier or neighbor in explored_set):
            # pq.heappush(self.frontier, (self.heuristic(neighbor), neighbor))
            self.frontier.push(neighbor, self.heuristic(neighbor) + neighbor.depth)

## many errors
