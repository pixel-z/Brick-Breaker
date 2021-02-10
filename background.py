"""Class to get background"""
from colorama import *

init()

class Background:
    def __init__(self, rows, columns):
        self.grid = [[' ' for i in range(columns)] for j in range(rows)]
        self.rows = rows
        self.columns = columns

        # Upper border
        for j in range(0, columns - 2, 3):
            self.grid[0][j] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.grid[0][j + 1] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"|" +Style.RESET_ALL
            self.grid[0][j + 2] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL

            self.grid[1][j] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.grid[1][j + 1] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"_" +Style.RESET_ALL
            self.grid[1][j + 2] = Fore.WHITE + Back.BLUE + Style.BRIGHT +"|" +Style.RESET_ALL

        # Lower border
        for j in range(columns):
            self.grid[rows - 3][j] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT +"-"+ Style.RESET_ALL
        for j in range(0,columns):
            self.grid[rows - 2][j] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT +"T"+ Style.RESET_ALL

            self.grid[rows - 1][j] = Fore.WHITE + Back.LIGHTBLACK_EX + Style.BRIGHT +"T"+ Style.RESET_ALL

