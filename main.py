import pygame, sys

clock = pygame.time.Clock()

from pygame.locals import *

pygame.init()

pygame.display.set_caption("Circle Clicker")

WINDOW_SIZE = (700, 500)

screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)


def run_game_events():
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()


def main():
    while True:
        screen.fill((0, 0, 0))

        run_game_events()
        pygame.display.update()
        clock.tick(60)


if "__main__" == __name__:
    main()
