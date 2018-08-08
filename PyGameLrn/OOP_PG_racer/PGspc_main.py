import pygame as pg
import time
from PG_Bkg import PG_Bkg
from PG_sprites import Block
from PG_music import PG_music
import os
from PG_utils import text_objects,get_sounds

#-------------------SOUND-------------------------------------
track1 = PG_music()
pg.init()#initialize Pygame
pg.mixer.init() #initialize game music
track1.load_music()
LASER = os.path.join('..','lsr.wav')
BOMB = os.path.join('..','bomb.wav')

#-------------------set up display-----------------------------
bg = PG_Bkg()
gameDisplay = bg.dsp_dims()
bg_img = bg.load_img()
#copy of copy dimensions of background image
bkg_rect = bg_img.get_rect()

#---------------------SPRITES----------------------------------
ship = Block(os.path.join('..','tiny_spaceShip.png'))#.convert()
astroid = Block(os.path.join('..','tiny_astroid.png'),20)#.convert()
spBullet = Block(os.path.join('..','space_bullet_11x20.png'))#.convert()
explosion = Block(os.path.join('..','explosion60x50.png'))

sprites = pg.sprite.Group([ship,astroid,spBullet,explosion])

clock = pg.time.Clock() #frames per second constructor

#--------------FUNCTIONS-------------------
def blitMe(sprt,x,y):
    return gameDisplay.blit(sprt,(x,y))

def message_display(txt):
    largeTxt = pg.font.Font('freesansbold.ttf',36) #set font
    txtSurf,txtRect = text_objects(txt,largeTxt) #create text surface
    txtRect.center = (bg.dspW/2),(bg.dspH/2)
    gameDisplay.blit(txtSurf,txtRect) #shows on screen
    pg.display.update()
    time.sleep(3)

#-----------------GAME LOOP-------------------
def game_loop():
    bullets = []
    blitMe(bg_img,bkg_rect)
    pg.display.update()

    ob_x_start = random.randrange(0,bg.dspW)#(display_width * 0.30)
    ob_y_start = -600
    bg_y = 0
    ob_speed = 7
    bg_change_speed = 7
    #---------car location start
    ship_x = (bg.dspW * 0.45)
    ship_y = (bg.dspH * .5)

    #change location of ship
    x_change = 0
    y_change = 0

    #----------for moving the display----------------------
    #x1 = 0
    y1 = -bg.dspH
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

                #---------end event handling------
        ship_x+= x_change #this will set the actual location of the car
        ship_y+= y_change
        bg_y += bg_change_speed
        ob_y_start+= ob_speed
        y1 += 4.1
        y += 4.1

        blitMe(bg_img,(0,y))
        blitMe(bg_img,(0,y1))
