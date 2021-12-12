from os import system, name

board = [' ' for t in range(10)]

def inputLetter(letter, pos):
    board[pos] = letter

def freespace(pos):
    return board[pos] == ' '

def drawBoard(board):
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

def isWinner(bo, le):
    return ((bo[7] == le and bo[8] == le and bo[9] == le) or
            (bo[4] == le and bo[5] == le and bo[6] == le) or
            (bo[1] == le and bo[2] == le and bo[3] == le) or
            (bo[1] == le and bo[4] == le and bo[7] == le) or
            (bo[2] == le and bo[5] == le and bo[8] == le) or
            (bo[3] == le and bo[6] == le and bo[9] == le) or
            (bo[1] == le and bo[5] == le and bo[9] == le) or
            (bo[3] == le and bo[5] == le and bo[7] == le))

def playerMove():
    run = True
    while run:
        move = input('Select a position (1-9): ')
        print("Agent is 'O'")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if freespace(move):
                    run = False
                    inputLetter('X', move)
                else:
                    print('This space is occupied')
            else:
                print('Select a number within 1-9')
        except:
            print('Enter a number yo :/')

def compMove():
    possibleMoves = [t for t, letter in enumerate(board) if letter == ' ' and t != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    corners = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = selectRandom(corners)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    midedges = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            midedges.append(i)

    if len(midedges) > 0:
        move = selectRandom(midedges)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    drawBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            drawBoard(board)
        else:
            print('AGENT WON. DAMN... :(')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('DRAW LMAO')
            else:
                inputLetter('O', move)
                print('AGENT PLACED AT POSITION', move, ':')
                drawBoard(board)
        else:
            print('YOU WON IT! GOOD JOB!! :D')
            break

while True:
    a = input('Play OR Meh? (Y/N)')
    if a.lower() == 'y':
        board = [' ' for t in range(10)]
        print('-----------------------------------')
        main()
    else:
        break
