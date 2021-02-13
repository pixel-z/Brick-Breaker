from colorama import *
from background import bg
import random
from paddle import paddle

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
        self._Xspeed = 0
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

    def paddleCollision(self, x ,y):
        paddleX = paddle.getX()
        if y == 42:
            if x>=paddleX and x<paddleX+2:
                self._Xspeed -= 2
                self._Yspeed *= -1
            elif x>=paddleX+2 and x<paddleX+4:
                self._Xspeed -= 1
                self._Yspeed *= -1
            elif x>=paddleX+4 and x<paddleX+6:
                self._Yspeed *= -1
            elif x>=paddleX+6 and x<paddleX+8:
                self._Xspeed += 1
                self._Yspeed *= -1
            elif x>=paddleX+8 and x<paddleX+10:
                self._Xspeed += 2
                self._Yspeed *= -1
        
    # before launch
    def placeAbovePaddle(self, paddle_x):
        if self._offset < 2:
            self._Xspeed = -2
        elif self._offset < 4:
            self._Xspeed = -1
        elif self._offset < 6:
            self._Xspeed = 0
        elif self._offset < 8:
            self._Xspeed = 1
        elif self._offset < 10:
            self._Xspeed = 2

        bg.grid[self._y][self._x] = ' '
        self._x = paddle_x + self._offset
        bg.grid[40][self._x] = ball_fig

    def moveBall(self, LIVES, ball_launched):
        self.borderCollision(self._x + self._Xspeed, self._y - self._Yspeed, LIVES, ball_launched)
        self.paddleCollision(self._x + self._Xspeed, self._y - self._Yspeed)
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
