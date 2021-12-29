import pygame
from pygame.locals import *
from scripts.text import Text


class TextBox:
    def __init__(self, x, y, width, height, bg, bg_hover):
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, self.width, self.height)
        self.rect.x = x
        self.rect.y = y
        self.bg = bg
        self.bg_hover = bg_hover
        self.selected = False

    def draw_box(self, screen: pygame.Surface, mx, my, bg):
        self.bg = bg
        pygame.draw.rect(screen, self.bg, self.rect)

        if self.rect.collidepoint(mx, my):
            pygame.draw.rect(screen, self.bg_hover, self.rect)

    def isSelected(self):
        return self.selected

    def get_rect(self):
        return self.rect
