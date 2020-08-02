#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))

#Ask the user for number of hours spent online for each of the past 7 days
for i in range(1, 8):
  hours = input("How many hours did you spend online on day {}?".format(i))
  
  print(hours)
