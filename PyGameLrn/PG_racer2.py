#! python3
#https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
#https://www.youtube.com/watch?v=ZFo4mtLJEWs&index=2&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO
import pygame as pg

#PART 2

pg.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
#-----------------DISPLAY-----------------------------
display_width = 800
display_height = 600
#windows display size
gameDisplay = pg.display.set_mode((display_width,display_height))

#background image
bg = pg.image.load('road_bg.png')

pg.display.set_caption('DataType Racer')

carImg = pg.image.load('racer3.png') #SPRITE
#-------------------------------------------------------
clock = pg.time.Clock() #frames per second constructor

def car(x,y):
    '''Sets the location of the carImg.
    In pygame, variables can be refereced outside of
    the scope of a function (i.e gameDisplay).'''
    gameDisplay.blit(carImg,(x,y)) #adds your image to the background display

#Start the cars location 0,0 is on the upper left
# moving down increases y, moving over increases x...yes its wierd

x = (display_width * 0.45)
y = (display_height * .5)

crashed = False
#------------game loop---------------
while not crashed:
    #-----event loop-----------------
    for event in pg.event.get():
        if event.type == pg.QUIT:
            crashed = True
        #print(event)
    #change background
    gameDisplay.blit(bg,(0,0)) #this needs to go before the car
    car(x,y)#call function and display car

    pg.display.update() #flips the screen
    clock.tick(60) #sets frames per second

#-------------------------------------------------
pg.quit() #de-initialize pygame
quit()
