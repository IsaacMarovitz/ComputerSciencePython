import sys

# sys.argv error checking

try:
    int(sys.argv[1])
except IndexError:
    sys.exit("Error: No system arguments given\nProgram exiting")
except ValueError:
    sys.exit("Input system arguments must be positive intergers\nProgram exiting")

try:
    int(sys.argv[2])
except IndexError:
    sys.exit("Error: Second system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Input system arguments must be positive intergers\nProgram exiting")

try:
    int(sys.argv[3])
except IndexError:
    sys.exit("Error: Third system argument missing\nProgram exiting")
except ValueError:
    sys.exit("Input system arguments must be positive intergers\nProgram exiting")

if (int(sys.argv[1]) < 0) or (int(sys.argv[2]) < 0) or (int(sys.argv[3]) < 0):
    sys.exit("Input system argument must be positive intergers\nProgram exiting")

#  ----------
# |Question 1|
#  ----------

userInputRecieved = False
num = 0

def GetUserInput():
    global num
    num = float(input("Input number: "))

while userInputRecieved == False:
    try:
        GetUserInput()
        userInputRecieved = True
    except ValueError:
        print("Only input numbers!")

numCheck = False

# (num//10) * 10 returns the smaller multiple of ten nearest num
smallerMultiple = (num//10)*10
largerMultiple = smallerMultiple+10

# This checks if the difference between each multiple and num is less than 
# or equal to 2
if (num-smallerMultiple) <= 2 or (largerMultiple-num) <= 2:
    numCheck = True 

print(numCheck)

#  ----------
# |Question 2|
#  ----------

if ((int(sys.argv[1]) % int(sys.argv[2])) == 0):
    print("System argument intergers evenly divide")
else:
    print("System arguemtn intergers do not evenly divide")

#  ----------
# |Question 3|
#  ----------

# Forumla for determining a leap year from here: https://docs.microsoft.com/en-us/office/troubleshoot/excel/determine-a-leap-year

year = int(sys.argv[3])

if (year%400 == 0) or ((year%4 == 0) and (year%100 != 0)):
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#  ----------
# |Question 4|
#  ----------

#  ----------
# |Question 5|
#  ----------
