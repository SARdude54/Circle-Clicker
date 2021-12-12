import pygame


class Text:
    def __init__(self, text, font_file: str, font_size: int, center_cords, text_color: tuple, background_text_color=None):
        self.font_file = font_file
        self.font_size = font_size
        self.text_color = text_color
        self.background_text_color = background_text_color
        self.center_cords = center_cords
        self.font = pygame.font.Font(font_file, font_size)
        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = center_cords

    def get_text_rect(self):
        return self.text_rect

    def get_text(self):
        return self.text
