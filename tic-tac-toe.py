import random

board = ""
number_plays = 0

def reset_board(board):
    board = list(range(1,10))
    return board

def print_board(board):
    print("")
    print(str(board[0]) + "|" + str(board[1]) + "|" + str(board[2]))
    print(str(board[3]) + "|" + str(board[4]) + "|" + str(board[5]))
    print(str(board[6]) + "|" + str(board[7]) + "|" + str(board[8]))
    print("")

def check_win(board):
    #Return 0 if X wins, 1 if O wins
    if board[1] == board[4] == board[7] or board[3] == board[4] == board[5] or board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        if board[4] == "X":
            return 0
        elif board[4] == "O":
            return 1
        else:
            print("An invalid input was detected. Quitting.")
            exit()
    if board[0] == board[1] == board[2] or board[0] == board[3] == board[6]:
        if board[0] == "X":
            return 0
        elif board[0] == "O":
            return 1
        else:
            print("An invalid input was detected. Quitting.")
            exit()
    if board[2] == board[5] == board[8] or board[6] == board[7] == board[8]:
        if board[8] == "X":
            return 0
        elif board[8] == "O":
            return 1
        else:
            print("An invalid input was detected. Quitting.")
            exit()

board = reset_board(board)

print("Welcome to tic-tac-toe. This is the board:")
print_board(board)
print("To play, simply type the number correspondent to the square you want to play in.")

while True:
    single_or_multi = input("Do you want to play against the computer or another person (C/P)? ")
    if single_or_multi == "C" or single_or_multi == "P":
        break
    print("Sorry, I didn't get that. Try again.")

if single_or_multi == "C":
    while True:
        x_or_o = input("Do you want to play as \"X\" or \"O\" (X/O)? ")
        if x_or_o == "X" or x_or_o == "O":
            break
    print("Sorry, I didn't get that. Try again.")
    print("Let's start. Here's the board:")
    while True: #Running until the game is over
        while True: #Running until the player picks a valid square
            print_board(board)
            play = int(input("Where do you want to play (1-9)? "))
            if play in range(1, 10):
                if int(board[play - 1]) in range(1, 10):
                    break
            else:
                print("Invalid input. Try again.")
        board[play - 1] = x_or_o
        number_plays += 1
        if number_plays == 9:
            print("It's a draw!")
            exit()
        if number_plays >= 5:
            if check_win(board) == 0 or check_win(board) == 1:
                break
        while True: #Computer play
            computer_play = random.randint(0,8)
            if board[computer_play] in list(range(1, 9)):
                if x_or_o == "X":
                    board[computer_play] = "O"
                    break
                elif x_or_o == "O":
                    board[computer_play] = "X"
                    break
        number_plays += 1
    if check_win(board) == 0:
        print("X wins!")
        print_board(board)
        exit()
    elif check_win(board) == 1:
        print("O wins!")
        print_board(board)
        exit()

if single_or_multi == "P":
    while True:
        x_or_o = input("Is player 1 play as \"X\" or \"O\" (X/O)? ")
        if x_or_o == "X" or x_or_o == "O":
            break
        print("Sorry, I didn't get that. Try again.")
    if x_or_o == "X":
        print("Player 1 will start. They're playing as \"X\".")
    elif x_or_o == "O":
        print("Player 1 will start. They're playing as \"O\".")
    else:
        print("Something went wrong in the symbol selecting. Exiting")
        exit()
    print("Here's the board:")
    while True: #Running until the player picks a valid square
        print_board(board)
        play = int(input("Player 1, where do you want to play (1-9)? "))
        if play in range(1, 10):
            if int(board[play - 1]) in range(1, 10):
                board[play - 1] = x_or_o
        else:
            print("Invalid imput. Try again.")
        number_plays += 1
        if number_plays == 9:
            print("It's a draw!")
            exit()
        if number_plays >= 5:
            if check_win(board) == 0 or check_win(board) == 1:
                break
        print_board(board)
        play = int(input("Player 2, where do you want to play (1-9)? "))
        if play in range(1, 10):
            if int(board[play - 1]) in range(1, 10):
                if x_or_o == "X":
                    board[play - 1] = "O"
                else:
                    board[play - 1] = "X"
        else:
            print("Invalid imput. Try again.")
        number_plays += 1
        if number_plays == 9:
            print("It's a draw!")
            exit()
        if number_plays >= 5:
            if check_win(board) == 0 or check_win(board) == 1:
                break
    if check_win(board) == 0:
        print("X wins!")
        print_board(board)
        exit()
    elif check_win(board) == 1:
        print("O wins!")
        print_board(board)
        exit()