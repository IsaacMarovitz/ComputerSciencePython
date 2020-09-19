# Isaac Marovitz
# 18/09/2020
# Descriptions Do not touch story.txt or art.txt 
# Sources:
# 1. https://www.geeksforgeeks.org/clear-screen-python/
# 2. https://www.youtube.com/watch?time_continue=184&v=2h8e0tXHfk0&feature=emb_logo&ab_channel=LearnLearnScratchTutorials
# 3. https://blog.miguelgrinberg.com/post/how-to-make-python-wait

import sys, json, os, time, threading

# Variables

charWrapLimit = 150
currentRoomIndex = 0
playerName = ""

# Input wait solution taken from Source 3
inputReceivedEvent = threading.Event()

# Functions

# Solution taken from Source 1
def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system("clear")

# Solution taken from Source 2
def typewriter(message):
    charCount = 0
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)
        charCount = charCount + 1
        if char == "\r":
            charCount = 0
        if charCount > charWrapLimit and char == " ":
            print("\r")
            charCount = 0
        if char == "." or char == "!":
            time.sleep(0.5)

def getTextUserInput(inputMessage, failureMessage):
    userInputReceived = False
    userInput = ""
    while not userInputReceived:
        try:
            typewriter(inputMessage)
            userInput = str(input())
            userInputReceived = True
        except ValueError:
            typewriter(failureMessage)
            userInputReceived = False

    inputReceivedEvent.set()
    return userInput

try:
    with open('story.json', 'r') as storyFile:
        storyData = storyFile.read()
except FileNotFoundError:
    sys.exit("Error: story.json is missing or corrupted!\nProgram exiting.")

storyData = json.loads(storyData)

def go(inputMessage):
    global currentRoomIndex
    inputMessage = inputMessage.title()
    if inputMessage in storyData['rooms'][currentRoomIndex]['roomConnections']:
        for room in storyData['rooms']:
            if room['roomName'] == inputMessage:
                currentRoomIndex = storyData['rooms'].index(room)
                typewriter(f"You move into {inputMessage}.\n")
                getCommand()
                return True
    else:
        typewriter(f"There's no connecting room called {inputMessage}.\n")
        getCommand()
        return False

def look(inputMessage):
    global currentRoomIndex
    inputMessage = inputMessage.title()
    for interactable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
        if interactable['interactableName'] == inputMessage:
            typewriter(interactable['interactableText'] + "\n")
            getCommand()
            return True
    typewriter(f"No interactables called {inputMessage}.\n")
    getCommand()
    return False

def cry():
    typewriter("Lmao you cry I guess. Quarantine sux.\n")
    getCommand()

def helpCmd(inputMessage):
    if inputMessage == "go":
        typewriter("go ___ = This command will move you to the connecting room you pass into it.\n")
    elif inputMessage == "look":
        typewriter("look ___ = This command will give you more information about interactables in the current room.\n")
    elif inputMessage == "help":
        typewriter("help ___ = This command will give you more information about a given command, or will tell you about all available commands.\n")
    elif inputMessage == "inventory":
        typewriter("inventory = This command will print the current items in your inventory.\n")
    else:
        typewriter('''Avilable Commands:\n    go\n    look\n    inventory\n    help\nType help followed by each command to learn more information about them.\n''')
    getCommand()

def inventory(inputMessage):
    typewriter("There's no inventory system yet lol.\n")
    getCommand()

def parseUserInput(inputMessage):
    inputMessage = str(inputMessage).lower()
    textArray = inputMessage.split(" ")
    if textArray[0] == "go":
        try:
            go(inputMessage.replace('go', '').strip())
        except IndexError:
            typewriter("No room given.\n")
            getCommand()
    elif textArray[0] == "look":
        try:
            look(inputMessage.replace('look', '').strip())
        except IndexError:
            typewriter("No object to looks at given.\n")
            getCommand()
    elif textArray[0] == "help":
        try:
            helpCmd(textArray[1])
        except IndexError:
            helpCmd("")
    elif textArray[0] == "inventory":
        inventory('')
    elif textArray[0] == "cry":
        cry()
    else:
        typewriter("Command not recognised.\n")
        getCommand()

def getCommand():
    command = getTextUserInput("What do you want to do?: ", "Please only input strings.\n")
    inputReceivedEvent.wait()
    parseUserInput(command)

# Program

clear()
print("Welcome to:")

print(r"""             _____       _   _                               _                 _                  
            |  __ \     | | | |                     /\      | |               | |                 
            | |__) |   _| |_| |__   ___  _ __      /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
            |  ___/ | | | __| '_ \ / _ \| '_ \    / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \
            | |   | |_| | |_| | | | (_) | | | |  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/
            |_|    \__, |\__|_| |_|\___/|_| |_| /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
                    __/ |                                                                         
                   |___,/                                                                          """)

print("                        ------------------------ Quarantine Edition ------------------------", end = '\n\n\n')

typewriter("It's recommended that you play this game in fullscreen, so that ASCII art is correctly displayed.")
time.sleep(0.5)
#clear()

playerName = getTextUserInput("What's your name?: ", "Please only input strings.\n")
inputReceivedEvent.wait()
typewriter(f"Nice to meet you {playerName}.\n")
typewriter("Let's go on an adventure!")
clear()
typewriter("The year is 2020. A global pandemic has taken over the world, and you're stuck at home. It's getting late, it's almost 1 AM now, but you haven't been able to sleep yet. Suddenly you hear a noise from downstairs. Better go check it out.\n")

#clear()
getCommand()

# On my honour, I have neither given nor receieved unauthorised aid
# Isaac Marovitz