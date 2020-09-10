import sys

from board import Board
from colorama import init, Fore, Style
from utility import Location

init(convert=True)
#####
# Variables
#####
Game_board = Board()
TempLocation = Location()
CurrentLocation = TempLocation.Location_1
MovingLocation = TempLocation.Location_1
Data = 0
GoatKillLimit = 6

while(True):

    if Game_board.getNumberOfDeadGoat() >= GoatKillLimit:
        Game_board.PrintBoard()
        print(f'{Fore.GREEN}', end="")
        print("======================================")
        print("              Tiger player wins!   ")
        print("======================================")  
        print(f'{Style.RESET_ALL}', end="")    
        break


    ##################
    # Goat Player
    ##################
    while(True):

        print(f'{Fore.BLUE}', end="")
        print("======================================")
        print("              Goat   ")
        print(" Number of Goats placed: " + str(Game_board.getNumberOfGoats()))
        print(" Number of Goats Killed: " + str(Game_board.getNumberOfDeadGoat()))
        print("======================================")  
        print(f'{Style.RESET_ALL}', end="")  
        
        # Board
        Game_board.PrintBoard()

        if Game_board.getNumberOfGoats() == 15:  
            while(True):
                try:
                    Data = int(input("Current Piece moving: "))
                except ValueError:
                    print("That's not a Location!") 
                if Data > 23 or Data < 1:
                    print("Not valid location")
                else:
                    CurrentLocation = TempLocation.getLocation(Data)
                    break    

        while(True):
            try:
                Data = int(input("Where do you want to move: "))
            except ValueError:
                print("That's not a Location!") 
            if Data > 23 or Data < 1:
                print("Not valid location")                
            else:
                MovingLocation = TempLocation.getLocation(Data)
                break             

        if(Game_board.PlayGoat(CurrentLocation, MovingLocation) == 1):
            break

    if Game_board.StaleMate() == 1:
        Game_board.PrintBoard()
        print(f'{Fore.GREEN}', end="")
        print("======================================")
        print("              Goat player wins!   ")
        print("======================================")  
        print(f'{Style.RESET_ALL}', end="")    
        break

    ##################
    # Tiger Player
    ##################15
    while(True):
        print(f'{Fore.RED}', end="")
        print("======================================")
        print("              TIGER   ")
        print("======================================")  
        print(f'{Style.RESET_ALL}', end="")  
        Game_board.PrintBoard()
        
        while(True):
            try:
                Data = int(input("Current Piece moving: "))
            except ValueError:
                print("That's not a Location!") 
            if Data > 23 or Data < 1:
                print("Not valid location")
            else:
                CurrentLocation = TempLocation.getLocation(Data)
                break    

        while(True):
            try:
                Data = int(input("Where do you want to move: "))
            except ValueError:
                print("That's not a Location!") 
            if Data > 23 or Data < 1:
                print("Not valid location")                
            else:
                MovingLocation = TempLocation.getLocation(Data)
                break             

        if(Game_board.PlayTiger(CurrentLocation, MovingLocation) == 1):
            break        