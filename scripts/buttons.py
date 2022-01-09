import pygame
from pygame.locals import *

from scripts.text import Text

BLACK = (0, 0, 0)


class TextButton:
    def __init__(self, x, y, scale, text, font_file: str, font_size: int, text_color: tuple, background_text_color=None):
        """
        Initialize button
        :param x: int
        :param y: int
        :param scale: int
        :param text: str
        :param font_file: str
        :param font_size: str
        :param text_color: tuple[int]
        :param background_text_color: tuple[int]
        """
        self.x = x
        self.y = y
        self.scale = scale
        self.text_color = text_color
        self.text = Text(self.x, self.y, text, font_file, font_size, text_color, background_text_color)
        self.rect = self.text.get_text_rect()
        self.clicked = False
        self.selected = False

    def draw(self, surface: pygame.Surface):
        """
        draws button on screen
        :param surface: pygame.Surface
        :return: bool
        """
        action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not self.clicked:
                action = True
                self.clicked = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        surface.blit(self.text.get_text(), self.rect)

        return action

    def delete(self, screen):
        """
        deletes the button by drawing a black rect on top
        :param screen: pygame.Surface
        :return: None
        """
        rect = Rect(self.x, self.y, self.rect.width, self.rect.height)
        pygame.draw.rect(screen, BLACK, rect)

    def update(self, selected_color, deselected_color):

        """
        Updates the color of the text button
        :param selected_color: tuple[int]
        :param deselected_color: tuple[int]
        :return: None
        """

        if self.is_selected():
            self.text.set_color(deselected_color)
            self.selected = False
        else:
            self.text.set_color(selected_color)
            self.selected = True

    def set_y(self, y):
        self.rect.y = self.y = y

    def is_selected(self):
        return self.selected

    def get_rect(self):
        return self.rect

    def get_bottom(self):
        return self.rect.bottom

    def get_right(self):
        return self.rect.right

    def get_left(self):
        return self.rect.left
