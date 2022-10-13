from turtle import Turtle, Screen, onkey

timmy_the_turtle = Turtle()
screen = Screen()

def up():
    timmy_the_turtle.setheading(90)
    timmy_the_turtle.forward(100)
 
 
def down():
    timmy_the_turtle.setheading(270)
    timmy_the_turtle.forward(100)
 
 
def left():
    timmy_the_turtle.setheading(180)
    timmy_the_turtle.forward(100)
 
 
def right():
    timmy_the_turtle.setheading(0)
    timmy_the_turtle.forward(100)
    
    
screen.listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')
screen.exitonclick()
    
    
