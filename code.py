# Create-Patterns-using-python

#part 1- creating random o's 

import random

def placeRandomOs( n ):
    """Given an int n that describes the number of spots,
    randomly place an "o" with a chance of 20%. Return a string of length
    n that consists of spaces and randomly placed o's."""

    spots= ''
    for i in range(n):
        randomNum= random.randint(1,5)
        if randomNum==1: 
            spots= spots + "o"
            
        else: 
            spots= spots + ' ' 
    return spots        

  
#random.seed( 1837 )


#placing o's in the middle 

def placeOneO( n ):
    """Given an int n that describes the number of spots,
    place exactly one o in the middle and return that string."""

###################### MAIN CODE IS HERE ######################
    spots=""
    space=""
    space1=""
    if n%2 == 1: 
        for i in range(int(n/2)): 
            space=space + " "
        spots= space+ "o"+ space
    elif n%2 == 0 and n!= 0 : 
        for i in range(int(n/2)): 
            space=space+" " 
        for i in range(int((n/2)-1)): 
            space1= space1 + " " 
        spots= space + "o" + space1
    return spots

print(placeOneO(5))
print(placeOneO(8))


    
print ("01234")

#code to test with 6 spots to check even case

print ("012345")


#calculating the next row 

def calculateNextRow( currentRow ):
    """ Given a string of the currentRow of the pattern, generate the next row.
    Return a string that has an "o" if exactly one neighbor
    in the current level has an "o" and otherwise has a space."""
    space='' 
    nextRow=''
###################### CODE TO TEST calculateNextRow ######################
    for x in range(len(currentRow)): 
        n= int(x) 
        if n==0: 
            if currentRow[1]!= 'o': 
                nextRow = nextRow + ' ' 
            else: 
                nextRow= nextRow + 'o' 
        elif n!= 0 and n<(len(currentRow)-1):
            if currentRow[n+1] !='o' and currentRow[n-1]=='o' or currentRow[n+1] =='o' and currentRow[n-1]!= 'o' :
                 nextRow = nextRow +'o'
            else: 
                nextRow = nextRow + ' '
        elif n==len(currentRow)-1: 
            if currentRow[n-1]=='o': 
                nextRow= nextRow + 'o' 
            else: 
                nextRow= nextRow + ' ' 
        
    
    return nextRow     
       

currentLevel = "  o  "
print (calculateNextRow (currentLevel))


##creating the pattern ##

def createPattern( startingRow, numberOfLevels ):
    """ Given an initial string of the top row, generate numberOfLevels more rows.
    Return a string with each row on a new line. The top line
    should be the initial startingRow, with each subsequent line below it."""
    b= startingRow
    d= startingRow 
    
    for x in range(numberOfLevels): 
        b= calculateNextRow(b)
        d= d + '\n' + b
        
    return d    




