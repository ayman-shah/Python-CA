DELIVERY = 10
PIZZA_PRICE = 15

# Set variable equal to input
num_pizzas = int(input("How many pizzas do you want?"))

#Set variable to pizzas times price
order_total = num_pizzas * PIZZA_PRICE

# if pizzas are less than 3
if num_pizzas < 3:
  print("Delivery will cost ${}".format(DELIVERY))
  order_total += DELIVERY
else:
  print("Free delivery for 3 or more pizzas!")
  
#Print "Your order comes to:..."
print("Your order of {} pizzas comes to: ${}".format(num_pizzas, order_total))


