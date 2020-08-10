Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 22:20:52) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Set amount of pocket money
pocket_money = 40.00

#Ask the user for the price of items until they can't afford anymore
while pocket_money > 0:
  price = float(input("How much do you want to spend on this item? "))
  pocket_money -= price
  print("You have ${:.2f} left".format(pocket_money))
