# Instructions
# The game is played on a grid that’s 3 squares by 3 squares.
# Players take turns putting their marks (O or X) in empty squares.
# The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
# When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


# Hint
# To do this project, you basically need to create four functions:

# display_board() – To display the Tic Tac Toe board (GUI).
# player_input(player) – To get the position from the player.
# check_win() – To check whether there is a winner or not.
# play() – The main function, which calls all the functions created above.
# Note: The 4 functions above are just an example. You can implement many more helper functions or choose a completely different appoach if you want.

# Tips : Consider The Following:
# What functionality will need to accur every turn to make this program work?
# After contemplating the question above, think about splitting your code into smaller pieces (functions).
# Remember to follow the single responsibility principle! each function should do one thing and do it well!


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