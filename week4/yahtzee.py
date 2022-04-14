'''this is a game of yahtzee and it takes in any number of dice with any number of faces and prints the results'''
import random

class Die:

    def __init__(self,faces):
        self.faces = faces


    def roll(self):
        roll_value = random.randint(1,self.faces)
        return roll_value

    def getCurrentFaceValue(self,roll_value):
        self.faces = roll_value
        
    def showDieFace(self):
        return self.faces
    

def gen_dice(amount, faces):
    dice_list = [Die(faces) for die in range(amount)]
    return dice_list


# print(gen_dice(3,4))

def play(dice):
    values = [die.roll() for die in dice]
    for die in values:
        print(f"({die})", end=" ")
    result = values.count(values[0]) == len(values)
    if result:
        print("\nYAHTZEE")

    

our_dice = gen_dice(5,1)
our_dice
play(our_dice)




