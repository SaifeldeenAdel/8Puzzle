from Game import Game
from StateNode import StateNode
from DFS import DFS

s = StateNode(132045678)
game = Game(s)

while True:
    game.new_game()
    game.play()

# s = StateNode(132045678)
# n = s.numpy_format()
# print(n)
# print(n.dtype)
