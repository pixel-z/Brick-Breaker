from colorama import *
from background import bg

PADDLE_Y = 41
SPEED = 3

class Paddle:
    def __init__(self):
        self._x = 75     # COLUMNS/2 = 150/2

    # 1 if obstacle blocking else 0
    def __checkBorders(self, dirn):
        if dirn == 'a':
            if self._x - SPEED <= 0:
                return 1
        else:
            if self._x + 10 + SPEED >= 149:
                return 1
        return 0

    def movePaddle(self, dirn):
        if dirn == 'a' and self.__checkBorders("a") == 0:
            x = self._x - SPEED
            for i in range(10):
                bg.grid[PADDLE_Y][x + i] = bg.grid[PADDLE_Y][x + i + SPEED]

            bg.grid[PADDLE_Y][x + 10] = ' '
            bg.grid[PADDLE_Y][x + 11] = ' '
            bg.grid[PADDLE_Y][x + 12] = ' '
            self._x = x

        if dirn == 'd' and self.__checkBorders("d") == 0:
            x = self._x + SPEED
            for i in range(9,-1,-1):
                bg.grid[PADDLE_Y][x + i] = bg.grid[PADDLE_Y][x + i - SPEED]

            bg.grid[PADDLE_Y][x - 3] = ' '
            bg.grid[PADDLE_Y][x - 2] = ' '
            bg.grid[PADDLE_Y][x - 1] = ' '
            self._x = x

    def placePaddle(self):
        for i in range(10):
            bg.grid[PADDLE_Y][self._x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "I" + Style.RESET_ALL

paddle = Paddle()
