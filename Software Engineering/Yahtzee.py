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

def RollAgain(diceList):
    reroll = int(input("How many dice do you want to re-roll?:"))
    if(reroll > 5):
        print("You only have 5 dice, so we'll re-roll them all")
        reroll = 5
    elif(reroll < 1):
        print("I guess you didn't want to re-roll any dice after all")
        reroll = 0
    
    if(reroll == 5):
        diceList.clear()
        for x in range (reroll):
            diceList.append(RollDice())
    elif(reroll == 0):
        print("No dice rolled")
    else:
        for x in range(reroll):
            num = int(input("Which dice do you want re-rolled?:"))
            while(num < 1 or num > 5):
                num = int(input("Please put in 1-5: "))
            diceList[num - 1] = RollDice()
            
    print(diceList)
    
def ScoreCard(diceList):
    print("Score")
    
def PlayYahtzee():
    num = int(0)
    for round in range (13):
        num += 1
        print("Round:", end = "")
        print(num)
        RollOne(diceList)
        answer = input("Do you want to re-roll any dice? Y or N: ")
        if('y' in answer or 'Y' in answer):
            RollAgain(diceList)
            answer = input("Do you want to Re-roll any dice? Y or N: ")
            if('y' in answer or 'Y' in answer):
                RollAgain(diceList)
        ScoreCard(diceList)
        diceList.clear() 

print("Welcome to Yahtzee")
name = input("(R)ules or (P)lay? :")

if('r' in name or 'R' in name):
    Rules()
elif('p' in name or 'P' in name):
    PlayYahtzee()
else:
    print("That is not a valid option")
