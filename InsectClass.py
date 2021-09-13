import random

# The Coin class simulates a coin that can
# be flipped.

class Insect:
    # The _ _init_ _ method initializes the
    # sideup data attribute with 'Heads'.

    def __init__(self):
        self.distance = 0
        self.legs = 2
        self.wings = 4
    # The toss method generates a random number
    # in the range of 0 through 1. If the number
    # is 0, then sideup is set to 'Heads'.
    # Otherwise, sideup is set to 'Tails'.

    def randistance(self):
        self.distance = random.randint(0,10)
    # The get_sideup method returns the value
    # referenced by sideup.

    def get_distance(self):
            return self.distance
