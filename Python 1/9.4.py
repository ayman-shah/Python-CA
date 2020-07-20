donut_price = 5

#Ask how many donuts
num_donuts = int(input("How many gourmet donuts would you like? "))

#Calculate price and apply Super Saturday discount
print("But wait! It's Saturday so you get $1 off your total order for each donut purchased!")
order_total = num_donuts * donut_price - num_donuts

#Display order total
print("That will cost: ${}".format(order_total))

