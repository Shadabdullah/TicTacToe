from ctypes.wintypes import RGB
from re import S
from turtle import Screen
from matplotlib.lines import Line2D
from matplotlib.pyplot import draw
import pygame ,sys
import numpy as np

#Intialization of pygame
pygame.init()

#Constants

WIDTH = 600
HEIGHT = 600
LINE_WIDTH = 15
CIRCLE_WIDTH = 15
CIRCLE_RADIUS= 60
BORD_COLS = 3
BORD_ROWS = 3
CROSS_WIDTH = 25
SPACE = 55
#Color
RED = (250,0,0)
RGB_COLOR = '#14BDAC'
XLINE_COLOR = "#545454"
LINE_COLOR = "#0DA192"
CIRCLE_COLOR = "#FFFFFF"
#Screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption( "Tic Tac Toe" )
screen.fill(RGB_COLOR)

#Board
board =np.zeros((BORD_ROWS,BORD_COLS))

def drawLine():
    #Horizontal Lines
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    #Vertical Lines
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400 ,0),(400,600),LINE_WIDTH)





#marked Square
def draw_figure():
    for row in range(BORD_ROWS):
        for col in range(BORD_COLS):
            
            if board[row][col]==1:
                pygame.draw.circle(screen,CIRCLE_COLOR,(int(col*200+100),int(row*200+100)),CIRCLE_RADIUS,CIRCLE_WIDTH)
            elif board[row][col]== 2:
                pygame.draw.line(screen,XLINE_COLOR,(col* 200 +SPACE,row*200+200-SPACE),(col *200+200-SPACE,row*200+SPACE),CROSS_WIDTH)
                pygame.draw.line(screen,XLINE_COLOR,(col* 200 +SPACE,row*200+SPACE),(col *200+200-SPACE,row*200+200-SPACE),CROSS_WIDTH)
            
                

def mark_square(row,col,player):
    board[row][col]= player

def is_available(row,col):
    return board[row][col]==0

def is_board_full():

    for r in range(BORD_ROWS):
        for c in range(BORD_COLS):
            if board[r][c]==0:
                return False
    return True
    
drawLine()

#Main loop
player = 1
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

        if event.type ==pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row =int(mouseY//200)
            clicked_col = int(mouseX//200)
            if not is_board_full():
                if is_available(clicked_row,clicked_col):
                    if player ==1:
                        mark_square(clicked_row,clicked_col,player)
                        board[clicked_row][clicked_col]=player
                        player = 2

                    elif player==2:
                        mark_square(clicked_row,clicked_col,player)
                        board[clicked_row][clicked_col]=player
                        player =1
                    
                    draw_figure()
                   

                    
                  
                    

    pygame.display.update()


