from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
import time


class AlgorithmHandler:

    def __init__(self, strategy: SearchStrategyInterface):
        self.strategy = strategy
        self.max_depth = -10000

    def set_strategy(self, new_strategy: SearchStrategyInterface):
        self.strategy = new_strategy

    def __goal_test(self, potential_goal: StateNode) -> bool:
        return potential_goal.get_state() == 12345678

    def do_algorithm(self, initial_state: StateNode) -> (StateNode, int, float, int):  # type: ignore
        begin = time.time()
        print("Solving ")

        self.strategy.create_frontier(initial_state)
        explored_set = set()

        while not self.strategy.is_frontier_empty():

            next_state: StateNode = self.strategy.get_next_state()
            if next_state.depth > self.max_depth:
                self.max_depth = next_state.depth

            explored_set.add(next_state)
            if self.__goal_test(next_state):
                end = time.time()
                running_time = end - begin
                return next_state, len(explored_set), running_time, self.max_depth 

            for neighbor in next_state.get_neighbors():
                self.strategy.check_neighbor_state(neighbor, explored_set)

