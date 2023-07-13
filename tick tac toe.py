#TicTacToe
import random
EMPTY = '[ ]'

#operations (sub-tasks)
def display_board(board):
    print()
    for row in board:
        for col in row:
            print(col, end='')
        print()

def toss(call):
    return call == random.choice(['heads','tails'])

def is_full(board):
    for row in board:
        for col in row:
            if col == EMPTY:
                return False
    return True 

def validate_move(board, row, col):
    if row <0 or row > 2:
        return False
    elif col < 0 or col > 2:
        return False
    elif board[row][col] != EMPTY:
        return False
    else:
        return True

def wins(board, symbol):
    #horizontal check
    for i in range(3):
        if board[i][0] == symbol and board[i][1] == symbol and board[i][2] == symbol:
            return True
    # vertical check
    for i in range(3):
        if board[0][i] == symbol and board[1][i] == symbol and board[2][i] == symbol:
            return True
    #diagnols check
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol:
        return True
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol:
        return True

    return False #not a win

def tic_tac_toe():
    #Entities : Data Sttructures
    #Board
    board = [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY],[EMPTY, EMPTY, EMPTY]]
    #Players
    players = [input('Enter name of Player1 ').title(), input('Enter name of Player2 ').title()]
    #Symbols
    symbols = ['[X]', '[0]'] #preset

    #Toss to decide the order of playing
    print(players[0], 'flips the coin ')
    print(players[1], 'makes a call (heads/tails) ')
    call = input().lower()
    if toss(call):
        print(players[1], 'wins the toss and starts the game!!!')
        current_player = 1
    else:
        print(players[1], 'loses the toss, hence', players[0], 'starts the game!!!')
        current_player = 0

    is_there_a_win = False #assume

    #lets play until the board is not full
    while not is_full(board):
        display_board(board)
        print(players[current_player], symbols[current_player], ' plays ')
        print('Enter row coordinate (0-2)')
        row = int(input())
        print('Enter column coordinate (0-2)')
        col = int(input())

        if validate_move(board, row, col):
            #apply the move
            board[row][col] = symbols[current_player]
            #is this a win
            if wins(board, symbols[current_player]): #lets play until theres a win
                display_board(board)
                print(players[current_player], 'WINS!!!')
                is_there_a_win = True
                break #stop the game
            else:
                #change the player
                current_player = (current_player+1) % 2
        else:
            print('Invalid Move!!!')

    if is_there_a_win == False:
        display_board(board)
        print('GAME DRAW!!!')

def main():
    tic_tac_toe()

main() 