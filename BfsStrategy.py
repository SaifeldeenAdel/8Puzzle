from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
from queue import Queue
from typing import Set

class BfsStrategy(SearchStrategyInterface):
    def __init__(self, initial_state):
        super().__init__(initial_state=initial_state)
        
    def create_frontier(self, initial_state: StateNode):
        # Declare an empty frontier
        self.frontier = Queue()

    def get_next_state(self) -> StateNode:
        return self.queue.get()  # .get == .dequeue

    def check_neighbor_state(self,neighbor : StateNode):
        if neighbor in self.queue or neighbor in self.explored_set:
            self.queue.put(neighbor)
