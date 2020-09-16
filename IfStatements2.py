# Python Homework 09/16/2020

import sys

try:
    float(sys.argv[1])
except IndexError:
    sys.exit("Error: No system arguments given\nProgram exiting")
except ValueError:
    sys.exit("Error: First system argument must be a float\nProgram exiting")

user_score = float(sys.argv[1])

if user_score < 0 or user_score > 5:
    sys.exit("Error: First system argument must be greater than 0 or less than 5\nProgram exiting")

def get_user_score(user_score):
    if user_score <= 1:
        return "F"
    elif user_score <= 1.33:
        return "D-"
    elif user_score <= 1.67:
        return "D"
    elif user_score <= 2:
        return "D+"
    elif user_score <= 2.33:
        return "C-"
    elif user_score <= 2.67:
        return "C"
    elif user_score <= 3:
        return "C+"
    elif user_score <= 3.33:
        return "B-"
    elif user_score <= 3.67:
        return "B"
    elif user_score <= 4:
        return "B+"
    elif user_score <= 4.33:
        return "A-"
    elif user_score <= 4.67:
        return "A"
    else:
        return "A+"
    
print(f"Your score is {get_user_score(user_score)}")

input("Press ENTER to exit")

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz