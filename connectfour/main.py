import pygame
import keypress as kp
from Board import *
import GameLogic as gl

GRAY = (0,0,0)


def run_game():
    pygame.init()
    board = Board()
    screen_height = 600
    screen_width = board.square_size * board.col + (board.square_size // 2)
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Connect Four")

    #screen.fill((20,20,235))
    board.initialize_board(screen)
    #font = pygame.font.Font(None, 50)

    while True:
        #board.draw_board(screen)
        gl.running_game(screen, board)
        kp.mouse_click(screen, board)
        #screen.blit(font.render("QUIT", True, GRAY), (screen_width / 2 + 50, screen_height / 2))
        pygame.display.flip()


if __name__ == '__main__':
    run_game()


