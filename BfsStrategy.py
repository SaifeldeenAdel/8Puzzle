from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
from queue import Queue
from typing import Set


class BfsStrategy(SearchStrategyInterface):
    def __init__(self):
        self.queue = None

    def create_frontier(self, initial_state: StateNode):
        # create a queue and insert initial state
        self.queue = Queue()
        self.queue.put(initial_state)

    def get_next_state(self) -> StateNode:
        return self.queue.get()  # .get == .dequeue

    def check_neighbor_state(self, neighbor: StateNode, explored_set: Set[StateNode]):
        if not (neighbor in self.queue or neighbor in explored_set):
            self.queue.put(neighbor)

    def is_frontier_empty(self) -> bool:
        return self.queue.empty()

