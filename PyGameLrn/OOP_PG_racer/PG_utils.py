import pygame as pg

#--------------FUNCTIONS-------------------
def text_objects(txt,font):
    txtSurface = font.render(txt,True,RED)
    return txtSurface, txtSurface.get_rect()

def get_sounds(soundPath):
    return pg.mixer.Sound(soundPath)
