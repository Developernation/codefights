import pygame as pg
from PG_Bkg import PG_Bkg as pgb

#--------------FUNCTIONS-------------------
def text_objects(txt,font):
    txtSurface = font.render(txt,True,pgb.colors['RED'])
    return txtSurface, txtSurface.get_rect()

def get_sounds(soundPath):
    return pg.mixer.Sound(soundPath)
