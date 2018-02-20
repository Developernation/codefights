#! python3
__author__ = "Educode,llc"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Educode,llc"
__email__ = " "
__status__ = "Production"
#Enter this in to your browswer: https://codehs.com/editor/579512/525359/0/0
import turtle
import time
import random

#-------------Function---------------
def draw_circles():
    alex.left(90)
    alex.forward(50)
    alex.down()
    alex.pencolor("blue")

    for i in range(50):
        alex.speed(7)
        alex.forward(70)
        alex.left(123)
    alex.up()
    alex.speed(2)

def ninja_turtle():
    #alex.up()
    alex.speed(10)
    alex.pencolor("red")
    for i in range(181):
        alex.forward(100)
        alex.right(30)
        alex.forward(20)
        alex.left(60)
        alex.forward(50)
        alex.right(30)

        alex.penup()
        alex.setposition(0, 0)
        alex.pendown()

        alex.right(2)
    alex.up()
    alex.home()
    turtle.done()


def draw_poly():
    x = 0
    alex.clear()
    alex.right(90)
    alex.forward(124)
    alex.right(45)
    alex.down() # sets down the pen, so that turtle can draw
    alex.speed(10)
    while x < 120: # while the value of x is lesser than 120,
                    #continuously do this:
        alex.fd(100)
        alex.pencolor("blue")
        alex.rt(85)
        alex.pencolor("red")
        alex.fd(100)
        alex.pencolor("green")
        alex.rt(85)
        alex.pencolor("yellow")
        alex.fd(100)
        alex.pencolor("pink")
        alex.rt(85)
        alex.pencolor("blue")
        alex.fd(100)
        alex.pencolor("yellow")
        alex.rt(85)
        alex.pencolor("pink")
        alex.fd(100)
        alex.pencolor("red")
        alex.rt(85)
        alex.pencolor("green")
        alex.fd(100)
        alex.pencolor("blue")
        alex.rt(85)

        alex.rt(11.1111)
        x = x+1 # adds 1 to the value of x,
                # so that it is closer to 120 after every loop

def rand_num_plus():
    alex.home()
    alex.right(90)
    alex.forward(35)
    numOne = random.randint(1,20)
    numTwo = random.randint(1,20)
    #numThree = random.randint(1,20)
    answer = numOne + numTwo
    alex_talk = "{} + {} = ?".format(numOne,numTwo)
    alex.write(alex_talk, True, align="center", font=("Ariel",24,"normal"))
    alex.forward(25)
    return answer

def right_answer():
    alex.home()
    alex.up()
    alex.right(90)
    alex.forward(30)
    alex.clear()
    alex.write("Nice Job!", True, align="center", font=("Ariel",14,"normal"))
    alex.forward(10)
    alex.up()
    time.sleep(2)
    alex.clear()

def cool_thing():
    alex.home(8)
    draw_circles()

#-----------------------Turtle Characteristics----------------------------------
alex = turtle.Turtle()
alex.shape("turtle")
alex.color("green")
#------------------------Screen Characteristics---------------------------------
ts = turtle.Screen()
ts.bgcolor("orange")
#---------------BEGIN FOR LOOP WITH BOOLEANS USING CONDITIONALS-----------------
for i in range(10):
    alex.up()
    math_result = rand_num_plus()
    your_answer = input("{} Enter your number: ".format(i+1))
    if str(math_result) is your_answer: #if this is True then....
        #do this stuff
        right_answer()
        draw_circles()
        input()
        alex.clear()
    elif your_answer.title() is "We Love Educode":
        alex.clear()
        alex.write("That is ALWAYS right :)", True, align="center", font=("Ariel",14,"normal"))
        time.sleep(2)
        alex.forward(20)
        draw_poly()
        time.sleep(2)
        alex.speed(2)
        alex.color("green")
        alex.clear()
    else: #else if you get the wrong answer
          # math_result is not your answer
        #do this stuff
        alex.home()
        alex.left(90)
        alex.forward(20)
        alex.clear()
        alex.write("False: your answer doesn't equal the result", True, align="center", font=("Ariel",14,"normal"))
        alex.color("blue")
        alex.forward(25)
        alex.up()
        time.sleep(2)
        alex.color("green")
        alex.clear()

#------------end for loop---------------------------
alex.home()
alex.left(90)
alex.fd(20)
alex.write("Good Job! Thanks for playing!", True, align="center", font=("Ariel",14,"normal"))
alex.up()
time.sleep(1)
alex.clear()
ts.bgcolor("black")
ninja_turtle()


#--------sources---------------
#http://www.instructables.com/id/Easy-Designs-Turtle-Graphics-Python/
#https://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/OurFirstTurtleProgram.html
#https://docs.python.org/2/library/turtle.html#turtle.bgcolor
#https://michael0x2a.com/blog/turtle-examples
#http://www.instructables.com/id/Easy-Designs-Turtle-Graphics-Python/
