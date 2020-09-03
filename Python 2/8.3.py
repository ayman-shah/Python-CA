#This code shows the user a list of classic games and asks them to choose their favorite. This value gets moved to the top of the list, and then the user can add another game to the list.

#Create a list of some of the top classic games
top_games = ["pacman", "tetris", "space invaders", "sonic the hedgehog", "super mario brothers", "street fighter", "pong", "donkey kong", "paperboy"]

#Print list of games
print("Here is a list of some top classic games: ", top_games)

#Ask the user which game they think is the best, and move it to the first position
choice = input("Which game do you think is the best? Type the name accurately: ").strip().lower()

#Remove the game from its current position
top_games.remove(choice)

#Add it to the start of the list
top_games.insert(0, choice)

#Ask the user if they would like to add any other games to the list
add_more = input("Would you like to add another game that you think is cool? Y/N: ").strip().lower()

if add_more in ["y", "yes", "yep", "yeah"]:
  new_game = input("Enter the title of the game: ").strip().lower()
  
  if not new_game in top_games:
    top_games.append(new_game)
  else:
    print("That game is already in the list!")
    
else:
  print("OK")
  
#Print the new list
print("Here is the new list: ", top_games)
