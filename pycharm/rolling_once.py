import dice
a=dice.Dice()
b=dice.Dice()

for i in range(1,4):
    a.roll()
    b.roll()
    print("Player 1: {} \n Player 2 : {} \n Player 1 {} \n\n".format(a.getDice(),b.getDice(),a.__eq__(b)))