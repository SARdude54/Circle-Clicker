import pygame
import random


class Circle:
    def __init__(self, screen, color, radius):
        """
        init a circle object
        :param screen: pygame.Screen
        :param color: tuple
        :param radius: int
        """
        self.screen = screen
        self.color = color
        self.radius = radius
        self.circle_x = random.randint(50, 450)
        self.circle_y = random.randint(100, 450)

    def draw_circle(self):
        """
        Draws circle object
        :return: None
        """
        pygame.draw.circle(self.screen, self.color, (self.circle_x, self.circle_y), self.radius, 0)

    def mouse_collide(self, mx, my):
        """
        Checks if mouse collides with circle
        :param mx: int
        :param my: int
        :return: bool
        """
        if Circle.distance(self.circle_x, mx, self.circle_y, my) <= 50:
            return True
        return False

    def delete(self):
        """
        deletes a circle by drawing a black square over it
        :return: None
        """
        rect = pygame.Rect(self.circle_x - 50, self.circle_y - 50, 100, 100)
        pygame.draw.rect(self.screen, (0, 0, 0), rect)

    def set_color(self, color):
        """
        Sets color of circle
        :param color: tuple[int, int, int]
        :return: None
        """
        self.color = color

    @staticmethod
    def distance(x1, x2, y1, y2):
        """
        Calculates distance
        :param x1: int
        :param x2: int
        :param y1: int
        :param y2: int
        :return: int
        """
        return (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1 / 2)
