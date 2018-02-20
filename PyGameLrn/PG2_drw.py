#! python3

import pygame,math
pygame.init()

#---------------------
#Basic game logic
#----------------------
# While not done:
# For each event (keypress, mouse click, etc.):
# Use a chain of if statements to run code to handle each event.
# Run calculations to determine where objects move, what happens when objects collide, etc.
# Clear the screen
# Draw everything
#----------------------------------------------------------------------

#Color Constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

PI = math.pi
#CREATE WINDOW SIZE CONSTANT
WIN_SIZE = (400,400)

disObj = pygame.display.set_mode(WIN_SIZE)

pygame.display.set_caption("Sims Cool Game")

clock = pygame.time.Clock()

#-------MAIN PROGRAM LOOP------------------------------------

#loop until user clicks the close buttong
done = False
#------EVENT PROCESSING BELOW THIS LINE----------
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #--EVENT PROCESSING GOES ABOVE THIS LINE

    #--GAME LOGIC BELOW HERE

    #--GAME LOGIC ABOVE HERE

    #---DRAWING CODE BELOW THIS COMMENT------------
    #clear the screen First
    disObj.fill(WHITE)

    #draw stuff                    x/y        x/y
                                #origin(top left)
    #                                         wide/tall
    pygame.draw.rect(disObj, RED, [20, 20, 250, 100],2)
    pygame.draw.ellipse(disObj, BLACK, [20,20,250,100], 2)

    # Draw an arc as part of an ellipse. Use radians to determine what
    # angle to draw.
    pygame.draw.arc(disObj, GREEN, [100,100,250,200],  PI/2,     PI, 2)
    pygame.draw.arc(disObj, BLACK, [100,100,250,200],     0,   PI/2, 2)
    pygame.draw.arc(disObj, RED,   [100,100,250,200],3*PI/2,   2*PI, 2)
    pygame.draw.arc(disObj, BLUE,  [100,100,250,200],    PI, 3*PI/2, 2)

    for y_offset in range(0, 100, 30):
        pygame.draw.line(disObj,RED,[0,0+y_offset],[100,210+y_offset],5)
    #y is smallest at the top and increases as we move down
    #flip screen
    pygame.display.flip()
    #----DRAWING CODE ABOVE THIS COMMENT-----------
#sets frames per second
    clock.tick(1)
pygame.quit()
