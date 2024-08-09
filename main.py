from Game import Game
from StateNode import StateNode
from DfsStrategy import DfsStrategy
from prio_q import PriorityQueue

pq = PriorityQueue()
pq.push(StateNode(12345678),12)
pq.push(StateNode(13245678),11)
pq.push(StateNode(13254678),10)

print(pq.pop())
print(pq.pop())
s = StateNode(182043765, depth=0)
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
