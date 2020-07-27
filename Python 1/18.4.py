score = 30
 
#Ask the next question
answer = input("What is the name of Saturn's largest moon?")
answer = answer.strip().lower()

#Check if answer is correct and add or remove points
if answer == "titan":
  print("That is correct, you get 10 points!")
  score += 10
elif answer == "ganymede":
  print("You're thinking of Jupiter! You lose 5 points")
  score -= 5
else:
  print("Sorry, incorrect, You lose 5 points")
  score -= 5
  
print("Your score is now: {} points".format(score))

