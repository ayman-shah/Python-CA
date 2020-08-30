#For loop printing numbers
for i in range(1, 16):
  print(i)

#For loop printing text
for i in range(3):
  print("I see red!")
  
#While loop printing numbers
i = 0
while i <= 10:
  print(i)
  i += 1
  
#While loop that repeats until input matches the condition
password = input("Enter the password: ")
while password != "monty":
  print("Wrong password!")
  password = input("Enter the password: ")

print("Password accepted")
