from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
import time


class AlgorithmHandler:

    def __init__(self, strategy: SearchStrategyInterface):
        self.strategy = strategy

    def set_strategy(self, new_strategy: SearchStrategyInterface):
        self.strategy = new_strategy

    def __goal_test(self, potential_goal: StateNode) -> bool:
        return potential_goal.get_state() == 12345678

    def do_algorithm(self, initial_state: StateNode) -> (StateNode, int, float):  # type: ignore
        limit = 500
        begin = time.time()

        self.strategy.create_frontier(initial_state)
        explored_set = set()
        i = 0
        while not self.strategy.is_frontier_empty():

            next_state: StateNode = self.strategy.get_next_state()
            print(next_state.state)
            i += 1
            print(f"i={i}")
            explored_set.add(next_state)
            if self.__goal_test(next_state):
                end = time.time()
                running_time = end - begin
                return next_state, len(explored_set)-1, running_time

            for neighbor in next_state.get_neighbors():
                self.strategy.check_neighbor_state(neighbor, explored_set)
            print(f"current level: {next_state.depth}")
            print(f"frontier: {len(self.strategy.frontier)}")
            print(f"explored_set: {len(explored_set)}")
