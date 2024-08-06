from Game import Game
from StateNode import StateNode
#game = Game()
#while True:
#    game.new_game()
#    game.play()

s = StateNode("012342678")
n = s.numpy_format()
print(n)
print(n.dtype)