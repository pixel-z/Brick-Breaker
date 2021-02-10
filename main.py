import os
import time
from colorama import *
from input import *
from background import *

# Windows doesn't support ANSI coloring but Windows API does
# init() makes Windows API run these colors  
init()

# initialize variables
start_time = time.time()
prev_time = start_time
LIVES = 3
ROWS = 45
COLS = 150
bg = Background(ROWS,COLS)

def Message(msg):
    if msg == "q":
        print("\t\t\t _____                ______\n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|----|   |-------|   |----- \n" +
              "\t\t\t|     |      |       |      \n" +
              "\t\t\t|_____|      |       |______\n" )
    print("\n")

def Scoreboard():
    bg.grid[0][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"SCORE: "+ Style.RESET_ALL
    
    bg.grid[1][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"LIVES: "+ Style.RESET_ALL
    bg.grid[1][1] = int(LIVES)
    
    bg.grid[2][0] = Fore.WHITE + Back.MAGENTA + Style.BRIGHT +"Timer: "+ Style.RESET_ALL
    bg.grid[2][1] = int(time.time() - start_time)

os.system("clear")
while True:
    if time.time() - prev_time >= 0.1:
        prev_time = time.time()

        Scoreboard()

        # taking input
        letter = input_to()
        if letter == 'q':
            Message("q")
            break

        print("\033[%d;%dH" % (0, 0)) # position cursor at x across, y down

        for i in range(ROWS):
            for j in range(0, COLS + 0):
                print(bg.grid[i][j], end = "")
            print()

        print(Style.RESET_ALL)
