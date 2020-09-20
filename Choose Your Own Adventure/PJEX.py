import re

def IF(bool, textValues):
    pass

def NULLSW(listValues, textValues):
    pass

def evaluateExpression(expression, storyData):
    expression = re.findall(r"{.+}", expression)[0]
    func = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", expression)
    funcName = str(func[0][0])
    print(funcName)
    funcData = str(func[0][2])
    funcValues = re.findall(r"[^#\(\)]+", funcData)
    print(funcValues)

    if "IF" in funcData:
        func2 = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", funcData)
        funcName2 = str(func2[0][0])
        funcData2 = str(func2[0][2])
        funcValues2 = re.findall(r"[^#\(\)]+", funcData2)
    elif "NULLSW" in funcData:
        func2 = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", funcData)
        funcName2 = str(func2[0][0])
        funcData2 = str(func2[0][2])
        funcValues2 = re.findall(r"(\(((?:[\w#\(\)\[\]\'])*)\)+([\w#]*))", funcData2)
        nullwsListValues = re.findall(r"[^#\(\)]+", funcValues2[0][1])
        nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues2[0][2])
        NULLSW(nullwsListValues, nullwsTextValues)
    else:
        if funcName == "IF":
            ifBool = funcValues[0][1]
            ifTextValues = (funcValues[0][2], funcValues[0][3])
            IF(ifBool, ifTextValues)
        elif funcName == "NULLSW":
            nullwsListValues = re.findall(r"[^#\(\)]+", funcValues[0][1])
            nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues[0][2])
            NULLSW(nullwsListValues, nullwsTextValues)
        else:
            pass

storyData = [4, 5, '4']
evaluateExpression(r"{IF(storyData['player']#off#NULLSW((storyData['player']#storyData['player']#storyData['player'])#0#1#2))}", storyData)