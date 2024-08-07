from __future__ import annotations  # for forward refrencing
import numpy as np
from numpy.typing import NDArray


class StateNode:

    def __init__(self, state: int , parent: StateNode = None):
        self.state = state
        while not self.validate_state():
            self.state = input("State not valid, please reenter")
        self.parent = parent

    def numpy_format(self) -> NDArray[np.int64]:
        
        return np.array([int(letter) for letter in str(self.state)]).reshape(3, 3)

    def validate_state(self):
        ls = [0] * 9
        temp = self.state
        i = 0
        while i <= 9:
            digit = temp % 10
            if digit > 8:
                return False
            ls[digit] = 1
            temp = temp //10
            i+=1
        if 0 in ls: 
            return False
        else: return True



    def get_neighbors(self):
        pass

