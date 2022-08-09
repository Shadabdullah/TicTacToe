from ctypes.wintypes import RGB
from matplotlib.lines import Line2D
from matplotlib.pyplot import draw
import pygame ,sys
pygame.init()

#Constants
RED = (250,0,0)
RGB_COLOR = (28,170,156)
WIDTH = 600
HEIGHT = 600
LINE_COLOR =(23 ,145,135)
LINE_WIDTH = 15
#Screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption( "Tic Tac Toe" )
screen.fill(RGB_COLOR)


def drawLine():
    #Horizontal Lines
    pygame.draw.line(screen,LINE_COLOR,(0,200),(600,200),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(0,400),(600,400),LINE_WIDTH)
    #Vertical Lines
    pygame.draw.line(screen,LINE_COLOR,(200,0),(200,600),LINE_WIDTH)
    pygame.draw.line(screen,LINE_COLOR,(400 ,0),(400,600),LINE_WIDTH)



drawLine()
#Main loop
while True:
    for event in pygame.event.get():
        if pygame.event ==pygame.QUIT:
            sys.exit()

    pygame.display.update()


