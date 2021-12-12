import pygame
import sys
from circle import Circle
from game_timer import Timer
from window import Window
from text import Text

clock = pygame.time.Clock()
timer = Timer(clock)


from pygame.locals import *

WINDOW_SIZE = (700, 500)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

screen = Window(WINDOW_SIZE, "Circle Clicker").get_screen()

title_text = Text("Circle Clicker", "arcade_font.TTF", 32, (100, 20), BLUE)

font = pygame.font.Font("arcade_font.TTF", 32)

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
        timer_text = Text(timer.get_time(), "arcade_font.TTF", 32, (350, 20), RED, None)

        score_text = Text(f"Score: {score}", "arcade_font.TTF", 32, (600, 20), (0, 0, 255))

        screen.fill((0, 0, 0))
        screen.blit(title_text.get_text(), title_text.get_text_rect())
        screen.blit(score_text.get_text(), score_text.get_text_rect())
        screen.blit(timer_text.get_text(), timer_text.get_text_rect())

        mx, my = pygame.mouse.get_pos()

        circle.draw_circle()

        if timer.is_finished():
            circle.delete()
            screen.fill((0, 0, 0))
            score_text.get_text_rect().center = ((WINDOW_SIZE[0]/2), (WINDOW_SIZE[1]/2))
            screen.blit(score_text.get_text(), score_text.get_text_rect())

        run_game_events(mx, my)

        pygame.display.update()

        clock.tick(60)


if "__main__" == __name__:
    main()
