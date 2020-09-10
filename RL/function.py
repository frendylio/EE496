import sys
from utility import PieceType, Orientation, Piece, Location
from board import Board

def getAllPossibleTigerLocations():
    list = []
    listTemp = [0,0,0]
    i = 1
    j = 2 
    k = 3

    # Tiger 1
    while i <= 21:
        
        j = i + 1

        # Tiger 2
        while j <= 22:

            k = j + 1

            # Tiger 3
            while k <= 23:
                listTemp = {}
                listTemp[0] = i
                listTemp[1] = j
                listTemp[2] = k

                list.append(listTemp)

                k = k + 1

            j = j + 1

        i = i + 1

    return list

def getBestStalematePositions(_ListOfTigers):
    tempLocation = -1
    listOfGoatLocation = []
    TempListOrigin = [3,4,5,6,9,10,11,12] # Check if need to go origin or not
    Tiger_1 = _ListOfTigers[0]
    Tiger_2 = _ListOfTigers[1]
    Tiger_3 = _ListOfTigers[2]

    #################################
    ## Origin check
    #################################
    if Tiger_1 == 1: # Tiger 1 is the only one in the origin
        for x in TempListOrigin:
            listOfGoatLocation.append(x)
    
    #################################
    ## If any of the tiger in 3 4 5 6 or 9 10 11 12, we need to insert into origin
    #################################    
    if (
            Tiger_1 in TempListOrigin 
        or  Tiger_2 in TempListOrigin 
        or  Tiger_3 in TempListOrigin
    ):
        listOfGoatLocation.append(1)
    
    #################################
    ## Now we ignore origin// and try to insert into all 2 blocks
    #################################   
    i = 1

    # To the left
    while(i <= 2):
        tempLocation = Tiger_1 - i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation)

        tempLocation = Tiger_2 - i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation) 

        tempLocation = Tiger_3 - i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation)   

        i = i + 1

    i = 1
    # To the right
    while(i <= 2):
        tempLocation = Tiger_1 + i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation)

        tempLocation = Tiger_2 + i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation) 

        tempLocation = Tiger_3 + i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation)   
                                 
        i = i + 1       
    
    i = 1
    # up
    while(i <= 2):
        tempLocation = Tiger_1 - 6*i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation)

        tempLocation = Tiger_2 - 6*i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation) 

        tempLocation = Tiger_3 - 6*i
        if(tempLocation >= 2 and tempLocation <= 23):
            listOfGoatLocation.append(tempLocation)   
                                 
        i = i + 1            

    i = 1
    # down
    while(i <= 2):
        tempLocation = Tiger_1 + 6*i
        if(tempLocation >= 2 and tempLocation <= 23 and Tiger_1 != 1):
            listOfGoatLocation.append(tempLocation)

        tempLocation = Tiger_2 + 6*i
        if(tempLocation >= 2 and tempLocation <= 23 and Tiger_2 != 1):
            listOfGoatLocation.append(tempLocation) 

        tempLocation = Tiger_3 + 6*i
        if(tempLocation >= 2 and tempLocation <= 23 and Tiger_3 != 1):
            listOfGoatLocation.append(tempLocation)   
                                 
        i = i + 1 

    listOfGoatLocation = set(listOfGoatLocation) # remove duplicates

    listOfGoatLocation.remove(Tiger_1)
    listOfGoatLocation.remove(Tiger_2)
    listOfGoatLocation.remove(Tiger_3)

    return listOfGoatLocation

ListOfTigers = getAllPossibleTigerLocations()
print(ListOfTigers[0])
print(getBestStalematePositions(ListOfTigers[0]))