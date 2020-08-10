#Give the user 5 tries to guess a number
NUMBER = 4
GUESSES = 5

for i in range(GUESSES):
  print("You have {} guesses left.".format(GUESSES - i))
  guess = int(input("Guess the number: "))
  
  if guess == NUMBER:
    print("Yes! That's right!")
    break
  else:
    print("Wrong!")
    
else:
  print("Out of guesses, the answer was {}!".format(NUMBER))
