import pygame
import json
import os
from datetime import datetime
from pygame.locals import *
from scripts.text import Text

BLUE = (0, 0, 255)


def read_json(file):
    """
    Reads and returns game list from the json file
    :param file: str
    :return: list
    """
    with open(file) as f:
        data = json.load(f)
    return data


def append_game_data(score: int, level: str, file: str):
    """
    appends game info to json file
    :param score: int
    :param level: str
    :param file: str
    :return: None
    """
    data = {"score": score, "level": level, "date": datetime.now().strftime("%m/%d/%Y %H:%M:%S")}
    with open(file, "r+") as f:
        game_list = json.load(f)
        game_list.append(data)
        f.seek(0)
        json.dump(game_list, f, indent=4)


def clear_data(file):
    """
    Clears the data of json file by deleting the file and adding a new one with an empty list
    :param file: str
    :return: None
    """
    try:
        os.remove(file)

    except FileNotFoundError as e:
        print(e)

    with open(file, "w") as f:
        game_list = []
        json.dump(game_list, f)


def draw_activity_widget(y, screen: pygame.Surface, score, level, date):
    """
    draws a rectangle with the information of recent games
    :param y: int
    :param screen: pygame.Surface
    :param score: int
    :param level: str
    :param date: str
    :return: None
    """
    rect = Rect(screen.get_width() // 2 - 350//2, y, 350, 70)
    pygame.font.init()
    date_text = Text(rect.x + 6, rect.y + 45, "Date: " + date, "assets/dpcomic.ttf", 20, BLUE)
    level_text = Text(rect.x + 6, rect.y + 25, "Level: " + level, "assets/dpcomic.ttf", 20, BLUE)
    score_text = Text(rect.x + 6, rect.y + 5, "Score: " + str(score), "assets/dpcomic.ttf", 20, BLUE)
    pygame.draw.rect(screen, BLUE, rect, width=5)
    date_text.draw(screen)
    level_text.draw(screen)
    score_text.draw(screen)


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
