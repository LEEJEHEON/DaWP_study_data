import random

class Dice:

    def __init__(self,number=1):
        self.number = number

    def roll(self):
        random_num = random.randint(1,6)
        self.number = random_num

    def getDice(self):
        return self.number

    def __str__(self):
        return "Dice number : " + str(self.number)

    def __eq__(self,other_dice):
        if (self.number)>(other_dice.number):
            return "wins"
        elif (self.number)==(other_dice.number):
            return "ties"
        else :
            return "losses"
