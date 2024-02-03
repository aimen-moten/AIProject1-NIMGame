import random

def handleTurn(currTurn, stcks):
    print(currTurn +"'s Turn:")
    # generate random number between 1 and 4 inclusive
    if currTurn == "Computer":
        move = random.randint(1,5)
        while move > stcks:
            move = random.randint(1,5)
    else:
        move = int(input("Enter the number of sticks you would like to take: "))
        while move > stcks:
            move = input("Sorry, please choose a number less than "+ str(stcks))
    print("The "+ currTurn+ " took "+ str(move) + " sticks.")
    stcks = stcks - move
    print("There are " + str(stcks) +" sticks left.")
    return stcks

sticks = input("Enter number of sticks")
print("Game Starting")
currentTurn = "Computer"
while  int(sticks) > 0: # while the last stick has not been taken
   sticks = handleTurn(currentTurn, int(sticks))
   if sticks == 0:
       print(currentTurn + " won!")
   currentTurn = "User" if currentTurn == "Computer" else "Computer"
print("Game Over. Exiting...")
