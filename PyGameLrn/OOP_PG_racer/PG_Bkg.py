#!/usr/bin/env python
import pygame as pg
import os

class PG_Bkg:
    #Class contants
    colors = {
        'BLACK':(   0,   0,   0),
        'WHITE':( 255, 255, 255),
        'GREEN':(   0, 255,   0),
        'RED':( 255,   0,   0),
        'BLUE':(   0,   0, 255)
        }

    def __init__(self,fldr_path='../',dsp_w=800,dsp_h=600,\
                dsp_img='stars2.png',
                ):
        self.dspW = dsp_w
        self.dspH = dsp_h
        self.dspImg = dsp_img
        self.fldr_path = fldr_path

    def dsp_dims(self):
        '''display dimensions'''
        return pg.display.set_mode((self.dspW,self.dspH))

    def load_img(self):
        '''loads the background'''
        return pg.image.load(os.path.join(self.fldr_path,self.dspImg))

    def get_bg_rect(self):
        '''get a duplicate background
        ..used for moving the background image'''
        return self.load_img().get_rect()

if __name__ == "__main__":
    #test
    bkg_path = '<add folder path here>'
    tBkg = PG_Bkg()
    gameDisplay = tBkg.dsp_dims()
    tBkg.load_img()
    tBkg.get_bg_rect()
    gameDisplay.blit(tBkg.load_img(),(0,0))
    pg.display.update()
