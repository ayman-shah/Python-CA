# Force the user to choose a valid option
while True:
  answer = input("True or false? Sharks are mammals: ").strip().lower()
  #Exit loop if user has entered a valid answer
  if answer == "true" or answer == "false": 
    break
  else: #Tell them to enter a valid answer
    print("Please answer with true or false")

#Go on to check if they were right or wrong
