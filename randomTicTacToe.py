from random import randint
def tictactoe():
    board = [0,1,2,3,4,5,6,7,8]
    player = 1
    win = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for time_outer in range(0,9):
        selection = randint(0,8-time_outer)
        board_index = -1
        for time_inner in range(0,9):
            if (board[time_inner] < 9):
                board_index += 1
            if (board_index == selection):
                board_index = time_inner
                break
        if (player != 1 and player != 2):
            return 3
        board[board_index] = player+8
        for i in range(0,8):
            set_ = {board[win[i][0]],board[win[i][1]],board[win[i][2]]}
            if (len(set_)==1):
                return player
        if (player == 1):
            player = 2
        elif (player == 2):
            player = 1
        else:
            return 3
    return 0
outcomes = [0,0,0,0]
numOfGames = input("Number of games: ")
if (numOfGames.isdecimal()):
    numOfGames = int(numOfGames)
    if (numOfGames > 0 and numOfGames <= 100000):
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
