# Ask and greet by name
name = input("What is your name?")
print("Hello {}!  Let's work out what you earned this week".format(name))

#Ask user for work data
hourly_rate = int(input("How much do you earn per hour? "))
hours_worked = int(input("How many hours do you work per day? "))
days = int(input("How many days per week do you work? "))

#Calculate wages for the week
wages = hourly_rate * hours_worked * days

print("Your pay this week before tax is: ${} ".format(wages))

#Take off 20% tax
wages *= 0.8

print("After tax @ 20% that is: ${}".format(wages))
