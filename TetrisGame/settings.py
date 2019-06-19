#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019-6-17 14:31:10
# @Author   : WUGE
# @Email    : 
# @Copyright: 

SCREEN_WIDTH = 1200    #窗口宽度
SCREEN_HEIGHT = 900    #窗口高度
CELL_WIDTH = 40         #方块在20x10个单元格组成的游戏区内移动。每个单元格的边长是40个像素。
GAME_AREA_WIDTH = CELL_WIDTH * 10       #一行10个单元格
GAME_AREA_HEIGHT = CELL_WIDTH * 20      #一共20行
GAME_AREA_LEFT = (SCREEN_WIDTH - GAME_AREA_WIDTH) // 2      #游戏区左侧的空白区的宽度
GAME_AREA_TOP = SCREEN_HEIGHT - GAME_AREA_HEIGHT - 50        #游戏区顶部的空白区的宽度
EDGE_COLOR = (100, 255, 255)          #游戏区单元格边界线的颜色。今后，网格线会被去除。
CELL_COLOR = (100, 100, 100)    #单元格填充色。
BG_COLOR = (230, 230, 230)      #窗口背景色

COLUMN_NUM = 10
LINE_NUM = 20

S_SHAPE_TEMPLATE = [['.OO.',
                     'OO..',
                     '....'],
                    ['.O..',
                     '.OO.',
                     '..O.']]
# S_SHAPE_TEMPLATE = ['.OO.',
#                      'OO..',
#                      '....']

Z_SHAPE_TEMPLATE = [['OO..',
                     '.OO.',
                     '....'],
                    ['..O.',
                     '.OO.',
                     '.O..']]

I_SHAPE_TEMPLATE = [['.O..',
                     '.O..',
                     '.O..',
                     '.O..'],
                    ['....',
                     'OOOO',
                     '....',
                     '....']]

O_SHAPE_TEMPLATE = [['OO',
                     'OO']]

J_SHAPE_TEMPLATE = [['.O.',
                     '.O.',
                     'OO.'],
                    ['O..',
                     'OOO',
                     '...'],
                    ['OO.',
                     'O..',
                     'O..'],
                    ['OOO',
                     '..O',
                     '...']]

L_SHAPE_TEMPLATE = [['O..',
                     'O..',
                     'OO.'],
                    ['...',
                     'OOO',
                     'O..'],
                    ['OO.',
                     '.O.',
                     '.O.'],
                    ['..O',
                     'OOO',
                     '...']]

T_SHAPE_TEMPLATE = [['.O.',
                     'OOO',
                     '...'],
                    ['.O.',
                     '.OO',
                     '.O.'],
                    ['...',
                     'OOO',
                     '.O.'],
                    ['..O',
                     '.OO',
                     '..O']]
PIECES = {
    'S': S_SHAPE_TEMPLATE,
    'Z': Z_SHAPE_TEMPLATE,
    'J': J_SHAPE_TEMPLATE,
    'L': L_SHAPE_TEMPLATE,
    'I': I_SHAPE_TEMPLATE,
    'O': O_SHAPE_TEMPLATE,
    'T': T_SHAPE_TEMPLATE
}

PIECES_TYPE = ['S', 'Z', 'J', 'L', 'I', 'O', 'T']
PIECE_COLORS = {
    'S': (0, 255, 128),
    'Z': (255, 128, 255),
    'J': (128, 0, 255),
    'L': (0, 0, 255),
    'I': (0, 128, 0),
    'O': (255, 0, 0),
    'T': (255, 128, 0)
}

WALL_BLANK_LABEL = '-'

TIMER_INTERVAL = 1000

SCORE_LABEL_COLOR = (200, 255, 255)
SCORE_COLOR = (255, 0, 0)

EDGE_WIDTH = 3      #游戏区域外框线宽度
MARGIN_WIDTH = 40   #游戏区域边界离其他窗口元素的间距