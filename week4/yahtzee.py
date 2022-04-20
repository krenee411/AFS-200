'''this is a game of yahtzee and it takes in any number of dice with any number of faces and prints the results'''
import random

class Die:

    def __init__(self,faces):
        self.faces = faces
        self.value = 1

    def roll(self):
        self.value = random.randint(1,self.faces)
        return self.value


    # you have to actually get a value not set it so it needs a return!
    def getCurrentFaceValue(self):
        return self.value 
        
        # this is showing somthing it has to print. 
    def showDieFace(self):
        print(f'({self.value})')
    

def gen_dice(amount, faces):
    dice_list = [Die(faces) for die in range(amount)]
    return dice_list


# print(gen_dice(3,4))

# def play(dice):
#     values = [die.roll() for die in dice]
#     for die in values:
#         print(f"({die})", end=" ")
#     result = values.count(values[0]) == len(values)
#     if result:
#         print("\nYAHTZEE")

def play(dice):
    for die in dice:
        die.roll()

    for die in dice:
        die.showDieFace()
        if dice[0].roll() == dice.getCurrentFaceValue:
            print("got it")
            
    
        

       



our_dice = gen_dice(3,2)
play(our_dice)




