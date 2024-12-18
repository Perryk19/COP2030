
import random

class Dice:
    def __init__(self):
        # Initialize the faceValue to 1 when the dice is created
        self.faceValue = 1

    def roll(self):
        # Generate a random number between 1 and 6
        self.faceValue = random.randint(1, 6)

    def getFaceValue(self):
        # Return the current faceValue of the dice
        return self.faceValue
