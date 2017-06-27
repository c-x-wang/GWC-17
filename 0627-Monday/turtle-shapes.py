from turtle import *
import math

# Name your Turtle.
t = Turtle()

# Set Up your screen and starting position.
setup(500,300)
x_pos = 0#-250
y_pos = 0#-150
t.setposition(x_pos, y_pos)

### Write your code below:
t.pendown()
for i in range(4):
    t.forward(50)
    t.right(90)

# Close window on click.
exitonclick()
