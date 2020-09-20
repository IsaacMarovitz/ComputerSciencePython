# Isaac Marovitz
# 18/09/2020
# Descriptions Do not touch story.txt or art.txt 
# Sources:
# 1. https://www.geeksforgeeks.org/clear-screen-python/
# 2. https://www.youtube.com/watch?time_continue=184&v=2h8e0tXHfk0&feature=emb_logo&ab_channel=LearnLearnScratchTutorials
# 3. https://blog.miguelgrinberg.com/post/how-to-make-python-wait
# 4. https://stackoverflow.com/questions/14061724/how-can-i-find-all-placeholders-for-str-format-in-a-python-string-using-a-regex

import sys, json, os, time, threading, re

# Variables

charWrapLimit = 100
currentRoomIndex = 0
playerName = ""
quick = False

try:
    skipIntro = bool(sys.argv[1])
except:
    skipIntro = False

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
    sleepTime = 0.5
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
            time.sleep(sleepTime)

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

def getBooleanUserInput(inputMessage, failureMessage):
    userInputReceived = False
    textInput = ""
    userInput = False
    while not userInputReceived:
        try:
            typewriter(inputMessage)
            textInput = str(input())
            userInputReceived = True
            if textInput.lower().strip() == "yes" or textInput.lower().strip() == "y":
                userInput = True
            elif textInput.lower().strip() == "no" or textInput.lower().strip() == "n":
                userInput = False
            else:
                typewriter(failureMessage)
                userInputReceived = False
        except ValueError:
            typewriter(failureMessage)
            userInputReceived = False

    inputReceivedEvent.set()
    return userInput

def waitForEnter():
    typewriter("Press ENTER to continue.")
    input("")
    inputReceivedEvent.set()

try:
    with open('story.json', 'r') as storyFile:
        storyData = storyFile.read()
except FileNotFoundError:
    sys.exit("Error: story.json is missing or corrupted!\nProgram exiting.")

storyData = json.loads(storyData)

def go(inputMessage):
    global currentRoomIndex
    global quick
    inputMessage = inputMessage.title()
    if inputMessage in storyData['rooms'][currentRoomIndex]['roomConnections']:
        for room in storyData['rooms']:
            if room['roomName'] == inputMessage:
                currentRoomIndex = storyData['rooms'].index(room)
                typewriter(f"You move into {inputMessage}.\n")
                quick = False
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return True
    else:
        typewriter(f"There's no connecting room called {inputMessage}.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return False

def look(inputMessage):
    global currentRoomIndex
    if inputMessage == "around":
        try:
            typewriter(f"You look around. {storyData['rooms'][currentRoomIndex]['roomLookAround']}\n")
        except KeyError:
            typewriter("Hmmmm. I'm missing some data about this room. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return True
    else:
        inputMessage = inputMessage.title()
        for interactable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
            if interactable['interactableName'] == inputMessage:
                typewriter(interactable['interactableText'] + "\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return True
        typewriter(f"No interactables called {inputMessage}.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return False

def use(inputMessage):
    global currentRoomIndex
    inputMessage = inputMessage.title()
    for useable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
        if useable['interactableName'] == inputMessage and useable['interactableUseable']:
            if not useable['interactableUseableDisabled']:
                if useable['interactableUseableState']:
                    userBool = getBooleanUserInput(str(useable['interactableUseText1']), "Please only input y/n.\n")
                    inputReceivedEvent.wait()
                    if userBool:
                        useable['interactableUseableState'] = False
                        typewriter(f"{useable['interactableName']} was set to false.\n")
                else:
                    userBool = getBooleanUserInput(str(useable['interactableUseText0']), "Please only input y/n.\n")
                    inputReceivedEvent.wait()
                    if userBool:
                        useable['interactableUseableState'] = True
                        typewriter(f"{useable['interactableName']} was set to true.\n")
            else:
                typewriter(f"{useable['interactableDisabled']}\n")
        else:
            typewriter(f"No usable objects called {inputMessage}.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()

def cry():
    typewriter("Lmao you cry I guess. Quarantine sux.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()

def helpCmd(inputMessage):
    if inputMessage == "go":
        typewriter("go ___ = This command will move you to the connecting room you pass into it.\n")
    elif inputMessage == "look":
        typewriter("look ___ = This command will give you more information about interactable objects in the current room. Type 'look around' to get a summary of interactable objects in the current room.\n")
    elif inputMessage == "use":
        typewriter("use ___ = This command will use the object you pass in.\n")
    elif inputMessage == "inventory":
        typewriter("inventory = This command will print the current items in your inventory.\n")
    elif inputMessage == "help":
        typewriter("help ___ = This command will give you more information about a given command, or will tell you about all available commands.\n")
    else:
        typewriter('''Avilable Commands:\n    go\n    look\n    use\n    inventory\n    help\nType help followed by each command to learn more information about them.\n''')
    waitForEnter()
    inputReceivedEvent.wait()
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
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
    elif textArray[0] == "look":
        try:
            look(inputMessage.replace('look', '').strip())
        except IndexError:
            typewriter("No object to looks at given.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
    elif textArray[0] == "use":
        try:
            use(inputMessage.replace('use', '').strip())
        except IndexError:
            typewriter("No object to use given.\n")
            waitForEnter()
            inputReceivedEvent.wait()
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
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()

def getCommand():
    global quick
    clear()
    displayRoom()
    quick = True
    command = getTextUserInput("What do you want to do?: ", "Please only input strings.\n")
    inputReceivedEvent.wait()
    parseUserInput(command)

def printHeader(text):
    print("┌", end='')
    for _ in text:
        print("─",end='')
    print("──┐\r")
    print(f"│ {text} │")
    print("└", end='')
    for _ in text:
        print("─",end='')
    print("──┘\n")

def displayRoom():
    global currentRoomIndex
    global quick
    try:
        roomName = str(storyData['rooms'][currentRoomIndex]['roomName'])
        roomDescription = str(storyData['rooms'][currentRoomIndex]['roomDescription']) + "\n"
        # Solution taken from Source 4
        # This finds any instance of {} I put in my roomDescription text, and replaces it with some regex magic.
        placeHolders = re.findall(r"{(\w+)}", roomDescription)
        for index in placeHolders:
            if bool(storyData['rooms'][currentRoomIndex]['roomInteractables'][int(index)]['interactableUseableState']):
                roomDescription = roomDescription.replace('{'+index+'}', 'on')
            else:
                roomDescription = roomDescription.replace('{'+index+'}', 'off')
        printHeader(roomName)
        if not quick:
            typewriter(roomDescription)
        else:
            print(roomDescription)
    except KeyError:
        if not quick:
            typewriter("Hmmmm. I'm missing some data about this room. Your story.json file may be incomplete.\n\n")
        else:
            print("Hmmmm. I'm missing some data about this room. Your story.json file may be incomplete.\n\n")
    

# TO DO:
# ADD TAKE COMMAND
# ADD ASCII ART
# ADD UI
# IMPLEMENT INVENTORY

# Program
clear()
if not skipIntro:
    print("Welcome to:")

    print(r"""                 _____       _   _                               _                 _                  
                |  __ \     | | | |                     /\      | |               | |                 
                | |__) |   _| |_| |__   ___  _ __      /  \   __| |_   _____ _ __ | |_ _   _ _ __ ___ 
                |  ___/ | | | __| '_ \ / _ \| '_ \    / /\ \ / _` \ \ / / _ \ '_ \| __| | | | '__/ _ \
                | |   | |_| | |_| | | | (_) | | | |  / ____ \ (_| |\ V /  __/ | | | |_| |_| | | |  __/
                |_|    \__, |\__|_| |_|\___/|_| |_| /_/    \_\__,_| \_/ \___|_| |_|\__|\__,_|_|  \___|
                        __/ |                                                                         
                       |___/                                                                          """)

    print("                        ------------------------ Quarantine Edition ------------------------", end = '\n\n\n')

    typewriter("It's recommended that you play this game in fullscreen, so that ASCII art is correctly displayed.")
    time.sleep(0.5)
    clear()

    printHeader("Setup")
    playerName = getTextUserInput("What's your name?: ", "Please only input strings.\n")
    inputReceivedEvent.wait()
    typewriter(f"Nice to meet you {playerName}.\n")
    typewriter("Let's go on an adventure!\n")
    typewriter("If you ever feel stuck or unsure use the 'help' command to get a summary of each usable command.\n")
    typewriter("Please bare in mind that each command will only work with basic statments like 'look computer' not 'look at the computer'.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    clear()

    printHeader("Exposition")
    try:
        typewriter(f"{str(storyData['exposition'])}\n")
    except KeyError:
        print("Error: story.json is missing or corrupted!")
    waitForEnter()
    inputReceivedEvent.wait()
    clear()
displayRoom()
quick = True
getCommand()

# On my honour, I have neither given nor receieved unauthorised aid
# Isaac Marovitz