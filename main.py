from Game import Game
from StateNode import StateNode
from DFS import DFS

s = StateNode(182043765, depth=0)

game = Game(s)

while True:
  game.new_game()
  game.play()

# s = StateNode(1234568)
# n = s.numpy_format()
# print(n)
# print(n.dtype)
