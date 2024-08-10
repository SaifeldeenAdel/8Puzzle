from Game import Game
from StateNode import StateNode
from DfsStrategy import DfsStrategy
from prio_q import PriorityQueue

s = StateNode(182043765, depth=0)
game = Game(s)

while True:
    game.new_game()
    game.play()
