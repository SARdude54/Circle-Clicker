import pygame
import sys

from scripts.circle import Circle
from scripts.game_timer import Timer
from scripts.window import Window
from scripts.text import Text
from scripts.button import Button

clock = pygame.time.Clock()
timer = Timer(clock)

from pygame.locals import *

WINDOW_SIZE = (700, 500)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

screen = Window(WINDOW_SIZE, "Circle Clicker").get_screen()

title_text = Text(WINDOW_SIZE[0]//2 - 180, 20, "Circle Clicker", "assets/arcade_font.TTF", 64, BLUE)

circle = Circle(screen, (255, 0, 0), 50)

start_img = pygame.image.load("assets/start.png")
exit_img = pygame.image.load("assets/exit.png")

start_btn = Button(WINDOW_SIZE[0] / 2 - 65, WINDOW_SIZE[1] / 2 - 80, start_img, 1)
exit_btn = Button(WINDOW_SIZE[0] / 2 - 50, WINDOW_SIZE[1] / 2 - 30, exit_img, 1)

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


start_game = False


def main():
    global circle, score, start_game
    run = True
    while run:

        mx, my = pygame.mouse.get_pos()

        if not start_game:
            screen.blit(title_text.get_text(), title_text.get_text_rect())
            if start_btn.draw(screen):
                start_game = True

            if exit_btn.draw(screen):
                run = False

        else:
            timer.start()
            timer_text = Text(30, 20, timer.get_time(), "assets/arcade_font.TTF", 32, RED, None)

            score_text = Text(550, 20, f"Score: {score}", "assets/arcade_font.TTF", 32, (0, 0, 255))

            screen.fill((0, 0, 0))
            screen.blit(score_text.get_text(), score_text.get_text_rect())
            screen.blit(timer_text.get_text(), timer_text.get_text_rect())

            circle.draw_circle()

            if timer.is_finished():
                circle.delete()
                screen.fill((0, 0, 0))
                score_text.get_text_rect().center = ((WINDOW_SIZE[0] // 2), (WINDOW_SIZE[1] / 2))
                screen.blit(score_text.get_text(), score_text.get_text_rect())

        run_game_events(mx, my)

        pygame.display.update()

        clock.tick(60)


if "__main__" == __name__:
    main()
