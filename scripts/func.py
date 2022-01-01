import pygame


def center(screen: pygame.Surface, surface: pygame.Surface):
    """
    Centers a surface to another surface
    :param screen: pygame.Surface
    :param surface: pygame.Surface
    :return: int
    """
    return (screen.get_width() / 2) - (surface.get_width() / 2)


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
