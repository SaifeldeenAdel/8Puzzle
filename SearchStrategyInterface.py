from __future__ import annotations
from abc import ABC, abstractmethod
from StateNode import StateNode
from typing import Set

class SearchStrategyInterface(ABC):
    @abstractmethod
    def create_frontier(self, initial_state: StateNode):
        pass
        # self.frontier = xxx

    @abstractmethod
    def get_next_state(self) -> StateNode:
        pass
        # return self.frontier.pop

    @abstractmethod
    def check_neighbor_state(self,neighbor: StateNode, explored_set : Set[StateNode]):
        pass
        # all actions require frontier list which can be accessed from "self"
        # only need explored set in if statement
