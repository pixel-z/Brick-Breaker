import os
import time
from colorama import *
from input import *
from background import *

# Windows doesn't support ANSI coloring but Windows API does
# init() makes Windows API run these colors  
init()

# initialize variables
prev_time = time.time()
ROWS = 45
COLS = 150
bg = background(ROWS,COLS)

def Message(msg):
    if msg == "q":
        print("\t\t\t _____                ______\n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|     |  |       |   |      \n" +
              "\t\t\t|----|   |-------|   |----- \n" +
              "\t\t\t|     |      |       |      \n" +
              "\t\t\t|_____|      |       |______\n" )
    print("\n")

os.system("clear")
while True:
    if time.time() - prev_time >= 0.1:
        prev_time = time.time()

        letter = input_to()
        if letter == 'q':
            Message("q");
            break

        print("\033[%d;%dH" % (0, 0))
        print(Fore.WHITE)

        for i in range(ROWS):
            for j in range(0, COLS + 0):
                print(bg.grid[i][j], end = "")
            print()
        print("\033[%d;%dH" % (0, 0))  # position cursor at x across, y down


        
        print(Style.RESET_ALL)
