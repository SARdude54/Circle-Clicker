import pygame


class Text:
    def __init__(self, x, y, text, font_file: str, font_size: int, text_color: tuple, background_text_color=None):
        self.x = x
        self.y = y
        self.font_file = font_file
        self.font_size = font_size
        self.text_color = text_color
        self.background_text_color = background_text_color
        self.font = pygame.font.Font(font_file, font_size)
        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.x = self.x
        self.text_rect.y = self.y

    def get_text_rect(self):
        return self.text_rect

    def get_text(self):
        return self.text
