#!/usr/bin/env python
import pygame as pg
import os
from PG_Bkg import PG_Bkg
#http://thepythongamebook.com/en:pygame:step002
#programarcadegames.com/index.php?chapter=introduction_to_sprites
#
class Block(pg.sprite.Sprite):
    def __init__(self,imgPath,rotation=None):
        super().__init__() #call to the parent class constructor in SPRITE
        #load image
        self.image = pg.image.load(imgPath).convert()
        #set transparent color
        self.image.set_colorkey(PG_Bkg.colors['WHITE'])
        self.rect = self.image.get_rect()
        self.rotation = rotation
        if rotation != None:
            pg.transform.rotate(self.image,self.rotation)






    # def __init__(self,\
    #             fldr_path='../'):
    #     self.spaceShip = pg.image.load(os.path.join(fldr_path,'tiny_spaceShip.png')) #SPRITE
    #     self.rockImage = pg.image.load(os.path.join(fldr_path,'tiny_astroid.png'))
    #     self.bulletPic = pg.image.load(os.path.join(fldr_path,'space_bullet.png'))
    #     #self.fldr_path = fldr
    #
    # def space_ship(self,ss_x,ss_y):
    #     return self.spaceShip,(ss_x,ss_y)
    #
    # def rock_image(self,rock_x,rock_y):
    #     return self.rockImage,(rock_x,rock_y)
    #
    # def bulletPic(self,bullet_x,bullet_y):
    #     return self.bulletPic,(bullet_x,bullet_y)
    #
    # def rotate_sprite(self,sprite,deg):
    #     '''enter sprite and degrees to rotate sprite'''
    #     return pg.transform.rotate(sprite,deg)

    #blit these like this:
        #gameDisplay = pg.display.set_mode((display_width,display_height))
        #sprites = PgSprites()
        #gameDisplay.blit(sprites.space_ship()[0],sprites.space_ship()[1])
    #





# if __name__ == "__main__":
#     sprites = PgSprites()
#     spriteObj = sprites.space_ship(2,3)
