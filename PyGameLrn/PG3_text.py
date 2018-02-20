#! python3
import pygame
pygame.init()

#COLOR CONTSTANTS
BLK = (0,0,0)
WHT = (255,255,255)
GRN = (0,255,0)
BLU = (0,0,255)
RED = (255,0,0)

#SET WINDOW CONSTANT
WIN_SIZE = (400,400)

dispObj  = pygame.display.set_mode(WIN_SIZE)

pygame.display.set_caption("Sims Cool Game")

clock = pygame.time.Clock()
a_number = 3
#-------------MAIN PROGRAM LOOP ---------------
    #-----EVENT PROCESSING BELOW------------
done = False
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    #--EVENT PROCESSING GOES ABOVE THIS LINE

    #--GAME LOGIC BELOW HERE

    #--GAME LOGIC ABOVE HERE

    #---DRAW BELOW THIS LINE---
    #clear screen
    dispObj.fill(WHT)
    #  Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri',25,True)
    text = font.render("My text: " + str(3),True,BLK)
    # Put the image of the text on the screen at 250x250
    dispObj.blit(text,[250,250])


    pygame.display.flip()
    #frames per second
    clock.tick(60)

pygame.quit()
