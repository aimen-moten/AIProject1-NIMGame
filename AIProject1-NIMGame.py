import random


def alphaBeta(sticks):
    alpha = -1
    beta = 1
    value = -1
    for i in range(1, sticks+1):     
        v = minValue(sticks-i, alpha, beta)
        if v > value:
            value = v
            bestMove = i
        # value = max(value, v)
        alpha = max(alpha, value)
    return bestMove #eturn i that updates max

def minValue(sticks, alpha, beta):
    if sticks <= 0:
        return 1
    value = 1
    for i in range(1, sticks+1):
        v = maxValue(sticks-i, alpha, beta)
        value = min(value, v)
        if value <= alpha:
            return value
        beta = min(beta, value)         
    return value

def maxValue(sticks, alpha, beta):
    if sticks <= 0:
        return -1
    value = -1
    for i in range(1, sticks+1):
        v = minValue(sticks-i, alpha, beta)
        value = max(value, v)
        if value >= beta:
            return value
        alpha = max(alpha, value)
    return value


def handleTurn(currTurn, stcks: int, maxStcks: int):
    print(currTurn +"'s Turn:")
    # generate random number between 1 and 4 inclusive
    if currTurn == "Computer":
        move = int(min(alphaBeta(stcks), maxStcks))
        while move > stcks or move not in range(1, maxStcks+1):
            move = alphaBeta(stcks)
    else:
        move = int(input("Enter the number of sticks you would like to take: "))
        while move > stcks or move not in range(1,maxStcks+1):
            move = int(input("Sorry, please choose a number less than "+ str(stcks) 
                         + " and less than " + str(maxStcks) + ":"))
    print("The "+ currTurn+ " took "+ str(move) + " sticks.")
    stcks = stcks - move
    print("There are " + str(stcks) +" sticks left.")
    return stcks

sticks = input("Enter number of sticks")
maxSticks = input("Enter max number of sticks to take per turn")
while int(maxSticks) > int(sticks):
  maxSticks = input("Enter max number of sticks to take per turn")  
print("Game Starting")
currentTurn = "Computer"
while  int(sticks) > 0: # while the last stick has not been taken
   sticks = handleTurn(currentTurn, int(sticks), int(maxSticks))
   if sticks == 0:
       print(currentTurn + " won!")
   currentTurn = "User" if currentTurn == "Computer" else "Computer"

print("Game Over. Exiting...")