#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019-6-18 10:30:14
# @Author   : WUGE
# @Email    : 
# @Copyright: 

import random
from settings import *
from piece import Piece
from gamewall import GameWall
import pygame
import time

class GameState(object):
    """游戏状态控制类"""
    def __init__(self, screen):
        self.screen = screen
        self.wall = GameWall(screen)
        self.piece = None
        self.new_piece = None

        self.timer_interval = TIMER_INTERVAL    # 1000ms，定时器时间间隔
        self.game_score = 0
        self.stopped = True
        self.paused = False
        self.session_count = 0
        self.state = False      # 自己家的总的状态，利于状态约束键盘

    def set_timer(self, timer_interval):
        self.game_timer = pygame.time.set_timer(pygame.USEREVENT, timer_interval)

    def add_score(self, score):
        self.game_score += score

    def start_game(self):
        """开始游戏"""
        self.stopped = False
        self.paused = False
        self.session_count += 1
        self.set_timer(TIMER_INTERVAL)
        self.timer_interval = TIMER_INTERVAL
        # self.piece = Piece(random.choice(PIECES_TYPE), self.screen, self.wall)
        self.wall.clear()
        self.game_score = 0
        self.piece = self.new_piece1()
        self.piece = self.new_piece1()
        random.seed(int(time.time()))

    def new_piece1(self):
        self.piece = self.new_piece
        self.new_piece = Piece(random.choice(PIECES_TYPE), self.screen, self.wall)
        return self.piece


    def pause_game(self):
        pygame.time.set_timer(pygame.USEREVENT, 0)
        self.paused = True

    def resume_game(self):
        self.set_timer(self.timer_interval)
        self.paused = False

    # def touch_bottom(self):
    #     self.wall.add_to_wall(self.piece)
    #     self.add_score(self.wall.eliminate_line())
    #     for c in range(COLUMN_NUM):
    #         if self.wall.is_wall(0, c):
    #             self.stopped = True
    #             break
    #     if not self.stopped:
    #         self.piece = Piece(random.choice(PIECES_TYPE), self.screen, self.wall)
    #     else:
    #         self.stop_timer()

    def stop_timer(self):
        pygame.time.set_timer(pygame.USEREVENT, 0) # 清除定时器

    def touch_bottom(self):
        """结束规则，任由一列相没有空白格子，则表示失败"""
        for c in range(COLUMN_NUM):
            for r in range(LINE_NUM):
                if self.wall.area[r][c] == WALL_BLANK_LABEL:
                    break
                else:
                    self.stopped = True
        if not self.stopped:
            # self.piece = Piece(random.choice(PIECES_TYPE), self.screen, self.wall)
            self.piece = self.new_piece1()
            if self.piece.hit_wall():
                self.stopped = True
        else:
            self.stop_timer()
