from __future__ import annotations
import numpy as np
from numpy.typing import NDArray


class StateNode:
    def __init__(self, state: int, parent: StateNode = None, depth=0):
        self.state = state
        while not self.validate_state():
            self.state = int(input("State not valid, please reenter"))
        self.parent = parent
        self.depth = depth

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
        if length > 9:
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
        return "".join(str_state)

    def get_neighbors(self) -> list[StateNode]:
        neighbors = []
        temp = str(self.state)
        if len(temp) == 8:
            temp = '0' + temp
        i = temp.index('0')
        if i == 0:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), parent=self, depth=self.depth + 1))
        elif i == 1:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), parent=self, depth=self.depth + 1))
        elif i == 2:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), parent=self, depth=self.depth + 1))
        elif i == 3:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), parent=self, depth=self.depth + 1))
        elif i == 4:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), parent=self, depth=self.depth + 1))
        elif i == 5:
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), parent=self, depth=self.depth + 1))
        elif i == 6:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), parent=self, depth=self.depth + 1))
        elif i == 7:
            neighbors.append(StateNode(int(self.__swap(temp, i, i + 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), parent=self, depth=self.depth + 1))
        elif i == 8:
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 1)), parent=self, depth=self.depth + 1))
            neighbors.append(StateNode(int(self.__swap(temp, i, i - 3)), parent=self, depth=self.depth + 1))
        return neighbors

    def get_state(self) -> int:
        return self.state

    def get_parent(self) -> StateNode:
        return self.parent

    def set_depth(self, n):
        self.depth = n

    def get_depth(self) -> int:
        return self.depth

    def __repr__(self) -> str:
        return str(self.numpy_format()) + "\n"

    def __hash__(self):
        return hash(self.state)

    def __eq__(self, other: StateNode) -> bool:
        if isinstance(other, StateNode):
            return self.state == other.state
        return False
