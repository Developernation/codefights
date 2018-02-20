#! python3

import math
import turtle

#draw the circle using turtle
#(x,y) is the center of the circle
def drawCircleTurtle(x:'x coordinate',y:'y coordinate',r:'radians'):
    # move to the start of circle
    turtle.shape('turtle')
    turtle.color('black','green')
    turtle.begin_fill()
    turtle.up() # takes the pen off of the virtual paper so that it won't draw as
                # you move the turtle.
    turtle.setpos(x+r,y) # positions the turtle -- moves the turtle to the perimeter of where you
                         # want to draw your circle
    turtle.down() # puts the virtual pen back down

    #draw circle start/stop/step
    for i in range(0,300,5): # i is the angle perameter
        a = math.radians(i) #most computers use radians for angle based calculations
        turtle.setpos(x + r*math.cos(a), y + r*math.sin(a))
    turtle.end_fill()

drawCircleTurtle(0,0,50)
turtle.mainloop()

# def moveTurtle(x,y):
#     turtle.color('black','red')
#     turtle.begin_fill()
#     turtle.up()
#     turtle.setpos(0,0)
#     turtle.down()
#     turtle.up()
#     turtle.setpos(x,y)
#     turtle.down()
#     turtle.circle(60)
#     turtle.end_fill()

# moveTurtle(100,100)
# moveTurtle(-200,-200)
# turtle.mainloop()
