import pygame


class Timer:
    def __init__(self, clock: pygame.time.Clock()):
        """
        Initialize new timer object
        :param clock: pygame.time.Clock
        """
        self.time = None
        self.clock = clock
        self.milliseconds = self.clock.get_time()
        self.seconds_first = 0
        self.seconds_tenth = 0
        self.minutes = 0
        self.finished = False
        self.started = False

    def start(self):
        """
        starts the timer
        :return: None
        """
        self.started = True
        if self.seconds_first == 0 and self.seconds_tenth == 0 and self.minutes == 0:
            self.finished = True
        if self.time == f"0:10":
            self.finished = False

        if self.milliseconds >= 500:
            self.seconds_first -= 1
            if self.seconds_first == -1 and self.seconds_tenth == 0:
                self.seconds_first = 9
                self.seconds_tenth = 5
                self.minutes -= 1
            if self.seconds_first == -1 and self.seconds_tenth != 0:
                self.seconds_first = 9
                self.seconds_tenth -= 1
            self.milliseconds -= 500
        self.time = f"{self.minutes}:{self.seconds_tenth}{self.seconds_first}"
        self.milliseconds += self.clock.tick_busy_loop(60)

        if self.seconds_first == 0:
            self.started = False

    def set_timer(self, init_min, init_sec):
        """
        sets the timer
        :param init_min: int
        :param init_sec: int
        :return: None
        """
        if init_sec < 10:
            init_sec_str = f"0{init_sec}"
        else:
            init_sec_str = str(init_sec)
        self.minutes = init_min
        self.seconds_tenth = int(init_sec_str[0])
        self.seconds_first = int(init_sec_str[1])

    def get_time(self):
        return self.time

    def is_finished(self):
        return self.finished

    def is_started(self):
        return self.started
