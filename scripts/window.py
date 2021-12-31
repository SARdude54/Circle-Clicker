import pygame


class Window:
    def __init__(self, window_size: tuple, screen_caption):
        """
        Inits a window object
        :param window_size: tuple[int]
        :param screen_caption: str
        """
        self.window_size = window_size
        pygame.display.set_caption(screen_caption)
        self.screen = pygame.display.set_mode(self.window_size, 0, 32)

    def get_screen(self):
        return self.screen
