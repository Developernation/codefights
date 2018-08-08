from PG_sprites import PG_sprites
from PG_music import PG_music
from PG_message import make_caption,text_objects,message_display
from PG_Bkg import PG_Bkg
import pygame as pg
import random
import time


#-----Constructors---
track1 = PG_music()
sprites = PG_sprites()
bg = PG_Bkg()
#---initialize Pygame ----
pg.init()
#---initialize music in Pygame
pg.mixer.init()
#-----------------------------
#-----------------------------
track1.load_music()

#-------VARIABLES----
color = PG_Bkg.colors
#---Constants--------
display_width = 800
display_height = 600
#--------------------

ship_x = (display_width * 0.45)
ship_y = (display_height * .5)
ship = sprites.space_ship(ship_x,ship_y)

ast_x_start = random.randrange(0,display_width)#(display_width * 0.30)
ast_y_start = -600
astroid = sprites.rock_image(ast_x_start,ast_y_start)

astImage_w = 50
astImage_h = 94
shipImg_w = 40 #pixels
shipImg_h = 40 #pixels
#---------rotate sprite image-------
astroid_rot = sprites.rotate_sprite(astroid[0],20)
#-----------------------------------

#----Background display dimensions
gameDisplay = bg.dsp_dims()
bg_img = bg.load_img()

#copy of backgrou image
bkg_rect = bg_img.get_rect()

clock = pg.time.Clock() #frames per second constructor

def game_loop(disp_w=800,disp_h=600,ast_x=random.randrange(50,750) \
    ,ast_y=-600,ast_speed=7,bg_speed=7,bg_y=0): #this is how we control our game
    #----background -----------
    gameDisplay.blit(bg_img,bkg_rect)
    pg.display.update()
    #---------rock location start
    #change location of car
    ship_x = (disp_w * 0.45)
    ship_y = (disp_h * .5)

    x_change = 0
    y_change = 0

    #----------for moving the display----------------------
    #x1 = 0
    y1 = -disp_h
    y = 0
    #-------------------------------------------------------

    gameExit = False #we don't want the game to exit only from a crash
    #------------game loop---------------
    while not gameExit:
        #-----event loop-----------------
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameExit = True

            #if L or R key is pressed down
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q: #quits if the user pressses q
                    print('q')
                    gameExit = True

                if event.key == pg.K_LEFT:
                    x_change = -5
                elif event.key == pg.K_RIGHT:
                    x_change = 5
                #up down
                if event.key == pg.K_UP:
                    y_change = -5
                elif event.key == pg.K_DOWN:
                    y_change = 5
            #if L or R key is released
            if event.type == pg.KEYUP:
                if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                    x_change = 0
                if event.key == pg.K_UP or event.key == pg.K_DOWN:
                    y_change = 0
        #---------end event handling------
        ship_x += x_change #this will set the actual location of the car
        ship_y += y_change
        bg_y += bg_speed
        ast_y += ast_speed
        y1 += 4.1
        y += 4.1
            #print(event)

        #change background (need to be before the car )
        #moving the background-------------------

        gameDisplay.blit(bg_img,(0,y))
        gameDisplay.blit(bg_img,(0,y1))

        if y > disp_h:
            y = -disp_h
        if y1 > disp_h:
            y1 = -disp_h
        #----------------------------------------
        #---------sprites------------------
        gameDisplay.blit(astroid_rot,(ast_x,ast_y))

                #-----------------------------------------------------------------------

        if ast_y > disp_h:#moves the rock to the top of the screen if it is at the bottom
            ast_y = 0 - astImage_h
            ob_x_start = random.randrange(0,display_width-astImage_w)

        pg.display.update() #flips the screen
        clock.tick(60) #sets frames per second
#-------------------------------------------------
game_loop()
pg.quit() #de-initialize pygame
quit()
