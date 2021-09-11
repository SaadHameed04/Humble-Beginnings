import math
import random

playerInput = input() #player input


#randomiser 
choices = ['Scissors', 'Paper', 'Rock'] #options for the randomiser to choose from
botChoice = random.choice(choices) #randomiser making those options from line 7 random 
print(botChoice)


#player winning scenarios
if botChoice == 'Rock' and playerInput == 'Paper':
    print("Player Wins")

if botChoice == 'Paper' and playerInput == 'Scissors':
    print('Player Wins')

if botChoice == 'Scissors' and playerInput == 'Rock':
    print('Player Win')

#bot winning scenarios
if playerInput == 'Rock' and botChoice == 'Paper':
    print('Bot Wins')

if playerInput == 'Paper' and botChoice == 'Scissors':
    print('Bot Wins')

if playerInput == 'Scissors' and botChoice == 'Rock':
    print('Bot Wins')

