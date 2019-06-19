#!/usr/bin/python 
# -*- coding:utf-8 -*-
# @Time     : 2019-6-17 22:32:44
# @Author   : WUGE
# @Email    : 
# @Copyright:

from settings import *
import pygame

class GameDisplay(object):
    @staticmethod
    def draw_cell(screen, r, c, color):
        """第y行x列的格子，填充color颜色"""

        cell_position = (c * CELL_WIDTH + GAME_AREA_LEFT + 3,
                         r * CELL_WIDTH + GAME_AREA_TOP + 3)
        cell_width_height = (CELL_WIDTH - 5, CELL_WIDTH - 5)
        cell_rect = pygame.Rect(cell_position, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)

    @staticmethod
    def draw_game_area(screen, game_state, game_resource):
        """绘制游戏区域"""
        # 水平线
        # for r in range(21):
        #     pygame.draw.line(screen, EDGE_COLOR,
        #                      (GAME_AREA_LEFT, GAME_AREA_TOP + r * CELL_WIDTH),
        #                      (GAME_AREA_LEFT + GAME_AREA_WIDTH, GAME_AREA_TOP + r * CELL_WIDTH))
        #
        # # 垂直线
        # for c in range(11):
        #     pygame.draw.line(screen, EDGE_COLOR,
        #                      (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP),
        #                      (GAME_AREA_LEFT + c * CELL_WIDTH, GAME_AREA_TOP + GAME_AREA_HEIGHT))
        # 绘制游戏运动区域
        GameDisplay.draw_border(screen, GAME_AREA_LEFT - EDGE_WIDTH, GAME_AREA_TOP, LINE_NUM, COLUMN_NUM)

        GameDisplay.draw_wall(game_state.wall)
        # 绘制分数
        GameDisplay.draw_score(screen, game_state.game_score)
        # 绘制游戏次数
        GameDisplay.draw_count(screen, game_state.session_count)

        # 绘制下一块方块
        GameDisplay.darw_next_piece(screen, game_state.new_piece)
        # 绘制开始提示
        if game_state.stopped:
            if game_state.session_count > 0:
                GameDisplay.draw_gameover_prompt(screen, game_resource)
            else:
                GameDisplay.draw_start_prompt(screen, game_resource)
        if game_state.paused:
            GameDisplay.draw_pause_prompt(screen, game_resource)

    @staticmethod
    def draw_start_prompt(screen, game_resource):
        """绘制开始提示"""
        start_tip_position = (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2)
        screen.blit(game_resource.load_newgame_img(), start_tip_position)
    @staticmethod
    def draw_pause_prompt(screen, game_resource):
        """绘制暂停提示"""
        start_tip_position = (SCREEN_WIDTH / 2 - 200, SCREEN_HEIGHT / 2)
        screen.blit(game_resource.load_pausing_img(), start_tip_position)
    @staticmethod
    def draw_gameover_prompt(screen, game_resource):
        """绘制结束提示"""
        start_tip_position = (SCREEN_WIDTH / 2 - 100, SCREEN_HEIGHT / 2 - 100)
        screen.blit(game_resource.load_gameover_img(), start_tip_position)

    @staticmethod
    def draw_wall(game_wall):
        """绘制墙体"""
        for r in range(LINE_NUM):
            for c in range(COLUMN_NUM):
                if game_wall.area[r][c] != WALL_BLANK_LABEL:
                    GameDisplay.draw_cell(game_wall.screen, r, c, PIECE_COLORS[game_wall.area[r][c]])
    @staticmethod
    def draw_score(screen, score):
        """绘制游戏得分"""
        # 字体大小、编码格式
        score_label_font = pygame.font.SysFont('simhei', 28)
        # 字体内容，颜色
        score_label_surface = score_label_font.render(u'得分：', False, SCORE_LABEL_COLOR)
        score_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 40, GAME_AREA_TOP + 200)
        screen.blit(score_label_surface, score_label_position)

        score_font = pygame.font.SysFont('arial', 28)
        score_surface = score_font.render(str(score), False, SCORE_COLOR)
        score_label_width = score_label_surface.get_width()
        score_position = (score_label_position[0] + score_label_width + 20, score_label_position[1])
        screen.blit(score_surface, score_position)

    @staticmethod
    def draw_count(screen, count):
        '''次数'''
        count_label_font = pygame.font.SysFont('simhei', 28)
        # 字体内容，颜色
        count_label_surface = count_label_font.render(u'游戏次数：', False, SCORE_LABEL_COLOR)
        count_label_position = (GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + 40, GAME_AREA_TOP + 250)
        screen.blit(count_label_surface, count_label_position)

        count_font = pygame.font.SysFont('arial', 28)
        count_surface = count_font.render(str(count), False, SCORE_COLOR)
        count_label_width = count_label_surface.get_width()
        count_position = (count_label_position[0] + count_label_width + 20, count_label_position[1])
        screen.blit(count_surface, count_position)

    @staticmethod
    def darw_next_piece(screen, next_piece):
        """绘制下一块方块"""
        # 绘制边框
        start_x = GAME_AREA_LEFT + COLUMN_NUM * CELL_WIDTH + MARGIN_WIDTH
        start_y = GAME_AREA_TOP
        GameDisplay.draw_border(screen, start_x, start_y, 4, 4)

        if next_piece:
            start_x += EDGE_WIDTH
            start_y += EDGE_WIDTH
            cells = []  # cells变量存储姿态矩阵中有砖块的单元格
            # 扫描姿态矩阵，得出有砖块的单元格
            shape_template = PIECES[next_piece.shape]
            shape_turn = shape_template[next_piece.turn_times]
            for r in range(len(shape_turn)):
                for c in range(len(shape_turn[0])):
                    if shape_turn[r][c] == 'O':
                        cells.append((c, r, PIECE_COLORS[next_piece.shape]))

            max_c = max([cell[0] for cell in cells])
            min_c = min([cell[0] for cell in cells])
            start_x += round((4 - (max_c - min_c + 1)) / 2 * CELL_WIDTH)
            max_r = max([cell[1] for cell in cells])
            min_r = min([cell[1] for cell in cells])
            start_y += round((4 - (max_r - min_r + 1)) / 2 * CELL_WIDTH)

            # 绘制方块
            for cell in cells:
                color = cell[2]
                left_top = (start_x + (cell[0] - min_c) * CELL_WIDTH,
                            start_y + (cell[1] - min_r) * CELL_WIDTH)
                GameDisplay.draw_cell_rect(screen, left_top, color)

    @staticmethod
    def draw_border(screen, start_x, start_y, line_num, column_num):
        top_border = pygame.Rect(start_x, start_y, 2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, top_border)

        left_border = pygame.Rect(start_x, start_y, EDGE_WIDTH, 2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, left_border)

        right_border = pygame.Rect(start_x + EDGE_WIDTH + column_num * CELL_WIDTH, start_y, EDGE_WIDTH,
                                   2 * EDGE_WIDTH + line_num * CELL_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, right_border)

        bottom_border = pygame.Rect(start_x, start_y + EDGE_WIDTH + line_num * CELL_WIDTH,
                                    2 * EDGE_WIDTH + column_num * CELL_WIDTH, EDGE_WIDTH)
        pygame.draw.rect(screen, EDGE_COLOR, bottom_border)

    @staticmethod
    def draw_cell_rect(screen, left_top_anchor, color):
        left_top_anchor = (left_top_anchor[0] + 1, left_top_anchor[1] + 1)
        cell_width_height = (CELL_WIDTH - 2, CELL_WIDTH - 2)
        cell_rect = pygame.Rect(left_top_anchor, cell_width_height)
        pygame.draw.rect(screen, color, cell_rect)
