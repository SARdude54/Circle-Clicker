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

    def delete(self, screen, screen_size):
        rect = pygame.Rect(self.text_rect.x, self.text_rect.y,  self.text_rect.width, self.text_rect.height )
        pygame.draw.rect(screen, (255, 0, 0), rect)

    def set_center_cords(self, center_cords):
        self.center_cords = center_cords
        self.text_rect.center = center_cords

    def set_font_size(self, text, font_size):
        self.font_size = font_size
        self.font = pygame.font.Font(self.font_file, self.font_size)
        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = self.text.get_rect()

    def get_text_rect(self):
        return self.text_rect

    def get_text(self):
        return self.text
