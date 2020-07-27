score = 300
 
#Ask the next question
answer = int(input("How many bees does it take to equal approximately the same weight as one M&M candy?"))
 
#Check if answer is correct and add or remove points
if answer == 10:
  print("That is correct, you get 100 points!")
  score += 100
elif answer > 10:
  print("The answer is lower! You lose 20 points")
  score -= 20
elif answer < 10:
  print("The answer is higher! You lose 20 points")
  score -= 20
  
print("Your score is now: {} points".format(score))
