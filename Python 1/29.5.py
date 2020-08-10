#Ask the user to enter the number of hours sleep they got last night. This should accept values between 0 and 24 inclusive, and force the user to re-enter if they enter invalid data.
while True:
  try:
    sleep_hours = float(input("How many hours sleep did you get last night?"))
    if sleep_hours < 0 or sleep_hours > 24:
      print("You can't sleep negative hours, or more than 24 hours in one day!")
    else:
      break

  except ValueError:
    print("Please enter a number.")

#Check if they are getting enough sleep
if sleep_hours >= 12:
  print("Wow, that's a lot of sleep!")
elif sleep_hours < 12 and sleep_hours >= 8:
  print("You got enough sleep last night")
else:
  print("You should try to get more sleep!")
