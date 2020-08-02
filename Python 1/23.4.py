#Set up turtle
import turtle
spiro = turtle.Turtle()
spiro.color("blue")

#Draw a spirograph
for i in range(100):
  #Change colors
  if i == 20:
    spiro.color("red")
  elif i == 40:
    spiro.color("orange")
  elif i == 60:
    spiro.color("yellow")
  elif i == 80:
    spiro.color("green")
    
  #Draw the spirograph
  spiro.forward(200)
  spiro.left(184)
  spiro.forward(40)
  spiro.right(30)
  
