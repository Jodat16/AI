import math

# The initial state of the game
INITIAL_STATE = [['X', ' ', ' '], ['O', ' ', ' '], ['X', ' ', 'O']]

def draw_board(board):
    print("-------------")
    print("| " + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + " |")
    print("-------------")
    print("| " + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + " |")
    print("-------------")
    print("| " + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + " |")
    print("-------------")

def get_possible_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
    # Check columns
    for i in range(3):
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    return False

def evaluate(board):
    if check_win(board, 'X'):
        return 1
    elif check_win(board, 'O'):
        return -1
    else:
        return 0

def minimax(board, depth, player):
    if player == 'X':
        best = [-1, -1, -math.inf]
    else:
        best = [-1, -1, math.inf]

    if depth == 0 or check_win(board, 'X') or check_win(board, 'O'):
        score = evaluate(board)
        return [-1, -1, score]

    for move in get_possible_moves(board):
        row, col = move
        board[row][col] = player
        score = minimax(board, depth - 1, 'O' if player == 'X' else 'X')
        board[row][col] = ' '
        score[0], score[1] = row, col

        if player == 'X':
            if score[2] > best[2]:
                best = score
        else:
            if score[2] < best[2]:
                best = score

    return best

def tic_tac_toe():
    board = INITIAL_STATE
    draw_board(board)
    while True:
        row = int(input("Enter row (1-3): ")) - 1
        col = int(input("Enter column (1-3): ")) - 1
        if board[row][col] != ' ':
            print("That spot is already taken!")
            continue
        board[row][col] = 'X'
        draw_board(board)
        if check_win(board, 'X'):
            print("You win!")
            break
        if len(get_possible_moves(board)) == 0:
          print("It's a draw!")
          break

        print("Computer is thinking...")
        row, col, score = minimax(board, 4, 'O')
        board[row][col] = 'O'
        draw_board(board)
        if check_win(board, 'O'):
            print("You lose!")
            break


tic_tac_toe()
