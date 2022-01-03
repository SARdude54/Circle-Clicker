import pygame

from scripts.circle import Circle
from scripts.game_timer import Timer
from scripts.window import Window
from scripts.text import Text
from scripts.buttons import TextButton

clock = pygame.time.Clock()
timer = Timer(clock)

WINDOW_SIZE = (700, 500)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (253, 236, 0)

pygame.init()

screen = Window(WINDOW_SIZE, "Circle Clicker").get_screen()

FONT = "assets/dpcomic.ttf"

title_text = Text(WINDOW_SIZE[0] // 2 - 326//2, 20, "Circle Clicker", FONT, 64, BLUE)

level = "EASY"

level_surf = pygame.Surface((WINDOW_SIZE[0], 50))
level_surf_rect = level_surf.get_rect()
level_surf_rect.y = 150

circle = Circle(screen, (255, 0, 0), None)

medium_btn = TextButton(screen.get_width() // 2 - 44, level_surf_rect.y, 1, "Medium", FONT, 32, BLUE)
easy_btn = TextButton(200, level_surf_rect.y, 0.85, "Easy", FONT, 32, BLUE)
hard_btn = TextButton(440, level_surf_rect.y, 0.94, "Hard", FONT, 32, BLUE)

start_btn = TextButton(screen.get_width() // 2 - 32, 250, 1, "Start", FONT, 32, BLUE)
activity_btn = TextButton(screen.get_width() // 2 - 45, 300, 1, "Activity", FONT, 32, BLUE)
exit_btn = TextButton(screen.get_width() // 2 - 22, 350, 1, "Exit", FONT, 32, BLUE)

menu_btn = TextButton(screen.get_width() // 2 - 59//2, 250, 1, "Menu", FONT, 32, BLUE)

selected_level_text = Text(100, 100, "Level: " + level.title(), FONT, 32, GREEN)

score = 0

timer.set_timer(0, 10)
