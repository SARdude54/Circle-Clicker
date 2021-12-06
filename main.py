import pygame
import sys
from circle import Circle
from game_timer import Timer

clock = pygame.time.Clock()
timer = Timer(clock)

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

timer.set_timer(0, 10)


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
        if event.type == MOUSEBUTTONDOWN and circle.mouse_collide(mx, my) and not timer.is_finished():
            score += 1
            circle.delete()
            circle = Circle(screen, (255, 0, 0), 50)
            circle.draw_circle()


def main():
    global circle, score
    while True:
        timer.start()

        timer_text = font.render(timer.get_time(), True, (255, 0, 0))
        timer_text_rect = timer_text.get_rect()
        timer_text_rect.center = ((WINDOW_SIZE[0]/2) - (timer_text_rect.width/2), 50)

        score_text = font.render(f"Score: {score}", True, (0, 0, 255))
        score_text_rect = score_text.get_rect()
        score_text_rect.center = (600, 20)

        screen.fill((0, 0, 0))
        screen.blit(title, title_rect)
        screen.blit(score_text, score_text_rect)
        screen.blit(timer_text, timer_text_rect)

        mx, my = pygame.mouse.get_pos()

        circle.draw_circle()

        if timer.is_finished():
            circle.delete()
            screen.fill((0, 0, 0))
            score_text_rect.center = ((WINDOW_SIZE[0]/2), (WINDOW_SIZE[1]/2))
            screen.blit(score_text, score_text_rect)

        run_game_events(mx, my)

        pygame.display.update()

        clock.tick(60)


if "__main__" == __name__:
    main()
