# Set amount of pocket money
pocket_money = 40.00
still_shopping = True

#Ask the user for the price of items until they can't afford anymore
while still_shopping == True:
  price = float(input("How much do you want to spend on this item? "))
  pocket_money -= price
  print("You have ${:.2f} left".format(pocket_money))
  
  #Check if the user wants to purchase more
  confirm = input("would you like to continue shopping")
  if confirm == "no":
    still_shopping = False
    
