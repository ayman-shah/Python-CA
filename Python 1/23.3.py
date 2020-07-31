#Set up turtle
import turtle
tiny = turtle.Turtle()
tiny.pensize(5)

#Go to position 
tiny.penup()
tiny.goto(60, 220)
tiny.pendown()

#Draw a red hexagon
tiny.pencolor("red")
for i in range(6):
  tiny.forward(100)
  tiny.left(60)

#Go to position
tiny.penup()
tiny.goto(360, 220)
tiny.pendown()

#Draw a triangle that has a blue line and yellow fill
tiny.pencolor("blue")
tiny.fillcolor("yellow")
tiny.begin_fill()
for i in range(3):
  tiny.forward(100)
  tiny.left(120)
tiny.end_fill()
#Go to position
tiny.penup()
tiny.goto(200, 440)
tiny.pendown()

#Draw a filled pink pentagon
tiny.pencolor("pink")
tiny.fillcolor("pink")
tiny.begin_fill()
for i in range(5):
  tiny.forward(100)
  tiny.left(72)
tiny.end_fill()
