# NIM Game
##  Project Stage 1
### Description:
This project should implement the game of NIM. For those who are unfamiliar with NIM, here are the rules for our version of the game:

- There are two players. Your program should have one human player (the user) and
one computer player, and the computer should always move first.
- Between the two players is a pile of sticks (or other objects). Your program should start with 12 sticks, but the program should be flexible enough that the number of
sticks could be easily changed.
- The players take turns (your program should allow the computer player to start all the
time). On each turn, a player may take 1, 2, 3, or 4 sticks from the pile in the middle. Again, you should make your program flexible enough that you could change this rule to allow taking any number of sticks relatively easily.
- The winner of the game is the player that takes the last stick from the pile.
  
Your program does not need to have any graphics (although it can if you want to spend the extra time), but for each player’s turn it should be obvious whose turn it is, how many sticks were taken, and how many sticks are left in the pile. When a player wins, there should be a clear message as to who won.

For this assignment, you may have the computer make any move you like on its turn. You can feel free to make the computer player as good as you like, though. You do need to make sure that the computer can only make legal moves; for example, if there are only 2 sticks left, it should not try to take 3. You should also make sure the human player makes only legal moves as well.

## Project Stage 2
### Description:

This project will have you revisiting the NIM game you wrote for project #1. In this version, the computer will use the ALPHA-BETA algorithm to select its moves. Your program does not need to have any graphics or graphical user interface, but it should be obvious whose turn it is and how to enter a move.

You should be able to start with the code you have for project #1. You should change your code to ask the user to select the initial number of sticks in the pile, as well as the maximum number of sticks that you can choose in a move. The computer should still make the first move, however.
The project should implement the full version of ALPHA-BETA; you do not need to cut the search short and use evaluation functions. The algorithm will take longer the more sticks you start with; you can assume that I will not test it on values that are too large.
For this particular version of the game, it would make sense to have MIN-VALUE and MAX-VALUE return integers instead of floats, since the only values possible are +1 and -1. Additionally, it might make sense to use -1 and +1 as starting values for alpha and beta, although this is up to you.
Finally, note that “state current” is just a placeholder for however you choose to represent the state of the game. In NIM it could be as simple as an integer representing the number of sticks left.

### Specifications:
Your program must meet the following specifications:
1. Your program represents a sincere attempt to solve the problem.
2. Your program compiles and runs, assuming specification 1 is met.
3. Your program has the user enter the initial number of sticks.
4. Your program has the user enter the maximum number of sticks a player can take.
5. Your program always has the computer make the first move.
6. Your program prevents the user from picking an inappropriate number of sticks.
7. Your program successfully implements the ALPHA-BETA algorithm.
8. Your program wins the game if it is possible for it to do so.
9. Your program makes it clear how many sticks are left after each move.
10. Your program successfully reports who the winner of the game is at the end.
11. Your program is well-written and styled (formatting, consistent indentation, comments, etc.).
