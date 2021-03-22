theBoard = {'top-L':' ','top-M':' ','top-R':' ',
            'mid-L':' ','mid-M':' ','mid-R':' ',
            'bot-L':' ','bot-M':' ','bot-R':' '}

def printBoard(borad):
    print(borad['top-L'] + '|' +borad['top-M'] + '|' +borad['top-R'])
    print('-+-+-')
    print(borad['mid-L'] + '|' +borad['mid-M'] + '|' +borad['mid-R'])
    print('-+-+-')
    print(borad['bot-L'] + '|' +borad['bot-M'] + '|' +borad['bot-R'])

    
turn = 'X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for '+ turn+ '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
printBoard(theBoard)            
     
