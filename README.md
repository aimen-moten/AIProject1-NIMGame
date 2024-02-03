# NIM Game
## Justification:
This project is intended to be fairly simple, so that you can “ease” your way back into programming if you haven’t done so in a while. Additionally, it will leave you with an implementation of the game of NIM, which you will modify and expand upon in future assignments.
## Description:
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
