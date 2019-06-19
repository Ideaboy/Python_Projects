#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019-6-17 14:34:31
# @Author   : WUGE
# @Email    : 
# @Copyright:
from settings import *
from gamedisplay import *
import pygame

class Piece(object):
    """俄罗斯方块类"""
    def __init__(self, shape, screen, gamewall):
        self.x = 4
        self.y = 0
        self.shape = shape
        self.turn_times = 0
        self.screen = screen
        self.is_on_botton = False
        self.game_wall = gamewall   # 添加一个墙体，作用：方框与墙体区域碰撞联系

    def paint(self):
        shape_template = PIECES[self.shape][self.turn_times]

        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    self.draw_cell(self.y + r, self.x + c)

    def draw_cell(self, r, c):
        GameDisplay.draw_cell(self.screen, r, c, PIECE_COLORS[self.shape])

    def move_d(self):
        if self.can_move_d():
            self.y += 1
        else:
            self.is_on_botton = True
    def move_l(self):
        if self.can_move_l():
            self.x -= 1
    def move_r(self):
        if self.can_move_r():
            self.x += 1

    def can_move_r(self):
        shape_template = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    if self.x + c >= COLUMN_NUM - 1 or self.game_wall.is_wall(self.y + r, self.x + c + 1):
                        return False
        return True
    def can_move_l(self):
        shape_template = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    if self.x + c <= 0 or self.game_wall.is_wall(self.y + r, self.x + c - 1):
                        return False
        return True
    def can_move_d(self):
        shape_template = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    # 扩展 碰撞区域
                    # if self.y + r >= LINE_NUM - 1:
                    if self.y + r >= LINE_NUM - 1 or self.game_wall.is_wall(self.y + r + 1, self.x + c):
                        return False
        return True

    def turn(self):
        if self.can_turn():
            shape_list_len = len(PIECES[self.shape])
            self.turn_times = (self.turn_times + 1) % shape_list_len

    def can_turn(self):
        shape_list_len = len(PIECES[self.shape])
        turn_times = (self.turn_times + 1) % shape_list_len
        shape_template = PIECES[self.shape][turn_times]
        for r in range(len(shape_template)):
            for c in range(len(shape_template[0])):
                if shape_template[r][c] == 'O':
                    if (self.x + c < 0 or self.x + c >= COLUMN_NUM) or (self.y + r < 0 or self.y + r >= LINE_NUM - 1\
                            or self.game_wall.is_wall(self.y + r, self.x + c)):
                        return False
        return True

    def fall_down(self):
        while not self.is_on_botton:
            self.move_d()

    def hit_wall(self):
        shape_mtx = PIECES[self.shape][self.turn_times]
        for r in range(len(shape_mtx)):
            for c in range(len(shape_mtx[0])):
                if shape_mtx[r][c] == 'O':
                    if self.game_wall.is_wall(self.y + r, self.x + c):
                        return True
        return False
