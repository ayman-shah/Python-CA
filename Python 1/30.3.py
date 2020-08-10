# Ask user to enter sleep data for day 1 through to day 7
for i in range(1,8):
  hours_sleep = int(input("Enter hours of sleep on day {}: ".format(i)))
  print("Hours of sleep on day {}: {}".format(i, hours_sleep))

#Print out 1 - 3 times tables
for i in range(1, 4):
  for j in range(1, 4):
    print("{} x {} = {}".format(i, j, i * j))
    
    
