#List of computer's favorites
favorites = ['blue', 9, 'pizza', 3.14159]

#Print statement
print(favorites[0].upper())

#Ask the user for their favorite food, check if it is the same as the computer
food = input("What is your favorite food?")
food = food.strip().lower()

if food == favorites[2]:
  #A function is used to make sure there is a capital at the start of the print statement
  print("{} is my favorite food too!".format(favorites[2].capitalize()))
  
else:
  print("{} is OK, but I prefer {}.".format(food.capitalize(), favorites[2]))
