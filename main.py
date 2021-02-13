import os
import time
from colorama import *
from input import *
from background import *
from paddle import *
from ball import *

# Windows doesn't support ANSI coloring but Windows API does
# init() makes Windows API run these colors  
init()

# initialize variables
start_time = time.time()
prev_time = start_time
LIVES = [3]     # only object can be passed by reference
ROWS = 45
COLS = 150
ball_launched = [0]   # 1 = ball launched from paddle

def Message(msg):
    if msg == "q":
        print("\t\t\t _____                ______\n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|----|   |-------|   |----- \n" +
              "\t\t\t|     |      |       |      \n" +
              "\t\t\t|_____|      |       |______\n" )

    elif msg == "gameOver":
        print("\t\t\t $$$$$$\   $$$$$$\  $$\      $$\ $$$$$$$$\        $$$$$$\  $$\    $$\ $$$$$$$$\ $$$$$$$\  \n" +
              "\t\t\t$$  __$$\ $$  __$$\ $$$\    $$$ |$$  _____|      $$  __$$\ $$ |   $$ |$$  _____|$$  __$$\ \n" +
              "\t\t\t$$ /  \__|$$ /  $$ |$$$$\  $$$$ |$$ |            $$ /  $$ |$$ |   $$ |$$ |      $$ |  $$ |\n" +
              "\t\t\t$$ |$$$$\ $$$$$$$$ |$$\$$\$$ $$ |$$$$$\          $$ |  $$ |\$$\  $$  |$$$$$\    $$$$$$$  |\n" +
              "\t\t\t$$ |\_$$ |$$  __$$ |$$ \$$$  $$ |$$  __|         $$ |  $$ | \$$\$$  / $$  __|   $$  __$$< \n" +
              "\t\t\t$$ |  $$ |$$ |  $$ |$$ |\$  /$$ |$$ |            $$ |  $$ |  \$$$  /  $$ |      $$ |  $$ |\n" +
              "\t\t\t\$$$$$$  |$$ |  $$ |$$ | \_/ $$ |$$$$$$$$\        $$$$$$  |   \$  /   $$$$$$$$\ $$ |  $$ |\n" +
              "\t\t\t \______/ \__|  \__|\__|     \__|\________|       \______/     \_/    \________|\__|  \__|\n" )

    print("\n")

def Scoreboard():
    bg.grid[0][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"S"+ Style.RESET_ALL
    bg.grid[0][1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"C"+ Style.RESET_ALL
    bg.grid[0][2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"O"+ Style.RESET_ALL
    bg.grid[0][3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"R"+ Style.RESET_ALL
    bg.grid[0][4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
    bg.grid[0][5] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
    
    bg.grid[1][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"L"+ Style.RESET_ALL
    bg.grid[1][1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
    bg.grid[1][2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"V"+ Style.RESET_ALL
    bg.grid[1][3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
    bg.grid[1][4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"S"+ Style.RESET_ALL
    bg.grid[1][5] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
    bg.grid[1][6] = int(LIVES[0])
    
    bg.grid[2][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"T"+ Style.RESET_ALL
    bg.grid[2][1] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"I"+ Style.RESET_ALL
    bg.grid[2][2] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"M"+ Style.RESET_ALL
    bg.grid[2][3] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"E"+ Style.RESET_ALL
    bg.grid[2][4] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +":"+ Style.RESET_ALL
    bg.grid[2][5] = int(time.time() - start_time)

os.system("clear")
while True:
    if time.time() - prev_time >= 0.1:
        prev_time = time.time()

        Scoreboard()
        paddle.placePaddle()
        if ball_launched[0] == 0:
            ball[0].placeAbovePaddle(paddle.getX())
        else:
            for i in list(ball):
                i.moveBall(LIVES, ball_launched)

        # taking input
        letter = input_to()
        if letter == 'q':
            Message("q")
            break
        elif letter == 'a':
            paddle.movePaddle("a")
        elif letter == 'd':
            paddle.movePaddle("d")
        elif letter == 'w' and ball_launched[0] == 0:
            ball_launched[0] = 1
        # temporary for duplicative powerup
        elif letter == 'x':
            size = len(ball)
            for i in range(size):
                ball.append(duplicateBall(ball[i]))
        
        print("\033[%d;%dH" % (0, 0)) # position cursor at x across, y down

        for i in range(ROWS):
            for j in range(0, COLS + 0):
                print(bg.grid[i][j], end = "")
            print()

        print(Style.RESET_ALL)

        if LIVES[0] <= 0:
            Message("gameOver")
            break