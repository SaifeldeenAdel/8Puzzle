from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


class StateNode:

    def __init__(self, state: int, parent: StateNode = None):
        self.state = state
        while not self.validate_state():
            self.state = input("State not valid, please reenter")
        self.parent = parent

    def numpy_format(self) -> NDArray[np.int64]:
        if len(str(self.state)) == 8:
            print_state = '0' + str(self.state)
        else:
            print_state = str(self.state)

        return np.array([int(letter) for letter in print_state]).reshape(3, 3)

    def validate_state(self) -> bool:
        ls = [0] * 9
        temp = self.state
        i = 0

        length = len(str(temp))

        # length check
        if length>9:
            return False

        while i <= 9:
            digit = temp % 10
            if digit > 8:
                return False
            ls[digit] = 1
            temp = temp // 10
            i += 1
        if 0 in ls:
            return False
        else:
            return True

    def __swap(self, string, i: int, j: int) -> str:

        str_state = list(string)
        str_state[i], str_state[j] = str_state[j], str_state[i]
        return str(str_state)

    def get_neighbors(self) -> list[StateNode]:
        neighbors = []
        temp = str(self.state)
        if len(temp) == 8:
            temp = '0' + temp
        i = temp.index('0')
        if i == 0:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), self))
        elif i == 1:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), self))
        elif i == 2:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), self))
        elif i == 3:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), self))
        elif i == 4:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), self))
        elif i == 5:
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), self))
        elif i == 6:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), self))
        elif i == 7:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), self))
        elif i == 8:
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), self))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), self))
        return neighbors
        
    def __repr__(self) -> str:
        return str(self.numpy_format())
  

    def get_state(self) -> int:
        return self.state

    def get_parent(self) -> StateNode:
        return self.parent
