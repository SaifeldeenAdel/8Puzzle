from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
from collections import deque
from typing import Set


class BfsStrategy(SearchStrategyInterface):
    def __init__(self, initial_state):
        super().__init__(initial_state=initial_state)
        
    def create_frontier(self, initial_state: StateNode):
        # create a queue and insert initial state
        self.frontier = deque()
        self.frontier.append(initial_state)

    def get_next_state(self) -> StateNode:
        return self.frontier.popleft()

    def check_neighbor_state(self, neighbor: StateNode, explored_set: Set[StateNode]):
        if not (neighbor in self.frontier or neighbor in explored_set):
            self.frontier.append(neighbor)

    def is_frontier_empty(self) -> bool:
        return len(self.frontier) == 0
    
    def __repr__(self) -> str:
        return "DFS"

