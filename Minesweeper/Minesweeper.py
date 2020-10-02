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

for x in range(0, height):
    tempWidthGrid = []
    for x in range(0, width):
        tempWidthGrid.append('0')
    mineGrid.append(tempWidthGrid)

for x in range(0, mineCount):
    xPosition = random.randint(0, width-1)
    yPosition = random.randint(0, height-1)
    mineGrid[yPosition][xPosition] = '*'

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

def printGrid():
    for y in range(0, height):
        for x in range(0, width):
            print(mineGrid[y][x], end=' ')
        print('\n',end='')

printGrid()

input("Press ENTER to exit")