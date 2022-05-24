from multiprocessing.connection import wait
from time import sleep
from pynput import keyboard
from printFunctions import printHorses
import threading
import random

import traceback

# --- Art ---
StartingLineArt = '''
 ______  __  __  ______       ______  ______  ______  ______       __  ______       ______  ______  ______  __  __  ______     ______  ______       ______  ______  ______  ______  ______  
/\__  _\/\ \_\ \/\  ___\     /\  == \/\  __ \/\  ___\/\  ___\     /\ \/\  ___\     /\  __ \/\  == \/\  __ \/\ \/\ \/\__  _\   /\__  _\/\  __ \     /\  ___\/\__  _\/\  __ \/\  == \/\__  _\ 
\/_/\ \/\ \  __ \ \  __\     \ \  __<\ \  __ \ \ \___\ \  __\     \ \ \ \___  \    \ \  __ \ \  __<\ \ \/\ \ \ \_\ \/_/\ \/   \/_/\ \/\ \ \/\ \    \ \___  \/_/\ \/\ \  __ \ \  __<\/_/\ \/ 
   \ \_\ \ \_\ \_\ \_____\    \ \_\ \_\ \_\ \_\ \_____\ \_____\    \ \_\/\_____\    \ \_\ \_\ \_____\ \_____\ \_____\ \ \_\      \ \_\ \ \_____\    \/\_____\ \ \_\ \ \_\ \_\ \_\ \_\ \ \_\ 
    \/_/  \/_/\/_/\/_____/     \/_/ /_/\/_/\/_/\/_____/\/_____/     \/_/\/_____/     \/_/\/_/\/_____/\/_____/\/_____/  \/_/       \/_/  \/_____/     \/_____/  \/_/  \/_/\/_/\/_/ /_/  \/_/ 
            '''

## --- Variables ---
newCard = True
waitForNewCard = True
usedCards = []
moveBackCards = []

# --- Functions ---
def race():
    ## Allows for shared variables between threads
    global waitForNewCard
    global usedCards
    global newCard
    global card

    ## Used for generating art
    count = -1

    ## Scores
    horse1Score = 7 # Diamond
    horse2Score = 7 # Clubs
    horse3Score = 7 # Hearts
    horse4Score = 7 # Spades
    
    ## Used for backwards cards
    minScoreHolder = 7
    ThisSmallNumber = 6

    ## Print String for later
    statusString = ''

    ## Start of the game we need to draw go back cards
    if count == -1:
        for i in range(6):
            newCard = True
            while newCard == True:
                rank = random.choice( ('2','3','4','5','6','7','8','9','T','J','Q','K') )
                suit = random.choice( ('Diamonds','Clubs','Hearts','Spades') )
                card = rank + suit
                if card in usedCards:
                    newCard = True
                else:
                    usedCards.append(card)
                    moveBackCards.append(card)
                    newCard = False

    card = ''

    ## This creats a loop for the horses to dispay running progress and bring the horses forward or backward
    while running:
        try:
            ## Make sure we only change the score once.
            if waitForNewCard == False:
                waitForNewCard = True      
                if card[1] == 'D':
                    horse1Score = horse1Score - 1
                if card[1] == 'C':
                    horse2Score = horse2Score - 1
                if card[1] == 'H':
                    horse3Score = horse3Score - 1
                if card[1] == 'S':
                    horse4Score = horse4Score - 1
                
                ## Horses can also move backwards!! This is only done if the lead horse is the new min (Closer to winning)
                minScoreHolder = min((horse1Score,horse2Score,horse3Score,horse4Score))
                if minScoreHolder < ThisSmallNumber:
                    ThisSmallNumber = minScoreHolder
                    backwardCard = moveBackCards.pop(0)
                    if backwardCard[1] == 'D' and horse1Score != 7:
                        statusString = f'Diamond\'s horse fell behind with {backwardCard}!'
                        horse1Score = horse1Score + 1
                    if backwardCard[1] == 'C' and horse2Score != 7:
                        statusString = f'Club\'s horse fell behind with {backwardCard}!'
                        horse2Score = horse2Score + 1
                    if backwardCard[1] == 'H' and horse3Score != 7:
                        statusString = f'Heart\'s horse fell behind with {backwardCard}!'
                        horse3Score = horse3Score + 1
                    if backwardCard[1] == 'S' and horse4Score != 7:
                        statusString = f'Spade\'s horse fell behind with {backwardCard}!'
                        horse4Score = horse4Score + 1
        except Exception: 
            traceback.print_exc()

        ## If used for starting line art not really needed.
        if card == '':
            print(StartingLineArt)
        else:
            print(f'The Current card: {card}')
            print(statusString)
        
        ## This count is used to know what art to use.
        count = count + 1
        ## Grabs art of horses and prints it out
        stringOutput1, stringOutput2, stringOutput3, stringOutput4 = printHorses(horse1Score, horse2Score, horse3Score, horse4Score, count)
        print(stringOutput1)
        print(stringOutput2)
        print(stringOutput3)
        print(stringOutput4)

        if count == 11:
            count = 0

        # Print the winners!
        if horse1Score == 0:
            print('Diamond\'s Horse Wins!')
            return False

        if horse2Score == 0:
            print('Club\'s Horse Wins!')
            return False

        if horse3Score == 0:
            print('Heart\'s Horse Wins!')
            return False

        if horse4Score == 0:
            print('Spade\'s Horse Wins!')
            return False

        ## This slows or speeds up the horses. Change as you like.
        sleep(.25)        


def on_press(key):
    global running 
    global card
    global waitForNewCard
    newCard = True

    if key == keyboard.Key.f1:
        running = True
        waitForNewCard = True
        # Create race tread for print out and main game items.
        t = threading.Thread(target=race)
        # Start thread
        t.start()
        
    if key == keyboard.Key.end:
        # stop listener
        running = False
        return False

    # Draws new cards and adds them to used card list
    if key == keyboard.Key.space:
        try:
            while newCard == True:
                #Ace is not used as that is the card running
                rank = random.choice( ('2','3','4','5','6','7','8','9','T','J','Q','K') )
                suit = random.choice( ('Diamonds','Clubs','Hearts','Spades') )
                card = rank + suit
                if card in usedCards:
                    newCard = True
                else:
                    usedCards.append(card)
                    waitForNewCard = False
                    newCard = False
        except:
            print("Cards fell on ground please restart")
        
        # If you want to see all the used cards
        #print(usedCards)

        
#--- main ---
print('Welcome to horse races! \nPress F1 to START \nPress End to STOP \nPress Space Bar to pick next card \nCreated by Jordan Meidinger')
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
