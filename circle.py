# Python program to draw 
# Spiral  Helix Pattern
# using Turtle Programming
 

import turtle

loadWindow = turtle.Screen()

turtle.speed(1000000000000000)
 

for i in range(1000):

    turtle.circle(3*i)

    turtle.circle(-3*i)

    turtle.left(i)
 
turtle.exitonclick()