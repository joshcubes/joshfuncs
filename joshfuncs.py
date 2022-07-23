######
# Name: Joshfuncs
# Author: Joshcubes
# Last Commit: 23/07/22
######

def intinput(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please Enter A Number")

def intinputrange(prompt, min, max):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a number between " + str(min) + " and " + str(max) + ".")
