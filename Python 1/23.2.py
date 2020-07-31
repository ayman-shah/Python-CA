#Set up turtle
import turtle
tiny = turtle.Turtle()
tiny.pensize(5)

#Make a list of colors
colors = ["red", "yellow", "blue", "green"]

#Draw a square with one side each color using a loop
for colors in colors:
  tiny.color("{}".format(colors))
  tiny.forward(150)
  tiny.right(90)
  
