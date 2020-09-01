#Import the random module
import random

#A list of cards
cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

#Shuffle the cards and print
random.shuffle(cards)
print(cards)

#Use a loop to print the first 3 cards
for i in range(3):
  print(cards[i])
