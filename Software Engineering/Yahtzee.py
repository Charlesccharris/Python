import random
played = 0
diceList = []
dice = int()
answer = ""
card = ["Score Card:", "(1)Aces", "(2)Twos", "(3)Threes", "(4)Fours", "(5)Fives", "(6)Sixes", "(7)3 of a kind", "(8)4 of a kind", "(9)Full House", "(10)Sm Straight (Sequence of 4)", "(11)Lg. Straight (Sequence of 5)", "(12)YAHTZEE (5 of a kind)", "(13)Chance"]
score = []

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
        print("You only have 5 dice, so we'll roll them all")
        reroll = 5
    elif(reroll < 1):
        print("I guess you didn't want to roll any dice after all")
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
    
def ScoreCard(diceList, card, score):
    matched = 0
    for x in card:
        print(x)

    while(matched != 1):
        choice = input("Choose which category to score: ")
        match choice:
            case '1':
                print("Ace")
                matched = 1
            case '2':
                print("Two")
                matched = 1
            case '3':
                print("Three")
                matched = 1
            case '4':
                print("Four")
                matched = 1
            case '5':
                print("Five")
                matched = 1
            case '6':
                print("Six")
                matched = 1
            case '7':
                print("Seven")
                matched = 1
            case '8':
                print("Eight")
                matched = 1
            case '9':
                print("NIn")
                matched = 1
            case '10':
                print("Ten")
                matched = 1
            case '11':
                print("eleven")
                matched = 1
            case '12':
                print("twelve")
                matched = 1
            case '13':
                print("Thirteen")
                matched = 1
            case _:
                print("Not a valid option")
                matched = 0
            
def ScoreGame(score):
    counter = int()
    upper = int()
    totalScore = int()
    
    for x in score:
        if(counter < 6):
            counter += 1
            upper += x
            print("No")
        totalScore += x
        
    if(upper >= 63):
        totalScore += 35
        
    print(totalScore)    
def FillCard(score):
    for x in range (13):
        score.append(-1)

def PlayYahtzee():
    num = int(0)
    for round in range (13):
        num += 1
        print("Round:", end = "")
        print(num)
        RollOne(diceList)
        answer = input("Do you want to Re-roll any dice? Y or N: ")
        if('y' in answer or 'Y' in answer):
            RollAgain(diceList)
            answer = input("Do you want to Re-roll any dice? Y or N: ")
            if('y' in answer or 'Y' in answer):
                RollAgain(diceList)
        ScoreCard(diceList, card, score)
        diceList.clear() 
    ScoreGame(score)

while(played != 1):
    print("Welcome to Yahtzee")
    name = input("(R)ules or (P)lay? :")
    if('r' in name or 'R' in name):
        Rules()
    elif('p' in name or 'P' in name):
        FillCard(score)
        PlayYahtzee()
        played = 1
    else:
        print("That is not a valid option")
