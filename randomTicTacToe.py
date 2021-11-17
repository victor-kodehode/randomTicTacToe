# used to randomly pick moves
from random import randint

def tictactoe():
    # the 3x3 board represented as a line of 9 elements
    # 0 : blank square
    # 1 : square filled in by player 1
    # 2 : square filled in by player 2
    board = [0,0,0,0,0,0,0,0,0]
    # starting player
    player = 1
    for time_outer in range(0,9):
        # if it's player 1's turn
        if (player == 1):
            selection = randint(0,8-time_outer)
            board_index = -1
            for time_inner in range(0,9):
                if (board[time_inner] == 0):
                    board_index += 1
                if (board_index == selection):
                    board_index = time_inner
                    break
            board[board_index] = 1
        # if it's player 2's turn
        elif (player == 2):
            selection = randint(0,8-time_outer)
            board_index = -1
            for time_inner in range(0,9):
                if (board[time_inner] == 0):
                    board_index += 1
                if (board_index == selection):
                    board_index = time_inner
                    break
            board[board_index] = 2
        # if it's somehow nobody's turn
        else:
            print("error 2")
            return 3
        # check if game is won
        if(board[0] == board[1] == board[2] != 0):
            return player
        if(board[3] == board[4] == board[5] != 0):
            return player
        if(board[6] == board[7] == board[8] != 0):
            return player
        if(board[0] == board[3] == board[6] != 0):
            return player
        if(board[1] == board[4] == board[7] != 0):
            return player
        if(board[2] == board[5] == board[8] != 0):
            return player
        if(board[0] == board[4] == board[8] != 0):
            return player
        if(board[2] == board[4] == board[6] != 0):
            return player
        # swap player for next turn
        if (player == 1):
            player = 2
        elif (player == 2):
            player = 1
        else:
            print("error 1")
            return 3
        # end of loop block
    return 0
# index 0 : tie
# index 1 : player 1 wins
# index 2 : player 2 wins
# index 3 : error
# this list will keep count of the game outcomes
outcomes = [0,0,0,0]
# how many games does the user want the program to play?
# limited to integers from 1 to 10000
numOfGames = input("Number of games: ")
# checks if the user's input is valid
if (numOfGames.isdecimal()):
    numOfGames = int(numOfGames)
    if (numOfGames > 0 and numOfGames <= 10000):
        # counts the game outcomes
        for x in range(0,numOfGames):
            outcomes[tictactoe()] += 1
        print(f"{numOfGames} games later...\nHere are the results:")
        print(f"Player 1 wins {outcomes[1]} games.")
        print(f"Player 2 wins {outcomes[2]} games.")
        print(f"{outcomes[0]} games end in a tie.")
    else:
        print("invalid")
else:
    print("invalid")