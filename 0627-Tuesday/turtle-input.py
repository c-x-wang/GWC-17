from turtle import *
import math

# Name your Turtle.
t = Turtle()

# set up screen and starting position
setup(500,300)
x_pos = 0#-250
y_pos = 0#-150
t.penup()
t.setposition(x_pos, y_pos)

### Write your code below:

# input
color = input('What color would you like to draw in? ')
t.pencolor(color)
t.fillcolor(color)
sides = int(input('How many sides would you like your shape to have? '))

# draw shape
t.pendown()
t.begin_fill()
for i in range(sides):
    t.circle(50, 360, sides)
    t.right(360/sides)
# for i in range (sides):
#     t.forward(50)
#     t.right(360/sides)
t.end_fill()
t.penup()

# end position
t.setposition(-210, -110)

# close window on click
exitonclick()
