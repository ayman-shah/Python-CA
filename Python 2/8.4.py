#This time, our code lets the user specify how many random top games they would like to choose from the list, shuffles the list, then chooses that many games and prints the list out in alphabetical order.

import random

#Create a list of some of the top classic games
top_games = ["pacman", "tetris", "space invaders", "sonic the hedgehog", "super mario brothers", "street fighter", "pong", "donkey kong", "paperboy"]

#Print list of games, this time with better formatting using a loop
print("Here is a list of some top classic games: ")

for game in top_games:
  print(game)
  
#Ask the user how many games to pick
num_games = int(input("How many games would you like to randomly choose?"))

#Shuffle the list
random.shuffle(top_games)

#Get the first "n" games, based on the number the user picked
chosen_games = top_games[0:num_games]

#Sort chosen games into alphabetical order
chosen_games.sort()

#Print final list
print("\nYour list:")
for game in chosen_games:
  print(game)
