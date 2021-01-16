# Partner 1:
# Partner 2:
''' Instructions:
   Work with a partner to complete these tasks. Assume that all variables are declared; you need only write the if-statement using the variables indicated in the description. Write your solution below the commented description.
'''

''' 1. 
   Variable grade is a character. If it is an A, print good work. 
'''
grade = "A"
if (grade == "A"):
   print("Good work.")

''' 2. 
   Variable yards is an int. If it is less than 17, multiply yards by 2. 
'''
yards = 2
if (yards < 17):
   yards = yards * 2
print(yards)

''' 3. 
   Variable success is a boolean. If something is a success, print congratulations. 
'''
success = True
if (success):
   print("Congratulations")


''' 4. 
   Variable word is a String. If the string's second letter is 'f', print fun. 
'''
word = "sfg"
if (word[1] == "f"):
   print("Fun")

''' 5. 
   Variable temp is a float. Variable celsius is a boolean. If celsius is true, convert to fahrenheit, storing the result in temp. F = 1.8C + 32.
'''
celsius = 10
if (celsius):
   temp = 1.8 * celsius + 32
print(temp)

''' 6. 
   Variable numItems is an int. Variable averageCost and totalCost are floats. If there are items, calculate the average cost. If there are no items, print no items.
'''
numItems = 5
totalCost = 50
if (numItems > 0):
   averageCost = totalCost / numItems
   print(averageCost)
else:
   print("No items")


''' 7. 
   Variable pollution is a float. Variable cutoff is a float. If pollution is less than the cutoff, print safe condition. If pollution is greater than or equal to cutoff, print unsafe condition. 
'''
pollution = 3.54
cutoff = 2.5
if (pollution < cutoff):
   print("Safe")
elif (pollution >= cutoff):
   print("Unsafe")

''' 8. 
   Variable score is a float, and grade is a char. Store the appropriate letter grade in the grade variable according to this chart.
   F: <60; B: 80-89; D: 60-69; A: 90-100; C: 70-79.
'''
score = 90
if (score < 60):
   grade = "F"
elif (score < 70):
   grade = "D"
elif (score < 80):
   grade = "C"
elif (score < 90):
   grade = "B"
else:
   grade = "A"
print(grade)

''' 9. 
   Variable letter is a char. If it is a lowercase letter, print lowercase. If it is an uppercase, print uppercase. If it is 0-9, print digit. If it is none of these, print symbol.
'''
letter = "8"
if (letter.islower()):
   print("Lowercase")
elif (letter.isupper()):
   print("Uppercase")
elif (letter.isnumeric()):
   print("Digit")
else:
   print("Symbol")


''' 10. 
   Variable neighbors is an int. Determine where you live based on your neighbors.
   50+: city; 25+: suburbia; 1+: rural; 0: middle of nowhere. 
'''
neighbors = 32
if (neighbors >= 50):
   print("City")
elif (neighbors >= 25):
   print("Suburbia")
elif (neighbors >= 1):
   print("Rural")
elif (neighbors == 0):
   print("Middle of nowhere")


''' 11. 
   Variables doesSignificantWork, makesBreakthrough, and nobelPrizeCandidate are booleans. A nobel prize winner does significant work and makes a break through. Store true in nobelPrizeCandidate if they merit the award and false if they don't. 
'''
doesSignificantWork = True
makesBreakthrough = False
if (doesSignificantWork and makesBreakthrough):
   nobelPrizeCandidate = True
else:
   nobelPrizeCandidate = False
print(nobelPrizeCandidate)

''' 12. 
   Variable tax is a boolean, price and taxRate are floats. If there is tax, update price to reflect the tax you must pay.
'''
tax = True
taxRate = 0.3
if (tax):
   price = price * (1 + taxRate)
print(price)

''' 13.  
   Variable word and type are Strings. Determine (not super accurately) what kind of word it is by looking at how it ends. 
   -ly: adverb; -ing; gerund; -s: plural; something else: error   
'''
word = "Walking"
if (word[-2:] == "ly"):
   types = "Adverb"
elif (word[-3:] == "ing"):
   types = "Gerund"
elif (word[-1:] == "s"):
   types = "Plural"
else:
   types = "Error"
print(types)

''' 14. 
   If integer variable currentNumber is odd, change its value so that it is now 3 times currentNumber plus 1, otherwise change its value so that it is now half of currentNumber (rounded down when currentNumber is odd). 
'''
currentNumber = 5
if (currentNumber % 2 == 1):
   currentNumber = currentNumber * 3 + 1
else:
   currentNumber = currentNumber / 2
print(currentNumber)

''' 15. 
   Assign true to the boolean variable leapYear if the integer variable year is a leap year. (A leap year is a multiple of 4, and if it is a multiple of 100, it must also be a multiple of 400.) 
'''

if (year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
   leapYear = True
else:
   leapYear = False


''' 16. 
   Determine the smallest of three ints, a, b and c. Store the smallest one of the three in int result. 
'''
result = min(a, b, c)


''' 17. 
   If an int, number, is even, a muliple of 5, and in the range of -100 to 100, then it is a special number. Store whether a number is special or not in the boolean variable special. 
'''
if (number % 2 == 0 and number % 5 == 0 and number > -100 and number < 100):
   special = True
else:
   special = False


''' 18. 
   Variable letter is a char. Determine if the character is a vowel or not by storing a letter code in the int variable code.
   a/e/o/u/i: 1; y: -1; everything else: 0
'''
if (letter == "a" or letter == "A"):
   code = 1
elif (letter == "e" or letter == "E"):
   code = 1
elif (letter == "i" or letter == "I"):
   code = 1
elif (letter == "o" or letter == "O"):
   code = 1
elif (letter == "u" or letter == "U"):
   code = 1
elif (letter == "y" or letter == "Y"):
   code = -1
else:
   code = 0

''' 19. 
   Given a string dayOfWeek, determine if it is the weekend. Store the result in boolean isWeekend.
'''
if (dayOfWeek == "Saturday" or dayOfWeek == "Sunday"):
   isWeekend = True
else:
   isWeekend = False


''' 20. 
   Given a String variable month, store the number of days in the given month in integer variable numDays. 
'''
numDays = 31
months = ['April', 'June', 'September', 'November']
if (month in months):
   numDays = 30
elif (month == "Febuary"):
   numDays == 28


''' 21. 
   Three integers, angle1, angle2, and angle3, supposedly made a triangle. Store whether the three given angles make a valid triangle in boolean variable validTriangle.
'''
validTriangle = (angle1 + angle2 + angle3 == 180)


''' 22. 
   Given an integer, electricity, determine someone's monthly electric bill, float payment, following the rubric below. 
   First 50 units: 50 cents/unit
   Next 100 units: 75 cents/unit
   Next 100 units: 1.20/unit
   For units above 250: 1.50/unit, plus an additional 20% surcharge.
'''
if (electricity <= 50):
   payment = electricity * 0.5
elif (electricity <= 150):
   payment = (electricity-50) * 0.75 + 25
elif (electricity <= 250):
   payment = (electricity-150) * 1.2 + 100
else:
   payment = ((electricty-250) * 1.5 + 220) * 1.2


''' 23.
   String, greeting, stores a greeting. String language stores the language. If the language is English, greeting is Hello. If the language is French, the greeting is Bonjour. If the language is Spanish, the greeting is Hola. If the language is something else, the greeting is something of your choice.
'''
if (language == "English"):
   greeting = "Hello"
elif (language == "French"):
   greeting = "Bonjour"
elif (language == "Spanish"):
   greeting = "Hola"
else:
   greeting = "Salutations"

''' 24. 
   Generate a phrase and store it in String phrase, given an int number and a String noun. Here are some sample phrases:
   number: 5; noun: dog; phrase: 5 dogs
   number: 1; noun: cat; phrase: 1 cat
   number: 0; noun: elephant; phrase: 0 elephants
   number: 3; noun: human; phrase: 3 humans
   number: 1; noun: home; phrase: 3 homes
'''
phrase = str(num) + " " + noun
if (num == 1):
   phrase = phrase + "s"
 

''' 25. 
   If a string, userInput, is bacon, print out, "Why did you type bacon?". If it is not bacon, print out, "I like bacon." 
'''
if (userInput == "bacon"):
   print("Why did you type bacon?")
else:
   print("I like bacon")

''' 26.
   Come up with your own creative tasks someone could complete to practice if-statements. Also provide solutions.
'''

''' Task 1:

'''

# solution



''' Task 2:

'''

# solution



''' Task 3:

'''

# solution



''' Sources
 http://www.bowdoin.edu/~ltoma/teaching/cs107/spring05/Lectures/allif.pdf
 http://www.codeforwin.in/2015/05/if-else-programming-practice.html
 Ben Dreier for pointing out some creative boolean solutions.
'''