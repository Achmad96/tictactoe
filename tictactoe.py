import math

game_board = [
    [" "] * 3,
    [" "] * 3,
    [" "] * 3
]

def print_board():
    print(end="\n")
    for i in range(len(game_board)):
        print(f"{game_board[i]}", end = "\n")

def update_board(game_board, k, player):
    p = math.ceil(k / len(game_board))
    q = (k - 1) % len(game_board)
    if game_board[p-1][q] != " ":
        print("The location is exists")
        return
    game_board[p - 1][q] = "X" if player == 1 else "O"

def validate_board(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return player
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return player

def stop_game():
    exit(0)

print('''
*********************

      TIC-TAC-TOE

*********************''')
def game(player):
    print_board()
    who = 1 if player == 2 else 2
    try:
        k = int(input(f"Player-{player}: "))
        if k < 1 or k > 9: 
            print("The input must be between 1 and 9")
            game(player)
        update_board(game_board, k, player)
    except:
        game(who)
    whoWins = validate_board(game_board, "X" if player == 1 else "O")
    if whoWins is not None:
        print_board()
        print(f"Player {"1" if whoWins == "X" else "2"} wins")
        stop_game()
    game(who)

if __name__ == "__main__":
    game(1);