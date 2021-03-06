from paddle import *
from brick import *
bossFinish = [0]

class Boss:
    def __init__(self):
        self.__health = 5
        self.__x = paddle.getX()
        self.__y = 3
        self.__Xrange = 10
        self.__Yrange = 1
        str = [[' ' for i in range(self.__Xrange)] for j in range(self.__Yrange)]
        with open("boss.txt") as obj:
            y=0
            for row in obj:
                x=0
                for char in row:
                    if char == '\n': break
                    else:
                        str[y][x] = Fore.WHITE + Back.GREEN + Style.NORMAL + char + Style.RESET_ALL
                    x+=1
                y+=1
        self.__body = str

    def getHealth(self):
        return self.__health
    def decHealth(self, grid):
        self.__health -= 1
        if self.__health <= 0:
            bossFinish[0] = 100
        elif self.__health == 3:
            generateBricks_boss1(grid)
        elif self.__health == 1:
            generateBricks_boss2(grid)

    def getX(self):
        return self.__x
    def getY(self):
        return self.__y

    def placeBoss(self, grid):
        for y in range(self.__y,self.__y+self.__Yrange):
            for x in range(self.__x,self.__x+self.__Xrange):
                grid[y][x] = ' '
        self.__x = paddle.getX()
        for y in range(self.__y,self.__y+self.__Yrange):
            for x in range(self.__x,self.__x+self.__Xrange):
                grid[y][x] = self.__body[y-self.__y][x-self.__x]

boss = Boss()