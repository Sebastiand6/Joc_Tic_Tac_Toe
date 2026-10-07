def print_board(board):
    print(f"\n {board[0]} | {board[1]} | {board[2]} \n---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} \n---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} \n")

def check_win(board):
    wins = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for w in wins:
        if board[w[0]] == board[w[1]] == board[w[2]]:
            return 1 if board[w[0]] == 'X' else 2
    return 0

def check_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def minimax(board, is_max):
    score = check_win(board)
    if score == 2: return 10
    if score == 1: return -10
    if check_draw(board): return 0

    if is_max:
        best = -1000
        for i in range(9):
            if board[i] not in ['X', 'O']:
                backup = board[i]
                board[i] = 'O'
                best = max(best, minimax(board, False))
                board[i] = backup
        return best
    else:
        best = 1000
        for i in range(9):
            if board[i] not in ['X', 'O']:
                backup = board[i]
                board[i] = 'X'
                best = min(best, minimax(board, True))
                board[i] = backup
        return best

def execute_player_move(board):
    while True:
        try:
            choice = int(input("Alege o poziție (1-9): ")) - 1
            if 0 <= choice <= 8 and board[choice] not in ['X', 'O']:
                board[choice] = 'X'
                break
            print("Mutare invalidă. Încearcă din nou.")
        except ValueError:
            print("Te rog introdu un număr valid.")

def execute_computer_move(board):
    best_val = -1000
    best_move = -1
    for i in range(9):
        if board[i] not in ['X', 'O']:
            backup = board[i]
            board[i] = 'O'
            move_val = minimax(board, False)
            board[i] = backup
            if move_val > best_val:
                best_move = i
                best_val = move_val
    
    board[best_move] = 'O'
    print(f"Computerul a ales poziția {best_move + 1}")

def play_game(board):
    player_turn = True
    status = 0
    while status == 0:
        print_board(board)
        if player_turn:
            execute_player_move(board)
        else:
            execute_computer_move(board)
            
        status = check_win(board)
        if status == 0 and check_draw(board):
            status = -1
        player_turn = not player_turn
        
    print_board(board)
    return status

def main():
    board = [str(i + 1) for i in range(9)]
    final_status = play_game(board)
    
    if final_status == 1:
        print("Ai câștigat!")
    elif final_status == 2:
        print("Computerul a câștigat!")
    else:
        print("Egalitate!")

if __name__ == "__main__":
    main()
