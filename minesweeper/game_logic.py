# game_logic.py

import pygame
import sys
import random

RED = (220,20,60)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
LIGHT_GRAY = (211,211,211)
DARK_GRAY = (169,169,169)
CF_BLUE = (70,130,180)
GREEN = (0, 255, 0)
GOLD = (240,185,30) #(255,223,0)
BLACK = (0, 0, 0)
AN_WHITE = (255,222,173)

BOMB = pygame.image.load("images/bomb.png")
FLAG = pygame.image.load("images/flag.png")
ONE = pygame.image.load("images/one.png")
TWO = pygame.image.load("images/two.png")
THREE = pygame.image.load("images/three.png")
FOUR = pygame.image.load("images/four.png")
FIVE = pygame.image.load("images/five.png")
SIX = pygame.image.load("images/six.png")
SEVEN = pygame.image.load("images/seven.png")
EIGHT = pygame.image.load("images/eight.png")
LOGO = pygame.transform.rotozoom(pygame.image.load("images/minesweeper.png"), 0, 0.32)
RESTART = pygame.transform.rotozoom(pygame.image.load("images/restart.png"), 0, 0.4)
TRY_AGAIN = pygame.transform.rotozoom(pygame.image.load("images/try_again.png"), 0, 0.4)
PLAY = pygame.transform.rotozoom(pygame.image.load("images/play.png"), 0, 0.4)
WIN = pygame.transform.rotozoom(pygame.image.load("images/win.png"), 0, 0.25)


def create_grid(screen, settings):
    for row in range(settings.size):
        for col in range(settings.size):
            pygame.draw.rect(screen, CF_BLUE, (col * settings.square_size, row * settings.square_size, settings.square_size, settings.square_size))
            pygame.draw.line(screen, SILVER, (col * settings.square_size, 0), (col*settings.square_size, settings.screen_size), 2)
        pygame.draw.line(screen, SILVER, (0, row*settings.square_size), (settings.screen_size, row*settings.square_size), 2)
    pygame.draw.line(screen, SILVER, (settings.screen_size-2, 0), (settings.screen_size-2, settings.screen_size), 2)
    pygame.draw.line(screen, SILVER, (0, settings.screen_size), (settings.screen_size, settings.screen_size), 2)
    pygame.draw.line(screen, AN_WHITE, (0, settings.screen_size+2), (settings.screen_size, settings.screen_size+2), 3)

    scale_images(settings)
    rect = RESTART.get_rect()
    rect.right = settings.screen_size - settings.square_size/4.4
    rect.bottom = settings.screen_size+settings.screen_bot-1
    screen.blit(RESTART, rect)
    logo_rect = LOGO.get_rect()
    logo_rect.left = settings.square_size/7
    logo_rect.bottom = settings.screen_size+settings.screen_bot-1
    screen.blit(LOGO, logo_rect)


def scale_images(settings):
    global BOMB, FLAG, ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT
    BOMB = pygame.transform.scale(BOMB, (settings.screen_size // settings.size - 1, settings.screen_size // settings.size - 1))
    FLAG = pygame.transform.scale(FLAG, (settings.screen_size // (settings.size+3) -1, settings.screen_size // (settings.size+3) -1))
    ONE = pygame.transform.scale(ONE, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    TWO = pygame.transform.scale(TWO, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    THREE = pygame.transform.scale(THREE, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    FOUR = pygame.transform.scale(FOUR, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    FIVE = pygame.transform.scale(FIVE, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    SIX = pygame.transform.scale(SIX, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    SEVEN = pygame.transform.scale(SEVEN, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))
    EIGHT = pygame.transform.scale(EIGHT, (settings.screen_size // (settings.size+3) -2, settings.screen_size // (settings.size+3) -2))


def create_bombs(settings):
    count = 0
    while count < settings.bombs:
        x = random.randint(0, settings.size-1)
        y = random.randint(0, settings.size-1)
        if settings.solution_list[x][y] != "B":
            count += 1
            settings.solution_list[x][y] = "B"
            if x > 0:
                if not settings.solution_list[x - 1][y] == 'B':  # left middle
                    settings.solution_list[x - 1][y] += 1

                if y > 0 and not settings.solution_list[x - 1][y - 1] == 'B':  # top left
                    settings.solution_list[x - 1][y - 1] += 1

                if y < settings.size - 1 and not settings.solution_list[x - 1][y + 1] == 'B':  # top right
                    settings.solution_list[x - 1][y + 1] += 1

            if x < settings.size - 1:
                if not settings.solution_list[x + 1][y] == 'B':  # bottom middle
                    settings.solution_list[x + 1][y] += 1

                if y < settings.size - 1 and not settings.solution_list[x + 1][y + 1] == 'B':  # bottom right
                    settings.solution_list[x + 1][y + 1] += 1

                if y > 0 and not settings.solution_list[x + 1][y - 1] == 'B':  # bottom left
                    settings.solution_list[x + 1][y - 1] += 1

            if y > 0 and not settings.solution_list[x][y - 1] == 'B':  # left middle
                settings.solution_list[x][y - 1] += 1

            if y < settings.size - 1 and not settings.solution_list[x][y + 1] == 'B':  # right middle
                settings.solution_list[x][y + 1] += 1


def game_over(screen, settings):
    for row in range(settings.size):
        for col in range(settings.size):
            if settings.solution_list[row][col] == "B" and settings.text_list[row][col] != "F":
                pygame.draw.rect(screen, RED, (col * settings.square_size +2, row * settings.square_size +2, settings.square_size-2, settings.square_size-2))
                rect = BOMB.get_rect()
                rect = rect.move((col * settings.square_size + 4, row * settings.square_size+2))
                screen.blit(BOMB, rect)
    pygame.display.set_caption("Game Over!")
    pygame.draw.line(screen, RED, (0, settings.screen_size + settings.screen_bot-2), (settings.screen_size, settings.screen_size + settings.screen_bot-2), 3)
    rect = TRY_AGAIN.get_rect()
    rect.center = (settings.screen_size//2 + settings.square_size +2, settings.screen_size + (settings.screen_bot/2))
    screen.blit(TRY_AGAIN, rect)
    settings.game_over = True


def zero_reveal(screen, settings, row, col):
    if row > 0:
        if settings.text_list[row - 1][col] == '-':
            settings.text_list[row - 1][col] = settings.solution_list[row - 1][col]  # top middle
            update_square(screen, settings, row-1, col)
            if str(settings.text_list[row - 1][col]) == "0":
                zero_reveal(screen, settings, row - 1, col)  # if square is zero, calls on method again
        if col > 0:
            if settings.text_list[row - 1][col - 1] == '-':
                settings.text_list[row - 1][col - 1] = settings.solution_list[row - 1][col - 1]  # top left
                update_square(screen, settings, row-1, col-1)
                if str(settings.text_list[row - 1][col - 1]) == '0':
                    zero_reveal(screen, settings, row - 1, col - 1)  # if square is zero, calls on method again
        if col < settings.size - 1:
            if settings.text_list[row - 1][col + 1] == '-':
                settings.text_list[row - 1][col + 1] = settings.solution_list[row - 1][col + 1]  # top right
                update_square(screen, settings, row-1, col+1)
                if str(settings.text_list[row - 1][col + 1]) == '0':
                    zero_reveal(screen, settings, row - 1, col + 1)
    if row < settings.size - 1:
        if settings.text_list[row + 1][col] == '-':
            settings.text_list[row + 1][col] = settings.solution_list[row + 1][col]  # bottom middle
            update_square(screen, settings, row+1, col)
            if str(settings.text_list[row + 1][col]) == '0':
                zero_reveal(screen, settings, row + 1, col)
        if col > 0:
            if settings.text_list[row + 1][col - 1] == '-':
                settings.text_list[row + 1][col - 1] = settings.solution_list[row + 1][col - 1]  # bottom left
                update_square(screen, settings, row+1, col-1)
                if str(settings.text_list[row + 1][col - 1]) == '0':
                    zero_reveal(screen, settings, row + 1, col - 1)
        if col < settings.size - 1:
            if settings.text_list[row + 1][col + 1] == '-':
                settings.text_list[row + 1][col + 1] = settings.solution_list[row + 1][col + 1]  # bottom right
                update_square(screen, settings, row+1, col+1)
                if str(settings.text_list[row + 1][col + 1]) == '0':
                    zero_reveal(screen, settings, row + 1, col + 1)
    if col > 0:
        if settings.text_list[row][col - 1] == '-':
            settings.text_list[row][col - 1] = settings.solution_list[row][col - 1]  # left middle
            update_square(screen, settings, row, col-1)
            if str(settings.text_list[row][col - 1]) == '0':
                zero_reveal(screen, settings, row, col - 1)
    if col < settings.size - 1:
        if settings.text_list[row][col + 1] == '-':
            settings.text_list[row][col + 1] = settings.solution_list[row][col + 1]  # right middle
            update_square(screen, settings, row, col+1)
            if str(settings.text_list[row][col + 1]) == '0':
                zero_reveal(screen, settings, row, col + 1)
    update_square(screen, settings, row, col)


def check_events(screen, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.MOUSEBUTTONDOWN:
            left, mid, right = pygame.mouse.get_pressed()
            pos = pygame.mouse.get_pos()
            col = int(pos[0] // settings.square_size)
            row = int(pos[1] // settings.square_size)
            if left:
                if row >= settings.size:
                    menu_bar(screen, settings, pos[0])
                else:
                    select(screen, settings, row, col)
            elif right and not settings.game_over:
                flag(screen, settings, row, col)


def select(screen, settings, row, col):
    if settings.select_first:
        settings.start_time = pygame.time.get_ticks()
        settings.select_first = False
        selectFirst(settings, row, col)

    if settings.text_list[row][col] != "F" and not settings.game_over:
        settings.text_list[row][col] = settings.solution_list[row][col]
        update_square(screen, settings, row, col)
        if (type(settings.solution_list[row][col]) == int) and settings.solution_list[row][col] == 0:
            zero_reveal(screen, settings, row, col)
        if settings.solution_list[row][col] == "B":
            game_over(screen, settings)


def flag(screen, settings, row, col):
    if settings.text_list[row][col] == "-":
        settings.text_list[row][col] = "F"
        pygame.draw.rect(screen, GOLD, (col * settings.square_size+2, row * settings.square_size+2, settings.square_size-2, settings.square_size-2))
        rect = FLAG.get_rect()
        rect.center = (col*settings.square_size + (settings.square_size//2), row*settings.square_size + (settings.square_size//2)+1)
        screen.blit(FLAG, rect)

    elif settings.text_list[row][col] == "F":
        settings.text_list[row][col] = "-"
        pygame.draw.rect(screen, CF_BLUE, (col * settings.square_size+2, row * settings.square_size+2, settings.square_size-2, settings.square_size-2))


def update_square(screen, settings, row, col):
    if settings.text_list[row][col] == 0:
        pygame.draw.rect(screen, LIGHT_GRAY, (col * settings.square_size+2, row * settings.square_size+2, settings.square_size-2, settings.square_size-2))

    elif settings.text_list[row][col] == 1:
        pygame.draw.rect(screen, LIGHT_GRAY, (col * settings.square_size + 2, row * settings.square_size + 2, settings.square_size - 2, settings.square_size - 2))
        rect = ONE.get_rect()
        rect.center = (col*settings.square_size + (settings.square_size//2), row*settings.square_size + (settings.square_size//2))
        screen.blit(ONE, rect)

    elif settings.text_list[row][col] == 2:
        pygame.draw.rect(screen, LIGHT_GRAY, (col * settings.square_size + 2, row * settings.square_size + 2, settings.square_size - 2, settings.square_size - 2))
        rect = TWO.get_rect()
        rect.center = (col*settings.square_size + (settings.square_size//2), row*settings.square_size + (settings.square_size//2))
        screen.blit(TWO, rect)

    elif settings.text_list[row][col] == 3:
        pygame.draw.rect(screen, LIGHT_GRAY, (col * settings.square_size + 2, row * settings.square_size + 2, settings.square_size - 2, settings.square_size - 2))
        rect = THREE.get_rect()
        rect.center = (col * settings.square_size + (settings.square_size // 2), row * settings.square_size + (settings.square_size // 2))
        screen.blit(THREE, rect)

    elif settings.text_list[row][col] == 4:
        pygame.draw.rect(screen, LIGHT_GRAY, (col * settings.square_size + 2, row * settings.square_size + 2, settings.square_size - 2, settings.square_size - 2))
        rect = FOUR.get_rect()
        rect.center = (col * settings.square_size + (settings.square_size // 2)-1, row * settings.square_size + (settings.square_size // 2))
        screen.blit(FOUR, rect)
    elif settings.text_list[row][col] == 5:
        pygame.draw.rect(screen, LIGHT_GRAY, (col * settings.square_size + 2, row * settings.square_size + 2, settings.square_size - 2, settings.square_size - 2))
        rect = FIVE.get_rect()
        rect.center = (col * settings.square_size + (settings.square_size // 2), row * settings.square_size + (settings.square_size // 2))
        screen.blit(FIVE, rect)


def selectFirst(settings, row, col):
    if settings.solution_list[row][col] == "B":
        settings.solution_list[row][col] = 0
        # Increments selected square for every adjacent bomb.
        if row > 0:
            if settings.solution_list[row - 1][col] == 'B':  # top middle
                settings.solution_list[row][col] += 1
            else:  # Decrements every adjacent square (since bomb is gone)
                settings.solution_list[row -1][col] -= 1

            if col > 0:
                if settings.solution_list[row - 1][col - 1] == 'B':  # top left
                    settings.solution_list[row][col] += 1
                else:  # Decrements adjacent square
                    settings.solution_list[row - 1][col - 1] -= 1

            if col < settings.size - 1:
                if settings.solution_list[row - 1][col + 1] == 'B':  # top right
                    settings.solution_list[row][col] += 1
                else:  # Decrements adjacent square
                    settings.solution_list[row - 1][col + 1] -= 1

        if row < settings.size - 1:
            if settings.solution_list[row + 1][col] == 'B':  # bottom middle
                settings.solution_list[row][col] += 1
            else:  # Decrements adjacent square
                settings.solution_list[row + 1][col] -= 1

            if col < settings.size - 1:
                if settings.solution_list[row + 1][col + 1] == 'B':  # bottom right
                    settings.solution_list[row][col] += 1
                else:
                    settings.solution_list[row + 1][col + 1] -= 1

            if col > 0:
                if settings.solution_list[row + 1][col - 1] == 'B':  # bottom left
                    settings.solution_list[row][col] += 1
                else:
                    settings.solution_list[row + 1][col - 1] -= 1

        if col > 0:
            if settings.solution_list[row][col - 1] == 'B':  # left middle
                settings.solution_list[row][col] += 1
            else:
                settings.solution_list[row][col - 1] -= 1

        if col < settings.size - 1:
            if settings.solution_list[row][col + 1] == 'B':  # right middle
                settings.solution_list[row][col] += 1
            else:
                settings.solution_list[row][col + 1] -= 1

        # Creates new location for bomb
        newLocation = False
        while not newLocation:
            x = random.randint(0, settings.size-1)
            y = random.randint(0, settings.size-1)
            # Checks if already has bomb at location.
            if not settings.solution_list[x][y] == 'B':
                settings.solution_list[x][y] = 'B'
                newLocation = True
                # Increments adjacent squares
                if x > 0:
                    if not settings.solution_list[x-1][y] == 'B':
                        settings.solution_list[x-1][y] += 1
                    if y>0 and not settings.solution_list[x-1][y-1] == 'B':
                        settings.solution_list[x-1][y-1] += 1
                    if y<settings.size-1 and not settings.solution_list[x-1][y+1] == 'B':
                        settings.solution_list[x-1][y+1] += 1
                if x < settings.size - 1:
                    if not settings.solution_list[x+1][y] == 'B':
                        settings.solution_list[x+1][y] += 1
                    if y>0 and not settings.solution_list[x+1][y-1] == 'B':
                        settings.solution_list[x+1][y-1] += 1
                    if y<settings.size-1 and not settings.solution_list[x+1][y+1] == 'B':
                        settings.solution_list[x+1][y+1] += 1
                if y>0 and not settings.solution_list[x][y-1] == 'B':
                    settings.solution_list[x][y-1] += 1
                if y<settings.size-1 and not settings.solution_list[x][y+1] == 'B':
                    settings.solution_list[x][y+1] += 1


def menu_bar(screen, settings, x):
    if settings.game_over:
        try_rect = TRY_AGAIN.get_rect()
        try_rect.center = (settings.screen_size // 2 + settings.square_size, settings.screen_size + (settings.screen_bot / 2))

        if try_rect.left <= x <= try_rect.right:
            settings.play_again = True
    elif settings.game_won:
        play_rect = PLAY.get_rect()
        play_rect.center = (settings.screen_size // 2 + settings.square_size, settings.screen_size + (settings.screen_bot / 2))
        if play_rect.left <= x <= play_rect.right:
            settings.play_again = True

    reset_rect = RESTART.get_rect()
    reset_rect.right = settings.screen_size - settings.square_size / 4.4
    reset_rect.bottom = settings.screen_size + settings.screen_bot - 1
    if x > reset_rect.left:
        settings.game_over = True
        settings.play_again = True


def check_status(screen, settings):
    progressCheck = False
    for x in range(settings.size):
        for y in range(settings.size):
            # Checks if there are any squares not chosen
            if settings.text_list[x][y] == '-' or settings.text_list[x][y] == 'F':
                if not settings.solution_list[x][y] == 'B':  # Checks if square is bomb
                    progressCheck = True  # If square is not bomb, game is still in progress

    if not progressCheck:
        game_won(screen, settings)


def game_won(screen, settings):
    for row in range(settings.size):
        for col in range(settings.size):
            if settings.solution_list[row][col] == "B" and settings.text_list[row][col] != "F":
                flag(screen, settings, row, col)
    pygame.display.set_caption("Game Won!")

    rect = PLAY.get_rect()
    rect.center = (settings.screen_size//2 + settings.square_size*1.5, settings.screen_size + (settings.screen_bot/2))
    screen.blit(PLAY, rect)
    win = WIN.get_rect()
    win.center = (settings.screen_size//2, settings.screen_size//2)
    screen.blit(WIN, win)
    settings.game_won = True
