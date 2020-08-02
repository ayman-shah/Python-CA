#Set up - always do all imports together at the top of your code
import random
import turtle

spiro = turtle.Turtle()
spiro.pensize(2)
spiro.goto(100,250)

#Change colors
red = random.randrange(1, 256)
green = random.randrange(1, 256)
blue = random.randrange(1, 256)
spiro.color((red, green, blue))

#Draw a spirograph
for i in range(100):
  spiro.forward(300)
  spiro.left(184)

  
