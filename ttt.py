import math

          # Initialize the Tic-Tac-Toe board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

             # Check if there are empty spots on the board
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

              # Evaluate the board to determine if there's a winner
def evaluate(board):
    # Check rows for a win
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return 10 if row[0] == 'X' else -10

              # Check columns for a win
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return 10 if board[0][col] == 'X' else -10

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return 10 if board[0][0] == 'X' else -10
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return 10 if board[0][2] == 'X' else -10

                  # No one has won yet
    return 0

# The Minimax algorithm
def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    score = evaluate(board)

              # If the maximizer (X) has won, return the score
    if score == 10:
        return score - depth

            # If the minimizer (O) has won, return the score
    if score == -10:
        return score + depth

             # If there are no more moves and no winner, it's a tie
    if not is_moves_left(board):
        return 0

    # If it's the maximizer's move
    if is_maximizing:
        best = -math.inf

                    # Traverse all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Make the move
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, not is_maximizing, alpha, beta))
                    alpha = max(alpha, best)
                    # Undo the move
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
        return best

                # If it's the minimizer's move
    else:
        best = math.inf

        # Traverse all cells
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    # Make the move
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, not is_maximizing, alpha, beta))
                    beta = min(beta, best)
                    # Undo the move
                    board[i][j] = ' '
                    if beta <= alpha:
                        break
        return best

                     # Find the best move for the AI
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

              # Check if the game is over (win or draw)
def is_game_over(board):
    return evaluate(board) != 0 or not is_moves_left(board)

# Main game loop
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        # Human player's move
        row, col = map(int, input("Enter your move (row and column): ").split())
        if board[row][col] != ' ':
            print("Invalid move. Try again.")
            continue

        board[row][col] = 'O'
        print_board(board)

        if is_game_over(board):
            break

        # AI's move
        print("AI's move:")
        ai_move = find_best_move(board)
        board[ai_move[0]][ai_move[1]] = 'X'
        print_board(board)

        if is_game_over(board):
            break

    # Check the final result
    score = evaluate(board)
    if score == 10:
        print("AI wins!")
    elif score == -10:
        print("You win!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
