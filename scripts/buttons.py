import pygame


class Button:
    def __init__(self, x, y, image, scale):
        """
                Init button object
                :param x: int
                :param y: int
                :param image: str
                :param scale: int
                """
        width = image.get_width()
        height = image.get_height()
        self.x = x
        self.y = y
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.clicked = False

    def draw(self, surface: pygame.Surface):
        """
        draws button on screen
        :param surface: pygame.Surface
        :return: bool
        """

        surface.blit(self.image, (self.rect.x, self.rect.y))

    def get_bottom(self):
        return self.rect.bottom

    def get_right(self):
        return self.rect.right

    def get_left(self):
        return self.rect.left

    @staticmethod
    def center(screen: pygame.Surface, surface: pygame.Surface):
        """
        Centers a surface to another surface
        :param screen: pygame.Surface
        :param surface: pygame.Surface
        :return: int
        """
        return (screen.get_width() / 2) - (surface.get_width() / 2)

    @staticmethod
    def dist_to_btm_of(top_btn, distance):
        """
        Adjusts a button relative to the button above
        :param top_btn: Button
        :param distance: int
        :return: int
        """
        return top_btn.get_bottom() + distance

    @staticmethod
    def dist_to_right_of(right_btn, distance):
        """
        adjusts a button relative to the right
        :param right_btn: Button
        :param distance: int
        :return: int
        """
        return right_btn.rect.left + distance

    @staticmethod
    def dist_to_left_of(left_btn, distance):
        """
        adjusts a button relative to the left
        :param left_btn: Button
        :param distance: int
        :return: int
        """
        return left_btn.get_right() + distance


class MenuButton(Button):
    def __init__(self, x, y, image, scale):
        """
        Init button object
        :param x: int
        :param y: int
        :param image: str
        :param scale: int
        """
        super().__init__(x, y, image, scale)

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


