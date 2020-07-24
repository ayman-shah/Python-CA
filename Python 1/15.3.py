#Ask user how long they spend online
internet_hours = int(input("How many hours do you spend on the internet each day? "))

#Check if they spend too much time or not
if internet_hours < 3:
  print("That's a healthy amount of time")
elif internet_hours >= 3 and internet_hours <= 5:
  print("Make sure you are also being active")
elif internet_hours > 5 and internet_hours <= 8:
  print("You need to get more fresh air!")
else:
  print("There are only 24 hours in a day!")
  
