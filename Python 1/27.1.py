#Break this loop after 13 is printed  
for i in range(5, 15):
  print(i)
  if i == 13:
    break 
    
print("-----") #Separate the output from the 2 loops
#Make this loop skip printing 9
for i in range(12):
  if i == 9:
    continue
  print(i)
