def display_board(board):
# This function prints the board UI
    print("----+----+----")
    for row in range(0,len(board)):
        print("|", board[row][0], "|", board[row][1], " |", board[row][2], "|")
        print("----+----+----")
    return board

# Check if a player has won
def check_winner(board, player):
    # Check rows
    for row in board:
        if all(cell == player for cell in row):
            return True

    # Check columns
    for col in range(3):
        if all(row[col] == player for row in board):
            return True

    # Check diagonals
    if all(board[index][index] == player for index in range(3)) or all(board[index][2 - index] == player for index in range(3)):
        return True

    return False

# Check if the board is full
def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

# The game itself
def game():
# Initialize an empty board
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]
    current_player = "X"

    while True:
        # Display the current state of the board
        display_board(board)
        
        # Get the move (row and column)
        row, col = map(int, input(f"Player {current_player}, enter row (0-2) and column (0-2) separated by space: ").split())

        # Check if the selected cell is empty
        if board[row][col] == " ":
            # Place the player's symbol in the selected cell
            board[row][col] = current_player

            # Check if the current player has won
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break
            # Check if the board is full (a draw)
            elif is_board_full(board):
                display_board(board)
                print("It's a draw!")
                break
            else:
                # Switch to the other player
                current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("That cell is already occupied. Try again.")

game()