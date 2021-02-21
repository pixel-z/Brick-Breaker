from colorama import *
import time
from paddle import paddle, paddle_change
from ball import *

BOTTOM = 42
POWERUP_TIME = 5

class Powerup:
    def __init__(self,x=0,y=0):
        self._activated = 0
        self._start = 0
        self._x = x
        self._y = y
        self._dropSpeed = 1
        self._changed = 0

    def getActivated(self):
        return self._activated

    def setActivated(self, value):
        self._activated = value

    def __activate(self):
        if self._activated == 0:
            self._activated = 1
            self._start = time.time()

    def _paddleCollision(self, x ,y):
        paddleX = paddle.getX()
        if y == 41:
            if x>=paddleX and x<paddleX+10:
                self.__activate()

    # default of powerup box falling is F character
    def move(self, grid):
        self._paddleCollision(self._x, self._y + self._dropSpeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._dropSpeed][self._x] = Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "F" + Style.RESET_ALL
            self._y += self._dropSpeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '


class FastBall(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)

    def update(self, ball):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                # reset velocity after time limit
                if len(ball) != 0:
                    for i in list(ball):
                        if i._prevXspeed >= 0:
                            if i._Xspeed < 0: i._Xspeed = -1*i._prevXspeed
                            else: i._Xspeed = i._prevXspeed

            elif self._changed == 0:
                if len(ball) != 0:
                    for i in list(ball):
                        i._prevXspeed = abs(i._Xspeed)
                        if i._Xspeed < 0: i._Xspeed -= 3
                        else: i._Xspeed += 3
                self._changed = 1

class MultiplyBall(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)

    def update(self):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                
    def move(self, grid):
        self._paddleCollision(self._x, self._y + self._dropSpeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._dropSpeed][self._x] = Fore.BLACK + Back.LIGHTWHITE_EX + Style.BRIGHT + "M" + Style.RESET_ALL
            self._y += self._dropSpeed
        if self._y >= BOTTOM:
                grid[self._y][self._x] = ' '

class PaddleShrink(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)

    def update(self):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                paddle_change[0] += 1
                self._changed = 1
            elif self._changed == 0:
                paddle_change[0] -= 1
                self._changed = 1

    def move(self, grid):
        if self._changed == 0:
            self._paddleCollision(self._x, self._y + self._dropSpeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._dropSpeed][self._x] = Fore.BLACK + Back.LIGHTWHITE_EX + Style.BRIGHT + "S" + Style.RESET_ALL
            self._y += self._dropSpeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '
    
class PaddleExpand(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)

    def update(self):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                paddle_change[0] -= 1
                self._changed = 1
            elif self._changed == 0:
                paddle_change[0] += 1
                self._changed = 1

    def move(self, grid):
        if self._changed == 0:
            self._paddleCollision(self._x, self._y + self._dropSpeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._dropSpeed][self._x] = Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + "E" + Style.RESET_ALL
            self._y += self._dropSpeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '