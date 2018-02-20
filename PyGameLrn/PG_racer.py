#! python3
import pygame as pg

#PART 1

pg.init()

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#windows display size
gameDisplay = pg.display.set_mode((800,600))

pg.display.set_caption('DataType Racer')

clock = pygame.time.Clock() #frames per second constructor

crashed = False
#------------game loop---------------
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)

    pygame.display.update() #flips the screen
    clock.tick(60) #sets frames per second

#-------------------------------------------------
pygame.quit() #de-initialize pygame
quit()
