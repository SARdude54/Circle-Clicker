import pygame

from scripts.text import Text


class ImageButton:
    def __init__(self, x, y, image, scale):
        """
                Init button object
                :param x: int
                :param y: int
                :param image: str
                :param scale: int

        """
        self.width = image.get_width()
        self.height = image.get_height()
        self.x = x
        self.y = y
        self.scale = scale
        self.image = pygame.transform.scale(image, (int(self.width * self.scale), int(self.height * self.scale)))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
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

        surface.blit(self.image, (self.rect.x, self.rect.y))

        return action

    def update_image(self, screen):
        pass

    def delete(self, screen):
        rect: pygame.Rect = self.rect
        pygame.draw.rect(screen, (0, 0, 0), rect)

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


class TextButton:
    def __init__(self, x, y, scale, text, font_file: str, font_size: int, text_color: tuple, background_text_color=None):
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

    def update(self, selected_color, deselected_color):

        if self.is_selected():
            self.text.set_color(deselected_color)
            self.selected = False
        else:
            self.text.set_color(selected_color)
            self.selected = True

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
