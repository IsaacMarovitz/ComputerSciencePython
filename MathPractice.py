# Python Homework 09/11/2020

import math
import sys

# If sys.argv[1] == null then exit program to prevent errors later
try:
    test = sys.argv[1]
except IndexError:
    sys.exit("Error: No angle θ given in system arguments\nProgram exiting")

#  ----------
# |Question 1|
#  ----------

# A physics student gets unexpected results when using the code

G = 6.674e-11
mass1 = 5
mass2 = 15
radius = 10

force = G * mass1 * mass2 / radius * radius
print("Incorrect Force: " + str(force))

# The current problem with this approach is the lack of brackets around
# 'radius * radius'. The fixed code looks like this:

force = G * mass1 * mass2 / (radius * radius)
print("Correct Force: " + str(force))

# You can also use the math operator the square the radius

force = G * mass1 * mass2 / (radius**2)
print("Correct Force: " + str(force))

#  ----------
# |Question 2|
#  ----------

# Θ is read as the FIRST command line argument
# A good value for Θ to check is 365, as this seems to always return 0.9999999999999999

value = (math.cos(int(sys.argv[1]))**2) + (math.sin(int(sys.argv[1]))**2)
print("cos^2 + sin^2 of angle " + sys.argv[1] + " is " + str(value))

# This value sometimes prints to the console as 0.9999999999999999 even 
# though mathmatically it should always equal 1 because of a floating
# point error. Because computers work in Base2 not Base10, which means that
# any decimal is stored in Base2 as a recurring number. Computers sometimes
# don't add recurring numbers together currectly as they have to cut the 
# number off eventually at 15 decimal places, causing an imprecision that 
# results in the console outputing 0.9999999999999999 instead of 1.0 sometimes

#  ----------
# |Question 3|
#  ----------

# Return the distance from the origin from any given coordinates

receivedYInput = False
receivedXInput = False
yCoord = 0
xCoord = 0

# Get user input and ensure that they can only input floats

def GetYInput():
    global yCoord
    yCoord = float(input("Input yCoord: "))

while receivedYInput == False:
    try:
        GetYInput()
        receivedYInput = True
    except ValueError:
        print("Input only numbers")

def GetXInput():
    global xCoord
    xCoord = float(input("Input xCoord: "))

while receivedXInput == False:
    try:
        GetXInput()
        receivedXInput = True
    except ValueError:
        print("Input only numbers")

# Print the hypotenuse of a triangle with base and height of xCoord and yCoord using the math.hypot(x, y) function

print("Distance From Origin: " + str(math.hypot(xCoord, yCoord)))

# On my honour, I have not given nor received unauthorised aid
# Isaac Marovitz