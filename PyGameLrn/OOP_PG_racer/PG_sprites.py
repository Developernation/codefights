#!/usr/bin/env python
import pygame as pg
import os
#http://thepythongamebook.com/en:pygame:step002
class PG_sprites:
    def __init__(self,\
                fldr_path='../'):
        self.spaceShip = pg.image.load(os.path.join(fldr_path,'tiny_spaceShip.png')) #SPRITE
        self.rockImage = pg.image.load(os.path.join(fldr_path,'tiny_astroid.png'))
        self.bulletPic = pg.image.load(os.path.join(fldr_path,'space_bullet.png'))
        #self.fldr_path = fldr

    def space_ship(self,ss_x,ss_y):
        return self.spaceShip,(ss_x,ss_y)

    def rock_image(self,rock_x,rock_y):
        return self.rockImage,(rock_x,rock_y)

    def bulletPic(self,bullet_x,bullet_y):
        return self.bulletPic,(bullet_x,bullet_y)

    def rotate_sprite(self,sprite,deg):
        '''enter sprite and degrees to rotate sprite'''
        return pg.transform.rotate(sprite,deg)

    #blit these like this:
        #gameDisplay = pg.display.set_mode((display_width,display_height))
        #sprites = PgSprites()
        #gameDisplay.blit(sprites.space_ship()[0],sprites.space_ship()[1])
    #





if __name__ == "__main__":
    sprites = PgSprites()
    spriteObj = sprites.space_ship(2,3)
