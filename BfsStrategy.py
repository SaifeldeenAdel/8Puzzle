from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
from queue import Queue
from typing import Set

class BfsStrategy(SearchStrategyInterface):
    def __init__(self):
        self.queue = None

    def create_frontier(self, initial_state: StateNode):
        # Declare an empty queue
        self.queue = Queue()

    def get_next_state(self) -> StateNode:
        return self.queue.get()  # .get == .dequeue

    def check_neighbor_state(self,neighbor : StateNode,explored_set: Set[StateNode]):
        if neighbor in self.queue or neighbor in explored_set:
            self.queue.put(neighbor)