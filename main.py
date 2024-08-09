from Game import Game
from StateNode import StateNode
from DfsStrategy import DfsStrategy

s = StateNode(312645708, depth=0)
#  182043765
#  312645708
game = Game(s)

while True:
    game.new_game()
    game.play()

# s = StateNode(1234568)
# n = s.numpy_format()
# print(n)
# print(n.dtype)
