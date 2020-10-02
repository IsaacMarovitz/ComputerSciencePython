import sys

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
tempWidthGrid = []

for x in range(0, width):
    tempWidthGrid.append('*')

for x in range(0, height):
    mineGrid.append(tempWidthGrid)


input("Press ENTER to exit")