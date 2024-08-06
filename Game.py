import pygame.display
import pygame.event
import pygame
import numpy as np 
import random

from Tile import Tile

WIDTH = 750
HEIGHT = 510
CELL_SIZE = 500 // 3

class Game:
  def __init__(self):
    pygame.init()
    self.playing = True
    self.AI = False

    self.clock = pygame.time.Clock()
    self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
    self.surface.fill((202,228,241))

    self.moves = 0
    self.make_grid_and_buttons()


  def play(self):
    while self.playing:
      self.check_events()
      self.check_new_game()
      self.update()
      
    return

  def check_events(self):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
          quit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
          if self.solve_btn.collidepoint(event.pos):
            self.AI = True

          if self.new_game_btn.collidepoint(event.pos):
            self.playing = False
            print("New Game!")
                  
  def check_new_game(self):
    return

  def make_button(self, text, x,y,width,height):
    rect = pygame.Rect(x, y, width, height)
    font = pygame.font.Font(None, 33)
    text = font.render(text, True, (0,0,0))

    pygame.draw.rect(self.surface, (255,255,255), rect)
    self.surface.blit(text, text.get_rect(center=rect.center))
    return rect

  def make_grid_and_buttons(self):
    x_offset = 5
    y_offset = 5
    for i in range(4):
      pygame.draw.line(self.surface, (0,0,0), (x_offset, y_offset + i * CELL_SIZE), (x_offset + 500, y_offset + i * CELL_SIZE), 2)
      pygame.draw.line(self.surface, (0,0,0), (x_offset + i * CELL_SIZE, y_offset), (x_offset + i * CELL_SIZE, y_offset + 500), 2)
  
    self.solve_btn = self.make_button("Solve", 560, 164, 148, 46)
    self.new_game_btn = self.make_button("New Game", 560, 240, 148,46)

  def initialize_tiles(self):
    CELL_SIZE = 500 // 3
    x_offset = 5
    y_offset = 5

    random_state = np.random.permutation(9).reshape(3, 3)
    for i in range(3):
        for j in range(3):
            if random_state[i][j] != 0:
              self.state[i][j] = Tile(surface= self.surface, x= x_offset + j * CELL_SIZE + 10, y= y_offset + i * CELL_SIZE + 10, width =CELL_SIZE - 2 * 10, height=CELL_SIZE - 2 * 10, num=random_state[i][j], pos=(i,j))
              
    self.state = np.array(self.state)


  def new_game(self):
    self.state = [[0]*3 for _ in range(3)]
    self.initialize_tiles()
    self.playing = True
  
  def update(self):
    self.surface.fill((202,228,241))
    self.make_grid_and_buttons()

    if self.AI:
      # Get a sequence of actions and play them one by one?
      action = self.getNextAction()
      self.state = self.transition(self.state, action)
      
    for row in self.state:
      for tile in row:
        if tile != 0:
          tile.draw()
          if self.AI and tile.is_clicked():
            valid_action = tile.has_valid_action(self.state)
            if valid_action:
              self.state = self.transition(self.state, valid_action)

    pygame.display.update()
    self.clock.tick(5)
    
              

  def transition(self, state, valid_action):
    tile = valid_action[0]
    x,y = tile.pos
    new_x, new_y = valid_action[1]
    state[x][y], state[new_x][new_y] = state[new_x][new_y], state[x][y]

    tile.move(valid_action[1])
    self.moves += 1

    return state

  def getValidActions(self):
    valid_actions = []
    for row in self.state:
      for tile in row:
        if tile != 0:
          valid_action = tile.has_valid_action(self.state)
          if valid_action:
            valid_actions.append(valid_action)
    return valid_actions

  def getNextAction(self):
    rnd = random.randint(0, len(self.getValidActions()) - 1)
    return self.getValidActions()[rnd]


    



    
    
        
