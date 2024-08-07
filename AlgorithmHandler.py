from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode


class AlgorithmHandler:

    def __init__(self, strategy: SearchStrategyInterface):
        self.strategy = strategy

    def set_strategy(self, new_strategy: SearchStrategyInterface):
        self.strategy = new_strategy

    def __goal_test(self, potential_goal: StateNode) -> bool:
        return potential_goal.get_state() == 12345678

    def do_algorithm(self, initial_state: StateNode):

        self.strategy.create_frontier(initial_state)
        explored_set = set()

        while not self.strategy.is_frontier_empty():
            next_state: StateNode = self.strategy.get_next_state()
            explored_set.add(next_state)

            if self.__goal_test(next_state):
                #number_of_expanded_nodes = len(explored_set)
                return next_state  # ?

            for neighbor in next_state.get_neighbors():
                self.strategy.check_neighbor_state(neighbor, explored_set)
