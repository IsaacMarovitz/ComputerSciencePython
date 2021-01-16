# Python Homework 11/01/20
# In the Monty Hall Problem it is benefical to switch your choice
# This is because, if you switch, you have a rougly 2/3 chance of 
# Choosing a door, becuase you know for sure that one of the doors is
# The wrong one, otherwise if you didnt switch you would still have the 
# same 1/3 chance you had when you made your inital guess

# On my honour, I have neither given nor received unauthorised aid
# Isaac Marovitz

import random

num_simulations = 5000
no_of_wins_no_switching = 0
no_of_wins_switching = 0

# Runs Monty Hall simulation
def run_sim(switching):
    games_won = 0

    for _ in range(num_simulations):
        # Declare an array of three doors each with a tuple as follows (Has the car, has been selected)
        doors = [(False, False), (False, False), (False, False)]
        # Get the guess of the user by choosing at random one of the doors
        guess = random.randint(0, 2)
        # Select a door at random to put the car behind
        door_with_car_index = random.randint(0, 2)
        # Change the tuple of that door to add the car
        doors[door_with_car_index] = (True, False)

        # Open the door the user didn't chose that doesn't have the car behind it
        for x in range(2):
            if x != door_with_car_index and x != guess:
                doors[x] = (False, True)
        
        # If switching, get the other door that hasn't been revealed at open it, otherwise check if 
        # the current door is the correct one
        if switching:
            for x in range(2):
                if x != guess and doors[x][1] != True:
                    games_won += 1
        else:
            if guess == door_with_car_index:
                games_won += 1
                
    return games_won

# Run sim without switching for first run
no_of_wins_no_switching = run_sim(False)

# Run sim with switching for the next run
no_of_wins_switching = run_sim(True)

print(f"Ran {num_simulations} Simulations")
print(f"Won games with switching: {no_of_wins_switching} ({round((no_of_wins_switching / num_simulations) * 100)}%)")
print(f"Won games without switching: {no_of_wins_no_switching} ({round((no_of_wins_no_switching / num_simulations) * 100)}%)")


