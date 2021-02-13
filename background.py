"""Class to get background"""
from colorama import *

init()
ROWS = 45
COLS = 150

class Background:
    def __init__(self, rows, columns):
        self.__grid = [[' ' for i in range(columns)] for j in range(rows)]
        self.__rows = rows
        self.__columns = columns

        # Upper border
        for j in range(0, columns - 2, 3):
            self.__grid[0][j] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.__grid[0][j + 1] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"|" +Style.RESET_ALL
            self.__grid[0][j + 2] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL

            self.__grid[1][j] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.__grid[1][j + 1] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.__grid[1][j + 2] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"|" +Style.RESET_ALL

            self.__grid[2][j] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.__grid[2][j + 1] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.__grid[2][j + 2] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"|" +Style.RESET_ALL
        
        # Lower border
        for j in range(0,columns):
            self.__grid[rows - 2][j] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT +"T"+ Style.RESET_ALL

            self.__grid[rows - 1][j] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT +"T"+ Style.RESET_ALL

        # Left & Right borders
        for j in range(3,rows-2):
            self.__grid[j][0] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT + "|" + Style.RESET_ALL
            self.__grid[j][149] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT + "|" + Style.RESET_ALL

    def printGrid(self):
        for i in range(ROWS):
            for j in range(0, COLS + 0):
                print(self.__grid[i][j], end = "")
            print()

    def getGrid(self):
        return self.__grid

bg = Background(45,150)
