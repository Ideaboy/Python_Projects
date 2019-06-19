#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019-6-17 22:14:13
# @Author   : WUGE
# @Email    : 
# @Copyright: 
from settings import *
from gamedisplay import *

class GameWall(object):
    """游戏区墙体类。功能：记住落到底部的方块组成的“墙体”"""
    def __init__(self, screen):
        """游戏开始，有20*10 个格子为‘-’表示，墙为空"""
        self.screen = screen
        self.area = []
        line = [WALL_BLANK_LABEL] * COLUMN_NUM
        for i in range(LINE_NUM):
            self.area.append(line[:])

    def print(self):
        """打印 20*10 的二维矩阵 self.area 元素，便于调试"""
        print(len(self.area), "rows", len(self.area[0]), "colums")
        for line in self.area:
            print(line)

    def add_to_wall(self, piece):
        """把方块 piece 砌到墙体"""
        shape_turn = PIECES[piece.shape][piece.turn_times]
        for r in range(len(shape_turn)):
            for c in range(len(shape_turn[0])):
                if shape_turn[r][c] == 'O':
                    self.set_cell(piece.y + r, piece.x + c, piece.shape)

    def set_cell(self, r, c, shape_label):
        """把第 r 行  c 列的格子打上方块标记，表示此格子已占据"""
        self.area[r][c] = shape_label

    def is_wall(self, r, c):
        return self.area[r][c] != WALL_BLANK_LABEL

    def eliminate_line(self):
        """消除行，如果一行没有空白单位格子，就消掉该行，返回得分"""
        # 需要消除的几行
        lines_eliminated = []
        for r in range(LINE_NUM):
            if self.is_full(r):
                lines_eliminated.append(r)

        # 消行，更新墙体矩阵
        for r in lines_eliminated:
            self.copy_down(r)
            # 确保最上面一层下层效果如预期——清空
            for c in range(COLUMN_NUM):
                self.area[0][c] = WALL_BLANK_LABEL

        # 根据消除的行数，计算得分
        eliminate_num = len(lines_eliminated)
        assert(eliminate_num <= 4 and eliminate_num >= 0)
        if eliminate_num < 3:
            score = eliminate_num * 10
        elif eliminate_num == 3:
            score = 50
        else:
            score = 100
        return score

    def is_full(self, r):
        """判断下标为 r 的一行满了没"""
        for c in range(COLUMN_NUM):
            if self.area[r][c] == WALL_BLANK_LABEL:
                return False
        return True

    def copy_down(self, row):
        """把 r 行上面的各行下降一层"""
        for r in range(row, 0, -1):
            for c in range(COLUMN_NUM):
                self.area[r][c] = self.area[r - 1][c]
    def clear(self):
        """清除墙，为重开游戏做准备"""
        for i in range(COLUMN_NUM):
            for j in range(LINE_NUM):
                self.area[j][i] = WALL_BLANK_LABEL
