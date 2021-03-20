from colorama import *
from paddle import *
from brick import obj1

laser_fig = Fore.BLUE + Back.RED + Style.BRIGHT + "!" + Style.RESET_ALL

# shooting paddle laser
class Laser():
    def __init__(self):
        self._x1 = paddle.getX()
        self._x2 = paddle.getX()+10
        self._y = 40
        self._dead = 0
        self._Yspeed = 1
        self._f = 0
    
    def __borderCollision(self, y, grid):
        TOP = 3
        BOTTOM = 42
        if y < TOP:
            self._dead = 1
        if y > BOTTOM:
            self._dead = 1

    def __brickCollision(self, grid):
        for i in range(len(obj1)):
            if obj1[i].getX() <= self._x1 < obj1[i].getX()+5 and obj1[i].getY() == self._y:
                obj1[i].brickAfterCollision(i,grid, self._f, 0, self._Yspeed)
                self._dead = 1
            if obj1[i].getX() <= self._x2 < obj1[i].getX()+5 and obj1[i].getY() == self._y:
                obj1[i].brickAfterCollision(i,grid, self._f, 0, self._Yspeed)
                self._dead = 1

    def shoot(self, grid):
        self.__borderCollision(self._y - self._Yspeed, grid)
        self.__brickCollision(grid)
        grid[self._y][self._x1] = ' '
        grid[self._y][self._x2] = ' '

        if self._dead == 0:
            grid[self._y - self._Yspeed][self._x1] = laser_fig
            grid[self._y - self._Yspeed][self._x2] = laser_fig
            self._y -= self._Yspeed

laser = []