#! python3
#https://stackoverflow.com/questions/28005641/how-to-add-a-background-image-into-pygame
#https://www.youtube.com/watch?v=ZFo4mtLJEWs&index=2&list=PLQVvvaa0QuDdLkP8MrOXLe_rKuf6r80KO

#Scrolling Background
#https://stackoverflow.com/questions/17240442/how-to-make-the-background-continuously-scrolling-with-pygame
#rotate an image
#http://nullege.com/codes/search?cq=pygame.transform.rotate
#music
#http://freemusicarchive.org/genre/Chiptune/
#https://stackoverflow.com/questions/7746263/how-play-mp3-with-pygame

#the book
#http://thepythongamebook.com/en:pygame:step001

#bulletts
#https://stackoverflow.com/questions/21567250/how-to-create-bullets-in-pygame

import pygame as pg
import time
import random
#PART 2
pg.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag

pg.init() #initalize game
pg.mixer.init() #initialize game music

pg.mixer.music.load('moment_of_truth.mp3')
shot = pg.mixer.Sound('lsr.wav')
boom = pg.mixer.Sound('bomb.wav')

pg.mixer.music.play(-1)
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
bg = pg.image.load('stars2.png')
#copy of backgrou image
bkg_rect = bg.get_rect()
#----------------------------------
pg.display.set_caption('DataType Racer')

carImg = pg.image.load('tiny_spaceShip.png') #SPRITE
rockImage = pg.image.load('tiny_astroid.png')
bullet_pic = pg.image.load('space_bullet_11x20.png').convert_alpha()
explode_pic = pg.image.load('explosion60x50.png')



rockImage = pg.transform.rotate(rockImage,20)
rockImage_w = 50
rockImage_h = 94
carImg_width = 40 #pixels
carImg_height = 40 #pixels
bullet_pic_w = 11
bullet_pic_h = 20

clock = pg.time.Clock() #frames per second constructor

def rock_blit(rock_x,rock_y):
    gameDisplay.blit(rockImage,(rock_x,rock_y))

def space_bullet_blit(space_bullet_x,space_bullet_y):
    gameDisplay.blit(bullet_pic,(space_bullet_x+19,space_bullet_y-4))

def car(x,y):
    '''Sets the location of the carImg.
    In pygame, variables can be refereced outside of
    the scope of a function (i.e gameDisplay).'''
    gameDisplay.blit(carImg,(x,y)) #adds your image to the background display

def bg_blit(back_y):
    '''Moves the background image'''
    gameDisplay.blit(bg,(0,back_y))


def text_objects(txt,font):
    txtSurface = font.render(txt,True,RED)
    return txtSurface, txtSurface.get_rect()

def message_display(txt):
    largeTxt = pg.font.Font('freesansbold.ttf',36) #set font
    txtSurf,txtRect = text_objects(txt,largeTxt) #create text surface
    txtRect.center = (display_width/2),(display_height/2)
    gameDisplay.blit(txtSurf,txtRect) #shows on screen
    pg.display.update()
    time.sleep(3)



#Start the cars location 0,0 is on the upper left
# moving down increases y, moving over increases x...yes its wierd
def dodgyThings(thing_x,thing_y,thing_width,thing_height):
    pass

#-------------------------------------------------------------------------------

def game_loop(): #this is how we control our game
    bullets = []
    #----background -----------
    gameDisplay.blit(bg,bkg_rect)
    pg.display.update()
    #---------rock location start
    ob_x_start = random.randrange(0,display_width)#(display_width * 0.30)
    ob_y_start = -600
    bg_y = 0
    ob_speed = 7
    bg_change_speed = 7
    #---------car location start
    car_x = (display_width * 0.45)
    car_y = (display_height * .5)

    #change location of car
    x_change = 0
    y_change = 0

    #----------for moving the display----------------------
    #x1 = 0
    y1 = -display_height
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

                if event.key == pg.K_s:
                    shot.play()
                    bullets.append([(car_x+19),car_y])

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

        mx, my = pg.mouse.get_pos()


        #screen.blit(background, (0, 0))

        #---------end event handling------
        car_x+= x_change #this will set the actual location of the car
        car_y+= y_change
        bg_y += bg_change_speed
        ob_y_start+= ob_speed
        y1 += 4.1
        y += 4.1
            #print(event)

        #change background (need to be before the car )
        #moving the background-------------------

        gameDisplay.blit(bg,(0,y))
        gameDisplay.blit(bg,(0,y1))



        if y > display_height:
            y = -display_height
        if y1 > display_height:
            y1 = -display_height
        #----------------------------------------
        for b in range(len(bullets)):
            bullets[b][1] -= 10

        # Iterate over a slice copy if you want to mutate a list.
        for bullet in bullets[:]:
            if bullet[0] < 0:
                bullets.remove(bullet)


        for bullet in bullets:
            gameDisplay.blit(bullet_pic, pg.Rect(bullet[0], bullet[1], 0, 0))
            if ob_x_start<= bullet[0] <= ob_x_start + rockImage_w and ob_y_start <= bullet[1] <= ob_y_start + (rockImage_h-10):#collision handling
                    gameDisplay.blit(explode_pic,(ob_x_start,ob_y_start))
                    pg.display.update()
                    time.sleep(.01)
                    ob_y_start = 0 - rockImage_h

                    ob_x_start = random.randrange(0,display_width-rockImage_w)
                    boom.play()

        rock_blit(ob_x_start,ob_y_start)


        space_bullet_blit(car_x,car_y)
        car(car_x,car_y)#call function and display car

        #game_logic
        #----if the location of the car crosses the edge of the screen_dispOb aka gameDisplay

        if car_x > display_width - carImg_width or car_x < 0: #x is the locatin of the car
            message_display('You Crashed!')
            gameExit = True

        elif car_y < 0 or car_y > display_height - carImg_height:
            message_display('You Crashed!')
            gameExit = True
        #-----------------------------------------------------------------------
        #----------------------crash logic--------------------------------------
        if (ob_x_start <= car_x + carImg_width <= ob_x_start + rockImage_w and ob_y_start <= car_y + carImg_width <= ob_y_start + rockImage_h) or \
        (ob_x_start <= car_x <= ob_x_start + rockImage_w and ob_y_start <= car_y <= ob_y_start + (rockImage_h-10)):
            print(ob_x_start,car_x,(ob_x_start+rockImage_w))
            message_display('You Crashed!')
            #resets the location of the rock after you crash
            ob_x_start = random.randrange(0,display_width)
            ob_y_start = -600
            rock_blit(ob_x_start,ob_y_start)
        #-----------------------------------------------------------------------

        if ob_y_start > display_height:#moves the rock to the top of the screen if it is at the bottom
            ob_y_start = 0 - rockImage_h
            ob_x_start = random.randrange(0,display_width-rockImage_w)

        pg.display.update() #flips the screen
        clock.tick(80) #sets frames per second



#-------------------------------------------------
game_loop()
pg.quit() #de-initialize pygame
quit()
