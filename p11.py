import FreeSimpleGUI as sg

# Initialize the game board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Initialize the player
player = 'X'

# Create the GUI layout
layout = [
    [sg.Button('', size=(10, 5), key=(i, j)) for j in range(3)] for i in range(3)
]

# Create the GUI window
window = sg.Window('Tic-Tac-Toe', layout)

# Main game loop
while True:
    event, values = window.read()

    # If the window is closed, exit the game loop
    if event == sg.WIN_CLOSED:
        break

    # Get the row and column of the button that was clicked
    row, col = event

    # If the button is already filled, ignore the click
    if board[row][col] != ' ':
        continue

    # Set the player's move on the board
    board[row][col] = player

    # Update the button text to show the player's move
    window[event].update(player)

    # Check if the game is over
    game_over = False
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            game_over = True
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            game_over = True
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        game_over = True
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        game_over = True

    # If the game is over, display the winner and exit the game loop
    if game_over:
        sg.popup(f"{player} wins!")
        break

    # If the game is not over, switch to the other player's turn
    player = 'O' if player == 'X' else 'X'

# Close the GUI window when the game is over
window.close()