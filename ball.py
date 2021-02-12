from colorama import *
from background import bg
import random

ball_fig = Fore.LIGHTGREEN_EX + Back.LIGHTBLUE_EX + Style.BRIGHT + "O" + Style.RESET_ALL

# Borders
TOP = 3
BOTTOM = 42
LEFT = 1
RIGHT = 148

class Ball:
    def __init__(self):
        self._offset = random.randint(0,9)  # random position from start of paddle
        self._x = 75 + self._offset
        self._y = 40
        self._Xspeed = -2
        self._Yspeed = 2
        self._dead = 0      # dead = 1 means ball hit bottom of border

    # checks if collision occurs & changes speed accordingly
    def borderCollision(self, x, y, LIVES, ball_launched):
        if x < LEFT:
            self._Xspeed *= -1
        if x > RIGHT:
            self._Xspeed *= -1
        if y < TOP:
            self._Yspeed *= -1
        if y > BOTTOM:
            self._Yspeed *= -1
            self._Xspeed = 0
            self._dead = 1
            
            for i in list(ball):
                if i._dead == 1:
                    ball.remove(i)

            if len(ball) == 0:
                LIVES[0] -= 1
                ball_launched[0] = 0 
                self._offset = random.randint(0,9)
                ball.append(Ball())
            
    # before launch
    def placeAbovePaddle(self, paddle_x):
        bg.grid[self._y][self._x] = ' '
        self._x = paddle_x + self._offset
        bg.grid[40][self._x] = ball_fig

    def moveBall(self, LIVES, ball_launched):
        self.borderCollision(self._x + self._Xspeed, self._y - self._Yspeed, LIVES, ball_launched)
        bg.grid[self._y][self._x] = ' '
        if self._dead == 0:
            bg.grid[self._y - self._Yspeed][self._x + self._Xspeed] = ball_fig
            self._y -= self._Yspeed
            self._x += self._Xspeed

# ball = Ball()
ball = []
ball.append(Ball())

#  +ve |
#   ^  |
#   y  |----------
#       x > +ve

# subclass for duplicates of ball (powerup)
class duplicateBall(Ball):
    def __init__(self, Ball):
        self._offset = random.randint(0,9)  # random position from start of paddle
        self._x = Ball._x
        self._y = Ball._y
        self._Xspeed = -1 * Ball._Xspeed
        self._Yspeed = -1 * Ball._Yspeed
        self._dead = 0
