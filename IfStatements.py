is_raining = True
is_windy = True

if is_raining and is_windy:
    print("Maybe stay home today...")
elif is_raining:
    print("Bring your umbrella!")
elif is_windy:
    print("Wear your windbreaker!")
else:
    print("Enjoy the nice weather!")

receivedAgeInput = False

while receivedAgeInput == False:
    try:
        age = int(input("Input age: "))
        if age > 120 or age < 0:
            print("Input your actual age")
        else:
            receivedAgeInput = True
    except ValueError:
        print("Input only numbers")

if age < 10:
    print("Ok zoomer")
elif age < 30:
    print("Ok millennial")
else:
    print("Ok boomer")

input("Press ENTER to exit")