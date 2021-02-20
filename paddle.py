from colorama import *

PADDLE_Y = 41
SPEED = 3
paddle_change = [0]

class Paddle:
    def __init__(self):
        self.__x = 75     # COLUMNS/2 = 150/2

    # 1 if obstacle blocking else 0
    def __checkBorders(self, dirn):
        if dirn == 'a':
            if self.__x - SPEED <= 0:
                return 1
        else:
            if self.__x + 10 + SPEED >= 149:
                return 1
        return 0

    def movePaddle(self, dirn, grid):
        if dirn == 'a' and self.__checkBorders("a") == 0:
            x = self.__x - SPEED
            for i in range(10):
                grid[PADDLE_Y][x + i] = grid[PADDLE_Y][x + i + SPEED]

            grid[PADDLE_Y][x + 10] = ' '
            grid[PADDLE_Y][x + 11] = ' '
            grid[PADDLE_Y][x + 12] = ' '
            self.__x = x

        if dirn == 'd' and self.__checkBorders("d") == 0:
            x = self.__x + SPEED
            for i in range(9,-1,-1):
                grid[PADDLE_Y][x + i] = grid[PADDLE_Y][x + i - SPEED]

            grid[PADDLE_Y][x - 3] = ' '
            grid[PADDLE_Y][x - 2] = ' '
            grid[PADDLE_Y][x - 1] = ' '
            self.__x = x

    def placePaddle(self, grid):
        # paddle_shrink
        if paddle_change[0] < 0:
            for i in range(5):
                if i==0 or i==4:
                    grid[PADDLE_Y][self.__x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "2" + Style.RESET_ALL
                elif i==1 or i==3:
                    grid[PADDLE_Y][self.__x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "1" + Style.RESET_ALL
                elif i==2:
                    grid[PADDLE_Y][self.__x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "0" + Style.RESET_ALL
            for i in range(5):
                grid[PADDLE_Y][self.__x + 5 + i] = ' '
        else:
            for i in range(10):
                if i<2 or i>=8:
                    grid[PADDLE_Y][self.__x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "2" + Style.RESET_ALL
                elif i<4 or i>=6:
                    grid[PADDLE_Y][self.__x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "1" + Style.RESET_ALL
                elif i<6 or i>=4:
                    grid[PADDLE_Y][self.__x + i] = Fore.WHITE + Back.RED + Style.BRIGHT + "0" + Style.RESET_ALL

    def getX(self):
        return self.__x

paddle = Paddle()
