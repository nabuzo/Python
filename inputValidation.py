###############################################################
# Author: Nicole Abuzo                                        #
# Date: 11/6/16                                               #
# Purpose: To make a TV remote Simulator using functions.     #
###############################################################

# User Information
print("**Welcome to the TurtleTV Remote Simulator**")
print("Valid Inputs:")
print("P(power on/off), V+/V-(vol.up/down), C+/C-(chan.up/down), M(mute), Channel number(1 through 5)")

import turtle

# Input Validation
def validInput(choice):
    if choice == "P" or "V+" or "V-" or "C+" or "C-" or "M" or "1" or "2" or "3" or "4" or "5":
        return True
    else:
        return False

# Initializing power, volume, channel
tv = turtle.Turtle()
def processChoice(choice, power, volume, channel):
    if choice == "P":
        if power == "off":   # Vice versa
            power = "On"
            channel = 1
            volume = 1
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "pink")
        elif power == "on":
            power = "Off"
    elif choice == "V+": # Volume
        volume += 1
        if volume >4:
            volume = 0
    elif choice == "V-":
        volume -= 1
        if volume<1:
            volume = 4
    elif choice == "M": # Mute
        volume = 0
    elif choice == "1":
        channel = 1
        tv.pen(pencolor= "black", pensize= 5, fillcolor= "pink")
    elif choice == "2":
        channel = 2
        tv.pen(pencolor= "black", pensize= 5, fillcolor= "light blue")
    elif choice == "3":
        channel = 3
        tv.pen(pencolor= "black", pensize= 5, fillcolor= "yellow")
    elif choice == "4":
        channel = 4
        tv.pen(pencolor= "black", pensize= 5, fillcolor= "blue")
    elif choice == "5":
        channel = 5
        tv.pen(pencolor= "black", pensize= 5, fillcolor= "light green")
    elif choice == "C+": # Channel
        channel += 1
        if channel > 5:
            channel = 1
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "pink")
        elif channel == 1:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "pink")
        elif channel == 2:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "light blue")
        elif channel == 3:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "yellow")
        elif channel == 4:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "blue")
        elif channel == 5:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "light green")
    elif choice == "C-":
        channel -= 1
        if channel < 1:
            channel = 5
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "light green")
        elif channel == 1:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "pink")
        elif channel == 2:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "light blue")
        elif channel == 3:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "yellow")
        elif channel == 4:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "blue")
        elif channel == 5:
            tv.pen(pencolor= "black", pensize= 5, fillcolor= "light green")

    return power, volume, channel

# Creating TV with turtle graphics
def printTVState(power, volume, channel):
    tv.pu()
    tv.setposition(-300, -150)
    tv.pd()
    tv.begin_fill()
    for i in range(2):
        tv.fd(600)
        tv.lt(90)
        tv.fd(300)
        tv.lt(90)
    tv.end_fill()
    tv.pu()
    # Anthena
    tv.goto(0,150)
    tv.pd()
    tv.lt(45)
    tv.fd(100)
    tv.pu()
    tv.pd()
    tv.goto(0,150)
    tv.lt(90)
    tv.fd(100)
    tv.ht()
    # TV information
    tv.pu()
    tv.goto(-280, -130)
    tv.write("TV is " + str(power) + " Channel: " + str(channel) + " Volume Level: " + str(volume), align="left", font=("Britannic Bold", 15, "normal"))
    tv.speed(10)
    tv.setheading(0)

def main():
    power = "off"
    channel = 0
    volume = 0
    tv.pen(pencolor= "black", pensize= 5, fillcolor= "gray")
    while True:
        printTVState(power, volume, channel)
        choice = input("Enter your button choice: ").upper()
        if choice == "X":
            print("Goodbye and thank you for using this app :)")
            break
        else:
            power, volume, channel = processChoice(choice, power, volume, channel)
            print("TV is", power, "Channel:", channel, "Volume Level:", volume)
main()
