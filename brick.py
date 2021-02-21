from colorama import *
from background import bg
from powerup import *

# Brick dimension = [1x5]
# exploding bricks strength = -1 
# unbreakable bricks strength = -2

S1_BRICK = Fore.WHITE + Back.GREEN + Style.NORMAL + " " + Style.RESET_ALL
S1_BRICK1 = Fore.WHITE + Back.GREEN + Style.NORMAL + "1" + Style.RESET_ALL

S2_BRICK = Fore.WHITE + Back.BLUE + Style.NORMAL + " " + Style.RESET_ALL
S2_BRICK1 = Fore.WHITE + Back.BLUE + Style.NORMAL + "2" + Style.RESET_ALL

S3_BRICK = Fore.WHITE + Back.MAGENTA + Style.NORMAL + " " + Style.RESET_ALL
S3_BRICK1 = Fore.WHITE + Back.MAGENTA + Style.NORMAL + "3" + Style.RESET_ALL

EXPLODING = Fore.WHITE + Back.YELLOW + Style.NORMAL + " " + Style.RESET_ALL
EXPLODING1 = Fore.WHITE + Back.YELLOW + Style.NORMAL + "*" + Style.RESET_ALL

UNBREAKABLE = Fore.BLACK + Back.LIGHTBLACK_EX + Style.DIM + " " + Style.RESET_ALL
UNBREAKABLE1 = Fore.BLACK + Back.LIGHTBLACK_EX + Style.DIM + "U" + Style.RESET_ALL

ROWS = 45
COLUMNS = 150
SCORE = [0]

class Brick:
    def __init__(self, strength):
        self.__strength = strength
        self.__x = 0
        self.__y = 0

    def place(self, x, y, grid):
        self.__x = x
        self.__y = y

        if self.__strength == 0:
            for i in range(5):
                grid[y][x+i] = ' '
                SCORE[0] += 1
        if self.__strength == 1:
            for i in range(5):
                grid[y][x+i] = S1_BRICK
            grid[y][x+2] = S1_BRICK1
        elif self.__strength == 2:
            for i in range(5):
                grid[y][x+i] = S2_BRICK
            grid[y][x+2] = S2_BRICK1
        elif self.__strength == 3:
            for i in range(5):
                grid[y][x+i] = S3_BRICK
            grid[y][x+2] = S3_BRICK1
        elif self.__strength == -1:
            for i in range(5):
                grid[y][x+i] = EXPLODING
            grid[y][x+2] = EXPLODING1
        elif self.__strength == -2:
            for i in range(5):
                grid[y][x+i] = UNBREAKABLE
            grid[y][x+2] = UNBREAKABLE1

    def brickAfterCollision(self, i, grid, f):
        if f == 1:
            obj1[i].setStrength(0)
        strength = obj1[i].getStrength()-1
        if strength >= 0:
            obj1[i].setStrength(strength)

    # return 1 and apply consequences in subclasses
    def getX(self):
        return self.__x
    def getY(self):
        return self.__y
    def getStrength(self):
        return self.__strength
    def setStrength(self, strength):
        self.__strength = strength

class breakableBrick(Brick):
    def __init__(self, strength):
        super().__init__(strength)

class unbreakableBrick(Brick):
    def __init__(self):
        super().__init__(-2)

    def brickAfterCollision(self, i, grid, f):
        if f == 1:
            obj1[i].setStrength(0)
        pass

class explodingBrick(Brick):
    def __init__(self):
        super().__init__(-1)

    def brickAfterCollision(self, i, grid, f):
        arr = []
        arr.append(obj1[i])
        final = set()
        c=0
        # for k in list(arr):
        while c < len(arr):
            k = arr[c]
            x = k.getX()
            y = k.getY()
            final.add(k)
            for j in list(obj1):
                f = 0
                for p in list(arr):
                    if j.getX() == p.getX() and j.getY() == p.getY():
                        f = 1
                        break
                if f == 1:
                    continue

                flag=0
                if j.getY() == y:
                    if j.getX() == x-5 or j.getX() == x+5:
                        flag=1
                elif j.getY() == y+1 or j.getY() == y-1:
                    if j.getX() == x or j.getX() == x+5 or j.getX() == x-5:
                        flag=1
                if flag == 1:
                    if j.getStrength() == -1:
                        arr.append(j)
                        # final.add(j)
                    else:
                        final.add(j)
            c+=1

        for j in final:
            j.setStrength(0)

obj1 = []
fastBall = [' ']
fastBrickX = []
fastBrickY = []

multiplyBall = [' ']
multiplyBrickX = []
multiplyBrickY = []

paddleShrink = [' ']
paddleShrinkX = []
paddleShrinkY = []

paddleExpand = [' ']
paddleExpandX = []
paddleExpandY = []

thruBall = [' ']
thruBallX = []
thruBallY = []

def generateBricks(grid):
    # explosive
    for i in range(4):
        obj1.append(explodingBrick())
        obj1[len(obj1)-1].place(70+5*i,20,grid)
    for i in range(2):
        obj1.append(explodingBrick())
        obj1[len(obj1)-1].place(75+5*i,21,grid)
    
    # unbreakable
    for i in range(6):
        obj1.append(unbreakableBrick())
        obj1[len(obj1)-1].place(65+5*i,19,grid)
    
    # breakable
    # BRICK1
    for i in range(6):
        obj1.append(breakableBrick(1))
        obj1[len(obj1)-1].place(65+5*i,22,grid)
    # Powerup into random brick
    fastBrickX.append(obj1[len(obj1)-1].getX())
    fastBrickY.append(22)
    multiplyBrickX.append(65)
    multiplyBrickY.append(22)
    paddleShrinkX.append(70)
    paddleShrinkY.append(22)
    paddleExpandX.append(75)
    paddleExpandY.append(22)
    thruBallX.append(80)
    thruBallY.append(22)

    for i in range(3):
        obj1.append(breakableBrick(1))
        obj1[len(obj1)-1].place(70-5*i,18,grid)
    for i in range(4):
        obj1.append(breakableBrick(1))
        obj1[len(obj1)-1].place(80-5*i,17,grid)

    # BRICK2
    for i in range(4):
        obj1.append(breakableBrick(2))
        obj1[len(obj1)-1].place(70-5*i,21,grid)
    for i in range(4):
        obj1.append(breakableBrick(2))
        obj1[len(obj1)-1].place(85+5*i,21,grid)
    for i in range(5):
        obj1.append(breakableBrick(2))
        obj1[len(obj1)-1].place(75+5*i,18,grid)

    # BRICK3
    for i in range(4):
        obj1.append(breakableBrick(3))
        obj1[len(obj1)-1].place(65-5*i,20,grid)
    for i in range(4):
        obj1.append(breakableBrick(3))
        obj1[len(obj1)-1].place(90+5*i,20,grid)
    for i in range(2):
        obj1.append(breakableBrick(3))
        obj1[len(obj1)-1].place(60-5*i,19,grid)
    for i in range(2):
        obj1.append(breakableBrick(3))
        obj1[len(obj1)-1].place(95+5*i,19,grid)
    for i in range(2):
        obj1.append(breakableBrick(3))
        obj1[len(obj1)-1].place(85+5*i,17,grid)


def placeBricks(grid):
    l = len(obj1) - 1
    for i in range(l,-1,-1):
        if obj1[i].getStrength() == 0:
            if obj1[i].getX() == fastBrickX[0] and obj1[i].getY() == fastBrickY[0]:
                fastBall[0] = FastBall(fastBrickX[0], fastBrickY[0])
            if obj1[i].getX() == multiplyBrickX[0] and obj1[i].getY() == multiplyBrickY[0]:
                multiplyBall[0] = MultiplyBall(multiplyBrickX[0], multiplyBrickY[0])
            if obj1[i].getX() == paddleShrinkX[0] and obj1[i].getY() == paddleShrinkY[0]:
                paddleShrink[0] = PaddleShrink(paddleShrinkX[0], paddleShrinkY[0])
            if obj1[i].getX() == paddleExpandX[0] and obj1[i].getY() == paddleExpandY[0]:
                paddleExpand[0] = PaddleExpand(paddleExpandX[0], paddleExpandY[0])
            if obj1[i].getX() == thruBallX[0] and obj1[i].getY() == thruBallY[0]:
                thruBall[0] = ThruBall(thruBallX[0], thruBallY[0])
            obj1[i].place(obj1[i].getX(),obj1[i].getY(), grid)
            obj1.remove(obj1[i])

    for i in range(len(obj1)):
        obj1[i].place(obj1[i].getX(),obj1[i].getY(), grid)
