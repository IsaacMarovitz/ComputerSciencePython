startNum = 123
string = str(startNum)
finalNum = 0

for char in string:
    finalNum = finalNum + int(char)

print(finalNum)

startString = "Hello, good day!"
oldChar = None
finalString = ""

for char in startString:
    if char != oldChar:
        finalString = finalString + char
        oldChar = char

print(finalString)

