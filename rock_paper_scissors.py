import random, sys

print('ROCK, PAPER, SCISSORS')
#These variables keep track of numbers of wins, losses, and ties.
wins = 0
losses = 0
ties = 0

while True: # The main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    
    while True: # The player input loop:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input().lower()
        if playerMove == 'q':
            sys.exit() #Quit the program
        if playerMove == 'r' or playerMove =='p' or playerMove =='s':
            break #Break out of the player input loop   
        print('Type one of r,p,s or q.')    

    #Display what the player chose:
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('SCISSORS versus...')
    
    #Display what the computer chose:
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('SCISSORS')

    #from here it's my code
    # 
    #Compare who is the winner:
    #Ties
    if playerMove == 'r' and computerMove =='r':
        print('It is a tie!')
        ties = ties + 1
    if playerMove == 's' and computerMove == 's':
        print('It is a tie!') 
        ties += 1
    if playerMove =='p' and computerMove =='p':
        print('It is a tie!') 
        ties += 1 

    #Wins
    if playerMove =='p' and computerMove =='r':
        print('You won!')
        wins += 1                 
    if playerMove =='s' and computerMove =='p':
        print('You won!')
        wins += 1                         
    if playerMove =='r' and computerMove =='s':
        print('You won!')
        wins += 1               
                            
    #Losses
    if playerMove == 'p' and computerMove == 's':
        print('You lost...')
        losses += 1
    if playerMove == 's' and computerMove == 'r':
        print('You lost...')
        losses += 1
    if playerMove == 'r' and computerMove == 'p':
        print('You lost...')
        losses += 1  

print('hi!')
print('this will be merged')
 
      
