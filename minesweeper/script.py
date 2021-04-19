# Minesweeper script.py

import pygame
from settings import Settings
import game_logic as gl


clock = pygame.time.Clock()


def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_size, settings.screen_size + settings.screen_bot))
    pygame.display.set_caption("Minesweeper")

    screen.fill(settings.bg_color)
    gl.create_grid(screen, settings)
    gl.create_bombs(settings)

    # Prints solution to game
    """for row in range(settings.size):
        for col in range(settings.size):
            print(settings.solution_list[row][col], end='')
        print()"""

    while True:
        gl.check_events(screen, settings)

        pygame.display.flip()
        gl.check_status(screen, settings)

        if (settings.game_over or settings.game_won) and settings.play_again:
            break

        clock.tick(20)
    return settings.play_again


if __name__ == "__main__":
    play_again = True
    while play_again:
        play_again = run_game()