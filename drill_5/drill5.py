import turtle
import random

turtle.shape("turtle")
 
def movement_up():
    turtle.setheading(90)
    turtle.forward(50)
    turtle.stamp()

def movement_down():
    turtle.setheading(270)
    turtle.forward(50)
    turtle.stamp()
  
def movement_left():
    turtle.setheading(180)
    turtle.forward(50)
    turtle.stamp()
 
def movement_right():
    turtle.setheading(0)
    turtle.forward(50)
    turtle.stamp()
   
def restart():
    turtle.reset()
   
turtle.onkey(movement_up, 'w')
turtle.onkey(movement_down, 's')
turtle.onkey(movement_left, 'a')
turtle.onkey(movement_right, 'd')
turtle.onkey(restart, 'Escape')
turtle.listen()

