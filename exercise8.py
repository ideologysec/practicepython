# http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html
# rock paper scissors + while loops

import random

sourceList = ['rock','scissors','paper']
win = "Player ONE WINS! HURRAH! 🎉"
lose = "Player TWO WINS. YOU LOSE!! :("

print ("Welcome to Rock Paper Scissors. You know how to play.")

while True:
    player1 = input("Player ONE - Enter your choice: ").replace(" ", "").lower()
    #player2 = input("Player TWO - Enter your choice:").replace(" ", "").lower()
    
    player2 = sourceList[random.randint(0,2)]
    print(player2)

    if (player1 == player2):
        print("Draw!")

    elif player1.startswith( 'p' ):
        if player2.startswith( 'r' ):
            print(win)
        else: print(lose)

    elif player1.startswith('r'):
        if player2.startswith('s'):
            print(win)
        else: print(lose)

    else:
        if player2.startswith('p'):
            print(win)
        else: print(lose)

    again = input("Play again? (Y/y)es or anything else for (N/n)o: ").lower()

    if (again.startswith('y')):
        continue
    else: break