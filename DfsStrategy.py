from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
from typing import Set


class DfsStrategy(SearchStrategyInterface):
    def __init__(self, initial_state):
        super().__init__(initial_state=initial_state)

    def create_frontier(self, initial_state: StateNode):
        self.frontier = [initial_state]

    def get_next_state(self) -> StateNode:
        return self.frontier.pop()

    def check_neighbor_state(self, neighbor: StateNode, explored_set: Set[StateNode]):
        if not (neighbor in self.frontier or neighbor in explored_set or neighbor.depth > 31):
            self.frontier.append(neighbor)

    def is_frontier_empty(self) -> bool:
        return len(self.frontier) == 0
