# Python Homework 09/14/2020

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
        if abs(t) < 50:
            receivedTInput = True
        else:
            print("The temperature must be above -50 or below 50")
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
        if (v > 120 or v < 3):
            print("The wind speed must be below 120 or above 3")
        else:
            receivedVInput = True
    except ValueError:
        print("Input only numbers")

w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v**0.16)
print(f"The wind chill is {round(w, 1)}")