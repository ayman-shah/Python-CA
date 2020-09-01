#Create an empty grocery_list
grocery_list = []

#Start a loop to ask user to enter their grocery list
repeat = True
while repeat == True:
  item = input("Please enter an item or 'done' to end input: ").strip().lower()
  
  #Check if user has entered done so that loop can be stopped if so
  if item == "done":
    repeat = False
  else:
    #Check if item is already in list
    count = grocery_list.count(item)
    
    #If so, give user error message, otherwise add the item and give success message
    if count > 0:
      print("Sorry {} is already on the list!".format(item))
    else:
      grocery_list.append(item)
      print("{} has been added!".format(item))

#Once user is done, sort the list then print out their list for them
print("Your grocery list is: ")
grocery_list.sort()

for item in grocery_list:
  print(item.title()) #Add a capital letter
