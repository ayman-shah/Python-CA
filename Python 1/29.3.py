#Ask the user to choose a number between 1 and 10
number = int(input("Choose a number between 1 and 10: "))

while number < 1 or number > 10:
  print("Please enter a number between 1 and 10!")
  number = int(input("Choose a number between 1 and 10: "))
  
print("You chose: {}.".format(number))
