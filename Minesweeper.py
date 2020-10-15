# Python Homework 02/10/20
# Sources: N/A

import sys, random, os, time

# Get starting command line argument and check for errors
try:
    width = int(sys.argv[1])
    if width < 1 or width > 30:
        sys.exit("Width must be greater than 0 and less than 30!\nProgram exiting.")
except IndexError:
    sys.exit("Width not given!\nProgram exiting.")
except ValueError:
    sys.exit("Width can only be an interger!\nProgram exiting.")

try:
    height = int(sys.argv[2])
    if height < 1 or width > 30:
        sys.exit("Height must be greater than 0 and less than 30!\nProgram exiting.")
except IndexError:
    sys.exit("Height not given!\nProgram exiting.")
except ValueError:
    sys.exit("Height can only be an interger!\nProgram exiting.")

try:
    mineCount = int(sys.argv[3])
    if mineCount < 1 or mineCount > (width * height):
        sys.exit("Number of mines must be greater than 0 and less than the number of grid squares!\nProgram exiting.")
except IndexError:
    sys.exit("Number of mines not given!\nProgram exiting.")
except ValueError:
    sys.exit("Number of mines can only be an interger!\nProgram exiting.")

# Declaring needed arrays
mineGrid = []
gameGrid = []

# Clear the terminal
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

# Creates the mineGrid, which is the solved version of the grid that the user doesnt see
def createMineGrid(startX, startY):
    for _ in range(0, height):
        tempWidthGrid = [0 for x in range(width)]
        mineGrid.append(tempWidthGrid)

    totalMineCount = 0
    while totalMineCount < mineCount:
        xPosition = random.randint(0, width-1)
        yPosition = random.randint(0, height-1)
        if mineGrid[yPosition][xPosition] != '*':
            if startX != xPosition and startY != yPosition:
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
    createGameGrid(startX, startY)

# Create the gameGrid which stores hidden tiles with 'False', shown tiles with 'True', and flagged tiles with 'f', default it all to 'False'
def createGameGrid(startX, startY):
    for _ in range(0, height):
        tempWidthGrid = []
        for _ in range(0, width):
            tempWidthGrid.append(False)
        gameGrid.append(tempWidthGrid)
    
    recursiveCheck(startX, startY)

# Checks all tiles around a given tile and starts the check if it isn't already shown
def recursiveCheck(xPos, yPos):
    gameGrid[yPos][xPos] = True
    if mineGrid[yPos][xPos] != '*':
        if int(mineGrid[yPos][xPos]) == 0:
            gameGrid[yPos][xPos] = True
            if yPos < height-1 and xPos > 0 and not gameGrid[yPos+1][xPos-1]:
                gameGrid[yPos+1][xPos-1] = True
                recursiveCheck(xPos-1, yPos+1)
            if yPos < height-1 and not gameGrid[yPos+1][xPos]:
                gameGrid[yPos+1][xPos] = True
                recursiveCheck(xPos, yPos+1)
            if yPos < height-1 and xPos < width-1 and not gameGrid[yPos+1][xPos+1]:
                gameGrid[yPos+1][xPos+1] = True
                recursiveCheck(xPos+1, yPos+1)
            if xPos > 0 and not gameGrid[yPos][xPos-1]:
                gameGrid[yPos][xPos-1] = True
                recursiveCheck(xPos-1, yPos)
            if xPos < width-1 and not gameGrid[yPos][xPos+1]:
                gameGrid[yPos][xPos+1] = True
                recursiveCheck(xPos+1, yPos)
            if yPos > 0 and xPos > 0 and not gameGrid[yPos-1][xPos-1]:
                gameGrid[yPos-1][xPos-1] = True
                recursiveCheck(xPos-1, yPos-1)
            if yPos > 0 and not gameGrid[yPos-1][xPos]:
                gameGrid[yPos-1][xPos] = True
                recursiveCheck(xPos, yPos-1)
            if yPos > 0 and xPos < width-1 and not gameGrid[yPos-1][xPos+1]:
                gameGrid[yPos-1][xPos+1] = True
                recursiveCheck(xPos+1, yPos-1)

# This checks to see if the win conditions have been met yet by checking if there are any unrevealed non-mine tiles
def checkWin():
    totalSqauresLeft = 0
    for x in range(0, width):
        for y in range(0, height):
            if mineGrid[y][x] != '*' and gameGrid[y][x] == False:
                totalSqauresLeft = totalSqauresLeft + 1
    if totalSqauresLeft == 0:
        return True
    else:
        return False

# Parses user input coords for each turn and checks for errors
def parseUserInput(inputMessage):
    inputMessage = inputMessage.strip().split(" ")
    try:
        xPos = int(inputMessage[0]) - 1
        yPos = int(inputMessage[1]) - 1
        try:
            if inputMessage[2] == 'f' or inputMessage[2] == 'F':
                if gameGrid[yPos][xPos] == False:
                    gameGrid[yPos][xPos] = 'F'
                elif gameGrid[yPos][xPos] == 'F':
                    gameGrid[yPos][xPos] = False
                else:
                    print("You can't place flags on revealed squares!")
                    time.sleep(1)
            else:
                print("Type 'f' to place a flag at the given coordinates!")
                time.sleep(1)
        except IndexError:
            if gameGrid[yPos][xPos] != 'F':
                recursiveCheck(xPos, yPos)
                if mineGrid[yPos][xPos] == '*':
                    print("You died!")
                    return
            else:
                print("You cannot reveal sqaures with a flag!")
                time.sleep(1)
    except ValueError:
        print("Only input intergers for coordinates!")
        time.sleep(1)
    except IndexError:
        print("Only input valid coordinates!")
        time.sleep(1)
    if checkWin():
        printGrid()
        print("You won!")
    else:
        printGrid()
        parseUserInput(input("Input coords: "))

# Prints the grid with spacing and unicode box-drawing characters for added aesthetics 
def printGrid():
    clear()
    print('┌',end='')
    for x in range(0, width):
        if x < width-1:
            print('───┬', end='')
        else:
            print('───┐', end='')
    print('\n', end='')
    for y in range(0, height):
        for x in range (0, width):
            print('│', end='')
            if gameGrid[y][x] == 'F':
                print(' ⚑ ', end='')
            else:
                if gameGrid[y][x]:
                    print(f" {mineGrid[y][x]} ", end='')
                else:
                    print(' ◼ ', end='')
            if not (x < width-1):
                print('│', end='')
        print('\n',end='')
        if y < height-1:
            print('├', end='')
        else:
            print('└', end='')
        for x in range(0, width):
            if y < height-1:
                if x < width-1:
                    print('───┼', end='')
                else:
                    print('───┤', end='')
            else:
                if x < width-1:
                    print('───┴', end='')
                else:
                    print('───┘', end='')
        print('\n', end='')

# Starts the game, gets the starting coords from the user, checks for errors, keeps track of game time, and asks the user if they want to play again
def startGame():
    clear()
    print('Welcome to Minesweeper\n')
    startCoordsReceived = False

    while not startCoordsReceived:
        try:
            inputMessage = input('Where do you want to start? Input coords (x & y): ')
            inputMessage = inputMessage.strip().split(' ')
            xCoord = int(inputMessage[0]) - 1
            yCoord = int(inputMessage[1]) - 1
            if xCoord < width and yCoord < height:
                startCoordsReceived = True
            else:
                print(f"Width and height must be between 0 and {width} and {height} respectively!")
                startCoordsReceived = False
                time.sleep(1)
                clear()
                print('Welcome to Minesweeper\n')    
        except IndexError:
            print("Please input an x AND a y coordinate seperated by a space.")
            startCoordsReceived = False
            time.sleep(1)
            clear()
            print('Welcome to Minesweeper\n')
        except ValueError:
            print("Please only input whole intergers.")
            startCoordsReceived = False
            time.sleep(1)
            clear()
            print('Welcome to Minesweeper\n')

    startTime = time.time()
    createMineGrid(xCoord, yCoord)
    printGrid()
    parseUserInput(input("Input coords: "))

    print(f"You played for {round(time.time() - startTime, 2)} seconds!")
    playAgainReceived = False

    while not playAgainReceived:
        try:
            inputMessage = input('Do you want to play again? (y/n): ')
            inputMessage = inputMessage.strip().lower()
            if inputMessage == 'y' or inputMessage == 'yes':
                playAgainReceived = True
                startGame()
            elif inputMessage == 'n' or inputMessage == 'no':
                playAgainReceived = True
                input("Press ENTER to exit")
            else:
                print("Please input yes or no")
                time.sleep(1)
                clear()
                playAgainReceived = False
        except ValueError:
            print("Please input yes or no")
            time.sleep(1)
            clear()
            playAgainReceived = False

startGame()

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz