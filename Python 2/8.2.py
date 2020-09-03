#Questions and answers for a quiz - note that these longer list items are written on one line each to make it easy to read.
questions = ["How many bits are in a byte?",
            "True or False? A nibble is half a byte.",
            "What year was Google founded?",
            "How many zeroes are in a Googol?",
            "How many bytes are in a kilobyte?"]

answers = ["8", "true", "1998", "100", "1024"]

#Ask the user their name and welcome them to the quiz
name = input("What is your name?")
print("Welcome to the quiz, {}! There are 5 questions.".format(name))

#Ask the first question and get the user's guess from the input
guess = input(questions[0]).strip().lower()

if guess == answers[0]:
  print("Correct!")
else:
  print("Wrong! The correct answer was {}!".format(answers[0]))
