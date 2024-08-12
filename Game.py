import pygame.display
import pygame.event
import pygame

from Tile import Tile
from StateNode import StateNode

from AlgorithmHandler import AlgorithmHandler
from AStarStrategy import AStarStrategy
from BfsStrategy import BfsStrategy
from DfsStrategy import DfsStrategy

from heuristics import l1, l2

WIDTH = 750
HEIGHT = 510
CELL_SIZE = 500 // 3

BFS_mode = 1
DFS_mode = 2
L1_mode = 3
L2_mode = 4


class Game:
    def __init__(self, start_state: StateNode = None):
        pygame.init()
        self.playing = True
        self.AI_mode = None
        self.sequence = None
        self.moves = 0

        self.start_state = start_state
        self.current_state = self.start_state
        self.tiles = {}

        self.clock = pygame.time.Clock()
        self.surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.surface.fill((202, 228, 241))
        self.make_grid_and_buttons()

    def play(self):
        while self.playing:
            self.check_events()
            self.update()

        return

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.bfs_btn.collidepoint(event.pos):
                    self.AI_mode = BFS_mode

                if self.dfs_btn.collidepoint(event.pos):
                    self.AI_mode = DFS_mode

                if self.l1_btn.collidepoint(event.pos):
                    self.AI_mode = L1_mode

                if self.l2_btn.collidepoint(event.pos):
                    self.AI_mode = L2_mode

                if self.new_game_btn.collidepoint(event.pos):
                    self.playing = False
                    print("New Game!")
                    # call new game?

    def make_button(self, text, x, y, width, height):
        rect = pygame.Rect(x, y, width, height)
        font = pygame.font.Font(None, 33)
        text = font.render(text, True, (0, 0, 0))

        pygame.draw.rect(self.surface, (255, 255, 255), rect)
        self.surface.blit(text, text.get_rect(center=rect.center))
        return rect

    def make_grid_and_buttons(self):
        x_offset = 5
        y_offset = 5
        for i in range(4):
            pygame.draw.line(self.surface, (0, 0, 0), (x_offset, y_offset + i * CELL_SIZE),
                             (x_offset + 500, y_offset + i * CELL_SIZE), 2)
            pygame.draw.line(self.surface, (0, 0, 0), (x_offset + i * CELL_SIZE, y_offset),
                             (x_offset + i * CELL_SIZE, y_offset + 500), 2)

        self.dfs_btn = self.make_button("DFS", 560, 60, 148, 46)
        self.bfs_btn = self.make_button("BFS", 560, 130, 148, 46)
        self.l1_btn = self.make_button("A* L1", 560, 200, 148, 46)
        self.l2_btn = self.make_button("A* L2", 560, 270, 148, 46)
        self.new_game_btn = self.make_button("New Game", 560, 340, 148, 46)

    def create_tiles(self):
        cell_size = 500 // 3
        for i in range(1, 9):
            self.tiles[i] = Tile(surface=self.surface, x=1, y=1, width=cell_size - 2 * 10, height=cell_size - 2 * 10,
                                 num=i)

    def set_tiles(self, state: StateNode):
        for i, row in enumerate(state.numpy_format()):
            for j, col in enumerate(row):
                if col != 0:
                    self.tiles[col].move((i, j))
                    self.tiles[col].set_val(col)

    def new_game(self):
        self.state = [[0] * 3 for _ in range(3)]

        self.create_tiles()
        self.set_tiles(self.start_state)
        self.playing = True

    def update(self):
        self.surface.fill((202, 228, 241))
        self.make_grid_and_buttons()

        if self.AI_mode:
            handler = None
            if self.AI_mode == BFS_mode:
                bfs = BfsStrategy()
                handler = AlgorithmHandler(bfs)

            elif self.AI_mode == DFS_mode:
                dfs = DfsStrategy()
                handler = AlgorithmHandler(dfs)

            elif self.AI_mode == L1_mode:
                A_star_l1 = AStarStrategy(l1)
                handler = AlgorithmHandler(A_star_l1)

            elif self.AI_mode == L2_mode:
                A_star_l2 = AStarStrategy(l2)
                handler = AlgorithmHandler(A_star_l2)

            goal_state ,num_nodes_expanded, running_time = handler.do_algorithm(self.start_state)
            self.sequence = self.get_state_sequence(goal_state)

            goal_state: StateNode

            print(f"Total Moves: {len(self.sequence) - 1}")
            print(f"Solved in {running_time: .2f} seconds")
            print(f"Number of nodes expanded: {num_nodes_expanded}")
            print(f"Search Depth: {goal_state.get_depth()}")

            self.AI_mode = None
            self.moves = 0

        if self.sequence and self.moves < len(self.sequence):
            self.set_tiles(self.sequence[self.moves])
            self.moves += 1
            self.clock.tick(5)

        for k, tile in self.tiles.items():
            tile.draw()

        pygame.display.update()

    def transition(self, state, valid_action):
        tile = valid_action[0]
        x, y = tile.pos
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

    def get_state_sequence(self, goal: StateNode):
        curr = goal
        sequence = []
        while curr is not None:
            # print(sequence)
            sequence.append(curr)
            curr = curr.parent
        sequence.reverse()
        return sequence
