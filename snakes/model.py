# model.py

import pygame
import random


def draw_grid(screen, settings):

    for col in range(settings.columns):
        pygame.draw.line(screen, (40,40,40), (col * settings.block_size - 1, 0),(col * settings.block_size - 1, settings.game_height), 1)

    for row in range(settings.rows):
        pygame.draw.line(screen, (40,40,40), (0, row*settings.block_size-1), (settings.game_width, row*settings.block_size-1), 1)

    pygame.draw.rect(screen, (35,45,120), (0,0, settings.block_size, settings.game_height))
    pygame.draw.rect(screen, (35,45,120), (0,0, settings.game_width, settings.block_size))
    pygame.draw.rect(screen, (35,45,120), (settings.game_width-settings.block_size, 0, settings.block_size, settings.game_height))
    pygame.draw.rect(screen, (35,45,120), (0, settings.game_height-settings.block_size, settings.game_width, settings.block_size))


def food_tester(screen, settings):
    pygame.draw.rect(screen, (255,0,0), (settings.food[0]*settings.block_size+settings.block_size/5, settings.food[1]*settings.block_size+settings.block_size/5, 3*settings.block_size/5, 3*settings.block_size/5))


def new_food(screen, settings):
    settings.food = (random.randint(1,settings.columns-2), random.randint(1,settings.rows-2))
    pygame.draw.rect(screen, (255,0,0), (settings.food[0]*settings.block_size+settings.block_size*9/40, settings.food[1]*settings.block_size+settings.block_size*9/40, settings.block_size*11/20, settings.block_size*11/20))


def update(screen, settings):
    move = False
    if settings.count and settings.direction is not None:
        settings.clock.tick()
        settings.count = False
    settings.timer += settings.clock.tick()
    if settings.timer > 40:# and settings.direction is not None:
        if settings.direction is not None:
            settings.timer = 0
            settings.count = True
            move = True
        if len(settings.direction_queue) > 0:
            settings.direction = settings.direction_queue[0]
            settings.direction_queue = settings.direction_queue[1:]

    """ fix possible input lag when changing directions// delay """
    if settings.direction == "R" and move:
        settings.head[0] += 1
        settings.snake.insert(0, tuple(settings.head))
        settings.tail = settings.snake.pop()

    elif settings.direction == "D" and move:
        settings.head[1] += 1
        settings.snake.insert(0, tuple(settings.head))
        settings.tail = settings.snake.pop()

    elif settings.direction == "L" and move:
        settings.head[0] -= 1
        settings.snake.insert(0, tuple(settings.head))
        settings.tail = settings.snake.pop()

    elif settings.direction == "U" and move:
        settings.head[1] -= 1
        settings.snake.insert(0, tuple(settings.head))
        settings.tail = settings.snake.pop()

    if settings.direction is not None:
        food_check(screen, settings)

    if settings.tail is not None:
        pygame.draw.rect(screen, settings.bg_color, (settings.tail[0]*settings.block_size, settings.tail[1]*settings.block_size, settings.block_size-1, settings.block_size-1))

    for x,y in settings.snake:
        pygame.draw.rect(screen, (0, 128, 0), (x * settings.block_size, y * settings.block_size, settings.block_size - 1, settings.block_size - 1))
    pygame.draw.rect(screen, (0, 160, 0), (settings.head[0]*settings.block_size, settings.head[1]*settings.block_size, settings.block_size-1, settings.block_size-1))


def collisions_check(screen, settings):
    if settings.head[0] < 1 or settings.head[1] < 1:
        game_over(screen, settings)
    elif settings.head[0] >= settings.columns-1 or settings.head[1] >= settings.rows-1:
        game_over(screen, settings)

    for each in settings.snake[1:]:
        if each == tuple(settings.head):
            game_over(screen, settings)


def food_check(screen, settings):
    if tuple(settings.head) == settings.food:
        """Bounds check for if food is on edge // so game doesn't immediately end"""
        """if settings.direction == "R":
            settings.head[0] += 1

        elif settings.direction == "L":
            settings.head[0] -= 1

        elif settings.direction == "D":
            settings.head[1] += 1

        elif settings.direction == "U":
            settings.head[1] -= 1

        settings.snake_length += 1
        settings.snake.insert(0, tuple(settings.head))
        pygame.draw.rect(screen, (0, 128, 0), (settings.head[0] * settings.block_size, settings.head[1] * settings.block_size, settings.block_size - 1, settings.block_size - 1))"""

        settings.snake_length += 1
        settings.snake.append(settings.tail)
        pygame.draw.rect(screen, (0,128,0), (settings.tail[0]*settings.block_size, settings.tail[1]*settings.block_size, settings.block_size-1, settings.block_size-1))

        new_food(screen, settings)


def game_over(screen, settings):
    settings.game_over = True
    pygame.draw.rect(screen, (128, 128, 128), (settings.head[0] * settings.block_size, settings.head[1] * settings.block_size, settings.block_size - 1,settings.block_size - 1))
    pygame.display.set_caption("Game Over. Length: "+str(settings.snake_length)+ " (Press <space> to play again.)")


