import sys, pygame
from pygame.locals import *

FPS = 20
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
HALF_WINDOWWIDTH = int(WINDOWWIDTH / 2)
HALF_WINDOWHEIGHT = int(WINDOWHEIGHT / 2)

WHITE      = (0, 0, 0,)
BLACK      = (255, 255, 255)
BGCOLOR    = WHITE



def main():
    global FPSCLOCK, DISPLAYSURF, BASICFONT, SQUARE

    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    pygame.display.set_caption('False')

    SQUARE = pygame.image.load('images.bmp')
    
    while True:
        runGame()


def runGame():

    playerObj = {'surface': (SQUARE)}
    
    DISPLAYSURF.fill(BGCOLOR)

DISPLAYSURF.blit(playerObj['surface'], playerObj['rect']
