from Game import Game
from State_Node import State_Node
#game = Game()
#while True:
#    game.new_game()
#    game.play()

s = State_Node("012342678")
n = s.numpy_format()
print(n)
print(n.dtype)