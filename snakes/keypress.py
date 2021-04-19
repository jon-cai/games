# keypress.py

import pygame
import sys


def keycheck(screen, settings):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            keydown(event, screen, settings)


def keydown(event, screen, settings):
    if event.key == pygame.K_DOWN and (settings.snake[0][0] != settings.snake[1][0] or settings.direction is None):
        #settings.direction = "D"
        settings.direction_queue += "D"
        print("D", end="")

    elif event.key == pygame.K_UP and (settings.snake[0][0] != settings.snake[1][0] or settings.direction is None):
        #settings.direction = "U"
        settings.direction_queue += "U"
        print("U", end="")

    elif event.key == pygame.K_LEFT and settings.snake[0][1] != settings.snake[1][1]:
        #settings.direction = "L"
        settings.direction_queue += "L"
        print("L", end="")

    elif event.key == pygame.K_RIGHT and (settings.snake[0][1] != settings.snake[1][1] or settings.direction is None):
        #settings.direction = "R"
        settings.direction_queue += "R"
        print("R", end="")

    elif event.key == pygame.K_q:
        sys.exit(0)

    elif event.key == pygame.K_d:
        """debug"""
        print("Snake Length: ", settings.snake_length)
        print("Snake Coord: ", settings.snake)
        print("Snake Head: ", settings.head)
        print("Food Location: ", settings.food)
        print("Queue: ", settings.master_queue)
        print()

    elif event.key == pygame.K_SPACE and settings.game_over:
        settings.play_again = True