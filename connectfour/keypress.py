""" helper functions to check keypresses and mouse clicks"""

import pygame
import sys
import GameLogic as gl


def mouse_click(screen, board):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #left, mid, right = pygame.mouse.get_pressed()
            board.update = True
            pos = pygame.mouse.get_pos()
            if (board.player != board.opp and not board.game_over) or board.game_over:
                gl.update_board(screen, board, pos)
        #elif event.type == pygame.MOUSEBUTTONUP:
        #    pos = pygame.mouse.get_pos()
        #    print("up",pos)
