ANSWER = 9

#Ask user for their guess
guess = int(input("Guess a number: "))

#Check if they are correct
if guess == ANSWER:
  print("You chose: {}".format(guess))
  print("Analysing...")
  print("You are correct!")
else:
  print("You chose: {}".format(guess))
  print("You are incorrect...")
  print("Better luck next time!")
