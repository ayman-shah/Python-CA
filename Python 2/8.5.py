#Create a list of the alphabet using the list() function
alpha_string = "abcdefghijklmnopqrstuvwxyz"
alpha_list = list(alpha_string)

#Print the first 3 letters on new lines
for letter in alpha_list[0:3]:
  print(letter)
  
#Print l, m, n, o and p
print(alpha_list[11:16])

#Print the last 3 letters
print(alpha_list[23:])

#Print the last letter
print(alpha_list[-1])
