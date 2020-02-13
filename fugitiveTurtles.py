# Author : Nicole Abuzo
# Date : 10 / 24 / 16
# Program Purpose: To create a simple game with a random movement using the while loop.
import turtle
import random

# Create a graphic window of a suitable size and background color
mw = turtle.Screen()
mw.screensize(500, 500)
mw.bgcolor("Lightblue")

# Create 2 turtles
t1 = turtle.Turtle()
t2 = turtle.Turtle()
t1.shape("turtle")
t2.shape("turtle")
t1.color("green")
t2.color("yellow")
t1.speed("slow")
t2.speed("slow")

# Draw the holding pen
pen = turtle.Turtle()
pen.hideturtle()
pen.pencolor("blue")
pen.pensize(5)
pen.pu()
pen.goto(0, -50)
pen.pd()
pen.circle(50)

# Drawing the fence
fence = turtle.Turtle()
fence.hideturtle()
fence.pencolor("blue")
fence.pensize(5)
fence.pu()
fence.setposition(-250, -250) # x and y cooridnates of the fence
fence.pd()
for side in range(4):
    fence.fd(500)
    fence.lt(90)


# Random distance and direction
while True:
    distance = random.randint(10, 20)
    t1.fd(distance)
    turnNumber = random.randint(1,7)
    turnAmount = (turnNumber * 15)+ -60 # The total will determine if the turtle will turn right or left
    t1.right(turnAmount) # If the turnAmount is positive it will turn right and if its negative it will turn left
    if (t1.xcor() > 240 or t1.xcor() < -240) or (t1.ycor() > 240 or t1.ycor() < -240):
        print("Turtle Green got throught the fence travelling", round(turtle.distance(t1), 2), "feet!")
        break
    
    t2.fd(distance)
    turnNumber = random.randint(1,7)
    turnAmount = (turnNumber * 15)+ -60
    t2.right(turnAmount)
    if (t2.xcor() > 240 or t2.xcor() < -240) or (t2.ycor() > 240 or t2.ycor() < -240):
        print("Turtle Yellow got throught the fence travelling", round(turtle.distance(t2), 2), "feet!")
        break

# End
