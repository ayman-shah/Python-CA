#Ask user how long they have exercised for today
time = int(input("How many eercise today?"))

#If an invalid number is entered, repeat until they enter one between 0-1440
while time < 0 or time > 1440:
  print("Please enter a valid number. The total minutes in one day is 1440")
  time = int(input("How many eercise today?"))
