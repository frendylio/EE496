import sys

class PieceType:
    Empty = 0
    Tiger = 1
    Goat = 2
    Invalid = -1
    OutOfBounds = -1 

class Orientation:
    Up = 0
    Right = 1
    Down = 2
    Left = 3

class Coordinates: 

     def __init__(self, x, y):
        self.x = x
        self.y = y

class Location:

    # First row
    Location_1 = Coordinates(0,3)
    # Second Row
    Location_2 = Coordinates(1,0)
    Location_3 = Coordinates(1,1)
    Location_4 = Coordinates(1,2)
    Location_5 = Coordinates(1,4)
    Location_6 = Coordinates(1,5)
    Location_7 = Coordinates(1,6)
    # Third Row
    Location_8 = Coordinates(2,0)
    Location_9 = Coordinates(2,1)
    Location_10 = Coordinates(2,2)
    Location_11 = Coordinates(2,4)
    Location_12 = Coordinates(2,5)
    Location_13 = Coordinates(2,6)    
    # 4 Row
    Location_14 = Coordinates(3,0)
    Location_15 = Coordinates(3,1)
    Location_16 = Coordinates(3,2)
    Location_17 = Coordinates(3,4)
    Location_18 = Coordinates(3,5)
    Location_19 = Coordinates(3,6) 
     # 5 Row
    Location_20 = Coordinates(4,1)
    Location_21 = Coordinates(4,2)
    Location_22 = Coordinates(4,4)
    Location_23 = Coordinates(4,5)

    def getLocation(self, number):
        if number == 1:
            return self.Location_1
        elif number == 2:
            return self.Location_2
        elif number == 3:
            return self.Location_3
        elif number == 4:
            return self.Location_4            
        elif number == 5:
            return self.Location_5
        elif number == 6:
            return self.Location_6
        elif number == 7:
            return self.Location_7    
        elif number == 8:
            return self.Location_8
        elif number == 9:
            return self.Location_9
        elif number == 10:
            return self.Location_10    
        elif number == 11:
            return self.Location_11
        elif number == 12:
            return self.Location_12
        elif number == 13:
            return self.Location_13    
        elif number == 14:
            return self.Location_14
        elif number == 15:
            return self.Location_15    
        elif number == 16:
            return self.Location_16
        elif number == 17:
            return self.Location_17
        elif number == 18:
            return self.Location_18 
        elif number == 19:
            return self.Location_19
        elif number == 20:
            return self.Location_20    
        elif number == 21:
            return self.Location_21
        elif number == 22:
            return self.Location_22
        elif number == 23:
            return self.Location_23
        else:
            return -1             
class Piece:
    
    # :O Looks like in Python, you cannot have multiple Constructor
    # But you can pass a default parameter
    def __init__(self, PieceType, Number = 0, Location = Location.Location_1):
        self.Piece = PieceType
        self.Location = Location
        self.Number = Number

    def getNumber(self):
        return self.Number
