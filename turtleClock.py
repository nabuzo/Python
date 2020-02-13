# Import turtle
import turtle

# Set background size and color
mw = turtle.Screen()
mw.bgcolor("Lightblue")
mw.screensize(500,500)

# Make a turtle then costumize the pen
t=turtle.Turtle()
t.hideturtle()
t.pen(pencolor = "black", pensize = 5)

# Draw Circle
t.penup()
t.goto(0,-230)
t.pendown()
t.circle(230)

# Make 12 turtle and put line under it
n = turtle.Turtle() 
n.shape("turtle")
n.pen(pensize = 5)
turn = 30
for i in range(12):
    n.hideturtle()
    n.penup()
    n.forward(170)
    n.pendown()
    n.forward(20)
    n.penup()
    n.forward(20)
    n.stamp()
    n.home()
    n.right(turn)
    turn = turn + 30
    n.hideturtle()

# Make a clock hand
hand = turtle.Turtle()
hand.goto(0,0)
hand.left(90)
hand.pensize(5)
hand.fd(150)
hand.shape("arrow")
hand.stamp()
hand.goto(0,0)
hand.right(90)
hand.fd(100)

# Putting initial under the clock located at the center
n.penup()
n.goto(0, -260)
n.pendown()
n.write("N.A.", align = "center", font = ("Britannic Bold", 15, "normal"))
