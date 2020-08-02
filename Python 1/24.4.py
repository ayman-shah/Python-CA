#Ask the user's name and greet them
name = input("What is your name?")
print("Hello, {}!".format(name))

total_hours = 0
lowest_hours = None

#Ask the user for number of hours spent online for each of the past 7 days
for i in range(1, 8):
  hours = float(input("How many hours did you spend online on day {}?: ".format(i)))
  total_hours += hours
  if lowest_hours == None or hours < lowest_hours:
    lowest_hours = hours
  #Check if current hours are the lowest hours and store if so
  
  
print("You spent {} hours online in total.".format(total_hours))
print("The least time you spent online in one day was {} hours".format(lowest_hours))

