import random

# Initialize empty board
board = [' ' for _ in range(9)]

# Display the board
def display_board():
    print()
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

# Check for winner
def check_winner(symbol):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
        [0, 4, 8], [2, 4, 6]              # diagonals
    ]
    
    for combo in win_combos:
        if all(board[i] == symbol for i in combo):
            return True
    return False


# Check for draw
def is_draw():
    return ' ' not in board

# Player move
def player_move():
    while True:
        try:
            move = int(input("Choose your position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = 'X'
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")
def player2_move():
    while True:
        try:
            move = int(input("Choose your position (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != ' ':
                print("Invalid move. Try again.")
            else:
                board[move] = 'O'
                break
        except ValueError:
            print("Please enter a number between 1 and 9.")
# Computer move
def computer_move():
    empty_positions = [i for i in range(9) if board[i] == ' ']
    if empty_positions:
        move = random.choice(empty_positions)
        board[move] = 'O'
        print("Computer placed an 'O'.")

# Main game loop
def play_game():
    print("Enter the mode you want to play :" \
    "1 for single player" \
    "2 for multiplayer.")
    a= int(input())
    display_board()
    
    if(a==1):
        while True:
            # Player's turn
            player_move()
            display_board()
            if check_winner('X'):
                print("Congratulations! You win! 🎉")
                break
            if is_draw():
                print("It's a draw!")
                break

            # Computer's turn
            computer_move()
            display_board()
            if check_winner('O'):
                print("Computer wins! Better luck next time.")
                break
            if is_draw():
                print("It's a draw!")
                break
    elif(a==2):
        while True:
            # Player's turn
            player_move()
            display_board()
            if check_winner('X'):
                print("Congratulations! player 1 win! 🎉")
                break
            if is_draw():
                print("It's a draw!")
                break
            # Player's 2 turn
            player2_move()
            display_board()
            if check_winner('O'):
                print("Congratulations! player 2 win! 🎉")
                break
            if is_draw():
                print("It's a draw!")
                break
    else:
        print("Invalid option.")  
            


# Start the game
play_game()
