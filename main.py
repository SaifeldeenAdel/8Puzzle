from Game import Game
from StateNode import StateNode

s = StateNode("012345678")
game = Game(s)
while True:
    game.new_game()
    game.play()

# n = s.numpy_format()
# print(n)
# print(n.dtype)