#Ask the user how they feel
mood = input("How are you feeling today?")
 
#Print a response depending on their mood
if mood == "happy":
  print("That's great!")
elif mood == "sad":
  print("Sorry to hear that")
elif mood == "tired":
  print("You should get an early night")
else:
  print("Oh, really?")
