import pygame


class Text:
    def __init__(self, x, y, text_str, font_file: str, font_size: int, text_color: tuple, background_text_color=None):

        """
        Init new text
        :param x: int
        :param y: int
        :param text_str: str
        :param font_file: str
        :param font_size: int
        :param text_color: tuple[int]
        :param background_text_color: tuple[int]
        """

        self.x = x
        self.y = y
        self.text_str = text_str

        self.font_file = font_file
        self.font_size = font_size
        self.text_color = text_color
        self.background_text_color = background_text_color
        self.font = pygame.font.Font(font_file, font_size)
        self.text = self.font.render(text_str, True, self.text_color)
        self.text_rect = self.text.get_rect()

        self.text_rect.x = self.x
        self.text_rect.y = self.y

    def draw(self, screen: pygame.Surface):
        screen.blit(self.get_text(), self.get_text_rect())

    def delete(self, screen: pygame.Surface):
        """
        Deletes text by drawing a black square over it
        :param screen: pygame.Surface
        :return: None
        """
        rect = pygame.Rect(self.text_rect.x, self.text_rect.y,  self.text_rect.width, self.text_rect.height)
        pygame.draw.rect(screen, (255, 0, 0), rect)

    def center_x(self, surface: pygame.Surface):
        self.text_rect.x = self.x = surface.get_width() // 2 - self.get_width() // 2

    def set_y(self, y):
        self.text_rect.y = self.y = y

    def set_text(self, text_str):
        self.text_str = text_str
        self.text = self.font.render(text_str, True, self.text_color)

    def set_cords(self, x, y):
        """
        Sets the coordinates of the text object
        :param x: int
        :param y: int
        :return: None
        """
        self.text_rect.x = x
        self.text_rect.y = y

    def set_font_size(self, text, font_size):
        """
        Sets the font size of text
        :param text: str
        :param font_size: int
        :return: None
        """
        self.font_size = font_size
        self.font = pygame.font.Font(self.font_file, self.font_size)
        self.text = self.font.render(text, True, self.text_color)
        self.text_rect = self.text.get_rect()

    def set_color(self, color, background_color=None):
        self.text_color = color
        self.background_text_color = background_color
        self.text = self.font.render(self.text_str, True, self.text_color)

    def get_text_rect(self):
        return self.text_rect

    def get_text(self):
        return self.text

    def get_width(self):
        return self.text.get_width()
