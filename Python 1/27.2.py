# Ask user for login details and give them 3 tries
PASSWORD = "ekki-ekki-ekki"

for i in range(3):
  guess = input("Password: ").strip().lower()
  if guess == PASSWORD: # If correct
    print("Correct, authorisation complete.")
    break
  else: #If incorrect
    print("Incorrect")
    
else: #If incorrect 3 times
  print("Sorry, 3 incorrect guesses, your account has been locked.")
