# Set up price variables
ps3_game = 20
ps4_game = 45

#Ask for number of each game to be purchased
num_ps3_games = int(input("How many PS3 games?: "))
num_ps4_games = int(input("How many PS4 games?: "))

#Calculate total for each type of game
ps3_total = num_ps3_games * ps3_game
ps4_total = num_ps4_games * ps4_game

#Calculate total cost
total_cost = ps3_total + ps4_total

#Print out total order cost
print("Your order costs: ${}".format(total_cost))
