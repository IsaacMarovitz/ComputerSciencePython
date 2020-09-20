import re

def evaluateExpression(expression):
    expression = re.findall(r"{.+}", expression)[0]
    func = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", expression)
    funcName = str(func[0][0])
    funcData = str(func[0][2])
    funcValues = re.findall(r"[^#\(\)]+", funcData)
    #print(funcValues)

    if "IF" in funcData:
        func2 = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", funcData)
        funcName2 = str(func2[0][0])
        funcData2 = str(func2[0][2])
        funcValues2 = re.findall(r"[^#\(\)]+", funcData2)
    elif "NULLSW":
        func2 = re.findall(r"(IF|NULLSW)(\(((?:[\w#\(\)\[\]\'])*)\))", funcData)
        funcName2 = str(func2[0][0])
        funcData2 = str(func2[0][2])
        funcValues2 = re.findall(r"(\(((?:[\w#\(\)\[\]\'])*)\)+([\w#]*))", funcData2)
        print(funcData2)
        nullwsListValues = re.findall(r"[^#\(\)]+", funcValues2[0][1])
        print(nullwsListValues)
        nullwsTextValues = re.findall(r"[^#\(\)]+", funcValues2[0][2])
        print(nullwsTextValues)



evaluateExpression(r"{IF(storyData['player']#off#NULLSW((storyData['player']#storyData['player']#storyData['player'])#0#1#2))}")