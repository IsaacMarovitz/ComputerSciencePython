# Python Homework 02/10/20
# Sources:
# 1. http://inventwithpython.com/blog/2011/08/11/recursion-explained-with-the-flood-fill-algorithm-and-zombies-and-cats/

import sys, random

try:
    width = int(sys.argv[1])
    if width < 0 or width > 50:
        sys.exit("Width must be greater than 0 and less than 50!\nProgram exiting.")
except IndexError:
    sys.exit("Width not given!\nProgram exiting.")
except ValueError:
    sys.exit("Width can only be an interger!\nProgram exiting.")

try:
    height = int(sys.argv[2])
    if height < 0 or width > 50:
        sys.exit("Height must be greater than 0 and less than 50!\nProgram exiting.")
except IndexError:
    sys.exit("Height not given!\nProgram exiting.")
except ValueError:
    sys.exit("Height can only be an interger!\nProgram exiting.")

try:
    mineCount = int(sys.argv[3])
    if mineCount < 0 or mineCount > (width * height):
        sys.exit("Number of mines must be greater than 0 and less than the number of grid squares!\nProgram exiting.")
except IndexError:
    sys.exit("Number of mines not given!\nProgram exiting.")
except ValueError:
    sys.exit("Number of mines can only be an interger!\nProgram exiting.")

mineGrid = []
gameGrid = []

def createMineGrid(startX, startY):
    for _ in range(0, height):
        tempWidthGrid = []
        for _ in range(0, width):
            tempWidthGrid.append('0')
        mineGrid.append(tempWidthGrid)

    totalMineCount = 0
    while totalMineCount < mineCount:
        xPosition = random.randint(0, width-1)
        yPosition = random.randint(0, height-1)
        if mineGrid[yPosition][xPosition] != '*':
            if startX == xPosition or startY == yPosition:
                pass
            else:
                mineGrid[yPosition][xPosition] = '*'
                totalMineCount = totalMineCount + 1

    for y in range(0, height):
        for x in range(0, width):
            if mineGrid[y][x] != '*':
                surroundingMineCount = 0
                if y < height-1 and x > 0 and mineGrid[y+1][x-1] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if y < height-1 and mineGrid[y+1][x] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if y < height-1 and x < width-1 and mineGrid[y+1][x+1] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if x > 0 and mineGrid[y][x-1] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if x < width-1 and mineGrid[y][x+1] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if y > 0 and x > 0 and mineGrid[y-1][x-1] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if y > 0 and mineGrid[y-1][x] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                if y > 0 and x < width-1 and mineGrid[y-1][x+1] == '*':
                    surroundingMineCount = surroundingMineCount + 1
                mineGrid[y][x] = surroundingMineCount
    createGameGrid(0, 0)

def createGameGrid(startX, startY):
    for _ in range(0, height):
        tempWidthGrid = []
        for _ in range(0, width):
            tempWidthGrid.append(False)
        gameGrid.append(tempWidthGrid)
    
    floodFillCheck(startX, startY)

# Taken from Source 1 with major changes
def floodFillCheck(xPos, yPos):
    try:
        if int(mineGrid[yPos][xPos]) != 0:
            return
        gameGrid[yPos][xPos] = True
        if yPos < height-1 and xPos > 0 and not gameGrid[yPos+1][xPos-1]:
            gameGrid[yPos+1][xPos-1] = True
            floodFillCheck(yPos+1, xPos-1)
        if yPos < height-1 and not gameGrid[yPos+1][xPos]:
            gameGrid[yPos+1][xPos] = True
            floodFillCheck(yPos+1, xPos)
        if yPos < height-1 and xPos < width-1 and not gameGrid[yPos+1][xPos+1]:
            gameGrid[yPos+1][xPos+1] = True
            floodFillCheck(yPos+1, xPos+1)
        if xPos > 0 and not gameGrid[yPos][xPos-1]:
            gameGrid[yPos][xPos-1] = True
            floodFillCheck(yPos, xPos-1)
        if xPos < width-1 and not gameGrid[yPos][xPos+1]:
            gameGrid[yPos][xPos+1] = True
            floodFillCheck(yPos, xPos+1)
        if yPos > 0 and xPos > 0 and not gameGrid[yPos-1][xPos-1]:
            gameGrid[yPos-1][xPos-1] = True
            floodFillCheck(yPos-1, xPos-1)
        if yPos > 0 and not gameGrid[yPos-1][xPos]:
            gameGrid[yPos-1][xPos] = True
            floodFillCheck(yPos-1, xPos)
        if yPos > 0 and xPos < width-1 and not gameGrid[yPos-1][xPos+1]:
            gameGrid[yPos-1][xPos+1] = True
            floodFillCheck(yPos-1, xPos+1)
    except ValueError:
        return

def printGrid():
    for y in range(0, height):
        for x in range(0, width):
            if gameGrid[y][x]:
                print(mineGrid[y][x], end=' ')
            else:
                print('-', end=' ')
        print('\n',end='')

createMineGrid(0, 0)
printGrid()

input("Press ENTER to exit")

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz