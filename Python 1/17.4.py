HOURLY_RATE = 13.75
hours_worked = 37.5

wages = HOURLY_RATE * hours_worked

print("This week you worked: {:.1f} hours".format(hours_worked))

print("You earned: ${:.2f} before tax".format(wages))

#Take off 20% tax
wages *= 0.8

#Add your print statement here
print("After tax: ${:.2f}".format(wages))
