
'''
Tic-Tac-Toe: Game with x and o alignment as a "cse210-01" project
Author: Kosei Kameta
Published 2022_01_21

Although not yet completed, I am expanding this program to bord side
larger than 3 is not yet completed. But some parts are ready for >3.

'''

from msilib.schema import Billboard

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))  # change directory


def main():

    print()

    # size = int(input('Inpust a squire board size: '))
    size = 3  # currently size is fixed to 3, but this can be changed in future version

    player = input('\033[33m' + 'Which do you want to play first? (x or o): ' + '\033[39m')
    # player = next_player("") 
    
    board = set_bord(size)
    while not (judge_winner(board) or game_finished(board, size)):
        show_board(board, size)
        next_turn(player, board)
        player = next_player(player)
    show_board(board, size)

    if judge_winner(board):
        print(f"Congraturations! '{next_player(player)}' is the winner!") 
    elif game_finished(board, size):
        print("This game is draw! Try again.") 

    print()
    print("Game finished. Please try again!") 
    print()



# bord initialization by filling numbers
def set_bord(size):
    board = []
    for position in range(3*size):
        board.append(position + 1)
    return board


# re-drawing the boad on screen 
def show_board(board, size):
    print()
    for raw in range(size):
        for i in range(size-1):
            print(str(board[i + raw * size]) + '|', end='')
        print(str(board[size - 1 + raw * size]))
        if raw != (size - 1):
            for i in range(size-1):
                print('-+' , end='')
            print('-')    
    print()
 

def game_finished(board, size):
    for position in range(3 * size):
        if board[position] != "x" and board[position] != "o":
            return False
    return True 

# detect the game termination
def judge_winner(board):
    if  board[0] == board[1] == board[2] or \
        board[3] == board[4] == board[5] or \
        board[6] == board[7] == board[8] or \
        board[0] == board[3] == board[6] or \
        board[1] == board[4] == board[7] or \
        board[2] == board[5] == board[8] or \
        board[0] == board[4] == board[8] or \
        board[2] == board[4] == board[6]:
        return(True)

# next turn message to prompt number inputing
def next_turn(player, board):
    position = int(input(f"{player}'s turn to choose a position number: "))
    board[position - 1] = player

# switch the plaer
def next_player(current_player):
    if current_player == "" or current_player == "o":
        return "x"
    elif current_player == "x":
        return "o"

if __name__ == "__main__":
    main()

# BLACK          = '\033[30m'#(文字)黒
# RED            = '\033[31m'#(文字)赤
# GREEN          = '\033[32m'#(文字)緑
# YELLOW         = '\033[33m'#(文字)黄
# BLUE           = '\033[34m'#(文字)青
# MAGENTA        = '\033[35m'#(文字)マゼンタ
# CYAN           = '\033[36m'#(文字)シアン
# WHITE          = '\033[37m'#(文字)白
# COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す