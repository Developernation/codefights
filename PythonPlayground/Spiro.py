#! python3

import math,PIL,turtle

class Spiro:
'''draws a single curve using draw() and animates a set of random
   spiros using a timer and update()'''
    def __init__(self, xc:'x coord', yc:'y coord', col, R:'large circle radius', r:'small circle radius', l):
       #create turtle object
       self.ttl = turtle.Turtle() #helps you draw multiple spiros at the same time

       #set cursor shape
       self.ttl.shape('turtle')

       # set the step in degrees. its the angle for parametric drawing
       self.step = 5 #should this be radians?

       #set the drawing complete flag
       self.drawingComplete = False

       #set parameters
       self.setParams(xc, yc, col, R, r, l)

       # initialize the drawing
       self.restart()

    #set the paremeters
    def setParams(self,xc, yc, col, R, r, l):
        # the Spirograph parameters
        self.xc = xc # stores the coords of the center of the curve
        self.yc = yc # stores the coords of the center of the curve
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # reduce r/R to its smallest from by dividing with the GCD
        gcdVal = gcd(self.r,self.R) #built in. Used to compute the GCD of the radii
                #You’ll use this information to determine the periodicity of the curve
        self.nRot = self.r // gcdVal #periodicity of the curve
        # get ratio of radii
        self.k = r/float(R)
        # set color
        self.ttl.color(*col) # *args
        #store the current angle
        self.a = 0 #current angle used to create animation

    def restart(self):
        # set the flag
        #allows you to keep track of whether a particular spiro is complete
        self.drawingComplete = False
        # show the turtle
        self.ttl.showturtle() #shows it in case it was hidden
        # go to the first point
        self.ttl.up() #do this to move to the 1st position w/o drawing a line
        R, k, l = self.R,self.k,self.a
        a = 0.0
        # compute the x- and y-coordinates with the angle a set to 0 to get
        # the curve’s starting point.
        x = R*((1-k)*math.cos(a) + l*k*math.cos((1-k)*a/k))
        y = R*((1-k)*math.sin(a) - l*k*math.sin((1-k)*a/k))
        self.ttl.setpos(self.xc + x, self.yc + y)
        self.ttl.down() #you’ve finished, and you set the pen down. The
                        # setpos() call will draw the actual line.
        ##########page 25##################
