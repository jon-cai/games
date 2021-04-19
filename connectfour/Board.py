import pygame
import random


class Board:
    def __init__(self):
        self.row = 6
        self.col = 7
        self.square_size = 70
        self.circle_size = 25
        self.update = True
        self.mouse_x = -1
        self.mouse_y = -1
        self.grid = [[0] * self.col for _ in range(self.row)]
        self.color = [(52, 157, 234), (255, 255, 0), (255, 0, 0)]
        self.player = random.choice([1, 2])
        self.opp = 3 - self.player
        self.game_over = False
        self.win_set = []
        self.delay = 0
        self.empty = False

    def initialize_board(self, screen):
        screen.fill((20, 20, 235))
        pygame.draw.rect(screen, (52, 157, 234), (0, 0, int(self.square_size * self.col + (self.square_size / 2)), self.square_size * 9 / 10))
        pygame.draw.rect(screen, (52, 157, 234), (0, self.square_size * 11 / 8 + 6 * self.square_size, int(self.square_size * self.col + (self.square_size / 2)),self.square_size * 2))
        wo = self.square_size * 3/4
        ho = self.square_size * 6/4
        for col in range(self.col):
            for row in range(self.row):
                pygame.draw.circle(screen, self.color[self.grid[row][col]], (wo+col*self.square_size, ho+row*self.square_size), self.circle_size)

    def draw_piece(self, screen, row, col):
        if not self.update:
            return
        #screen.fill((20, 20, 235))
        #pygame.draw.rect(screen, (52, 157, 234), (0, 0, int(self.square_size * self.col + (self.square_size / 2)), self.square_size * 9/10))
        #pygame.draw.rect(screen, (52, 157, 234), (0, self.square_size * 11/8 + 6 * self.square_size, int(self.square_size * self.col + (self.square_size / 2)), self.square_size*2))
        wo = self.square_size * 3/4
        ho = self.square_size * 6/4

        if self.game_over and len(self.win_set) >= 4:
            self.win_set = sorted(self.win_set, key=lambda t: (t[0], t[1]))
            for row, col in self.win_set:
                pygame.draw.circle(screen, (10,10,10), (wo + col * self.square_size, ho + row * self.square_size), self.circle_size+4)
                pygame.draw.circle(screen, self.color[self.grid[row][col]], (wo + col * self.square_size, ho + row * self.square_size),self.circle_size)
        #    pygame.draw.line(screen, (10,10,10), (wo + self.win_set[0][1] * self.square_size, ho + self.win_set[0][0] * self.square_size), (wo + self.win_set[-1][1] * self.square_size, ho + self.win_set[-1][0] * self.square_size), width=int(self.circle_size/5))
        #for col in range(self.col):
        #    for row in range(self.row):
        #        pygame.draw.circle(screen, self.color[self.grid[row][col]], (wo+col*self.square_size, ho+row*self.square_size), self.circle_size)
        pygame.draw.circle(screen, self.color[self.grid[row][col]],(wo + col * self.square_size, ho + row * self.square_size), self.circle_size)
        self.update = False

    def check_game_over(self, loc):
        self.win_set = []
        for func in [self.horiz_check, self.vert_check, self.diag1_check, self.diag2_check]:
            self.win_set = []
            if func(loc[0], loc[1]) >= 4:
                pygame.display.set_caption("Game Over")
                self.game_over = True
                return
        for x in self.grid:
            for y in x:
                if y == 0:
                    return
        self.game_over = True

    def horiz_check(self, row, col, coord=(0,0)):
        if col < 0 or col >= self.col:
            return 0
        if self.grid[row][col] == self.player:
            self.win_set.append((row,col))
            if coord == (0, 0):
                return 1 + self.horiz_check(row, col + 1, (0, 1)) + self.horiz_check(row, col - 1, (0, -1))
            elif coord == (0, 1):
                return 1 + self.horiz_check(row, col + 1, (0, 1))
            elif coord == (0, -1):
                return 1 + self.horiz_check(row, col - 1, (0, -1))
        return 0

    def vert_check(self, row, col, coord=(0,0)):
        if row < 0 or row >= self.row:
            return 0
        if self.grid[row][col] == self.player:
            self.win_set.append((row,col))
            if coord == (0, 0):
                return 1 + self.vert_check(row + 1, col, (1, 0)) + self.vert_check(row - 1, col, (-1, 0))
            elif coord == (1, 0):
                return 1 + self.vert_check(row + 1, col, (1, 0))
            elif coord == (-1, 0):
                return 1 + self.vert_check(row - 1, col, (-1, 0))
        return 0

    def diag1_check(self, row, col, coord=(0,0)):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return 0
        if self.grid[row][col] == self.player:
            self.win_set.append((row,col))
            if coord == (0, 0):
                return 1 + self.diag1_check(row + 1, col + 1, (1, 1)) + self.diag1_check(row - 1, col - 1, (-1, -1))
            elif coord == (1, 1):
                return 1 + self.diag1_check(row + 1, col + 1, (1, 1))
            elif coord == (-1, -1):
                return 1 + self.diag1_check(row - 1, col - 1, (-1, -1))
        return 0

    def diag2_check(self, row, col, coord=(0,0)):
        if row < 0 or row >= self.row or col < 0 or col >= self.col:
            return 0
        if self.grid[row][col] == self.player:
            self.win_set.append((row,col))
            if coord == (0, 0):
                return 1 + self.diag2_check(row + 1, col - 1, (1, -1)) + self.diag2_check(row - 1, col + 1, (-1, 1))
            elif coord == (1, -1):
                return 1 + self.diag2_check(row + 1, col - 1, (1, -1))
            elif coord == (-1, 1):
                return 1 + self.diag2_check(row - 1, col + 1, (-1, 1))
        return 0

    def get_possible_moves(self):
        return [i for i, col in enumerate(self.grid[0]) if col is 0]

    def make_move(self, col, color):
        for r in reversed(range(self.row)):
            if self.grid[r][col] == 0:
                self.grid[r][col] = color

    def reset(self, screen):
        self.grid = [[0] * self.col for _ in range(self.row)]
        self.player = random.choice([1, 2])
        self.opp = 3 - self.player
        self.initialize_board(screen)
        self.game_over = False
