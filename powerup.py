from colorama import *
import time
from paddle import paddle

BOTTOM = 42
POWERUP_TIME = 3
INC_XSPEED = 1

class Powerup:
    def __init__(self,x,y):
        self._activated = 0
        self._start = 0
        self._x = x
        self._y = y
        self._dropSpeed = 1

    def getActivated(self):
        return self._activated

    def setActivated(self, value):
        self._activated = value

    def __activate(self):
        if self._activated == 0:
            self._activated = 1
            self._start = time.time()

    def __paddleCollision(self, x ,y):
        paddleX = paddle.getX()
        if y == 41:
            if x>=paddleX and x<paddleX+10:
                self.__activate()

    def move(self, grid):
        self.__paddleCollision(self._x, self._y + self._dropSpeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._dropSpeed][self._x] = Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "F" + Style.RESET_ALL
            self._y += self._dropSpeed


class FastBall(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)
        self._speedAdded = 0

    def update(self, ball):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
            elif self._speedAdded == 0:
                if len(ball) != 0:
                    for i in list(ball):
                        if i._Xspeed < 0: i._Xspeed -= 2
                        else: i._Xspeed += 2
                self._speedAdded = 1