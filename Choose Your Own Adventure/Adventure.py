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
        # Source End
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
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    if inputMessage in str(storyData['rooms'][currentRoomIndex]['roomConnections']).lower().replace(" ", ""):
        for room in storyData['rooms']:
            if str(room['roomName']).lower().replace(" ", "") == inputMessage:
                currentRoomIndex = storyData['rooms'].index(room)
                typewriter(f"You move into {originalMessage}.\n")
                quick = False
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return True
    else:
        typewriter(f"There's no connecting room called {originalMessage}.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return False

def look(inputMessage):
    global currentRoomIndex
    if inputMessage == "around":
        try:
            roomLookAround = f"You look around. {str(storyData['rooms'][currentRoomIndex]['roomLookAround'])}\n"
            if "{" in roomLookAround:
                try:
                    placeHolders = re.findall(r"{(.+), (.+), (.+), (.+)}", roomLookAround)
                    completeSection = re.findall(r"{.+}", roomLookAround)[0]
                    for info in placeHolders:
                        try:
                            index = int(info[0])
                            if bool(storyData['rooms'][currentRoomIndex]['roomInteractables'][index][info[3]]):
                                roomLookAround = roomLookAround.replace(completeSection, info[2])
                            else:
                                roomLookAround = roomLookAround.replace(completeSection, info[1])
                        except ValueError:
                            playerValue = str(info[0])
                            if bool(storyData['player'][0][playerValue]):
                                roomLookAround = roomLookAround.replace(completeSection, info[2])
                            else:
                                roomLookAround = roomLookAround.replace(completeSection, info[1])
                except IndexError:
                    completeSection = re.findall(r"{.+}", roomLookAround)[0]
                    for info in placeHolders:
                        roomLookAround = roomLookAround.replace(completeSection, info[1])
                typewriter(roomLookAround)
        except KeyError:
            typewriter("Hmmmm. I'm missing some data about this room. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return True
    else:
        originalMessage = inputMessage.strip().title()
        inputMessage = inputMessage.lower().replace(" ", "")
        for interactable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
            if str(interactable['interactableName']).lower().replace(" ", "") == inputMessage:
                typewriter(interactable['interactableText'] + "\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return True
        typewriter(f"No interactables called {originalMessage}.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return False

def useCheck(useable):
    if not useable['interactableUseableDisabled']:
        if useable['interactableUseableState']:
            userBool = getBooleanUserInput(str(useable['interactableUseText1']), "Please only input y/n.\n")
            inputReceivedEvent.wait()
            if userBool:
                useable['interactableUseableState'] = False
                try:
                    storyData['player'][0][useable['interactablePlayerValue']] = useable['interactableUseableState']
                except KeyError:
                    pass
                typewriter(f"{useable['interactableSetText0']}\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return True
        else:
            userBool = getBooleanUserInput(str(useable['interactableUseText0']), "Please only input y/n.\n")
            inputReceivedEvent.wait()
            if userBool:
                useable['interactableUseableState'] = True
                try:
                    storyData['player'][0][useable['interactablePlayerValue']] = useable['interactableUseableState']
                except KeyError:
                    pass
                typewriter(f"{useable['interactableSetText1']}\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return True
    else:
        typewriter(f"{useable['interactableDisabled']}\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return True

def use(inputMessage):
    global currentRoomIndex
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    for useable in storyData['inventory']:
        if str(useable['interactableName']).lower().replace(" ", "") == inputMessage:
            if useable['interactableSingleUse'] == True:
                userBool = getBooleanUserInput(str(useable['interactableUseText']), "Please only input y/n.\n")
                inputReceivedEvent.wait()
                if userBool:
                    storyData['player'][0][useable['interactableUseStat']] + useable['interactableUseStrength']
                    typewriter(f"Used {originalMessage}. {str(useable['interactableUseStat']).title()} increased by {str(useable['interactableUseStrength'])}.\n")
                    storyData['inventory'].remove(useable)
                    return False
            else:
                useCheck(useable)
                return True
    for useable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
        if str(useable['interactableName']).lower().replace(" ", "") == inputMessage and useable['interactableUseable']:
            if not useable['interactableCollectable']:
                useCheck(useable)
                return True
            else:
                typewriter(f"Add {originalMessage} to your inventory to use it.\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return False
                    
    typewriter(f"No usable objects called {originalMessage}.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()
    return False

def take(inputMessage):
    global currentRoomIndex
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    for collectable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
        if str(collectable['interactableName']).lower().replace(" ", "") == inputMessage and collectable['interactableCollectable']:
            storyData['inventory'].append(collectable)
            storyData['rooms'][currentRoomIndex]['roomInteractables'].remove(collectable)
            typewriter(f"{originalMessage} was added to your inventory.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
            return True

    typewriter(f"No collectable objects called {originalMessage}.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()
    return False

def stats():
    typewriter("You stats are as follows.\n")
    typewriter(f"   Player Name - {storyData['player'][0]['name']}\n")
    typewriter(f"   HP - {str(storyData['player'][0]['health'])}\n")
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
    elif inputMessage == "take":
        typewriter("take ___ = This comamnd will take the object you pass in and add it to your inventory.\n")
    elif inputMessage == "inventory":
        typewriter("inventory = This command will print the current items in your inventory.\n")
    elif inputMessage == "stats":
        typewriter("stats = This command will tell you your current player stats.\n")
    elif inputMessage == "help":
        typewriter("help ___ = This command will give you more information about a given command, or will tell you about all available commands.\n")
    else:
        typewriter('''Avilable Commands:\n    go\n    look\n    use\n    take\n    inventory\n    stats\n    help\nType help followed by each command to learn more information about them.\n''')
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()

def inventory(inputMessage):
    typewriter("You have the following items in your inventory.\n")
    for collectable in storyData['inventory']:
        try:
            typewriter(f"   {collectable['interactableName']} - {collectable['interactableInventoryDescription']}\n")
        except KeyError:
            typewriter("Hmmmm. I'm missing some data about this item. Your story.json file may be incomplete.\n")
    waitForEnter()
    inputReceivedEvent.wait()
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
    elif textArray[0] == "take":
        try:
            take(inputMessage.replace('take', '').strip())
        except IndexError:
            typewriter("No object to take given.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
    elif textArray[0] == "stats":
        stats()
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
        currentRoom = storyData['rooms'][currentRoomIndex]

        roomName = str(currentRoom['roomName'])
        roomDescription = eval(currentRoom['roomDescription'])
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
    waitForEnter()
    inputReceivedEvent.wait()
    clear()

    printHeader("Setup")
    storyData['player'][0]['name'] = getTextUserInput("What's your name?: ", "Please only input strings.\n")
    inputReceivedEvent.wait()
    typewriter(f"Nice to meet you {storyData['player'][0]['name']}.\n")
    typewriter("Let's go on an adventure!\n")
    typewriter("If you ever feel stuck or unsure use the 'help' command to get a summary of each usable command.\n")
    typewriter("Please bear in mind that each command will only work with basic statments like 'look computer' not 'look at the computer'.\n")
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