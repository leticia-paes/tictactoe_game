from IPython.display import clear_output

board = ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
marker = ['', '']


def display_board(board):
    clear_output()
    print(board[7] + '|' + board[8] + '|' + board[9])
    print('------')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('------')
    print(board[1] + '|' + board[2] + '|' + board[3])


def player_input():
    acclst = ['X', 'x', 'O', 'o']
    answ = 'wrong'
    global marker

    while answ not in acclst:
        answ = input("Please pick a marker 'X' or 'O':")
    if answ == 'X' or answ == 'x':
        player1_marker = 'X'
        player2_marker = 'O'
    else:
        player1_marker = 'O'
        player2_marker = 'X'
    print(f'Player One: {player1_marker}')
    print(f'Player Two: {player2_marker}')
    marker = [player1_marker, player2_marker]


def place_marker1(marker):
    global board
    cond = True

    while cond:

        position1 = int(input('Player 1: Choose a position (1-9):'))
        if position1 in range(1, 10):

            if board[position1] == ' ':
                board[position1] = marker[0]
                cond = False
            else:
                print('This position is not available.')
                continue
        else:
            continue


def place_marker2(marker):
    global board
    cond = True

    while cond:

        position2 = int(input('Player 2: Choose a position (1-9):'))
        if position2 in range(1, 10):

            if board[position2] == ' ':
                board[position2] = marker[1]
                cond = False
            else:
                print('This position is not available.')
                continue
        else:
            continue


def win_check(board):
    win = False
    if 'X' or 'O' in board:
        if board[1] == board[2] == board[3] != ' ':
            return True

        elif board[4] == board[5] == board[6] != ' ':
            return True

        elif board[7] == board[8] == board[9] != ' ':
            return True

        elif board[1] == board[4] == board[7] != ' ':
            return True

        elif board[2] == board[5] == board[8] != ' ':
            return True

        elif board[3] == board[6] == board[9] != ' ':
            return True

        elif board[7] == board[5] == board[3] != ' ':
            return True

        elif board[1] == board[5] == board[9] != ' ':
            return True
        else:
            return False


def full_board_check(board):
    if ' ' in board:
        return False
    else:
        return True


# Início da lógica de jogo:
ans = 'Y'
while ans == 'Y':
    clear_output()
    print('Welcome to Tic Tac Toe!')
    player_input()

    while not full_board_check(board) and not win_check(board):
        display_board(board)
        place_marker1(marker)
        display_board(board)
        if not full_board_check(board) and not win_check(board):
            place_marker2(marker)
            display_board(board)
        full_board_check(board)
        win_check(board)

    if full_board_check(board):

        print("It's a tie!")
        ans = input("Do you want to play again? ('Y' or 'N')")
        if ans == 'Y' or ans == 'y':
            continue
        elif ans == 'N' or 'n':
            break


    elif win_check(board):
        print('Congratualtions! You won!')
        ans = input("Do you want to play again? ('Y' or 'N')")
        if ans == 'Y' or ans == 'y':
            continue
        elif ans == 'N' or 'n':
            break