import random

# Create the Tic-Tac-Toe board
board = [' '] * 9

# Define a function to display the Tic-Tac-Toe board
def display_board():
    print(board[0] + '|' + board[1] + '|' + board[2])
    print('-|-|-')
    print(board[3] + '|' + board[4] + '|' + board[5])
    print('-|-|-')
    print(board[6] + '|' + board[7] + '|' + board[8])

# Define a function to check if the player has won
def check_win(player):
    if (board[0] == board[1] == board[2] == player or
        board[3] == board[4] == board[5] == player or
        board[6] == board[7] == board[8] == player or
        board[0] == board[3] == board[6] == player or
        board[1] == board[4] == board[7] == player or
        board[2] == board[5] == board[8] == player or
        board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player):
        return True
    else:
        return False

# Define a function to play the game
def play_game():
    # Set the first player to 'X'
    current_player = 'X'

    # Loop until the game is over
    while True:
        # Display the Tic-Tac-Toe board
        display_board()

        # Get the current player's move
        if current_player == 'X':
            position = int(input('Player X, enter a position (1-9): '))
        else:
            position = int(input('Player O, enter a position (1-9): '))

        # Update the board with the current player's move
        if board[position-1] == ' ':
            board[position-1] = current_player
        else:
            print('That position is already taken. Please choose a different position.')
            continue

        # Check if the game is over
        if check_win(current_player):
            print('Player', current_player, 'wins!')
            break
        elif ' ' not in board:
            print('The game is a tie!')
            break

        # Switch to the other player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Start the game
play_game()
