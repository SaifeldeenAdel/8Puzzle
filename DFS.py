from SearchStrategyInterface import SearchStrategyInterface
from StateNode import StateNode
from typing import Set

class DFS(SearchStrategyInterface):
  def __init__(self, initial_state):
    super().__init__(initial_state=initial_state)

  def create_frontier(self, initial_state: StateNode):
    self.frontier = [initial_state]

  def get_next_state(self) -> StateNode:
    return self.frontier.pop()
  
  def check_neighbor_state(self, neighbor: StateNode, explored_set: Set[StateNode]):
    if neighbor not in self.frontier or neighbor not in explored_set:
      self.frontier.append(neighbor)
