import random

print("---------------------------------")
print("        Guess the Number")
print("---------------------------------")

theNum = random.randint(0, 100)
userGuessInt = -1

userName = input("Enter your name: ")

while userGuessInt != theNum:

    userGuessTxt = input("Guess a number between 0 and 100: ")
    userGuessInt = int(userGuessTxt)

    if userGuessInt > theNum:
        print("Sorry {}, your guess of {} is too high!".format(userName,userGuessInt))

    elif userGuessInt < theNum:
        print("Sorry {}, your guess of {} is too low!".format(userName,userGuessInt))

    else:
        print("Dude, {}, your guess of {} is spot on!".format(userName,userGuessInt))

print("done")