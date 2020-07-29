#Write your code here
movie = int(input("Rate last movie"))

if movie == 3:
  print("Pretty average huh?")
elif movie < 3:
  print("Wow, that must have been bad!")
elif movie > 3 and movie <= 5:
  print("Sounds like a great movie!")
else:
  print("I said out of 5!")
