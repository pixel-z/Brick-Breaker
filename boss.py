from paddle import *

class Boss:
    def __init__(self):
        self.__health = 5
        self.__x = paddle.getX()
        self.__y = 5
        self.__Xrange = 10
        self.__Yrange = 2

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

    def placeBoss(self, grid):
        for y in range(self.__y,self.__y+self.__Yrange):
            for x in range(self.__x,self.__x+self.__Xrange):
                grid[y][x] = ' '
        self.__x = paddle.getX()
        for y in range(self.__y,self.__y+self.__Yrange):
            for x in range(self.__x,self.__x+self.__Xrange):
                grid[y][x] = self.__body[y-self.__y][x-self.__x]

boss = Boss()