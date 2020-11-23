# Isaac Marovitz - Python Homework 02/10/20
# Sources: N/A
# Blah blah blah
# On my honour, I have neither given nor received unauthorised aid

import sys, random, os, time

# Declaring needed arrays
mineGrid = []
gameGrid = []

# Clear the terminal
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

# Returns all items surrounding an item in a given array
def checkSurrounding(givenArray, x, y):
    returnArray = []
    height = len(givenArray) - 1
    width = len(givenArray[0]) - 1
    if y < height and x > 0:
        returnArray.append((givenArray[y+1][x-1], y+1, x-1))
    if y < height:
        returnArray.append((givenArray[y+1][x], y+1, x))
    if y < height and x < width:
        returnArray.append((givenArray[y+1][x+1], y+1, x+1))
    if x > 0:
        returnArray.append((givenArray[y][x-1], y, x-1))
    if x < width:
        returnArray.append((givenArray[y][x+1], y, x+1))
    if y > 0 and x > 0:
        returnArray.append((givenArray[y-1][x-1], y-1, x-1))
    if y > 0:
        returnArray.append((givenArray[y-1][x], y-1, x))
    if y > 0 and x < width:
        returnArray.append((givenArray[y-1][x+1], y-1, x+1))
    return returnArray

# Creates the mineGrid, which is the solved version of the grid that the user doesnt see
def createMineGrid(startX, startY):
    # Create 2D Array if given width and height
    for _ in range(0, height):
        tempWidthGrid = [0 for x in range(width)]
        mineGrid.append(tempWidthGrid)

    # Place mines in the grid until the mine count equals total mine count
    totalMineCount = 0
    while totalMineCount < mineCount:
        xPosition = random.randint(0, width-1)
        yPosition = random.randint(0, height-1)
        if mineGrid[yPosition][xPosition] != '*':
            if startX != xPosition and startY != yPosition:
                mineGrid[yPosition][xPosition] = '*'
                totalMineCount = totalMineCount + 1

    # Sets all the numbers in the grid to the number of mines surrounding that point
    for y in range(0, height):
        for x in range(0, width):
            if mineGrid[y][x] != '*':
                surroundingMineCount = 0
                checkArray = checkSurrounding(mineGrid, x, y)
                for value in checkArray:
                    if value[0] == '*':
                        surroundingMineCount += 1
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
            checkArray = checkSurrounding(gameGrid, xPos, yPos)
            for value in checkArray:
                if not value[0]:
                    gameGrid[value[1]][value[2]] = True
                    recursiveCheck(value[1], value[2])

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
    # Gets input message and splits it into an array 
    inputMessage = inputMessage.strip().split(" ")
    try:
        # Gets input coords from input message array
        xPos = int(inputMessage[0]) - 1
        yPos = int(inputMessage[1]) - 1
        # If an 'f' is included, toggle the flag on the given square
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
        # If no flag is included, check if the given square is a mine and either reveal it or end the game
        except IndexError:
            if gameGrid[yPos][xPos] != 'F':
                recursiveCheck(xPos, yPos)
                if mineGrid[yPos][xPos] == '*':
                    print("You died!")
                    return
            else:
                print("You cannot reveal sqaures with a flag!")
                time.sleep(1)
    # Error checking
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
                if gameGrid[y][x] and mineGrid[y][x] != '*':
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
    global mineGrid, gameGrid
    clear()
    print('Welcome to Minesweeper\n')
    startCoordsReceived = False
    mineGrid = []   
    gameGrid = []

    # Receive starting coords and check if they're valid
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

    # Record start time and create mine grid
    startTime = time.time()
    createMineGrid(xCoord, yCoord)
    printGrid()
    parseUserInput(input("Input coords: "))

    # When the game finishes, display final time
    print(f"You played for {round(time.time() - startTime, 2)} seconds!")
    playAgainReceived = False

    # Ask the user if they want to play again
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

startGame()
