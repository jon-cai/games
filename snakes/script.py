# script.py for Snake

import pygame
from settings import Settings
import keypress
import model


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.game_width, settings.game_height))
    pygame.display.set_caption("Snakes")

    screen.fill(settings.bg_color)
    model.draw_grid(screen, settings)
    model.new_food(screen, settings)

    while True:
        keypress.keycheck(screen, settings)

        if settings.game_over:
            model.game_over(screen, settings)
            if settings.play_again:
                break
        else:
            model.update(screen, settings)
            model.collisions_check(screen, settings)

        pygame.display.flip()

    return settings.play_again


if __name__ == "__main__":
    play_again = True
    while play_again:
        play_again = run_game()