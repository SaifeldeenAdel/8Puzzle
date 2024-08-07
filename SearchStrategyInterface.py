from __future__ import annotations
from abc import ABC, abstractmethod
from StateNode import StateNode
from typing import Set

class SearchStrategyInterface(ABC):
    def __init__(self, initial_state):
        self.frontier = None
        self.create_frontier(initial_state=initial_state)

        self.explored_set = {}
        
    @abstractmethod
    def create_frontier(self, initial_state: StateNode):
        pass
        # self.frontier = xxx

    @abstractmethod
    def get_next_state(self) -> StateNode:
        pass
        # return self.frontier.pop

    @abstractmethod
    def check_neighbor_state(self,neighbor: StateNode):
        pass
        # all actions require frontier list which can be accessed from "self"
        # only need explored set in if statement

        
    @abstractmethod
    def is_frontier_empty(self) -> bool:
        pass
