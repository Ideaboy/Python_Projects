#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019年6月17日12:37:03
# @Author   : WUGE
# @Email    : 
# @Copyright: 

import sys
import pygame
from settings import *
from piece import *
import random
import time
from gamewall import GameWall
from gamestate import  GameState
from gamesource import GameResource

def main():
    # 必须：初始化
    pygame.init()

    # 窗口对象，设置分辨率
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("俄罗斯方块")
    bg_color = BG_COLOR


    # 激活持续按键功能
    pygame.key.set_repeat(100, 100)

    '''垒墙'''
    game_state = GameState(screen)      # 该对象类里已经包装了 方块对象和墙体对象
    game_resource = GameResource()
    game_resource.play_bg_music()

    # 主循环
    while True:
        # 墙体、分数、方块控制
        if not game_state.stopped and game_state.piece.is_on_botton:
            game_state.wall.add_to_wall(game_state.piece)
            game_state.add_score(game_state.wall.eliminate_line())
            game_state.wall.print()
            # game_state.piece = Piece(random.choice(PIECES_TYPE), screen, game_state.wall)
            game_state.touch_bottom()

        # 事件监听
        game_state.state = game_state.paused | game_state.stopped
        check_events(game_state, game_resource)

        " # 设置屏幕背景色"
        screen.blit(game_resource.load_bg_img(), (0, 0))       # 设置画板背景色

        """# !!! 绘制要在背景画布后面,绘制都是在 SCREEN.FILL 后执行     !!!"""
        GameDisplay.draw_game_area(screen, game_state, game_resource)

        if game_state.piece:
            game_state.piece.paint()


        """一般不变绘制"""
        # draw_game_area(screen)
        # draw_game_area_grid(screen)

        pygame.display.flip()       # 刷新屏幕

def draw_game_area(screen):
    """绘制游戏区域"""
    """绘制一条线。第一参数，画板对象；第二参数，颜色；第三四坐标，x,y"""
    # 顶部
    pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                     (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP))
    # 底部
    pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP + GAME_AREA_HEIGHT),
                     (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))
    # 左侧
    pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT, GAME_AREA_TOP),
                     (GAME_AREA_LEFT, GAME_AREA_TOP + GAME_AREA_HEIGHT))
    # 右侧
    pygame.draw.line(screen, EDGE_COLOR, (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP),
                     (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))

def draw_game_area_grid(screen):
    """绘制格子"""
    # 垂直线
    for x in range(1, 10):
        pygame.draw.line(screen, EDGE_COLOR,
                         (GAME_AREA_LEFT + x * CELL_WIDTH, GAME_AREA_TOP),
                         (GAME_AREA_LEFT + x * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))
    # 水平线
    for y in range(1, 20):
        pygame.draw.line(screen, EDGE_COLOR,
                         (GAME_AREA_LEFT, GAME_AREA_TOP + y * CELL_WIDTH),
                         (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + y * CELL_WIDTH))

def draw_cell(screen, left, top):
    cell_left_top = (left, top)
    cell_width_height = (CELL_WIDTH, CELL_WIDTH)
    cell_rect = pygame.Rect(cell_left_top, cell_width_height)
    pygame.draw.rect(screen, CELL_COLOR, cell_rect)

def check_events(game_state, game_resource):
    """捕捉和处理键盘按键时间"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            on_key_down(event, game_state, game_resource)
        elif event.type == pygame.USEREVENT:
            game_state.piece.move_d()

def on_key_down(event, game_state, game_resource):
    if not game_state.state and event.key == pygame.K_DOWN:
        print("向下方向键被按下")
        print(game_state.stopped)
        if game_state.piece:
            game_state.piece.move_d()
    elif not game_state.state and event.key == pygame.K_UP:
        # print("向上方向键被按下")
        if game_state.piece:
            game_state.piece.turn()
    elif not game_state.state and event.key == pygame.K_LEFT:
        # print("向左方向键被按下")
        if game_state.piece:
            game_state.piece.move_l()
    elif not game_state.state and event.key == pygame.K_RIGHT:
        # print("向右方向键被按下")
        if game_state.piece:
            game_state.piece.move_r()
    elif not game_state.state and event.key == pygame.K_f:
        if game_state.piece:
            game_state.piece.fall_down()
    elif event.key == pygame.K_s and game_state.stopped:
        # 控制开始按键
        game_state.start_game()
    elif event.key == pygame.K_p and not game_state.stopped:
        if game_state.paused:
            game_state.resume_game()
        else:
            game_state.pause_game()
    elif event.key == pygame.K_r:
        game_state.start_game()
    elif event.key == pygame.K_m:
        game_resource.pause_bg_music()


if __name__ == "__main__":
    main()


