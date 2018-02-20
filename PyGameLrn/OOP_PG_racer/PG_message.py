#!/usr/bin/env python
import pygame as pg

def make_caption(caption):
    return pg.display.set_caption(caption)

def text_objects(txt,font):
    txtSurface = font.render(txt,True,RED)
    return txtSurface, txtSurface.get_rect()

def message_display(txt):
    largeTxt = pg.font.Font('freesansbold.ttf',36) #set font
    #txtSurf,txtRect --this should be enclosed in main
    return text_objects(txt,largeTxt) #create text surface
