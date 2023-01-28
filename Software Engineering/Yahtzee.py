import random
diceList = []
dice = int()
answer = ""

def Rules():
    print("Rules of Yahtzee")
    print("Yahtzee has 13 rounds")
    print("Each round you roll 5 dice")

def RollDice():
    return random.randrange(1,6)

def RollOne(diceList):
    for x in range(5):
        diceList.append(RollDice())
    print (diceList)   

def RollTwo(diceList):
    print("Second")
    
def RollThree(diceList):
    print("Third")
    
def ScoreCard(diceList):
    print("Score")
    
def PlayYahtzee():
    for round in range (13):
        RollOne(diceList)
        answer = input("Do you want to Re-roll any dice? Y or N: ")
        if('y' in answer or 'Y' in answer):
            RollTwo(diceList)
            RollThree(diceList)
        elif('n' in answer or 'N' in answer):
            ScoreCard(diceList)
        else:
            
        diceList.clear()
        
print("Welcome to Yahtzee")
name = input("(R)ules or (P)lay? :")

if('r' in name or 'R' in name):
    Rules()
elif('p' in name or 'P' in name):
    PlayYahtzee()
else:
    print("That is not a valid option")
