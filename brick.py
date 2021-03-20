from colorama import *
from background import bg
from powerup import *
import os

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
FALL_BRICK_TIME = [5]
FALL_BRICK = [0]    # 1 = bricks move down after collision
finish = [0]    # 1 = brick reached bottom

class Brick:
    def __init__(self, strength):
        self.__strength = strength
        self.__x = 0
        self.__y = 0
        self._rainbow = 0

        # these are just for powerup
        self._Xspeed = 0
        self._Yspeed = -1

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

    # f=1 thru ball & f=2 fireball
    def brickAfterCollision(self, i, grid, f, ballXspeed, ballYspeed):
        os.system("aplay sound/brickHit.wav -q &")
        self._Xspeed = ballXspeed
        self._Yspeed = ballYspeed
        if f == 2:
            # Explosive brickAfterCollision------------------------------------#
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
            # ---------------------------------------------------------------- #

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
    def setY(self, y):
        self.__y = y
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

    def brickAfterCollision(self, i, grid, f, ballXspeed, ballYspeed):
        os.system("aplay sound/brickHit.wav -q &")
        self._Xspeed = ballXspeed
        self._Yspeed = ballYspeed
        if f == 1:
            obj1[i].setStrength(0)
        elif f == 2:
            # Explosive brickAfterCollision------------------------------------#
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
            # ---------------------------------------------------------------- #

class explodingBrick(Brick):
    def __init__(self):
        super().__init__(-1)

    def brickAfterCollision(self, i, grid, f, ballXspeed, ballYspeed):
        self._Xspeed = ballXspeed
        self._Yspeed = ballYspeed
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

class rainbowBrick(Brick):
    def __init__(self):
        super().__init__(1)
        self._rainbow = 1
        self._touched = 0   # stops changing color after touch

    def brickAfterCollision(self, i, grid, f, ballXspeed, ballYspeed):
        os.system("aplay sound/brickHit.wav -q &")
        self._Xspeed = ballXspeed
        self._Yspeed = ballYspeed
        self._touched = 1
        if f==2:
            # Explosive brickAfterCollision------------------------------------#
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
            # ---------------------------------------------------------------- #
        if f == 1:
            obj1[i].setStrength(0)
        strength = obj1[i].getStrength()-1
        if strength >= 0:
            obj1[i].setStrength(strength)

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

paddleGrab = [' ']
paddleGrabX = []
paddleGrabY = []

fireBall = [' ']
fireBallX = []
fireBallY = []

shootingPaddle = [' ']
shootingPaddleX = []
shootingPaddleY = []

def generateBricks_lvl1(grid):
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

    for i in range(3):
        obj1.append(breakableBrick(1))
        obj1[len(obj1)-1].place(70-5*i,18,grid)

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

    # RAINBOW
    for i in range(4):
        obj1.append(rainbowBrick())
        obj1[len(obj1)-1].place(80-5*i,17,grid)

    ## Powerup into random brick
    # rand = random.randint(0,len(obj1)-1)
    # fastBrickX.append(obj1[rand].getX())
    # fastBrickY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # multiplyBrickX.append(obj1[rand].getX())
    # multiplyBrickY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # paddleShrinkX.append(obj1[rand].getX())
    # paddleShrinkY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # paddleExpandX.append(obj1[rand].getX())
    # paddleExpandY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # thruBallX.append(obj1[rand].getX())
    # thruBallY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # paddleGrabX.append(obj1[rand].getX())
    # paddleGrabY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # fireBallX.append(obj1[rand].getX())
    # fireBallY.append(obj1[rand].getY())
    # rand = random.randint(0,len(obj1)-1)
    # shootingPaddleX.append(obj1[rand].getX())
    # shootingPaddleY.append(obj1[rand].getY())

    fastBrickX.append(90)
    fastBrickY.append(22)
    multiplyBrickX.append(65)
    multiplyBrickY.append(21)
    paddleShrinkX.append(70)
    paddleShrinkY.append(22)
    paddleExpandX.append(75)
    paddleExpandY.append(22)
    thruBallX.append(80)
    thruBallY.append(22)
    paddleGrabX.append(85)
    paddleGrabY.append(22)
    fireBallX.append(90)
    fireBallY.append(22)
    shootingPaddleX.append(65)
    shootingPaddleY.append(22)

def generateBricks_lvl2(grid):
    # explosive
    obj1.append(explodingBrick())
    obj1[len(obj1)-1].place(75,20,grid)
    obj1.append(explodingBrick())
    obj1[len(obj1)-1].place(70+20,20,grid)
    for i in range(4):
        obj1.append(explodingBrick())
        obj1[len(obj1)-1].place(75+5*i,21,grid)
    
    # unbreakable
    for i in range(2):
        obj1.append(unbreakableBrick())
        obj1[len(obj1)-1].place(80+5*i,22,grid)
    
    # breakable
    # BRICK1
    for i in range(5):
        obj1.append(breakableBrick(1))
        obj1[len(obj1)-1].place(70,18+i,grid)

    # BRICK2
    for i in range(5):
        obj1.append(breakableBrick(2))
        obj1[len(obj1)-1].place(95,18+i,grid)

    # BRICK3
    for i in range(4):
        obj1.append(breakableBrick(3))
        obj1[len(obj1)-1].place(75+5*i,19,grid)

    # RAINBOW
    for i in range(4):
        obj1.append(rainbowBrick())
        obj1[len(obj1)-1].place(75+5*i,18,grid)

    # Powerup into random brick
    rand = random.randint(0,len(obj1)-1)
    fastBrickX.append(obj1[rand].getX())
    fastBrickY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    multiplyBrickX.append(obj1[rand].getX())
    multiplyBrickY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    paddleShrinkX.append(obj1[rand].getX())
    paddleShrinkY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    paddleExpandX.append(obj1[rand].getX())
    paddleExpandY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    thruBallX.append(obj1[rand].getX())
    thruBallY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    paddleGrabX.append(obj1[rand].getX())
    paddleGrabY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    fireBallX.append(obj1[rand].getX())
    fireBallY.append(obj1[rand].getY())
    rand = random.randint(0,len(obj1)-1)
    shootingPaddleX.append(obj1[rand].getX())
    shootingPaddleY.append(obj1[rand].getY())

def generateBricks_lvl3(grid):
    # unbreakable
    for i in range(4):
        obj1.append(unbreakableBrick())
        obj1[len(obj1)-1].place(70+5*i,20,grid)

def generateBricks_boss1(grid):
    for i in range(28):
        obj1.append(breakableBrick(1))
        obj1[len(obj1)-1].place(5*(i+1)+1,16,grid)

def generateBricks_boss2(grid):
    l = len(obj1) - 1
    for i in range(l,-1,-1):
        obj1.remove(obj1[i])
    for i in range(28):
        obj1.append(breakableBrick(2))
        obj1[len(obj1)-1].place(5*(i+1)+1,16,grid)

def placeBricks(grid):
    l = len(obj1) - 1
    for i in range(l,-1,-1):
        # change the strengths/colors of rainbow brick
        if obj1[i]._rainbow == 1 and obj1[i]._touched == 0:
            obj1[i].setStrength((obj1[i].getStrength()+1)%3 + 1)
        if obj1[i].getStrength() == 0:
            if obj1[i].getX() == fastBrickX[0] and obj1[i].getY() == fastBrickY[0]:
                fastBall[0] = FastBall(fastBrickX[0], fastBrickY[0])
                fastBall[0]._Xspeed = obj1[i]._Xspeed
                fastBall[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == multiplyBrickX[0] and obj1[i].getY() == multiplyBrickY[0]:
                multiplyBall[0] = MultiplyBall(multiplyBrickX[0], multiplyBrickY[0])
                multiplyBall[0]._Xspeed = obj1[i]._Xspeed
                multiplyBall[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == paddleShrinkX[0] and obj1[i].getY() == paddleShrinkY[0]:
                paddleShrink[0] = PaddleShrink(paddleShrinkX[0], paddleShrinkY[0])
                paddleShrink[0]._Xspeed = obj1[i]._Xspeed
                paddleShrink[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == paddleExpandX[0] and obj1[i].getY() == paddleExpandY[0]:
                paddleExpand[0] = PaddleExpand(paddleExpandX[0], paddleExpandY[0])
                paddleExpand[0]._Xspeed = obj1[i]._Xspeed
                paddleExpand[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == thruBallX[0] and obj1[i].getY() == thruBallY[0]:
                thruBall[0] = ThruBall(thruBallX[0], thruBallY[0])
                thruBall[0]._Xspeed = obj1[i]._Xspeed
                thruBall[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == paddleGrabX[0] and obj1[i].getY() == paddleGrabY[0]:
                paddleGrab[0] = PaddleGrab(paddleGrabX[0], paddleGrabY[0])
                paddleGrab[0]._Xspeed = obj1[i]._Xspeed
                paddleGrab[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == fireBallX[0] and obj1[i].getY() == fireBallY[0]:
                fireBall[0] = FireBall(fireBallX[0], fireBallY[0])
                fireBall[0]._Xspeed = obj1[i]._Xspeed
                fireBall[0]._Yspeed = -obj1[i]._Yspeed
            if obj1[i].getX() == shootingPaddleX[0] and obj1[i].getY() == shootingPaddleY[0]:
                shootingPaddle[0] = ShootingPaddle(shootingPaddleX[0], shootingPaddleY[0])
                shootingPaddle[0]._Xspeed = obj1[i]._Xspeed
                shootingPaddle[0]._Yspeed = -obj1[i]._Yspeed
            obj1[i].place(obj1[i].getX(),obj1[i].getY(), grid)
            obj1.remove(obj1[i])

    for i in range(len(obj1)):
        obj1[i].place(obj1[i].getX(),obj1[i].getY(), grid)
