weight = int(input("How much does your parcel weigh? "))

# Check the weight variable
if weight > 0 and weight <= 3:
  print("Shipping will cost $5")
elif weight > 3 and weight <= 10:
  print("Shipping will cost $10")
else:
  print("Contact us for a quote")
