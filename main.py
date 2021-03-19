import os
import time
from colorama import *
from input import *
from background import *
from paddle import *
from ball import *
from brick import *
from powerup import *
from boss import *

# Windows doesn't support ANSI coloring but Windows API does
# init() makes Windows API run these colors  
init()

# initialize variables
start_time = time.time()
prev_time = start_time
LIVES = [3]     # only object can be passed by reference
LVL = [1] 
ROWS = 45
COLS = 150
ball_launched = [0]   # 1 = ball launched from paddle
flag = 0

generateBricks_lvl1(bg.getGrid())

def Message(msg):
    if msg == "q":
        print("\t\t\t\t\t\t\t Score: ", SCORE[0])
        print("\t\t\t _____                ______\n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|----|   |-------|   |----- \n" +
              "\t\t\t|     |      |       |      \n" +
              "\t\t\t|_____|      |       |______\n" )

    elif msg == "gameOver":
        os.system("aplay sound/gameOver.wav -q &")
        print("\t\t\t\t\t\t\t Score: ", SCORE[0])
        print("\t\t\t $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\        $$$$$$\  $$\    $$\ $$$$$$$$\ $$$$$$$\  \n" +
              "\t\t\t$$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|      $$  __$$\ $$ |   $$ |$$  _____|$$  __$$\ \n" +
              "\t\t\t$$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |            $$ /  $$ |$$ |   $$ |$$ |      $$ |  $$ |\n" +
              "\t\t\t$$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\          $$ |  $$ |\$$\  $$  |$$$$$\    $$$$$$$  |\n" +
              "\t\t\t$$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|         $$ |  $$ | \$$\$$  / $$  __|   $$  __$$< \n" +
              "\t\t\t$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |            $$ |  $$ |  \$$$  /  $$ |      $$ |  $$ |\n" +
              "\t\t\t\$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\        $$$$$$  |   \$  /   $$$$$$$$\ $$ |  $$ |\n" +
              "\t\t\t \______/ \__|  \__|\__|     \__|\________|       \______/     \_/    \________|\__|  \__|\n" )

    print("\n")

def Scoreboard(grid):
    grid[0][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"S"+ Style.RESET_ALL
    grid[0][1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"C"+ Style.RESET_ALL
    grid[0][2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"O"+ Style.RESET_ALL
    grid[0][3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"R"+ Style.RESET_ALL
    grid[0][4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
    grid[0][5] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
    grid[0][6] = int(SCORE[0])
    grid[1][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"L"+ Style.RESET_ALL
    grid[1][1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
    grid[1][2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"V"+ Style.RESET_ALL
    grid[1][3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
    grid[1][4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"S"+ Style.RESET_ALL
    grid[1][5] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
    grid[1][6] = int(LIVES[0])
    grid[1][144] = Fore.WHITE + Back.RED + Style.BRIGHT +"L"+ Style.RESET_ALL
    grid[1][145] = Fore.WHITE + Back.RED + Style.BRIGHT +"V"+ Style.RESET_ALL
    grid[1][146] = Fore.WHITE + Back.RED + Style.BRIGHT +"L"+ Style.RESET_ALL
    grid[1][147] = Fore.WHITE + Back.RED + Style.BRIGHT +":"+ Style.RESET_ALL
    grid[1][148] = int(LVL[0])
    grid[2][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"T"+ Style.RESET_ALL
    grid[2][1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
    grid[2][2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"M"+ Style.RESET_ALL
    grid[2][3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
    grid[2][4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
    grid[2][5] = int(time.time() - start_time)

    if LVL[0] == 3:
        grid[2][141] = Fore.WHITE + Back.GREEN + Style.BRIGHT +"H"+ Style.RESET_ALL
        grid[2][142] = Fore.WHITE + Back.GREEN + Style.BRIGHT +"E"+ Style.RESET_ALL
        grid[2][143] = Fore.WHITE + Back.GREEN + Style.BRIGHT +"A"+ Style.RESET_ALL
        grid[2][144] = Fore.WHITE + Back.GREEN + Style.BRIGHT +"L"+ Style.RESET_ALL
        grid[2][145] = Fore.WHITE + Back.GREEN + Style.BRIGHT +"T"+ Style.RESET_ALL
        grid[2][146] = Fore.WHITE + Back.GREEN + Style.BRIGHT +"H"+ Style.RESET_ALL
        grid[2][147] = Fore.WHITE + Back.GREEN + Style.BRIGHT +":"+ Style.RESET_ALL
        grid[2][148] = int(boss.getHealth())

# returns 1 if all lvls finished
def lvlUp():
    os.system("aplay sound/lvlUp.wav -q &")

    # removing bricks from prev lvl
    while len(obj1)!=0:
        obj1.remove(obj1[0])

    grid = bg.getGrid()
    for rows in range(3,41):
        for col in range(1,149):
            grid[rows][col] = ' '

    # powerup resets
    if fastBall[0]!=' ': fastBall[0].resetPowerup()
    if multiplyBall[0]!=' ': multiplyBall[0].resetPowerup()
    if paddleShrink[0]!=' ': paddleShrink[0].resetPowerup()
    if paddleExpand[0]!=' ': paddleExpand[0].resetPowerup()
    if thruBall[0]!=' ': thruBall[0].resetPowerup()
    if paddleGrab[0]!=' ': paddleGrab[0].resetPowerup()
    
    LVL[0]+=1
    if LVL[0] > 3:
        Message("gameOver")
        return 1
    elif LVL[0] == 2:
        generateBricks_lvl2(bg.getGrid())
    elif LVL[0] == 3:
        boss.placeBoss(bg.getGrid())
        generateBricks_lvl3(bg.getGrid())
    Scoreboard(bg.getGrid())
    return 0

os.system("clear")
while True:
    if time.time() - prev_time >= 0.1:
        prev_time = time.time()

        Scoreboard(bg.getGrid())
        paddle.placePaddle(bg.getGrid())
        if ball_launched[0] == 0:
            ball[0].placeAbovePaddle(paddle.getX(), bg.getGrid())
        else:
            for i in list(ball):
                i.moveBall(LIVES, ball_launched, bg.getGrid())

        # taking input
        letter = input_to()
        if letter == 'q':
            Message("q")
            break
        elif letter == 'a':
            paddle.movePaddle("a", bg.getGrid())
        elif letter == 'd':
            paddle.movePaddle("d", bg.getGrid())
        elif letter == 'w' and ball_launched[0] == 0:
            ball_launched[0] = 1
        # temporary for duplicative powerup
        elif letter == 'x':
            size = len(ball)
            for i in range(size):
                ball.append(duplicateBall(ball[i]))
        # lvl change
        elif letter == 'l':
            if lvlUp()==1: 
                break

        if fastBall[0] != ' ':
            fastBall[0].move(bg.getGrid())
            fastBall[0].update(ball)
            # print(fastBall[0].getActivated())
        if multiplyBall[0] != ' ':
            multiplyBall[0].move(bg.getGrid())
            multiplyBall[0].update()
            if multiplyBall[0]._changed == 0 and multiplyBall[0]._activated == 1:
                multiplyBall[0]._changed = 1
                for i in range(len(ball)):
                    ball.append(duplicateBall(ball[i]))

            # powerup time elapsed 
            if multiplyBall[0]._changed == 1 and multiplyBall[0]._activated == 0 and flag == 0:
                flag=1
                for i in range(len(ball)-1,0,-1):
                    grid = bg.getGrid()
                    grid[ball[i]._y][ball[i]._x] = ' '
                    ball.remove(ball[i])
        if paddleShrink[0] != ' ':
            paddleShrink[0].move(bg.getGrid())
            paddleShrink[0].update()
        # print(paddle_change[0])
        if paddleExpand[0] != ' ':
            paddleExpand[0].move(bg.getGrid())
            paddleExpand[0].update()
        if thruBall[0] != ' ':
            thruBall[0].move(bg.getGrid())
            thruBall[0].update(ball)
        if paddleGrab[0] != ' ':
            paddleGrab[0].move(bg.getGrid())
            paddleGrab[0].update()
        if fireBall[0] != ' ':
            fireBall[0].move(bg.getGrid())
            fireBall[0].update(ball)

        print("\033[%d;%dH" % (0, 0)) # position cursor at x across, y down

        bg.printGrid()

        # if all bricks broken then lvl up
        if len(obj1) == 0 and LVL[0]!=3:
            if lvlUp() == 1:
                break
        if LVL[0] == 3:
            boss.placeBoss(bg.getGrid())

        placeBricks(bg.getGrid())

        print(Style.RESET_ALL)

        if LIVES[0] <= 0:
            Message("gameOver")
            break