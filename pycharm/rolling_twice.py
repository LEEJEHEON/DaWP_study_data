import dice
import random

a=dice.Dice()
b=dice.Dice()

for i in range(1,4):
    c = 0
    d = 0
    for j in range(1,3):
        a.roll()
        b.roll()
        c += a.getDice()
        d += b.getDice()
    if c > d:
        print("Player 1 : {} \n Player 2 : {} \n Player 1 wins \n\n".format(c,d) )
    elif c==d:
        print("Player 1 : {} \n Player 2 : {} \n Tie\n\n".format(c, d))
    else :
        print("Player 1 : {} \n Player 2 : {} \n Player 2 wins\n\n".format(c, d))