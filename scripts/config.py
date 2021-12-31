import pygame

from scripts.circle import Circle
from scripts.game_timer import Timer
from scripts.window import Window
from scripts.text import Text
from scripts.buttons import Button, MenuButton

clock = pygame.time.Clock()
timer = Timer(clock)

WINDOW_SIZE = (700, 500)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

screen = Window(WINDOW_SIZE, "Circle Clicker").get_screen()

title_text = Text(WINDOW_SIZE[0] // 2 - 180, 20, "Circle Clicker", "assets/arcade_font.TTF", 64, BLUE)

level_surf = pygame.Surface((WINDOW_SIZE[0], 50))
level_surf_rect = level_surf.get_rect()
level_surf_rect.y = 150

circle = Circle(screen, (255, 0, 0), 50)

easy_img = pygame.image.load("assets/easy.PNG")
medium_img = pygame.image.load("assets/medium.PNG")
hard_img = pygame.image.load("assets/hard.PNG")

start_img = pygame.image.load("assets/start.png")
activity_img = pygame.image.load("assets/activity.png")
exit_img = pygame.image.load("assets/exit.png")

medium_btn = Button(MenuButton.center(screen, medium_img), level_surf_rect.y, medium_img, 1)
easy_btn = Button(MenuButton.dist_to_right_of(medium_btn, 10) - easy_img.get_width(), level_surf_rect.y, easy_img, 0.85)
hard_btn = Button(MenuButton.dist_to_left_of(medium_btn, 10), level_surf_rect.y, hard_img, 0.94)

start_btn = MenuButton(MenuButton.center(screen, start_img), MenuButton.dist_to_btm_of(medium_btn, 100), start_img, 1)
activity_btn = MenuButton(MenuButton.center(screen, activity_img), MenuButton.dist_to_btm_of(start_btn, 5), activity_img, 1)
exit_btn = MenuButton(MenuButton.center(screen, exit_img), MenuButton.dist_to_btm_of(activity_btn, 5), exit_img, 1)

score = 0

timer.set_timer(0, 10)
