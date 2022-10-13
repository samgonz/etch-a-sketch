from turtle import Turtle, Screen, onkey

timmy_the_turtle = Turtle()
timmy_the_turtle.color('Blue')
tommy_the_turtle = Turtle()
tommy_the_turtle.color('Red')
screen = Screen()

def up():
    timmy_the_turtle.forward(10)
 
 
def down():
    timmy_the_turtle.backward(10)
 
 
def left():
    new_heading = timmy_the_turtle.heading() + 10
    timmy_the_turtle.setheading(new_heading)
 
def right():
    new_heading = timmy_the_turtle.heading() - 10
    timmy_the_turtle.setheading(new_heading)    
    
def clear_timmy():
    timmy_the_turtle.clear()
    
def goHome():
    timmy_the_turtle.home()
    timmy_the_turtle.clear()

    
screen.listen()
onkey(up, 'Up')
onkey(down, 'Down')
onkey(left, 'Left')
onkey(right, 'Right')
onkey(clear_timmy, 'space')
onkey(goHome, 'h')
screen.exitonclick()
    
    
