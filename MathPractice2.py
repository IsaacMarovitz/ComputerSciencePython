# Python Homework 09/14/2020
# I would prefer to be in a group with Joy An

import sys

# Error handeling for sys.argv

try:
    float(sys.argv[1])
except IndexError:
    sys.exit("Error: No system arguments given\nProgram exiting")
except ValueError:
    sys.exit("First system argument must be a float\nProgram exiting")

try:
    float(sys.argv[2])
except IndexError:
    sys.exit("Error: Second system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Second system argument must be a float\nProgram exiting")

try:
    float(sys.argv[3])
except IndexError:
    sys.exit("Error: Third system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Third system argument must be a float\nProgram exiting")

try:
    int(sys.argv[4])
except IndexError:
    sys.exit("Error: Third system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Fourth system argument must be an int\nProgram exiting")

try:
    int(sys.argv[5])
except IndexError:
    sys.exit("Error: Third system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Fifth system argument must be an int\nProgram exiting")

try:
    int(sys.argv[6])
except IndexError:
    sys.exit("Error: Third system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Sixth system argument must be an int\nProgram exiting")

#  ----------
# |Question 1|
#  ----------

receivedScaleInput = False
inFahrenheit = False
inputText = ""

def GetScaleInput():
    global inputText
    inputText = input("Input which scale you want to use (C/F): ")

while receivedScaleInput == False:
    GetScaleInput()
    if inputText.lower() ==  "c":
        receivedScaleInput = True
        inFahrenheit = False
    elif inputText.lower() == "f":
        receivedScaleInput = True
        inFahrenheit = True
    else:
        print("Only input C or F")

receivedTInput = False
t = 0

def GetTFInput():
    global t
    t = float(input("Input temperature (in Fahrenheit): "))

def GetTCInput():
    global t
    t = (float(input("Input temperature (in Celsius): ")) * (9/5)) + 32

while receivedTInput == False:
    try:
        if inFahrenheit:
            GetTFInput()
        else:
            GetTCInput()
        if t < 50:
            receivedTInput = True
        else:
            if inFahrenheit:
                print("The temperature must be below 50°F")
            else:
                print("The temperature must be below 10°C")
    except ValueError:
        print("Input only numbers")

receivedVInput = False
v = 0

def GetVInput():
    global v
    v = float(input("Input wind speed (in mph): "))

while receivedVInput == False:
    try:
        GetVInput()
        if (v >= 120 or v <= 3):
            print("The wind speed must be below 120 or above 3")
        else:
            receivedVInput = True
    except ValueError:
        print("Input only numbers")

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v**0.16)
if inFahrenheit:
    print(f"The wind chill is {round(w, 1)}°F")
else:
    w = (w-32) * (5/9)
    print(f"The wind chill is {round(w, 1)}°C")

#  ----------
# |Question 2|
#  ----------

x = float(sys.argv[1])
y = float(sys.argv[2])
z = float(sys.argv[3])

if (x < y) and (y < z):
    print("Floats are in order")
elif (x > y) and (y > z):
    print("Floats are in order")
else:
    print("Floats are not in order")

#  ----------
# |Question 3|
#  ----------

m = int(sys.argv[4])
d = int(sys.argv[5])
y = int(sys.argv[6])

# Switch statement alternative from: https://jaxenter.com/implement-switch-case-statement-python-138315.html
def getDay(argument):
    switcher = {
        0 : "Sunday",
        1 : "Monday",
        2 : "Tuesday",
        3 : "Wednesday",
        4 : "Thursday",
        5 : "Friday",
        6 : "Saturday",
    }
    print (switcher.get(argument, "Invalid day"))

y0 = y - (14 - m) // 12
x = y0 + y0 // 4 - y0 // 100 + y0 // 400
m0 = m + 12 * ((14 - m) // 12) - 2
d0 = (d + x + (31 * m0) // 12) % 7
print(d0)
getDay(d0)

input("Press ENTER to exit")

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz