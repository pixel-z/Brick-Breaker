from colorama import *
from background import bg

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

class Brick:
    def __init__(self, strength):
        self._strength = strength

    def place(self, x, y, grid):
        self._x = x
        self._y = y
        if self._strength == 1:
            for i in range(5):
                grid[y][x+i] = S1_BRICK
            grid[y][x+2] = S1_BRICK1
        elif self._strength == 2:
            for i in range(5):
                grid[y][x+i] = S2_BRICK
            grid[y][x+2] = S2_BRICK1
        elif self._strength == 3:
            for i in range(5):
                grid[y][x+i] = S3_BRICK
            grid[y][x+2] = S3_BRICK1
        elif self._strength == -1:
            for i in range(5):
                grid[y][x+i] = EXPLODING
            grid[y][x+2] = EXPLODING1
        elif self._strength == -2:
            for i in range(5):
                grid[y][x+i] = UNBREAKABLE
            grid[y][x+2] = UNBREAKABLE1

    # return 1 and apply consequences in subclasses
    def checkCollision(self):
        pass

class breakableBrick(Brick):
    def __init__(self, strength):
        super().__init__(strength)

class unbreakableBrick(Brick):
    def __init__(self):
        super().__init__(-2)

class explodingBrick(Brick):
    def __init__(self):
        super().__init__(-1)

obj1 = []   # breakable
obj2 = []   # unbreakable
obj3 = []   # explosive
def generateBricks(grid):
    # explosive
    for i in range(4):
        obj3.append(breakableBrick(-1))
        obj3[i].place(70+5*i,20,grid)
    for i in range(2):
        obj3.append(breakableBrick(-1))
        obj3[i].place(75+5*i,21,grid)
    
    # unbreakable
    for i in range(6):
        obj2.append(breakableBrick(-2))
        obj2[i].place(65+5*i,19,grid)
    
    # breakable
    # BRICK1
    for i in range(6):
        obj1.append(breakableBrick(1))
        obj1[i].place(65+5*i,22,grid)
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