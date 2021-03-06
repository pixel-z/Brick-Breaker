from colorama import *
import time
from paddle import paddle, paddle_change
from ball import *
import os

BOTTOM = 42
POWERUP_TIME = 10

class Powerup:
    def __init__(self,x=0,y=0):
        self._activated = 0
        self._start = 0
        self._x = x
        self._y = y
        self._Yspeed = 1
        self._Xspeed = 0
        self._changed = 0

        # for gravity effect in powerup
        self._time = 0
        self._maxtime = 10   # after this time we increase Yspeed

    def getActivated(self):
        return self._activated

    def setActivated(self, value):
        self._activated = value
    
    def resetPowerup(self):
        self._changed = 0
        self._start = -100  #so that the powerup time is exceeded always which 

    def __activate(self):
        if self._activated == 0:
            os.system("aplay sound/powerup.wav -q &")
            self._activated = 1
            self._start = time.time()

    def _paddleCollision(self, x ,y):
        paddleX = paddle.getX()
        if y == 41:
            if x>=paddleX and x<paddleX+10:
                self.__activate()

    def _borderCollision(self, x, y):
        # Borders
        TOP = 3
        BOTTOM = 42
        LEFT = 1
        RIGHT = 148

        if x < LEFT:
            self._Xspeed *= -1
        if x > RIGHT:
            self._Xspeed *= -1
        if y < TOP:
            self._Yspeed *= -1
        if y > BOTTOM:
            self._Yspeed = 0
            self._Xspeed = 0

    # default of powerup box falling is F character
    def move(self, grid):
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0

        self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
        self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.LIGHTWHITE_EX + Back.LIGHTBLACK_EX + Style.BRIGHT + "F" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
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
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
        self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.BLACK + Back.LIGHTWHITE_EX + Style.BRIGHT + "M" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
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
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        if self._changed == 0:
            self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
            self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.BLACK + Back.LIGHTWHITE_EX + Style.BRIGHT + "S" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
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
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        if self._changed == 0:
            self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
            self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.RED + Back.LIGHTWHITE_EX + Style.BRIGHT + "E" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '

class ThruBall(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)

    def update(self,ball):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                self._changed = 1
                for i in list(ball):
                    i._f = 0
            elif self._changed == 0:
                self._changed = 1
                for i in list(ball):
                    i._f = 1

    def move(self, grid):
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        if self._changed == 0:
            self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
            self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.RED + Back.BLUE + Style.BRIGHT + "T" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '

class PaddleGrab(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)
        self._grabbed = 0

    def update(self):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                self._changed = 1
                self._grabbed = 0
            elif self._changed == 0:
                self._changed = 1
                self._grabbed = 1

    def move(self, grid):
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        if self._changed == 0:
            self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
            self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT + "G" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '

class FireBall(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)

    def update(self,ball):
        if self._activated == 1:
            if time.time() - self._start >= POWERUP_TIME:
                self._activated = 0
                self._changed = 1
                for i in list(ball):
                    i._f = 0
            elif self._changed == 0:
                self._changed = 1
                for i in list(ball):
                    i._f = 2

    def move(self, grid):
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        if self._changed == 0:
            self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
            self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.RED + Back.BLUE + Style.BRIGHT + "$" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '

class ShootingPaddle(Powerup):
    def __init__(self, x, y):
        super().__init__(x,y)
        self._shoottime = 10
        self._shootmaxtime = 10

    def update(self, grid):
        self._shoottime += 1
        if self._activated == 1:
            paddle._color = 1
            # showing powerup time left
            grid[2][141] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"T"+ Style.RESET_ALL
            grid[2][142] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
            grid[2][143] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"M"+ Style.RESET_ALL
            grid[2][144] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
            grid[2][145] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
            grid[2][146] = int(POWERUP_TIME - time.time() + self._start)

            if time.time() - self._start >= POWERUP_TIME:
                paddle._color = 0
                grid[2][141] = Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL
                grid[2][142] = Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL
                grid[2][143] = Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL
                grid[2][144] = Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL
                grid[2][145] = Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL
                grid[2][146] = Fore.WHITE + Back.BLUE + Style.BRIGHT +" "+ Style.RESET_ALL
                self._activated = 0
                self._changed = 1
            elif self._changed == 0:
                self._changed = 1

    def move(self, grid):
        self._time += 1
        if self._time >= self._maxtime:
            self._time = 0
            
        if self._changed == 0:
            self._borderCollision(self._x + self._Xspeed, self._y + self._Yspeed)
            self._paddleCollision(self._x, self._y + self._Yspeed)
        grid[self._y][self._x] = ' '
            
        if self._y < BOTTOM and self._activated == 0:
            grid[self._y + self._Yspeed][self._x + self._Xspeed] = Fore.MAGENTA + Back.LIGHTWHITE_EX + Style.BRIGHT + "P" + Style.RESET_ALL
            self._y += self._Yspeed
            self._x += self._Xspeed
        if self._y >= BOTTOM:
            grid[self._y][self._x] = ' '
