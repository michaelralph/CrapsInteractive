from random import *
"""Here is the module comment for Dice"""


class Dice:

    def __init__(self):
        self.x = 1
        self.y = 1

    def roll(self):
        # randomly chooses two dice values between 1 and 6 inclusive
        self.x = randrange(1, 7, 1)
        self.y = randrange(1, 7, 1)

    def totaldice(self):
        # returns the total of the two dice
        return self.x + self.y

    def show(self):
        # returns the individual values of the dice
        return self.x, self.y

    def doubles(self):
        # checks if doubles were rolled
        if self.x == 1 and self.y == 1:
            print("You rolled snake eyes!")
        if self.x == 2 and self.y == 2:
            print("You rolled doubles!")
        if self.x == 3 and self.y == 3:
            print("You rolled doubles!")
        if self.x == 4 and self.y == 4:
            print("You rolled doubles!")
        if self.x == 5 and self.y == 5:
            print("You rolled doubles!")
        if self.x == 6 and self.y == 6:
            print("You rolled boxcars!")
