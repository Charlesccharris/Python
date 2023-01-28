import random


print("Welcome to Yahtzee")
name = input("(R)ules or (P)lay? :")

if('r' in name or 'R' in name):
    print("Rules of Yahtzee")
    Rules.rule
elif('p' in name or 'P' in name):
    print("This is Yahtzee")
    PlayYahtzee()
else:
    print("That is not a valid option")

dice = int()

#for x in range(5):
    #dice = random.randrange(1, 6)
   # print(dice)
   
class PlayYahtzee:
    def play():
        print("BYE")

class Rules:
    def rule():
        print("HI")
    
