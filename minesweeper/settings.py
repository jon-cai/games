# settings.py

import pygame


class Settings:
    def __init__(self):

        """Change these values based on game mode"""
        self.size = 9
        self.bombs = 10

        self.bg_color = (250,240,230)

        self.square_size = 40
        self.screen_size = self.size * self.square_size
        self.screen_bot = 55

        self.text_list = [["-" for x in range(self.size)] for y in range(self.size)]
        self.solution_list = [[0 for col in range(self.size)] for row in range(self.size)]

        self.select_first = True
        self.game_over = False
        self.play_again = False
        self.game_won = False


