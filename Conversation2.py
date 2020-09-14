# Python Homework 09/09/2020
# Inital grade 2/2
# Inital file Conversation.py
# Modified version after inital submisions, with error handeling and datetime year

# Importing the datetime module so that the value for the year later in the program isn't hardcoded
import datetime

def userAge():
    global user_age
    user_age = int(input("How old are you? (Please only input numbers) "))

print("\nHey there!", end=" ")
user_name = input("What's your name? ")
print("Nice to meet you " + user_name)
user_age_input_recieved = False

while (user_age_input_recieved == False):
    try:
        userAge()
        user_age_input_recieved = True
    except ValueError:
        print("Invalid Input")
        user_age_input_recieved = False

# I got this datetime solution from StackOverflow
# https://stackoverflow.com/questions/30071886/how-to-get-current-time-in-python-and-break-up-into-year-month-day-hour-minu
print("So, you were born in " + str((datetime.datetime.now().year-user_age)) + "!")
user_colour = input("What's your favourite colour? ")
if user_colour.lower() == "blue":
    print("Hey, my favourite is blue too!")
else:
    print(user_colour.lower().capitalize() +
          "'s a pretty colour! But my favourite is blue")
print("Goodbye!")
input("Press ENTER to exit")

# On my honor, I have neither given nor received unauthorized aid
# Isaac Marovitz
