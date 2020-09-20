import re

def IF(inputBool, textValues, storyData):
    print(f"IF input bool: {inputBool}")
    print(f"IF text values: {textValues}")
    return 5

def NULLSW(listValues, textValues, storyData):
    print(f"NULLSW input list: {listValues}")
    print(f"NULLSW text values: {textValues}")
    return 5

def evaluateExpression(expression, storyData):
    expression = re.findall(r"{.+}", expression)[0]
    func = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", expression)
    funcName = str(func[0][0])
    funcData = str(func[0][2])
    funcValues = re.findall(r"[^#\(\)]+", funcData)

    if "IF" in funcData:
        func2 = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", funcData)
        funcData2 = str(func2[0][2])
        funcValues2 = re.findall(r"[^#\(\)]+", funcData2)
        ifBool = funcValues2[0][1]
        ifTextValues = (funcValues2[0][2], funcValues2[0][3])
        returnText = IF(ifBool, ifTextValues, storyData)
        if funcName == "IF":
            ifBool = funcValues[0][1]
            ifTextValues = (funcValues[0][2], returnText)
            return IF(ifBool, ifTextValues, storyData)
        elif funcName == "NULLSW":
            nullwsListValues = re.findall(r"[^#\(\)]+", funcValues[0][1])
            nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues[0][2])
            return NULLSW(nullwsListValues, nullwsTextValues, storyData)
        else:
            pass
    elif "NULLSW" in funcData:
        func2 = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", funcData)
        funcData2 = str(func2[0][2])
        funcValues2 = re.findall(r"(\(((?:[\w#\(\)\[\]\'])*)\)+([\w#]*))", funcData2)
        nullwsListValues = re.findall(r"[^#\(\)]+", funcValues2[0][1])
        nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues2[0][2])
        returnText = NULLSW(nullwsListValues, nullwsTextValues, storyData)
        if funcName == "IF":
            ifBool = funcValues[0][1]
            ifTextValues = (funcValues[0][2], returnText)
            return IF(ifBool, ifTextValues, storyData)
        elif funcName == "NULLSW":
            nullwsListValues = re.findall(r"[^#\(\)]+", funcValues[0][1])
            nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues[0][2])
            return NULLSW(nullwsListValues, nullwsTextValues, storyData)
        else:
            pass
    else:
        if funcName == "IF":
            ifBool = funcValues[0][1]
            ifTextValues = (funcValues[0][2], funcValues[0][3])
            return IF(ifBool, ifTextValues, storyData)
        elif funcName == "NULLSW":
            nullwsListValues = re.findall(r"[^#\(\)]+", funcValues[0][1])
            nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues[0][2])
            return NULLSW(nullwsListValues, nullwsTextValues, storyData)
        else:
            pass

storyData = [4, 5, '4']
print(evaluateExpression(r"{IF(storyData['player']#off#NULLSW((storyData['player']#storyData['player']#storyData['player'])#0#1#2))}", storyData))