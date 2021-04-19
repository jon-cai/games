import pygame
import random
import time


def update_board(screen, board, pos):
    if pos is not None and not board.game_over:
        x_pos = [87.5, 157.5, 227.5, 297.5, 367.5, 437.5, 600]
        board.mouse_x = -1
        board.mouse_y = -1
        for y, coord in enumerate(x_pos):
            if pos[0] <= coord:
                for x in reversed(range(board.row)):
                    if board.grid[x][y] == 0:
                        board.grid[x][y] = board.player
                        #drop_piece(screen,board, x, y)
                        board.check_game_over((x, y))
                        board.player = 3 - board.player
                        #if board.player == board.opp and not board.game_over:
                        #    run_ai(screen, board)
                        board.draw_piece(screen, x, y)
                        return
                return
    elif board.game_over:
        pygame.display.set_caption("Connect Four")
        board.reset(screen)


def running_game(screen, board):
    color = board.color[board.player]
    x, y = pygame.mouse.get_pos()
    if board.player == board.opp and not board.game_over:
        if not board.empty:
            pygame.draw.rect(screen, (52, 157, 234), (0, 0, int(board.square_size * board.col + (board.square_size / 2)), board.square_size * 9 / 10))
            board.empty = True
        run_ai(screen, board)
        return
    if not pygame.mouse.get_focused() or board.game_over:
        if not board.empty:
            pygame.draw.rect(screen, (52, 157, 234), (0, 0, int(board.square_size * board.col + (board.square_size / 2)), board.square_size * 9 / 10))
            board.empty = True
        return
    if x == board.mouse_x and y == board.mouse_y:
        return
    board.mouse_x = x
    board.mouse_y = y
    x_pos = [87.5, 157.5, 227.5, 297.5, 367.5, 437.5, 600]
    pygame.draw.rect(screen, (52, 157, 234), (0,0,int(board.square_size * board.col + (board.square_size / 2)), board.square_size * 9/10))
    for i, coord in enumerate(x_pos):
        if x < coord:
            pygame.draw.circle(screen, color, (board.square_size * (3 + 4*i)/4, board.square_size * 5/11), board.circle_size)
            board.empty = False
            break

'''def drop_piece(screen, board, row, col):
    for i, row in enumerate(board.grid):
        if 
        pygame.draw.circle(screen, self.color[self.grid[row][col]],(wo + col * self.square_size, ho + row * self.square_size), self.circle_size)
'''

def run_ai(screen, board):
    if board.delay == 0:
        board.delay = time.time()
    if time.time() < board.delay + 0.5:
        return
    pos = [87.5, 157.5, 227.5, 297.5, 367.5, 437.5, 600]
    board.update = True
    board.delay = 0
    print(board.get_possible_moves())
    update_board(screen, board, (pos[random.choice(board.get_possible_moves())],1))
