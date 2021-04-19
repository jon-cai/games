# settings.py

import pygame


class Settings:
    def __init__(self):

        self.rows = 22
        self.columns = 32

        self.block_size = 20

        self.game_width = self.columns * self.block_size
        self.game_height = self.rows * self.block_size

        self.bg_color = (10, 10, 10)

        self.snake_length = 4
        self.direction = None
        self.direction_queue = ""

        self.snake = []
        self.head = [self.columns//4, self.rows//2]
        self.food = None
        self.tail = None

        for num in range(self.snake_length):
            self.snake.append((self.columns//4 - num, self.rows //2))

        self.clock = pygame.time.Clock()
        self.timer = 0
        self.count = True

        self.game_over = False
        self.play_again = False

