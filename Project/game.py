import random

def print_board(board):
    """Displays the game board."""
    print(f"\n {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_winner(board, player):
    """Checks if the given player has won."""
    # All winning combinations (rows, columns, diagonals)
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
        (0, 4, 8), (2, 4, 6)             # Diagonals
    ]
    
    for a, b, c in win_conditions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def is_draw(board):
    """Checks if the board is full (draw)."""
    return " " not in board

def computer_move(board):
    """Computer picks a random empty spot."""
    # Find all indices that are still " "
    empty_spots = [i for i, spot in enumerate(board) if spot == " "]
    if empty_spots:
        return random.choice(empty_spots)
    return None

def play_game():
    board = [" " for _ in range(9)] # Create empty board
    human = "X"
    computer = "O"
    
    print("Welcome to Tic-Tac-Toe!")
    print("Enter a number (1-9) to place your X.")
    
    while True:
        print_board(board)
        
        # --- Human Turn ---
        try:
            move = int(input("Your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("Invalid move! Try again.")
                continue
        except ValueError:
            print("Please enter a number.")
            continue

        board[move] = human
        
        if check_winner(board, human):
            print_board(board)
            print("🎉 You Win!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a Draw!")
            break

        # --- Computer Turn ---
        comp_move = computer_move(board)
        board[comp_move] = computer
        print(f"Computer chose position {comp_move + 1}")
        
        if check_winner(board, computer):
            print_board(board)
            print("💻 Computer Wins!")
            break
        if is_draw(board):
            print_board(board)
            print("It's a Draw!")
            break

if __name__ == "__main__":
    play_game()