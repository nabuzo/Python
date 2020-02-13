#===========================================================================================
# Purpose: Program uses Turtle graphics to simulate a simple game
# Nicole Abuzo
# Date: 09/11/2016
#===========================================================================================
import turtle

# Create turtle graphic window
mw = turtle.Screen()

# Set background color and size of window
mw.bgcolor("Lightblue")
turtle.screensize(500, 500)

# Create a builder turtle and hide it
bd = turtle.Turtle()
bd.hideturtle()

# Set builder turtle's pen color, size and fill color
bd.begin_fill()
bd.pen(pencolor = "black", pensize = 5, fillcolor = "white")

# Make builder go to 4 corners and create a food bowl
bd.penup()
bd.goto(150, 150)
bd.pendown()
bd.circle(30)
bd.end_fill()
bd.begin_fill()
bd.penup()
bd.goto(-150, 150)
bd.pendown()
bd.circle(30)
bd.end_fill()
bd.begin_fill()
bd.penup()
bd.goto(-150, -150)
bd.pendown()
bd.circle(30)
bd.end_fill()
bd.begin_fill()
bd.penup()
bd.goto(150, -150)
bd.pendown()
bd.circle(30)
bd.end_fill()

# Create 4 turtles with different colors 
a = turtle.Turtle()
a.shape("turtle")
a.color("red")
a.setheading(50) 
b = turtle.Turtle()
b.shape("turtle")
b.color("yellow")
b.setheading(130)
c = turtle.Turtle()
c.shape("turtle")
c.color("green")
c.setheading(220)
d = turtle.Turtle()
d.shape("turtle")
d.color("orange")
d.setheading(320)

# Creating prompt
bowlPosition = turtle.textinput("Bowl Position", "NW, NE, SW, SE")

# Make builder turtle go to bowl
s = turtle.Turtle()
s.pen(pencolor = "blue", pensize = 3, fillcolor = "blue")
s.hideturtle()
if bowlPosition == "NW":
    s.st()
    s.penup()
    s.speed(0)
    s.goto(-150,170)
    s.begin_fill
    s.pendown()
    s.shape("triangle")
    s.end_fill()
elif bowlPosition == "NE":
    s.st()
    s.penup()
    s.speed(0)
    s.goto(150,170)
    s.begin_fill
    s.pendown()
    s.shape("triangle")
    s.end_fill()
elif bowlPosition == "SW":
    s.st()
    s.penup()
    s.speed(0)
    s.goto(-150, -120)
    s.begin_fill
    s.pendown()
    s.shape("triangle")
    s.end_fill()
elif bowlPosition == "SE":
    s.st()
    s.penup()
    s.speed(0)
    s.goto(150, -120)
    s.begin_fill
    s.pendown()
    s.shape("triangle")
    s.end_fill()

# Make turtles move to bowls
a.penup()
a.speed("slowest")
a.fd(220)
b.penup()
b.speed("slowest")
b.fd(220)
c.penup()
c.speed("slowest")
c.fd(180)
d.penup()
d.speed("slowest")
d.fd(180)

# Declaring the winner
if bowlPosition == "NW":
    bd.penup()
    bd.goto(0,0)
    bd.write("And the WINNER is....turtle YELLOW!!!", align = "center", font = ("Britannic Bold", 13, "normal"))
elif bowlPosition == "NE":
    bd.penup()
    bd.goto(0,0)
    bd.write("And the WINNER is....turtle RED!!!", align = "center", font = ("Britannic Bold", 13, "normal"))
elif bowlPosition == "SW":
    bd.penup()
    bd.goto(0,0)
    bd.write("And the WINNER is....turtle GREEN!!!", align = "center", font = ("Britannic Bold", 13, "normal"))
elif bowlPosition == "SE":
    bd.penup()
    bd.goto(0,0)
    bd.write("And the WINNER is....turtle ORANGE!!!", align = "center", font = ("Britannic Bold", 13, "normal"))
else:
    bd.hideturtle()











