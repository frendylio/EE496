import sys

from utility import PieceType, Orientation, Piece, Location
from colorama import Fore, Style

#####
## -1 = Error
## 0 = False
## 1 = True
#####


class Board:
    
    # Variables
    Invalid = Piece(PieceType.Invalid)

    Empty_1 = Piece(PieceType.Empty,2, Location.Location_2)
    Empty_2 = Piece(PieceType.Empty,3, Location.Location_3)
    Empty_3 = Piece(PieceType.Empty,6, Location.Location_6)
    Empty_4 = Piece(PieceType.Empty,7, Location.Location_7)
    Empty_5 = Piece(PieceType.Empty,8, Location.Location_8)
    Empty_6 = Piece(PieceType.Empty,9, Location.Location_9)
    Empty_7 = Piece(PieceType.Empty,10, Location.Location_10)
    Empty_8 = Piece(PieceType.Empty,11, Location.Location_11)
    Empty_9 = Piece(PieceType.Empty,12, Location.Location_12)
    Empty_10 = Piece(PieceType.Empty,13, Location.Location_13)
    Empty_11 = Piece(PieceType.Empty,14, Location.Location_14)
    Empty_12 = Piece(PieceType.Empty,15, Location.Location_15)    
    Empty_13 = Piece(PieceType.Empty,16, Location.Location_16)
    Empty_14 = Piece(PieceType.Empty,17, Location.Location_17)
    Empty_15 = Piece(PieceType.Empty,18, Location.Location_18)
    Empty_16 = Piece(PieceType.Empty,19, Location.Location_19)
    Empty_17 = Piece(PieceType.Empty,20, Location.Location_20)   
    Empty_18 = Piece(PieceType.Empty,21, Location.Location_21)
    Empty_19 = Piece(PieceType.Empty,22, Location.Location_22)
    Empty_20 = Piece(PieceType.Empty,23, Location.Location_23)  


    # Empty_1 = Piece(PieceType.Goat,2, Location.Location_2)
    # Empty_2 = Piece(PieceType.Goat,3, Location.Location_3)
    # Empty_3 = Piece(PieceType.Goat,6, Location.Location_6)
    # Empty_4 = Piece(PieceType.Goat,7, Location.Location_7)
    # Empty_5 = Piece(PieceType.Empty,8, Location.Location_8)
    # Empty_6 = Piece(PieceType.Goat,9, Location.Location_9)
    # Empty_7 = Piece(PieceType.Goat,10, Location.Location_10)
    # Empty_8 = Piece(PieceType.Goat,11, Location.Location_11)
    # Empty_9 = Piece(PieceType.Goat,12, Location.Location_12)
    # Empty_10 = Piece(PieceType.Empty,13, Location.Location_13)
    # Empty_11 = Piece(PieceType.Empty,14, Location.Location_14)
    # Empty_12 = Piece(PieceType.Empty,15, Location.Location_15)    
    # Empty_13 = Piece(PieceType.Goat,16, Location.Location_16)
    # Empty_14 = Piece(PieceType.Goat,17, Location.Location_17)
    # Empty_15 = Piece(PieceType.Goat,18, Location.Location_18)
    # Empty_16 = Piece(PieceType.Empty,19, Location.Location_19)
    # Empty_17 = Piece(PieceType.Empty,20, Location.Location_20)   
    # Empty_18 = Piece(PieceType.Empty,21, Location.Location_21)
    # Empty_19 = Piece(PieceType.Empty,22, Location.Location_22)
    # Empty_20 = Piece(PieceType.Empty,23, Location.Location_23)      

    Tiger_1 = Piece(PieceType.Tiger, 1, Location.Location_1)
    Tiger_2 = Piece(PieceType.Tiger, 4, Location.Location_4)
    Tiger_3 = Piece(PieceType.Tiger, 5, Location.Location_5)
    NumberOfGoats = 0
    DeadGoats = 0
    # Constructor
    def __init__(self):
        self.board = [
            [self.Invalid  ,self.Invalid  ,self.Invalid  ,self.Tiger_1 ,self.Invalid  ,self.Invalid  ,self.Invalid],
            [self.Empty_1  ,self.Empty_2  ,self.Tiger_2  ,self.Invalid ,self.Tiger_3  ,self.Empty_3  ,self.Empty_4],
            [self.Empty_5  ,self.Empty_6  ,self.Empty_7  ,self.Invalid ,self.Empty_8  ,self.Empty_9  ,self.Empty_10],
            [self.Empty_11 ,self.Empty_12 ,self.Empty_13 ,self.Invalid ,self.Empty_14 ,self.Empty_15 ,self.Empty_16],
            [self.Invalid  ,self.Empty_17 ,self.Empty_18 ,self.Invalid ,self.Empty_19 ,self.Empty_20 ,self.Invalid]
        ]

    # Print Board Function
    def PrintBoard(self):
        counter = 1
        for i in range(0,5):
            for y in self.board[i]:
                Piece = y.Piece
                Number = str(y.getNumber())
                # Invalid
                if Piece == PieceType.Invalid:
                    print(f'{Fore.BLACK}', end="")
                    print(' X ', end="     ")
                    print(f'{Style.RESET_ALL}', end="")
                # Tiger
                elif Piece == PieceType.Tiger:
                    print(f'{Fore.RED}', end="")
                    print('T_' + Number, end="     ")
                    print(f'{Style.RESET_ALL}', end="")
                    counter = counter + 1
                # Goat
                elif Piece == PieceType.Goat:
                    print(f'{Fore.BLUE}', end="")
                    if(y.getNumber() >= 10):
                        print('G_' + Number, end="    ")
                    else:
                        print('G_' + Number, end="     ")
                    print(f'{Style.RESET_ALL}', end="")
                    counter = counter + 1
                #Else
                else:
                    # This is for display
                    print(f'{Fore.GREEN}', end="")
                    if(counter >= 10):
                        print(' ' + str(counter), end="     ")
                    else:
                        print(' ' + str(counter) + ' ', end="     ")
                    print(f'{Style.RESET_ALL}', end="")
                    counter = counter + 1

            print('')

    # Get Type of Piece
    def getTypeOfPiece(self,location):
        if(location.x < 0 or location.x > 4):
            return -1
        if(location.y < 0 or location.y > 6):
            return -1

        try:
            CurrentLocationValue = self.board[location.x][location.y].Piece
        except IndexError:
            return -1

        return CurrentLocationValue
    
    def getNumberOfGoats(self):
        return self.NumberOfGoats

    def getNumberOfDeadGoat(self):
        return self.DeadGoats

    def setTypeOfPiece(self,pieceType, location):
        self.board[location.x][location.y].Piece = pieceType
        self.board[location.x][location.y].Location = location

    # How many blocks
    def HowManyBlocksYouMoving(self, currentLocation , movingLocation):
        # Outputs 2, 1 or -1 (Error), -2 (Tiger jump from origin success)

        Moving_x = abs(currentLocation.x - movingLocation.x)
        Moving_y = abs(currentLocation.y - movingLocation.y)

        #Substract for the middle line
        if(
            # Jump going - >
            (
                    (currentLocation.y == 1 or currentLocation.y == 2)  
                and (movingLocation.y == 4 or movingLocation.y == 5)

            ) or 
            # Jump going < -
            (
                    (movingLocation.y == 1 or movingLocation.y == 2)  
                and (currentLocation.y == 4 or currentLocation.y == 5)                
            )
        ):
            Moving_y = Moving_y - 1
        

        #############
        # From origin
        #############
        if(currentLocation == Location.Location_1):
            # Row 1 
            if(
                    movingLocation == Location.Location_3 
                or  movingLocation == Location.Location_4 
                or  movingLocation == Location.Location_5
                or  movingLocation == Location.Location_6
            ):
                return 1
            
            # Since you can only do 2 for Tiger only, lets just check if this is a jump or not
            # Row 2
            elif(
                    (movingLocation == Location.Location_9 and self.board[Location.Location_3.x][Location.Location_3.y].Piece == PieceType.Goat) 
                or  (movingLocation == Location.Location_10 and self.board[Location.Location_4.x][Location.Location_4.y].Piece == PieceType.Goat) 
                or  (movingLocation == Location.Location_11 and self.board[Location.Location_5.x][Location.Location_5.y].Piece == PieceType.Goat) 
                or  (movingLocation == Location.Location_12 and self.board[Location.Location_6.x][Location.Location_6.y].Piece == PieceType.Goat) 
            ):
                return -2
            else:
                return -1

        #############
        # To the origin
        #############
        if(movingLocation == Location.Location_1):
            # Row 1 
            if(
                    currentLocation == Location.Location_3 
                or  currentLocation == Location.Location_4 
                or  currentLocation == Location.Location_5
                or  currentLocation == Location.Location_6
            ):
                return 1
            
            # Since you can only do 2 for Tiger only, lets just check if this is a jump or not
            # Row 2
            elif(
                    (currentLocation == Location.Location_9 and self.board[Location.Location_3.x][Location.Location_3.y].Piece  == PieceType.Goat) 
                or  (currentLocation == Location.Location_10 and self.board[Location.Location_4.x][Location.Location_4.y].Piece  == PieceType.Goat) 
                or  (currentLocation == Location.Location_11 and self.board[Location.Location_5.x][Location.Location_5.y].Piece  == PieceType.Goat) 
                or  (currentLocation == Location.Location_12 and self.board[Location.Location_6.x][Location.Location_6.y].Piece  == PieceType.Goat) 
            ):
                return -2 # Indicator that is the origin and we did check.
            else:
                return -1

        #############
        # Else
        #############        
        else:
            # You can only move horizontally or vertically, not both
            if(Moving_x != 0 and Moving_y != 0):
                return -1
            elif(Moving_x != 0):
                return Moving_x
            else:
                return Moving_y

        return 0

    #######################################################
    # Check if your move is valid
    #######################################################                       
    def IsValidMove(self, currentLocation, movingLocation):

        CurrentPieceType = self.getTypeOfPiece(currentLocation)
        MovingPieceType = self.getTypeOfPiece(movingLocation)
        MiddleLocation = Location.Location_1
        NumberOfBlocks = self.HowManyBlocksYouMoving(currentLocation, movingLocation)

        ###################
        ## Check if the number Of blocks is correct
        ###################
        if(NumberOfBlocks == -1):
            print("ERROR: Invalid Move")
            return 0

        ###################
        ## Check if the Piece is goat or tiger
        ###################
        if(CurrentPieceType == PieceType.Goat or CurrentPieceType == PieceType.Tiger):
            pass
        else:
            print("ERROR: Invalid Piece to Move")
            return 0

        ###################
        ## Check if there is a piece to the place you moving
        ###################
        if(MovingPieceType != PieceType.Empty and CurrentPieceType == PieceType.Goat):
            print("ERROR: There is a piece there already")
            return 0

        #####################
        # Goat
        #####################
        # Can only move one block at that time
        if(CurrentPieceType == PieceType.Goat):

            if(NumberOfBlocks != 1):
                print("ERROR: Invalid Goat Move")
                return 0            
        
        #####################
        # Tiger
        #####################
        # Jump(eating)
        # 1 or 2 blocks move
        else:
            if MovingPieceType != PieceType.Empty:
                print("ERROR: Moving to a location that is not empty or unable to eat goat")
                return 0

            # If 1 block
            if (NumberOfBlocks == 1):
                pass

            # 2 blocks
            elif NumberOfBlocks == 2:
                
                #############
                ## Horizontal Eating
                ############
                if(currentLocation.x == movingLocation.x):
                    ################################
                    # from a to c -> or c to a <-
                    ################################
                    if (currentLocation.y == 0 or movingLocation.y == 0):
                        MiddleLocation.x = movingLocation.x 
                        MiddleLocation.y = 1
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                            self.DeadGoats = self.DeadGoats + 1

                    ################################
                    # from b to d -> or d to b <-
                    ################################
                    elif (currentLocation.y == 1 or movingLocation.y == 1):
                        MiddleLocation.x = movingLocation.x 
                        MiddleLocation.y = 2                    
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                            self.DeadGoats = self.DeadGoats + 1

                    ################################
                    # from c to e -> or e to c <-
                    ################################
                    elif (currentLocation.y == 5 or movingLocation.y == 5):
                        MiddleLocation.x = movingLocation.x 
                        MiddleLocation.y = 4                           
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                            self.DeadGoats = self.DeadGoats + 1

                    ################################
                    # from d to f -> or f to d <-
                    ################################
                    elif (currentLocation.y == 6 or movingLocation.y == 6):
                        MiddleLocation.x = movingLocation.x 
                        MiddleLocation.y = 5                           
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                            self.DeadGoats = self.DeadGoats + 1
                    else:
                        return 0

                ################################
                # Vertical eating (Ignore Origin case)
                ################################
                elif (currentLocation.y == movingLocation.y):
                    # row 1 -> 3
                    if(currentLocation.x == 1 or movingLocation.x == 3):
                        MiddleLocation.x = 2 
                        MiddleLocation.y = movingLocation.y                           
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation) 
                            self.DeadGoats = self.DeadGoats + 1   

                    # row 2 -> 4
                    elif(currentLocation.x == 2 or movingLocation.x == 4) and movingLocation.y != 0 and movingLocation.y != 6:
                        MiddleLocation.x = 3 
                        MiddleLocation.y = movingLocation.y                           
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)  
                            self.DeadGoats = self.DeadGoats + 1      

                    # row 3 -> 1
                    elif(currentLocation.x == 3 or movingLocation.x == 1):
                        MiddleLocation.x = 2 
                        MiddleLocation.y = movingLocation.y                           
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                            self.DeadGoats = self.DeadGoats + 1    

                    # row 4 -> 2
                    elif(currentLocation.x == 4 or movingLocation.x == 2) and movingLocation.y != 0 and movingLocation.y != 6:
                        MiddleLocation.x = 3 
                        MiddleLocation.y = movingLocation.y                           
                        MiddlePieceType = self.getTypeOfPiece(MiddleLocation)

                        if(MiddlePieceType != PieceType.Goat):
                            return 0
                        else:
                            # clean location
                            self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                            self.DeadGoats = self.DeadGoats + 1     
                    else:
                        return 0                                                                   

                else:
                    return 0

            #  origin
            elif NumberOfBlocks == -2:
                # Going out from origin
                if(currentLocation == Location.Location_1):
                    if(movingLocation == Location.Location_9):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 1                            
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                        self.DeadGoats = self.DeadGoats + 1

                    elif(movingLocation == Location.Location_10):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 2                           
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                        self.DeadGoats = self.DeadGoats + 1

                    elif(movingLocation == Location.Location_11):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 4                           
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)   
                        self.DeadGoats = self.DeadGoats + 1                         

                    elif(movingLocation == Location.Location_12):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 5                           
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                        self.DeadGoats = self.DeadGoats + 1  
                    
                    else:
                        print("ERROR: Type: -2")
                        return 0
                # Going to origin
                if(movingLocation == Location.Location_1):
                    if(currentLocation == Location.Location_9):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 1                            
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                        self.DeadGoats = self.DeadGoats + 1

                    elif(currentLocation == Location.Location_10):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 2                           
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)
                        self.DeadGoats = self.DeadGoats + 1

                    elif(currentLocation == Location.Location_11):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 4                           
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation)  
                        self.DeadGoats = self.DeadGoats + 1                          

                    elif(currentLocation == Location.Location_12):
                        MiddleLocation.x = 1 
                        MiddleLocation.y = 5                           
                        self.setTypeOfPiece(PieceType.Empty,MiddleLocation) 
                        self.DeadGoats = self.DeadGoats + 1 
                    
                    else:
                        print("ERROR: Type: -2")
                        return 0

                # Check if you can eat Goat
                # At this point, we can forget about the Origin since we check it above, NumberOfBlocks == -2
            else:
                print("ERROR: Invalid Tiger Move")
                return 0

        # Reset Location, For some reason it was breaking??
        Location().Location_1.x = 0
        Location().Location_1.y = 3
        return 1

    #######################################################
    # Goat
    ####################################################### 
    def MoveGoat(self, currentLocation, movingLocation):
        CurrentPiece = self.getTypeOfPiece(currentLocation)

        if currentLocation == movingLocation:
            print("ERROR: You are not moving your Goat, is at the same location")
            return 0

        if CurrentPiece != PieceType.Goat:
            print("ERROR: You are not moving a Goat")
            return 0

        if self.NumberOfGoats != 15:
            print("ERROR: You have not placed all your Goats.")
            return 0
        
        if self.IsValidMove(currentLocation, movingLocation) == 0:
            print("ERROR: Invalid move.")
            return 0

        self.setTypeOfPiece(PieceType.Empty, currentLocation)
        self.setTypeOfPiece(PieceType.Goat, movingLocation)
        return 1

    def PlaceGoat(self, location):
        if self.getTypeOfPiece(location) != PieceType.Empty:
            print("ERROR: This location is not empty")
            return 0

        else:
            self.setTypeOfPiece(PieceType.Goat, location)
            self.NumberOfGoats = self.NumberOfGoats + 1
            return 1
    
    def PlayGoat(self, currentLocation, movingLocation):
        if self.NumberOfGoats != 15:
            return self.PlaceGoat(movingLocation)
        else:
            return self.MoveGoat(currentLocation, movingLocation)

    #######################################################
    # Tiger
    ####################################################### 
    def MoveTiger(self, currentLocation, movingLocation):
        CurrentPiece = self.getTypeOfPiece(currentLocation)
        IsValidMove = self.IsValidMove(currentLocation, movingLocation)

        if currentLocation == movingLocation:
            print("ERROR: You are not moving your Tiger, is at the same location")
            return 0

        if CurrentPiece != PieceType.Tiger:
            print("ERROR: You are not moving a Tiger")
            return 0

        if IsValidMove == 0:
            print("ERROR: Invalid move.")
            return 0

        self.setTypeOfPiece(PieceType.Empty, currentLocation)
        self.setTypeOfPiece(PieceType.Tiger, movingLocation)
        return 1

    def PlayTiger(self, currentLocation, movingLocation):
        return self.MoveTiger(currentLocation, movingLocation)

    #######################################################
    # StaleMate
    #######################################################
    def HelperCheckEmpty(self,location):
        # Going to origin
        if(location.x == 0) and (
                location.y == 1
            or  location.y == 2
            or  location.y == 4
            or  location.y == 5
        ):
            originLocation = Location()
            originLocation.x = 0
            originLocation.y = 3
            if(self.getTypeOfPiece(originLocation) == PieceType.Empty):
                return True            
            else:
                return False


        try:
            Piece = self.getTypeOfPiece(location)
            if(Piece == PieceType.Empty):
                return True
            else:
                return False
        except IndexError:
            return False
        else:
            return False

    def HelperStaleMate(self, location):

        checkLocation = Location()
        check = True

        #################
        # Check left
        #################
        checkLocation.x = location.x

        # Jump from d -> c
        if(location.y == 4):
            checkLocation.y = location.y - 2
        else:
            checkLocation.y = location.y - 1

        check = self.HelperCheckEmpty(checkLocation)

        if(check == True):
            return 0

        checkLocation.x = location.x
        # Jump from d -> b
        if(location.y == 4 or location.y == 5 ):
            checkLocation.y = location.y - 3
        else:
            checkLocation.y = location.y - 2

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0     

        
        #################
        # Check Right
        #################               
        checkLocation.x = location.x
        # jump from c -> d
        if(location.y == 2):
            checkLocation.y = location.y + 2
        else:
            checkLocation.y = location.y + 1

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0
        
        checkLocation.x = location.x
        # jump from c -> e
        if(location.y == 2 or location.y == 1):
            checkLocation.y = location.y + 3
        else:
            checkLocation.y = location.y + 2

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0   
        
        #################
        # Check Up
        #################               
        checkLocation.x = location.x + 1
        checkLocation.y = location.y

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0
        
        checkLocation.x = location.x + 2
        checkLocation.y = location.y

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0     
    
        #################
        # Check Down
        #################               
        checkLocation.x = location.x - 1
        checkLocation.y = location.y

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0
        
        checkLocation.x = location.x - 2
        checkLocation.y = location.y

        check = self.HelperCheckEmpty(checkLocation)
        if(check == True):
            return 0  
        
        return 1                          

    def HelperStaleMateOrigin(self, location):
        if(location == Location.Location_1):
            if(self.getTypeOfPiece(Location.Location_3) == PieceType.Empty or self.getTypeOfPiece(Location.Location_9) == PieceType.Empty):
                return 0
            if(self.getTypeOfPiece(Location.Location_4) == PieceType.Empty or self.getTypeOfPiece(Location.Location_10) == PieceType.Empty):
                return 0
            if(self.getTypeOfPiece(Location.Location_5) == PieceType.Empty or self.getTypeOfPiece(Location.Location_11) == PieceType.Empty):
                return 0
            if(self.getTypeOfPiece(Location.Location_6) == PieceType.Empty or self.getTypeOfPiece(Location.Location_12) == PieceType.Empty):
                return 0
            return 1
        
        return 0

    def PrintLocation(self,location):
        print("=========Location===========")
        print(location.x)
        print(location.y)     

    def StaleMate(self):
        foundTiger_1 = False
        foundTiger_2 = False
        foundTiger_3 = False

        ###
        # Find Tigers
        ###
        for i in range(0,5):

            if(foundTiger_1 == True and foundTiger_2 == True and foundTiger_3 == True):
                break

            for y in self.board[i]:
                if (y.Piece == PieceType.Tiger and foundTiger_1 == False):
                    Tiger_1 = y.Location
                    foundTiger_1 = True
                elif (y.Piece == PieceType.Tiger and foundTiger_2 == False):
                    Tiger_2 = y.Location
                    foundTiger_2 = True                    
                elif (y.Piece == PieceType.Tiger and foundTiger_3 == False):
                    Tiger_3 = y.Location
                    foundTiger_2 = True      
                
                if(foundTiger_1 == True and foundTiger_2 == True and foundTiger_3 == True):
                    break

        # print(self.HelperStaleMate(Tiger_1))
        # print(self.HelperStaleMate(Tiger_2))
        # print(self.HelperStaleMate(Tiger_3))

        # print(self.HelperStaleMate(Tiger_2))
        # print(self.HelperStaleMate(Tiger_2))
        # print(self.HelperStaleMate(Tiger_3))        
        #######
        # Check Tigers
        #######
        # Going to origin check
        if self.HelperStaleMateOrigin(Tiger_1) == 0 and Tiger_1 == Location.Location_1:
            return 0
        elif self.HelperStaleMateOrigin(Tiger_2) == 0 and Tiger_2 == Location.Location_1:
            return 0
        elif self.HelperStaleMateOrigin(Tiger_3) == 0 and Tiger_3 == Location.Location_1:
            return 0
        
        if( 
                self.HelperStaleMate(Tiger_1) == 1
            and self.HelperStaleMate(Tiger_2) == 1   
            and self.HelperStaleMate(Tiger_3) == 1 
            ):
            return 1
        else:
            return 0
        
