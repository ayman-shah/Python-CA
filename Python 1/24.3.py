#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))

total_hours = 0

#Ask the user for number of hours spent online for each of the past 7 days
for i in range(1, 8):
  hours = float(input("How many hours did you spend online on day {}?: ".format(i)))
  total_hours += hours
print("You spent {} hours online in total".format(total_hours))

