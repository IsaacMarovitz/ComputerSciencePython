# Python Homework 14/10/20
# Sources: 
# 1. https://en.wikipedia.org/wiki/Euclidean_algorithm#Procedure

aInputReceived = False
bInputReceived = False
a = 0
b = 0

while not aInputReceived:
    try:
        a = int(input("Input larger of two values: "))
        aInputReceived = True
    except ValueError:
        aInputReceived = False
        print("Input only numbers")

while not bInputReceived:
    try:
        b = int(input("Input smaller of two values: "))
        bInputReceived = True
    except ValueError:
        bInputReceived = False
        print("Input only numbers")

# I made this long one first by just reading through the procedure of the algorithm, not realising 
# you could just use modulo
def euclid(a, b):
    lessThanB = False
    c = 0
    i = 1
    while not lessThanB:
        c = a - (i * b)
        if c < b:
            lessThanB = True
        else:
            i = i + 1 
    if c == 0:
        return b
    else:
        return euclid(b, c)

# Taken from Source 1
def shortEuclid(a, b):
    if b == 0:
        return a
    else:
        return shortEuclid(b, a%b)

print(euclid(a, b))
print(shortEuclid(a, b))

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz