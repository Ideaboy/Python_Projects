#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019-6-18 16:06:55
# @Author   : WUGE
# @Email    : 
# @Copyright:

import pygame
import os

class GameResource(object):
    def __init__(self):
        # self.img_path = 'image'
        self.img_path = os.path.abspath('image/')
        self.newgame_img = None
        self.pasuing_img = None
        self.continue_img = None
        self.gameover_img = None
        self.music_path = os.path.abspath('music/')
        self.music_paused = False
        self.bg_img = None


    def load_newgame_img(self):
        if not self.newgame_img:
            self.newgame_img = pygame.image.load(self.img_path + 'press-s-newgame.png').convert_alpha()
        return self.newgame_img

    def load_pausing_img(self):
        if not self.pasuing_img:
            self.pasuing_img = pygame.image.load(self.img_path + "pause_img.png").convert_alpha()
        return self.pasuing_img

    def load_continue_img(self):
        if not self.continue_img:
            self.continue_img = pygame.image.load(self.img_path + "continue_img.png").convert_alpha()
        return self.continue_img

    def load_gameover_img(self):
        if not self.gameover_img:
            self.gameover_img = pygame.image.load(self.img_path + "gameover_img.png").convert_alpha()
        return self.gameover_img

    def play_bg_music(self):
        pygame.mixer.init()
        bg_music_file = self.music_path + "bg_music.mp3"
        pygame.mixer.music.load(bg_music_file)
        pygame.mixer.music.play(-1)     # -1 表示循环播放

    def pause_bg_music(self):
        if not self.music_paused:
            pygame.mixer.music.pause()
            self.music_paused = True
        else:
            pygame.mixer.music.unpause()
            self.music_paused = False

    def load_bg_img(self):
        if not self.bg_img:
            self.bg_img = pygame.image.load(self.img_path + "picture_bg.jpg")
        return self.bg_img