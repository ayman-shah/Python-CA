import turtle
timmy = turtle.Turtle()
timmy.pensize(5)

#Move to first position
timmy.penup()
timmy.goto(10, 60)
timmy.pendown()

#Draw a purple rectangle, 120 by 50
timmy.color("purple")
timmy.forward(120)
timmy.left(90)
timmy.forward(50)
timmy.left(90)
timmy.forward(120)
timmy.left(90)
timmy.forward(50)
timmy.left(90)


#Move to next position
timmy.penup()
timmy.goto(420,60)
timmy.setheading(0)
timmy.pendown()

#Draw an orange triangle with sides that are 60px long
timmy.color("orange")
timmy.forward(60)
timmy.left(120)
timmy.forward(60)
timmy.left(120)
timmy.forward(60)
timmy.left(120)

