import pygame
import sys

from scripts.circle import Circle
from scripts.game_timer import Timer
from scripts.window import Window
from scripts.text import Text
from scripts.button import Button
from scripts.text_box import TextBox

clock = pygame.time.Clock()
timer = Timer(clock)

from pygame.locals import *


def center(window: pygame.Surface, surface: pygame.Surface):
    return window.get_width() // 2 - surface.get_width() // 2


WINDOW_SIZE = (700, 500)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (143, 143, 143)
pygame.init()

screen = Window(WINDOW_SIZE, "Circle Clicker").get_screen()

title_text = Text(100, 20, "Circle Clicker", "assets/arcade_font.TTF", 32, BLUE)

font = pygame.font.Font("assets/arcade_font.TTF", 32)

circle = Circle(screen, (255, 0, 0), 50)

start_img = pygame.image.load("assets/start.png")
exit_img = pygame.image.load("assets/exit.png")
settings_img = pygame.image.load("assets/settings.png")
apply_img = pygame.image.load("assets/apply.png")
cancel_img = pygame.image.load("assets/cancel.png")

start_btn = Button(center(screen, start_img), 200, start_img, 1)
exit_btn = Button(center(screen, exit_img), 350, exit_img, 1)
settings_btn = Button(center(screen, settings_img), 275, settings_img, 1)
apply_btn = Button(center(screen, apply_img), 220, apply_img, 1)
cancel_btn = Button(center(screen, cancel_img), 320, cancel_img, 1)

minute_text_box = TextBox(WINDOW_SIZE[0]//2 - 130, 150, 130, 40, GREY, WHITE)
seconds_text_box = TextBox(WINDOW_SIZE[0]//2 + 10, 150, 130, 40, GREY, WHITE)

minutes_text = Text(WINDOW_SIZE[0]//2 - 113, 100, "Minutes", "assets/arcade_font.TTF", 32, BLUE)
seconds_text = Text(WINDOW_SIZE[0]//2 + 17, 100, "Seconds", "assets/arcade_font.TTF", 32, BLUE)

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


def init_settings_menu():
    running = True
    while running:
        mx, my = pygame.mouse.get_pos()

        screen.fill(BLACK)

        minute_text_box.draw_box(screen, mx, my, GREY)
        seconds_text_box.draw_box(screen, mx, my, GREY)
        screen.blit(minutes_text.get_text(), minutes_text.get_text_rect())
        screen.blit(seconds_text.get_text(), seconds_text.get_text_rect())

        if minute_text_box.isSelected():
            minute_text_box.draw_box(screen, mx, my, WHITE)
        else:
            minute_text_box.draw_box(screen, mx, my, GREY)

        if seconds_text_box.isSelected():
            seconds_text_box.draw_box(screen, mx, my, WHITE)
        else:
            seconds_text_box.draw_box(screen, mx, my, GREY)

        if apply_btn.draw(screen):
            running = False

        if cancel_btn.draw(screen):
            running = False

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN and minute_text_box.get_rect().collidepoint(mx, my):
                minute_text_box.selected = True
                seconds_text_box.selected = False

            if event.type == MOUSEBUTTONDOWN and seconds_text_box.get_rect().collidepoint(mx, my):
                minute_text_box.selected = False
                seconds_text_box.selected = True

            if event.type == QUIT:
                pygame.quit()

        print(minute_text_box.isSelected())

        pygame.display.update()

        clock.tick(60)


start_game = False


def main():
    global circle, score, start_game
    running = True
    while running:

        screen.fill(BLACK)

        mx, my = pygame.mouse.get_pos()

        if not start_game:

            title_text.set_font_size("Circle Clicker", 64)
            title_text.set_cords(center(screen, title_text.get_text()), 50)
            screen.blit(title_text.get_text(), title_text.get_text_rect())

            if start_btn.draw(screen):
                start_game = True
            if settings_btn.draw(screen):
                init_settings_menu()
            if exit_btn.draw(screen):
                running = False

        else:

            timer.start()
            timer_text = Text(30, 20, timer.get_time(), "assets/arcade_font.TTF", 32, RED)

            score_text = Text(565, 20, f"Score: {score}", "assets/arcade_font.TTF", 32, BLUE)

            screen.fill(BLACK)
            screen.blit(score_text.get_text(), score_text.get_text_rect())
            screen.blit(timer_text.get_text(), timer_text.get_text_rect())

            circle.draw_circle()

            if timer.is_finished():
                circle.delete()
                screen.fill(BLACK)
                score_text.get_text_rect().center = ((WINDOW_SIZE[0] // 2), (WINDOW_SIZE[1] // 2))
                screen.blit(score_text.get_text(), score_text.get_text_rect())

        run_game_events(mx, my)

        pygame.display.update()

        clock.tick(60)


if "__main__" == __name__:
    main()
