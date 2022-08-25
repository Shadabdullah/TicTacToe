from concurrent.futures.process import _ThreadWakeup
from ctypes.wintypes import RGB
from email.base64mime import body_encode
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
HEIGHT = WIDTH
LINE_WIDTH = 15
DIAG_WIDTH = 25
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
            


    drawLine() 

         
#Check win

def Win(player):
    
    hori = horizontalWin(player)
    verti = verticalWin(player)
    diag = digonalWin(player)
    return hori or verti or diag
def horizontalWin(player):
    for r in range(BORD_ROWS):
        if board[r][0]== player and board[r][1]==player and board[r][2]== player:
            pygame.draw.line(screen,CIRCLE_COLOR,(0,r*200+100),(600,r*200+100),LINE_WIDTH)
            return True
    return False
def verticalWin(player):
    for r in range(BORD_ROWS):
        if board[0][r]== player and board[1][r]==player and board[2][r] == player:
            pygame.draw.line(screen,CIRCLE_COLOR,(r*200+100,0),(r*200+100,600),LINE_WIDTH)
            return True

    return False

def digonalWin(player):
    if board[0][0]==player and board[1][1]==player and board[2][2]==player:
        pygame.draw.line(screen,CIRCLE_COLOR,(0,0),(600,600),DIAG_WIDTH)
        return True
    elif board[2][0]==player and board[1][1]==player and board[0][2]==player:
        pygame.draw.line(screen,CIRCLE_COLOR,(0,600),(600,0),DIAG_WIDTH)
        return True
    else:
        return False

def tie():
    screen.fill(RGB_COLOR)
    board =np.zeros((BORD_ROWS,BORD_COLS))
    pygame.draw.rect(screen,CIRCLE_COLOR,10,10,-1)
    
def restart():
    pass
#Check Horizontall
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
gameOver = False
while True:
    for event in pygame.event.get():
        if event.type ==pygame.QUIT:
            sys.exit()

        if event.type ==pygame.MOUSEBUTTONDOWN  and gameOver== False:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            clicked_row =int(mouseY//200)
            clicked_col = int(mouseX//200)
            if not is_board_full():
                if is_available(clicked_row,clicked_col):
                    if player ==1:
                        mark_square(clicked_row,clicked_col,player)
                        board[clicked_row][clicked_col]=player 
                        if Win(player):
                            gameOver = True
                        player = 2

                    elif player==2:
                        mark_square(clicked_row,clicked_col,player)
                        board[clicked_row][clicked_col]=player
                        if Win(player):
                            gameOver = True
                        player =1
                    
                    draw_figure()
                    if is_board_full():
                        tie()     
       
                    
                  
                    

    pygame.display.update()


