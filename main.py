import pygame
import sys
from circle import Circle

clock = pygame.time.Clock()

from pygame.locals import *

WINDOW_SIZE = (700, 500)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("Circle Clicker")

display = pygame.Surface((700, 500))

circle = Circle(screen, (255, 0, 0), 50)


def run_game_events(mx, my):
    global circle
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and circle.mouse_collide(mx, my):
            circle.delete()
            circle = Circle(screen, (255, 0, 0), 50)
            circle.draw_circle()


def main():
    global circle
    while True:
        screen.fill((0, 0, 0))

        mx, my = pygame.mouse.get_pos()

        circle.draw_circle()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == MOUSEBUTTONDOWN and circle.mouse_collide(mx, my):
                circle.delete()
                circle = Circle(screen, (255, 0, 0), 50)
                circle.draw_circle()

        # surf = pygame.transform.scale(display, WINDOW_SIZE)
        # screen.blit(surf, (0, 0))
        pygame.display.update()

        clock.tick(60)

if "__main__" == __name__:
    main()
