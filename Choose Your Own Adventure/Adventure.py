# Isaac Marovitz
# 18/09/2020
# Descriptions Do not touch story.txt or art.txt 
# Sources:
# 1. https://www.geeksforgeeks.org/clear-screen-python/
# 2. https://www.youtube.com/watch?time_continue=184&v=2h8e0tXHfk0&feature=emb_logo&ab_channel=LearnLearnScratchTutorials
# 3. https://blog.miguelgrinberg.com/post/how-to-make-python-wait
# 4. https://stackoverflow.com/questions/14061724/how-can-i-find-all-placeholders-for-str-format-in-a-python-string-using-a-regex
# 5. Help from CPU espically from Max Fan who helped with getting str.format() working correctly with story.json

import sys, json, os, time, threading, random, textwrap

# Variables

charWrapLength = 100
currentRoomIndex = 0
currentBattleName = ""
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
    message = textwrap.fill(message, charWrapLength, replace_whitespace = False, drop_whitespace = False)
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.02)

def wrappedPrint(message):
    print(textwrap.fill(message, charWrapLength, replace_whitespace = False, drop_whitespace = False))

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

try:
    storyData = json.loads(storyData)
except json.decoder.JSONDecodeError:
    sys.exit("Error: story.json is missing or corrupted!\nProgram exiting.")

def startBattle():
    global currentRoomIndex
    global currentBattleName
    currentBattleName = storyData['rooms'][currentRoomIndex]['battleText']

def go(inputMessage):
    global currentRoomIndex
    global quick
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    try:
        if inputMessage in str(storyData['rooms'][currentRoomIndex]['roomConnections']).lower().replace(" ", ""):
            for room in storyData['rooms']:
                if str(room['roomName']).lower().replace(" ", "") == inputMessage:
                    currentRoomIndex = storyData['rooms'].index(room)
                    typewriter(f"You move into {originalMessage}.\n")
                    quick = False
                    waitForEnter()
                    inputReceivedEvent.wait()
                    getCommand()
                    return 
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 
    else:
        typewriter(f"There's no connecting room called {originalMessage}.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 

def look(inputMessage):
    global currentRoomIndex
    if inputMessage == "around":
        try:
            currentRoom = storyData['rooms'][currentRoomIndex]
            if "format" in currentRoom['roomLookAround']:
                try:
                    roomLookAround = f"You look around. {eval(currentRoom['roomLookAround'])}\n"
                except SyntaxError:
                    roomLookAround = "Hmmmm. There was error when loading this room's description. Your story.json file may be incomplete.\n"
            else:
                roomLookAround = f"You look around. {currentRoom['roomLookAround']}\n"
            typewriter(roomLookAround)
        except KeyError:
            typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 
    else:
        originalMessage = inputMessage.strip().title()
        inputMessage = inputMessage.lower().replace(" ", "")
        try:
            for interactable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
                if str(interactable['interactableName']).lower().replace(" ", "") == inputMessage:
                    typewriter(interactable['interactableText'] + "\n")
                    waitForEnter()
                    inputReceivedEvent.wait()
                    getCommand()
                    return 
        except KeyError:
            typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
            return 

        typewriter(f"No interactables called {originalMessage}.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 

def useCheck(useable):
    if not useable['interactableUseableDisabled']:
        if useable['interactableUseableState']:
            userBool = getBooleanUserInput(str(useable['interactableUseText1']), "Please only input y/n.\n")
            inputReceivedEvent.wait()
            if userBool:
                useable['interactableUseableState'] = False
                try:
                    storyData['player'][useable['interactablePlayerValue']] = useable['interactableUseableState']
                except KeyError:
                    pass
                typewriter(f"{useable['interactableSetText0']}\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return 
            else:
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
        else:
            userBool = getBooleanUserInput(str(useable['interactableUseText0']), "Please only input y/n.\n")
            inputReceivedEvent.wait()
            if userBool:
                useable['interactableUseableState'] = True
                try:
                    storyData['player'][useable['interactablePlayerValue']] = useable['interactableUseableState']
                except KeyError:
                    pass
                typewriter(f"{useable['interactableSetText1']}\n")
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
                return 
            else:
                waitForEnter()
                inputReceivedEvent.wait()
                getCommand()
    else:
        typewriter(f"{useable['interactableDisabled']}\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 

def use(inputMessage):
    global currentRoomIndex
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    try:
        for useable in storyData['inventory']:
            for name in useable['interactableName']:
                if str(name).lower().replace(" ", "") == inputMessage:
                    if not useable['interactableBattleItem']:
                        useCheck(useable)
                        return 
                    else:
                        typewriter("You deside to save this item for a battle.\n")
                        waitForEnter()
                        inputReceivedEvent.wait()
                        getCommand()
                        return 
        for useable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
            for name in useable['interactableName']:
                if str(name).lower().replace(" ", "") == inputMessage and useable['interactableUseable']:
                    if not useable['interactableCollectable']:
                        useCheck(useable)
                        return 
                    else:
                        typewriter(f"Add {originalMessage} to your inventory to use it.\n")
                        waitForEnter()
                        inputReceivedEvent.wait()
                        getCommand()
                        return 
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 
                    
    typewriter(f"No usable objects called {originalMessage}.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()
    return 

def take(inputMessage):
    global currentRoomIndex
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    try:
        for collectable in storyData['rooms'][currentRoomIndex]['roomInteractables']:
            for name in collectable['interactableName']:
                if str(name).lower().replace(" ", "") == inputMessage and collectable['interactableCollectable']:
                    storyData['inventory'].append(collectable)
                    storyData['rooms'][currentRoomIndex]['roomInteractables'].remove(collectable)
                    typewriter(f"{originalMessage} was added to your inventory.\n")
                    waitForEnter()
                    inputReceivedEvent.wait()
                    getCommand()
                    return 
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()
        return 

    typewriter(f"No collectable objects called {originalMessage}.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()
    return 

def stats():
    try:
        typewriter("You stats are as follows.\n")
        typewriter(f"   Player Name - {storyData['player']['name']}\n")
        typewriter(f"   HP - {str(storyData['player']['health'])}\n")
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
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
        typewriter("help ___ = This command will give you more information about a given command, or will tell you all available commands.\n")
    else:
        typewriter('''Available Commands:\n    go\n    look\n    use\n    take\n    inventory\n    stats\n    help\nType help followed by each command to learn more information about them.\n''')
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()

def inventory():
    typewriter("You have the following items in your inventory.\n")
    try:
        for collectable in storyData['inventory']:
            typewriter(f"   {collectable['interactableName'][0]} - {collectable['interactableInventoryDescription']}\n")
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getCommand()

def start():
    global currentRoomIndex
    global currentBattleName
    try:
        currentBattleName = storyData['rooms'][currentRoomIndex]['battleText']
        getBattleCommand()
    except KeyError:
        typewriter("There's no battle to start in this room.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()

def parseUserInput(inputMessage):
    inputMessage = str(inputMessage).lower()
    forbiddenWords = ['to', 'at', 'a', 'an', 'my', 'your', 'some', 'of', 'into']
    for word in forbiddenWords:
        inputMessage = inputMessage.replace(f' {word} ', ' ')
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
            inputMessage = inputMessage.replace(f' the ', '')
            look(inputMessage.replace('look', '').strip())
        except IndexError:
            typewriter("No object to looks at given.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
    elif textArray[0] == "use":
        try:
            inputMessage = inputMessage.replace(f' the ', '')
            use(inputMessage.replace('use', '').strip())
        except IndexError:
            typewriter("No object to use given.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getCommand()
    elif textArray[0] == "take":
        try:
            inputMessage = inputMessage.replace(f' the ', '')
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
        inventory()
    elif textArray[0] == "cry":
        cry()
    elif inputMessage == "start battle":
        start()
    else:
        typewriter("Command not recognised.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getCommand()

def battleWin():
    global currentBattleName
    typewriter(f"{storyData[currentBattleName]['playerWin']}\n")
    typewriter(f"Congratulations! You completed Python Adventure (Quarantine Edition). Thank you for playing!\n")
    waitForEnter()
    inputReceivedEvent.wait()

def battleLose():
    global currentBattleName
    global currentRoomIndex
    global storyData
    global storyFile
    typewriter(f"{storyData[currentBattleName]['playerDeath']}\n")
    typewriter("You will now be sent back to the begining.\n")
    name = storyData['player']['name']
    try:
        with open('story.json', 'r') as storyFile:
            storyData = storyFile.read()
    except FileNotFoundError:
        sys.exit("Error: story.json is missing or corrupted!\nProgram exiting.")

    try:
        storyData = json.loads(storyData)
    except json.decoder.JSONDecodeError:
        sys.exit("Error: story.json is missing or corrupted!\nProgram exiting.")
    currentRoomIndex = 0
    storyData['player']['name'] = name
    getCommand()


def opponentTakeTurn():
    global currentBattleName
    randomMove = random.randint(0, len(storyData[currentBattleName]['opponentMoves'])-1)
    move = storyData[currentBattleName]['opponentMoves'][randomMove]
    storyData['player']['health'] = storyData['player']['health'] - move['damage']
    typewriter(f"{storyData[currentBattleName]['opponentName']} used '{move['moveName']}'!\n{move['moveDescription']}\n{move['playerReaction']}\n{storyData['player']['name']} lost {move['damage']} HP.\n")
    if storyData['player']['health'] <= 0:
        battleLose()
        return
    else:
        waitForEnter()
        inputReceivedEvent.wait()
        getBattleCommand()
        return

def battleUse(inputMessage):
    global currentBattleName
    originalMessage = inputMessage.strip().title()
    inputMessage = inputMessage.lower().replace(" ", "")
    try:
        for useable in storyData['inventory']:
            for name in useable['interactableName']:
                if str(name).lower().replace(" ", "") == inputMessage:
                    if useable['interactableBattleItem']:
                        userBool = getBooleanUserInput(str(useable['interactableUseText']), "Please only input y/n.\n")
                        inputReceivedEvent.wait()
                        if userBool:
                            storyData['player'][useable['interactableUseStat']] = storyData['player'][useable['interactableUseStat']] + useable['interactableUseStrength']
                            typewriter(f"Used {originalMessage}. {str(useable['interactableUseStat']).title()} increased by {str(useable['interactableUseStrength'])}.\n")
                            storyData['inventory'].remove(useable)
                            opponentTakeTurn()
                            return 
                        else:
                            waitForEnter()
                            inputReceivedEvent.wait()
                            getBattleCommand()
                    else:
                        typewriter("You can't use this item in battle.\n")
                        waitForEnter()
                        inputReceivedEvent.wait()
                        getBattleCommand()
                        return 

        for move in storyData['player']['playerMoves']:
            if str(move['moveCounter']) == inputMessage or str(move['moveName']).lower().replace(" ", "") == inputMessage:
                storyData[currentBattleName]['opponentHealth'] = storyData[currentBattleName]['opponentHealth'] - move['damage']
                typewriter(f"{storyData['player']['name']} used '{move['moveName']}'! {storyData[currentBattleName]['opponentName']} lost {move['damage']} HP.\n\n")
                if storyData[currentBattleName]['opponentHealth'] <= 0:
                    battleWin()
                    return
                else:
                    opponentTakeTurn()
                    return 

        typewriter(f"No moves or items called {originalMessage} found.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getBattleCommand()
        return

    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getBattleCommand()
        return 

def battleHelp(inputMessage):
    if inputMessage == "use":
        typewriter("use ___ = This command will use the object or move you pass in.\n")
    elif inputMessage == "inventory":
        typewriter("inventory = This command will print the current items in your inventory.\n")
    elif inputMessage == "stats":
        typewriter("stats = This command will tell you your current player stats.\n")
    elif inputMessage == "help":
        typewriter("help ___ = This command will give you more information about a given command, or will tell you all available commands.\n")
    else:
        typewriter('''Available Commands:\n    use\n    inventory\n    stats\n    help\nType help followed by each command to learn more information about them.\n''')
    waitForEnter()
    inputReceivedEvent.wait()
    getBattleCommand()

def battleInventory():
    typewriter("You have the following items in your inventory.\n")
    try:
        for collectable in storyData['inventory']:
            typewriter(f"   {collectable['interactableName'][0]} - {collectable['interactableInventoryDescription']}\n")
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getBattleCommand()

def battleStats():
    try:
        typewriter("You stats are as follows.\n")
        typewriter(f"   Player Name - {storyData['player']['name']}\n")
        typewriter(f"   HP - {str(storyData['player']['health'])}\n")
    except KeyError:
        typewriter("Hmmmm. I'm missing some data. Your story.json file may be incomplete.\n")
    waitForEnter()
    inputReceivedEvent.wait()
    getBattleCommand()

def parseUseBattleInput(inputMessage):
    inputMessage = str(inputMessage).lower()
    forbiddenWords = ['to', 'the', 'at', 'a', 'an', 'my', 'your', 'some', 'of', 'into']
    for word in forbiddenWords:
        inputMessage = inputMessage.replace(f' {word} ', ' ')
    textArray = inputMessage.split(" ")
    if textArray[0] == "go":
        typewriter("You can't go anywhere during a battle.\n")
    elif textArray[0] == "look":
        typewriter("You can't look at anything during a battle.\n")
    elif textArray[0] == "use":
        try:
            battleUse(inputMessage.replace('use', '').strip())
        except IndexError:
            typewriter("No move/item given.\n")
            waitForEnter()
            inputReceivedEvent.wait()
            getBattleCommand()
    elif textArray[0] == "take":
        typewriter("You can't take anything during a battle.\n")
    elif textArray[0] == "inventory":
        battleInventory()
    elif textArray[0] == "stats":
        battleStats()
    elif textArray[0] == "help":
        try:
            battleHelp(textArray[1])
        except IndexError:
            battleHelp("")
    elif textArray[0] == "cry":
        typewriter("You stay determined.\n")
    else:
        typewriter("Command not recognised.\n")
        waitForEnter()
        inputReceivedEvent.wait()
        getBattleCommand()

def getCommand():
    global quick
    clear()
    displayRoom()
    quick = True
    command = getTextUserInput("What do you want to do?: ", "Please only input strings.\n")
    inputReceivedEvent.wait()
    parseUserInput(command)

def getBattleCommand():
    global quick
    clear()
    displayBattle()
    quick = True
    command = getTextUserInput("What do you want to do?: ", "Please ony input string.\n")
    inputReceivedEvent.wait()
    parseUseBattleInput(command)

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
        if "format" in currentRoom['roomDescription']:
            try:
                roomDescription = f"{eval(currentRoom['roomDescription'])}\n"
            except SyntaxError:
                roomDescription = "Hmmmm. There was error when loading this room's description. Your story.json file may be incomplete.\n"
        else:
            roomDescription = f"{currentRoom['roomDescription']}\n"
        printHeader(roomName)
        if not quick:
            typewriter(roomDescription)
        else:
            wrappedPrint(roomDescription)
    except KeyError:
        if not quick:
            typewriter("Hmmmm. I'm missing some data about this room. Your story.json file may be incomplete.\n\n")
        else:
            wrappedPrint("Hmmmm. I'm missing some data about this room. Your story.json file may be incomplete.\n\n")

def displayBattle():
    global currentBattleName
    printHeader(currentBattleName)
    print(f"{storyData[currentBattleName]['opponentName']} --- HP: {storyData[currentBattleName]['opponentHealth']}\n\n",end='')
    print(storyData[currentBattleName]['opponentASCII'])
    print(f"{storyData['player']['name']} --- HP: {storyData['player']['health']}\n\n", end='')
    print(f"\x1b[4m\x1b[1mMoves\x1b[0m\n")
    for move in storyData['player']['playerMoves']:
        print(f"[{move['moveCounter']}] {move['moveName']} ({move['damage']} Damage)    ", end='')
    print("\n",end='')

    

# TO DO
# Change out 'waitForEnter' for a wait function It's cumbersome 
# IMPLEMENT EX MOVES IN BATTLES

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

    typewriter("It's recommended that you play this game in fullscreen, so that ASCII art is correctly displayed.\n\n")
    waitForEnter()
    inputReceivedEvent.wait()
    clear()

    printHeader("Setup")
    try:
        storyData['player']['name'] = getTextUserInput("What's your name?: ", "Please only input strings.\n")
        inputReceivedEvent.wait()
        typewriter(f"Nice to meet you {storyData['player']['name']}.\n")
    except KeyError:
        print("Error: story.json is missing or corrupted!")

    typewriter("Let's go on an adventure!\n")
    typewriter("If you ever feel stuck or unsure use the 'help' command to get a summary of each usable command.\n")
    typewriter("Commands will work with basic statements like 'look at the computer' or 'take my phone'.\n")
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

#displayBattle()
# On my honour, I have neither given nor receieved unauthorised aid
# Isaac Marovitz