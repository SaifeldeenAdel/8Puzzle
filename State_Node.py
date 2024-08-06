from __future__ import annotations  # for forward refrencing
import numpy as np
from numpy.typing import NDArray


class State_Node:

    def __init__(self, state: str, parent: State_Node = None):
        self.state = state
        while not self.validate_state():
            self.state = input("State not valid, please reenter")
        self.parent = parent

    def numpy_format(self) -> NDArray[np.int64]:
        return np.array([int(letter) for letter in self.state]).reshape(3, 3)

    def validate_state(self):
        if len(self.state) != 9:
            return False
        for letter in self.state:
            if not letter.isdigit():
                return False
        return True
