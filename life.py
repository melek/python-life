"""
    CONWAY'S GAME OF LIFE

    This small game is an ideal test game in any language.

    RULES:
    1. DEATH: If a cell has fewer than two neighbors, it dies from starvation.
    2. DEATH: If a cell has more than three neighbors that are populated, it dies from starvation.
    3. LIFE: If a grid location has exactly two cells as neighbors, it maintains the status quo: if it is a populated grid location (that is, there is a cell there already) it remains populated; if it is an empty grid location, it remains remain empty.
    4. BIRTH: If a grid location has exactly three cells as neighbors, there is a “birth” event. If the location is empty, it becomes populated. If the grid location is already populated, it remains populated.
    
"""
import random

class Life:
    # Attributes

    # Constructor / Initiatization
    def __init__(self, newBoardX = 100, newBoardY = 100)
    # Methods

ONE_IN = 10
RANDOM_SET = [0 for i in range(ONE_IN)]
RANDOM_SET[0] = 1

fieldY = 20
fieldX = 80

# For 10x10

BLANK_FIELD =  [[0 for x in range(fieldX)] for y in range(fieldY)]

def fieldCopy(sourceField):
    return [x[:] for x in sourceField]

def printStar(x, output = "*", blank = " "):
    if x == 0:
        return blank
    return output

SAMPLE_FIELD = fieldCopy(BLANK_FIELD)
if(fieldX >= 5 and fieldY >= 5):
    SAMPLE_FIELD[2][1] = 1
    SAMPLE_FIELD[2][2] = 1
    SAMPLE_FIELD[2][3] = 1

field = fieldCopy(SAMPLE_FIELD)
newField = fieldCopy(BLANK_FIELD)
