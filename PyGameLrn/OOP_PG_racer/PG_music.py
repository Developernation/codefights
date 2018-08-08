#!/usr/bin/env python
import pygame as pg
import os

class PG_music:
    def __init__(self,fldr_path='../'):
        pg.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
        self.fldr_path = fldr_path
    #make sure you initialize both pygame
    #and the pg.mixer.init() prior to running anython else

    def load_music(self,music_tmp='moment_of_truth.mp3'):
        pg.mixer.music.load(os.path.join(self.fldr_path,music_tmp))
        pg.mixer.music.play(-1)

    # def play_music(self):
    #     return pg.mixer.music.play(-1)
