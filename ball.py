from colorama import *
from background import bg

ball_fig = Fore.LIGHTGREEN_EX + Back.LIGHTBLUE_EX + Style.BRIGHT + "O" + Style.RESET_ALL

# Borders
TOP = 3
BOTTOM = 42
LEFT = 1
RIGHT = 148

class Ball:
    def __init__(self):
        self._x = 75 + 5    # center of paddle
        self._y = 40
        self._Xspeed = 0
        self._Yspeed = 2

    def borderCollision(self, x, y, LIVES, ball_launched):
        if y < TOP:
            self._Yspeed = -2
        if y > BOTTOM:
            self._Yspeed = 2
            self._Xspeed = 0
            LIVES[0] -= 1
            ball_launched[0] = 0 
            
    # before launch
    def placeAbovePaddle(self, paddle_x):
        bg.grid[self._y][self._x] = ' '
        self._x = paddle_x + 5
        bg.grid[40][self._x] = ball_fig

    def moveBall(self, LIVES, ball_launched):
        self.borderCollision(self._x + self._Xspeed, self._y - self._Yspeed, LIVES, ball_launched)
        bg.grid[self._y][self._x] = ' '
        bg.grid[self._y - self._Yspeed][self._x + self._Xspeed] = ball_fig
        self._y -= self._Yspeed
        self._x -= self._Xspeed

ball = Ball()

#  +ve |
#   ^  |
#   y  |----------
#       x > +ve
