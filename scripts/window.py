import pygame


class Window:
    def __init__(self, window_size: tuple, screen_caption):
        self.window_size = window_size
        pygame.display.set_caption(screen_caption)
        self.screen = pygame.display.set_mode(self.window_size, 0, 32)

    def init_window(self, background: tuple):
        self.screen.fill(background)

    def get_screen(self):
        return self.screen
