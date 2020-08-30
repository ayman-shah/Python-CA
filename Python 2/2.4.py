#Names list
name_string = "Becky Steve Thomas Rachel Bob Tom Miguel Hone Anahera Wei-ling"

#Split the names into a list on spaces (default)
names_list = name_string.split()
print(names_list)

#Create a string with items on new lines (you don't need \n)
item_string = """water
computer
school
network
hammer
walking
violently
mediocre
literature
chair
two
window
cords
musical
zebra
xylophone
penguin
home
dog kennel
final
ink
teacher
fun"""

#Turn it into a list using .split()
item_list = item_string.split("\n")
print(item_list)
