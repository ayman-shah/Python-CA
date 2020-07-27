score = 10
 
#Ask the next question
answer = input("Ganymede is a moon of which planet?")
answer = answer.strip().lower()
 
#Check if answer is correct and add or remove points
if answer == "jupiter":
  print("That is correct, you get 5 points!")
  score += 5
else:
  print("Sorry, that is incorrect, you lose 3 points")
  score -= 3
 
print("Your score is now: {} points".format(score))
