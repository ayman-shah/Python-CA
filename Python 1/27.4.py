#Force the user to enter a valid number
while True:
  try:
    height = float(input("Enter your height in metres: "))
    break
  except ValueError:
    print("Please enter a valid height in metres e.g. 1.65")
