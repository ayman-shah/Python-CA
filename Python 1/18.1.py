score = 10

#Ask the next question
answer = input("Which metal is heavier, silver or gold?")
answer = answer.strip().lower()

#Check if answer is correct and add or remove points
if answer == "gold":
  print("That is correct, you get 10 points!")
  score += 10
else:
  print("Sorry, that is incorrect, you lose 2 points")
  score -= 2

print("Your score is now: {} points".format(score))
