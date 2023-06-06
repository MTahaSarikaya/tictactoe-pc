import random
import time

# tahtayi belirle
board = [' ' for x in range(9)]

# tahtayi cizme
def print_board():
    row1 = '|{}|{}|{}|'.format(board[0], board[1], board[2])
    row2 = '|{}|{}|{}|'.format(board[3], board[4], board[5])
    row3 = '|{}|{}|{}|'.format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

# kazanan olup olmadigini kontrol et
def check_winner(board, player):
    # sira
    if board[0] == board[1] == board[2] == player or \
       board[3] == board[4] == board[5] == player or \
       board[6] == board[7] == board[8] == player:
        return True

    # sütun
    if board[0] == board[3] == board[6] == player or \
       board[1] == board[4] == board[7] == player or \
       board[2] == board[5] == board[8] == player:
        return True

    # caprazlar
    if board[0] == board[4] == board[8] == player or \
       board[2] == board[4] == board[6] == player:
        return True

    return False

# oyun kismi
def play():
    # ilk oyuncuyu rastgele belirle
    first_player = random.choice(['X', 'O'])
    print('The first player is', first_player)

    # bir taraf kazanana kadar veya tahta dolana kadar devam et 
    while True:
        # X in sirasi
        if first_player == 'X':
            # Choose a random move
            move = random.choice([x for x, letter in enumerate(board) if letter == ' '])
            board[move] = 'X'
            print_board()

            # Check if X wins
            if check_winner(board, 'X'):
                print('X kazandi!')
                break

        # O nun sirasi
        else:
            # rastgele hamle
            move = random.choice([x for x, letter in enumerate(board) if letter == ' '])
            board[move] = 'O'
            print_board()

            # O nun kazanip kazanmadigini kontrol et
            if check_winner(board, 'O'):
                print('O kazandi!')
                break

        # tahtanin dolu olup olmadigini kontrol et
        if ' ' not in board:
            print('Berabere!')
            break

        # hareketler arasindaki süre
        time.sleep(2)

        # oyuncu degisimi
        if first_player == 'X':
            first_player = 'O'
        else:
            first_player = 'X'

play()
