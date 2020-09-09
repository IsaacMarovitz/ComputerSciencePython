# Python Homework 09/09/2020

print("\nHey there!", end=" ")
user_name = input("What's your name? ")
print("Nice to meet you " + user_name)
user_age = int(input("How old are you? (Please only input numbers) "))
print("So, you were born in " + str((2020-user_age)) + "!")
user_colour = input("What's your favourite colour? ")
if user_colour.lower() == "blue":
    print("Hey, my favourite is blue too!")
else:
    print(user_colour + "'s a pretty colour! But my favourite it blue")
print("Goodbye! 👋")