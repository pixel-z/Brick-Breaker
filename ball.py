from colorama import *
import random
import math
from paddle import paddle, paddle_change
from brick import *

ball_fig = Fore.LIGHTGREEN_EX + Back.LIGHTBLUE_EX + Style.BRIGHT + "O" + Style.RESET_ALL

# Borders
TOP = 3
BOTTOM = 42
LEFT = 1
RIGHT = 148

class Ball:
    def __init__(self):
        self._offset = random.randint(0,9)  # random position from start of paddle
        # self._offset = 5
        self._x = 75 + self._offset
        self._y = 40
        self._Xspeed = 0
        self._Yspeed = 1
        self._dead = 0      # dead = 1 means ball hit bottom of border
        self._prevXspeed = -1   # for fastBall powerup
        self._f = 0

    # checks if collision occurs & changes speed accordingly
    def __borderCollision(self, x, y, LIVES, ball_launched):
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

                # remove powerup after life loss
                if fastBall[0] != ' ':
                    fastBall[0].setActivated(0)
                if multiplyBall[0] != ' ':
                    multiplyBall[0].setActivated(0)
                if paddleShrink[0] != ' ':
                    paddleShrink[0].setActivated(0)
                if thruBall[0] != ' ':
                    thruBall[0].setActivated(0)

    def __paddleCollision(self, x ,y, ball_launched):
        paddleX = paddle.getX()
        if paddleGrab[0] != ' ' and paddleGrab[0]._grabbed == 1:
            if y == 42:
                f=0
                if paddle_change[0] < 0 and paddleX<=x<paddleX+5: f=1
                if paddle_change[0] > 0 and paddleX<=x<paddleX+12: f=1
                elif paddleX<=x<paddleX+10: f=1
                if f == 1:
                    ball_launched[0] = 0
                    return

        if paddle_change[0]<0:
            if y == 42:
                if x==paddleX:
                    self._Xspeed -= 2
                    self._Yspeed *= -1
                elif x==paddleX+1:
                    self._Xspeed -= 1
                    self._Yspeed *= -1
                elif x==paddleX+2:
                    self._Yspeed *= -1
                elif x==paddleX+3:
                    self._Xspeed += 1
                    self._Yspeed *= -1
                elif x==paddleX+4:
                    self._Xspeed += 2
                    self._Yspeed *= -1
        elif paddle_change[0] > 0:
            if y == 42:
                if x>=paddleX and x<paddleX+2:
                    self._Xspeed -= 2
                    self._Yspeed *= -1
                elif x>=paddleX+2 and x<paddleX+4:
                    self._Xspeed -= 1
                    self._Yspeed *= -1
                elif x>=paddleX+4 and x<paddleX+8:
                    self._Yspeed *= -1
                elif x>=paddleX+8 and x<paddleX+10:
                    self._Xspeed += 1
                    self._Yspeed *= -1
                elif x>=paddleX+10 and x<paddleX+12:
                    self._Xspeed += 2
                    self._Yspeed *= -1    
        else:
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

    def __brickCollision(self, grid):
        x1 = self._x
        x2 = self._x + self._Xspeed
        y1 = self._y
        y2 = self._y - self._Yspeed

        halfx = x1 + (x2-x1)/2

        c1=1
        c2=1
        if x1>x2: c1=-1
        if y1>y2: c2=-1

        if self._Xspeed == 0:
            for i in range(len(obj1)):
                if obj1[i].getX() <= self._x < obj1[i].getX()+5 and obj1[i].getY() == self._y:
                    if self._f == 0:
                        self._Yspeed *= -1
                    obj1[i].brickAfterCollision(i,grid, self._f)

        flag = 0
        for x in range(x1,x2+c1,c1):
            if flag == 1:
                break
            if self._Xspeed > 0 and self._Yspeed > 0:
                for i in range(len(obj1)):
                    if x <= halfx:
                        if obj1[i].getY() == self._y and x == obj1[i].getX()-1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()+1 == self._y:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                    else:
                        if obj1[i].getY() == self._y-1 and x == obj1[i].getX()-1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()+1 == self._y-1:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
            elif self._Xspeed < 0 and self._Yspeed > 0:
                for i in range(len(obj1)):
                    if x <= halfx:
                        if obj1[i].getY() == self._y and x == obj1[i].getX()+5+1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()+1 == self._y:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                    else:
                        if obj1[i].getY() == self._y-1 and x == obj1[i].getX()+5+1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()+1 == self._y-1:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
            elif self._Xspeed > 0 and self._Yspeed < 0:
                for i in range(len(obj1)):
                    if x <= halfx:
                        if obj1[i].getY() == self._y and x == obj1[i].getX()-1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()-1 == self._y:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                    else:
                        if obj1[i].getY() == self._y+1 and x == obj1[i].getX()-1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()-1 == self._y+1:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
            elif self._Xspeed < 0 and self._Yspeed < 0:
                for i in range(len(obj1)):
                    if x <= halfx:
                        if obj1[i].getY() == self._y and x == obj1[i].getX()+5+1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()-1 == self._y:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                    else:
                        if obj1[i].getY() == self._y+1 and x == obj1[i].getX()+5+1:
                            if self._f == 0:
                                self._Xspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1
                        if obj1[i].getX() <= x < obj1[i].getX()+5 and obj1[i].getY()-1 == self._y+1:
                            if self._f == 0:
                                self._Yspeed *= -1
                            obj1[i].brickAfterCollision(i,grid, self._f)
                            flag = 1

    # before launch
    def placeAbovePaddle(self, paddle_x, grid):
        self._y = 40
        self._Yspeed = 1
        paddle_change[0] = 0
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

        grid[self._y][self._x] = ' '
        self._x = paddle_x + self._offset
        grid[40][self._x] = ball_fig

    def moveBall(self, LIVES, ball_launched, grid):
        self.__borderCollision(self._x + self._Xspeed, self._y - self._Yspeed, LIVES, ball_launched)
        self.__paddleCollision(self._x, self._y - self._Yspeed, ball_launched)
        self.__brickCollision(grid)
        grid[self._y][self._x] = ' '
        if self._dead == 0:
            grid[self._y - self._Yspeed][self._x + self._Xspeed] = ball_fig
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
        self._prevXspeed = -1
        self._f = Ball._f