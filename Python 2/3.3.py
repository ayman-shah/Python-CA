#A list of names
names =  ["charlotte", "olivia", "isla", "emily", "sophie", "oliver", "jack", "james", "mason", "liam"]

#Ask the user for their name and see if it is 
name = input("What is your name?").strip().lower()

if name in names:
  print("Hey guess what? Your name was one of the top 10 baby names of 2014.  Go you!")
else:
  print("{} is a great name, but it wasn't in the top 10 in 2014.".format(name.capitalize()))
  
#A list of primary colors of light, used in the pixels on your screen
primary_colors = ["red", "green", "blue"]

#Ask the user to pick a color
color = input("Pick a color: ")

#Tell them whether or not it is one of the primary colors of light
if color in primary_colors:
  print("{} is a primary color of light".format(color))
else:
  print("{} is not a primary color of light".format(color))
