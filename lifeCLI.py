from shutil import get_terminal_size
from life import *

verbose = False
userChoice = " " 
while not userChoice in ['q', 'quit']:    
    if(userChoice == ""):
        if(lastChoice in ['n', 'next']):
            userChoice = 'm'
        elif(lastChoice in ['m', 'move']):
            userChoice = 'n'
        elif(lastChoice in ['g', 'generate']):
            userChoice = 'g'

    if(userChoice in ["r", "randomize"]):
        field = [ [ random.choice(RANDOM_SET) for x in range(fieldX) ] for y in range(fieldY) ]
    elif(userChoice in ["s", "sample"]):
        field = fieldCopy(SAMPLE_FIELD)

    print("\n" * (get_terminal_size().lines - fieldY - 1), end='')    
    
    debugString = ""
    
    if(verbose):
        spacer = "  "
    else:
        spacer = ""

    titleRow = [str(x % 10) for x in range(fieldX)]

    print("   " + spacer.join(titleRow))       

    for y in range(fieldY):
        row = str(y % 10) + " "
        for x in range(fieldX):
            row += printStar(field[y][x])            
            debugTable = [[],[],[]]
            neighborCount = 0 - field[y][x]
            for cy in range(-1, 2):
                for cx in range(-1, 2):
                    ny = (y + cy) % fieldY
                    nx = (x + cx) % fieldX
                    neighborCount += field[ny][nx]
                    debugTable[cy + 1].append(str(nx) + "," + str(ny) + ":" + str(field[ny][nx]))

            if userChoice in ['d ' + str(x) + " " + str(y), 'debug ' + str(x) + " " + str(y)]:
                debugString = '\n'.join( [" | ".join(debugTable[dy]) for dy in range(3)] )
            
            if(verbose):
                row += printStar(neighborCount, str(neighborCount), "-")
            
            if userChoice in ["n", "next", "g", "generate"]: # Generate the next field
                if neighborCount == 2:
                    newField[y][x] = field[y][x]
                elif neighborCount == 3:
                    newField[y][x] = 1
                else:
                    newField[y][x] = 0            

            if(verbose):
                row += printStar(newField[y][x], ".")

        print(row)    

    if userChoice in ["m", "move", "g", "generate"]: # Move to the next field
        field = fieldCopy(newField)
        newField = fieldCopy(BLANK_FIELD)

    if not debugString == "":
        print("DEBUG CMD: " + userChoice)
        print(debugString)
        print(str(id(field)) + " : " + str(id(newField)) + " : " + str(id(BLANK_FIELD)) + " : " + str(id(SAMPLE_FIELD)))
        print(BLANK_FIELD)

    lastChoice = userChoice
    userChoice = input("Hit ENTER to generate or type QUIT to end... ").lower()
