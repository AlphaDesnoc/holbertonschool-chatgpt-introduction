#!/usr/bin/python3

def print_board(board):
    """
    Display the current state of the Tic Tac Toe board.

    Parameters:
    - board (list): A 2D list representing the Tic Tac Toe board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there is a winner on the board.

    Parameters:
    - board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
    - bool: True if there is a winner, otherwise False.
    """
    # Check rows for a winner
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns for a winner
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Check if the board is full (no empty spaces left).

    Parameters:
    - board (list): A 2D list representing the Tic Tac Toe board.

    Returns:
    - bool: True if the board is full, otherwise False.
    """
    for row in board:
        if " " in row:
            return False
    return True

def get_valid_input(prompt):
    """
    Prompt the user for input and ensure it is a valid integer within the board's range.

    Parameters:
    - prompt (str): The message to display when asking for input.

    Returns:
    - int: A valid integer input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value in [0, 1, 2]:
                return value
            else:
                print("Invalid input. Please enter 0, 1, or 2.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def tic_tac_toe():
    """
    Main function to play the Tic Tac Toe game.
    """
    board = [[" "]*3 for _ in range(3)]
    player = "X"
    while True:
        print_board(board)
        print(f"Player {player}'s turn.")
        
        # Get valid row and column input
        row = get_valid_input("Enter row (0, 1, or 2): ")
        col = get_valid_input("Enter column (0, 1, or 2): ")

        if board[row][col] == " ":
            board[row][col] = player
            # Check for a winner
            if check_winner(board):
                print_board(board)
                print(f"Player {player} wins!")
                break
            # Check for a draw
            if is_full(board):
                print_board(board)
                print("It's a draw!")
                break
            # Switch players
            player = "O" if player == "X" else "X"
        else:
            print("That spot is already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
