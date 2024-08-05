import pygame

CELL_SIZE = 500//3
class Tile:
  def __init__(self, surface, x,y,width, height, num, pos) -> None:
    self.surface = surface
    self.val = num
    self.pos = pos

    self.rect = pygame.Rect(x,y,width, height)
    
  
  def draw(self):
    font = pygame.font.Font(None, 45)
    text = font.render(str(self.val), True, (255,255,255))

    pygame.draw.rect(self.surface, (50, 50, 155), self.rect)
    self.surface.blit(text, text.get_rect(center=self.rect.center))
    

  def is_clicked(self):
    if self.rect.collidepoint(pygame.mouse.get_pos()):
      if pygame.mouse.get_pressed()[0] and self.clicked == False:
        self.clicked = True
        return True
      
    if not pygame.mouse.get_pressed()[0]:
      self.clicked = False
      
    return False
  
  def get_neighbors(self, state):
    neighbors = {'top': None, 'bottom': None, 'left': None, 'right': None}
    x, y = self.pos
    if y > 0:
        neighbors['top'] = state[x][y - 1]
    if y < len(state[0]) - 1:
        neighbors['bottom'] = state[x][y + 1]
    if x > 0:
        neighbors['left'] = state[x - 1][y]
    if x < len(state) - 1:
        neighbors['right'] = state[x + 1][y]
    return neighbors
  
  def has_valid_action(self,state):
    x, y = self.pos
    neighbors = self.get_neighbors(state)

    if neighbors['top'] is not None and neighbors['top'] == 0:
        return (self, (x, y - 1))
    if neighbors['bottom'] is not None and neighbors['bottom'] == 0:
        return (self, (x, y + 1))
    if neighbors['left'] is not None and neighbors['left'] == 0:
        return (self, (x - 1, y))
    if neighbors['right'] is not None and neighbors['right'] == 0:
        return (self, (x + 1, y))
    return None

  def move(self,pos):
    self.rect.x = 5 + pos[1] * CELL_SIZE + 10
    self.rect.y = 5 + pos[0] * CELL_SIZE + 10
    self.pos = pos
    
      
    