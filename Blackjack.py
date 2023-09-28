# Modified Blackjack

# Card values: 2-10, | J,Q,K-> 10 | A - 1 ili 11
# Give a card (random card) or Stay (satisfied with the one drawn)

import random

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]

playerHand = []
playerSum = 0

dealerHand = []
dealerSum = 0

whooseTurn = "Player"

gameEnd = False

def GiveACard():
    roll = random.choice(deck)
    return roll 


def start():
    global playerHand
    global dealerHand
    for initial in range(2):
        playerHand.append(GiveACard())
        dealerHand.append(GiveACard())

def hit(playerOrDealer):
    global playerHand
    global dealerHand
    if playerOrDealer == "Player":    
        playerHand.append(GiveACard())
    elif playerOrDealer == "Dealer":
        dealerHand.append(GiveACard())

def playerTurn():
    global whooseTurn
    print("Your current cards are: ")
    for card in playerHand:
        print("\t",card, end = "")
    print("\nDo you want an additional card (hit) or not(stand) ?\n")
    notStand = str(input(" Enter YES for hit or NO for stand: "))
    counter(playerHand)
    if playerSum < 22:
        if notStand == "YES" or notStand == "Yes" or notStand == "yes":
            notStand = True
            hit("Player")
        else:
            notStand = False
            whooseTurn = "Dealer"
            krajRunde = counter(playerHand)
            print(f"The sum of your cards is {playerSum}")
    else:
        print("EXCEEDING")
    endOfTheRound = counter(playerHand)
        
    print("counter")
    #endOfTheRound = counter(playerHand)
    return notStand, endOfTheRound

def dealerTurn():
    global whooseTurn
    global dealerSum
    print("Current dealer cards are: ")
    for card in dealerHand:
        print("\t",card, end = "")
    counterDealer(dealerHand)

    if dealerSum < 17 and dealerSum < playerSum: 
            hit("Dealer")
            print(f"\nThe dealer made the distinction of assigning a new ticket ({dealerHand[-1]})!")
    else:
        whooseTurn = "End"

    endOfTheRound = counterDealer(dealerHand)      

    
    return endOfTheRound

    


def turn(playerOrDealer):
    global whooseTurn
    global dealerSum
    global gameEnd
    end = False
    endDealer = False
    print("*"*60)
    if whooseTurn == "Player" and end != True:
        notStand, end = playerTurn()      
        while notStand == True:
            notStand, end = playerTurn()
            if end == True:
                break
    #Logic for dealer moves
    elif whooseTurn == "Dealer" and endDealer != True:
        endDealer = dealerTurn()

    else:
        gameEnd = True
        print("ENDENDENDENDENDENDENDENDEND")
        
        
    return end, endDealer

     
        
    

def oneOr10():
    print("One of the cards in your hand is \"A\"")
    howMuch = int(input("Do you want to \"A\" count as 1 or as 11: "))
    return howMuch


def counter(hand):
    global playerSum
    global gameEnd
    playerSum = 0
    end = False
    for card in hand:
        
        if card == "J" or card == "Q" or card == "K":
            hand.remove(card)
            hand.append(10)
            playerSum += 10
        elif card == "A":
            hand.remove(card)
            card = int(oneOr10()) 
            hand.append(card)
            playerSum += card
        
        else:
            playerSum += card
    if playerSum == 21:
        print("\nYou won")
        end = True
        gameEnd = True
    elif playerSum > 21:
        print(f"\nYou lose, the sum of your cards is: {playerSum}")
        end = True
        gameEnd = True
    return end

def counterDealer(hand):
    global dealerSum
    global gameEnd
    dealerSum = 0
    end = False
    for card in hand:
        
        if card == "J" or card == "Q" or card == "K":
            hand.remove(card)
            hand.append(10)
            dealerSum += 10
        elif card == "A":
            hand.remove(card)
            hand.append(11)
            dealerSum += 11
        
        else:
            dealerSum += card
    if dealerSum == 21:
        print("\nThe dealer has blackjack")
        end = True
        gameEnd = True
    elif dealerSum > 21:
        print(f"\nYou win, the sum of the dealer's cards is: {dealerSum} TEST")
        end = True
        gameEnd = True
    
    return end



start()
playerHandInit = playerHand
dealerHandInit = dealerHand
print(f"Your cards are: ")

for card in playerHandInit:
    print(card,"\t", end = "")
print()
print(f"The dealer's cards are: ")
for card in dealerHandInit:
    print(card,"\t", end = "")
print()

whooseTurn = "Player"
gameEnd = False
while gameEnd != True:    
    endPlayer, endDealer = turn(whooseTurn)
    if endPlayer == True and endDealer == True:
        gameEnd = True
        break


print(playerHand,dealerHand)
print(playerSum,dealerSum)