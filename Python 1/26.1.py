# Set a correct answer
ANSWER = 9

# Give the user 3 lives
lives = 3

# Give the user 3 tries to guess the number, and tell them whether they are correct or not
while lives >= 1:
  guess = int(input("Try guess the number"))
  if guess == ANSWER:
    print("Correct!")
    lives = 0
  else:
    print("Wrong!")
    lives -= 1
