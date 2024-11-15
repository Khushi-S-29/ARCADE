# helpers.py for Tic Tac Toe

# Function to initialize a 3x3 board
def initialize_board():
    return [['-' for _ in range(3)] for _ in range(3)]

# Function to check if a player has won
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != '-':
            return True

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    return False

# Function to check if the board is full (tie situation)
def is_board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True
