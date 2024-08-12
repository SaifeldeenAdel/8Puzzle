from math import sqrt

from StateNode import StateNode


def get_hypo(state: str, num: int) -> float:
    goal_state = "012345678"
    goal_pos = goal_state.index(str(num))
    state_pos = state.index(str(num))
    y_goal = goal_pos // 3
    x_goal = goal_pos % 3
    y_state = state_pos // 3
    x_state = state_pos % 3
    return sqrt((y_goal - y_state) ** 2 + (x_goal - x_state) ** 2)


def get_man_diff(state: str, num: int) -> int:
    goal_state = "012345678"
    goal_pos = goal_state.index(str(num))
    state_pos = state.index(str(num))
    y_goal = goal_pos // 3
    x_goal = goal_pos % 3
    y_state = state_pos // 3
    x_state = state_pos % 3
    return abs(y_goal - y_state) + abs(x_goal - x_state)


def l1(state_node: StateNode) -> int:
    # get the heuristic value of the initial state
    state_str = str(state_node.get_state())
    length = len(state_str)
    h = 0
    if length == 8:
        state_str = '0' + state_str

    for i in range(9):
        h = h + get_man_diff(state_str, i)
    return h


def l2(state_node: StateNode) -> int:
    # get the heuristic value of the initial state
    state_str = str(state_node.get_state())
    length = len(state_str)
    h = 0
    if length == 8:
        state_str = '0' + state_str

    for i in range(9):
        h = h + get_hypo(state_str, i)
    return h
