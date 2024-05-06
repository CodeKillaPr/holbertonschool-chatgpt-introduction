def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    moves = 0
    while not check_winner(board) and moves < 9:
        print("\nCoordinates for the board:")
        print(" 0 | 1 | 2 ")
        print("-----------")
        print(" 3 | 4 | 5 ")
        print("-----------")
        print(" 6 | 7 | 8 ")
        print_board(board)
        try:
            move = int(input("\nEnter a position (0-8) for player " + player + ": "))
            if move < 0 or move > 8:
                raise ValueError("Position out of range.")
        except ValueError:
            print("Invalid input. Please enter a number between 0 and 8.")
            continue
        row = move // 3
        col = move % 3
        if board[row][col] == " ":
            board[row][col] = player
            moves += 1
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")
    print_board(board)
    if check_winner(board):
        print("Player " + player + " wins!")
    else:
        print("Game Over. It's a tie!")

tic_tac_toe()
