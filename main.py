import pygame
import sys
from circle import Circle

clock = pygame.time.Clock()

from pygame.locals import *

WINDOW_SIZE = (700, 500)

pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE, 0, 32)
pygame.display.set_caption("Circle Clicker")

font = pygame.font.Font("arcade_font.TTF", 32)

title = font.render("Circle Clicker", True, (0, 0, 255))
title_rect = title.get_rect()
title_rect.center = (100, 20)

display = pygame.Surface((700, 500))

circle = Circle(screen, (255, 0, 0), 50)

score = 0


def run_game_events(mx, my):
    """
    Loops through pygame events
    :param mx: int
    :param my: int
    :return: None
    """
    global circle, score
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN and circle.mouse_collide(mx, my):
            score += 1
            circle.delete()
            circle = Circle(screen, (255, 0, 0), 50)
            circle.draw_circle()


def main():
    global circle, score
    while True:
        score_text = font.render(f"Score: {score}", True, (0, 0, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (600, 20)

        screen.fill((0, 0, 0))
        screen.blit(title, title_rect)
        screen.blit(score_text, score_text_rect)

        mx, my = pygame.mouse.get_pos()

        circle.draw_circle()

        run_game_events(mx, my)

        pygame.display.update()

        clock.tick(60)


if "__main__" == __name__:
    main()
