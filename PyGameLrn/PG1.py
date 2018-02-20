import pygame
#http://programarcadegames.com/index.php?chapter=introduction_to_graphics&lang=en#section_5
#https://www.webpagefx.com/web-design/color-picker/

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
# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)

#CRATE WINDOW SIZE
win_size = (700,700)
#
screen_dispObj = pygame.display.set_mode(win_size)
#
# setting the window title
pygame.display.set_caption("EduCode Racer")

#loop until user clicks the close buttong
done = False

clock = pygame.time.Clock()

#----------MAIN PROGRAM LOOP-----------------------------
while not done:
    #---main even loop
    for event in pygame.event.get(): #User did something
        #this is the proper way to shut down a pygame program
        if event.type == pygame.QUIT: # if user clicked close
            done = True #flag that we are done so we exit the loop
#--EVENT PROCESSING GOES ABOVE THIS LINE

#--GAME LOGIC BELOW HERE

#--GAME LOGIC ABOVE HERE

#---DRAWING CODE BELOW THIS COMMENT------------

#First, clear the screen to white. Don't put other drawing elements above here
#or they will be erased with this command
    screen_dispObj.fill(WHITE) #clears the screen
    for i in range(0,700,10):
#                          origin is at top left
#                          origin,desination,how thick we want the line
        pygame.draw.line(screen_dispObj,GREEN,[i,0],[350,350],5)
        pygame.draw.line(screen_dispObj,GREEN,[700,i],[350,350],5)
#--lets the user see what is on the screen
    pygame.display.flip()
#---DRAWING CODE ABOVE THIS COMMENT-------------


#--limits to 60 frames per second
    clock.tick(60)
#----Update the screen with what we've drawing
pygame.quit()

# #create window SIZE
# win_size = (500,500)
#
# screen = pygame.display.set_mode(win_size)
#
# #setting the window title
# py game.display.set_caption("Sims Cool Game")
