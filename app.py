def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
    if board[0][0] == board[1][1] == board[2][2] == player or \
       board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def is_draw(board):
    """Checks if the game is a draw."""
    return all(cell in ['X', 'O'] for row in board for cell in row)

def tic_tac_toe():
    """Main function to play Tic Tac Toe."""
    while True:
        board = [[' ' for _ in range(3)] for _ in range(3)]

        # Allow players to choose their symbols
        player1 = input("Player 1, choose your symbol (X/O): ").upper()
        while player1 not in ['X', 'O']:
            print("Invalid choice. Please choose 'X' or 'O'.")
            player1 = input("Player 1, choose your symbol (X/O): ").upper()

        player2 = 'O' if player1 == 'X' else 'X'
        print(f"Player 1 is {player1} and Player 2 is {player2}")

        current_player = player1

        while True:
            print_board(board)
            print(f"Player {current_player}'s turn")

            # Get the player's move
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
            except ValueError:
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue

            # Check if the move is valid
            if row not in range(3) or col not in range(3) or board[row][col] != ' ':
                print("Invalid move. Try again.")
                continue

            # Make the move
            board[row][col] = current_player

            # Check for a winner
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break

            # Check for a draw
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break

            # Switch players
            current_player = player2 if current_player == player1 else player1

        # Ask if players want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    tic_tac_toe()