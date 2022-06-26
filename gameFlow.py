from operator import ge
from snackBody import Snack
from draw import Draw
from block import Block
import pygame as pg
import random
import time

BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255,0,0)
BLUE = (0,0,255)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 800
BLOCK_SIZE = 20
SPEED = 15
GRID_ROW = int(WINDOW_WIDTH/(2*BLOCK_SIZE))
GRID_COL = int(WINDOW_HEIGHT/BLOCK_SIZE)

def validateMove(head_x,head_y,snackBody):
    if(head_x < 0 or head_y < 0 or head_x >= GRID_COL or head_y >= GRID_ROW):
        return False

    for block in snackBody:
        if block.getX() == head_x and block.getY() == head_y:
            return False

    return True

def move(dir,head_x,head_y):
    rx = 0
    ry = 0

    if(dir == 'W'):
        rx = head_x
        ry = head_y - 1
    elif(dir == 'A'):
        rx = head_x - 1
        ry = head_y
    elif(dir == 'S'):
        rx = head_x
        ry = head_y + 1
    elif(dir == 'D'):
        rx = head_x + 1
        ry = head_y
    
    rx = rx % GRID_COL
    ry = ry % GRID_ROW
    return rx, ry

def changeDir(dir,idir):
    rdir = ''
    if(idir == pg.K_UP):
        if(dir != 'S'):
            rdir = 'W'
        else:
            rdir = 'S'
    elif(idir == pg.K_LEFT):
        if(dir != 'D'):
            rdir = 'A'
        else:
            rdir = 'D'
    elif(idir == pg.K_DOWN):
        if(dir != 'W'):
            rdir = 'S'
        else:
            rdir = 'W'
    elif(idir == pg.K_RIGHT):
        if(dir != 'A'):
            rdir = 'D'
        else:
            rdir = 'A'

    return rdir

def generateFood():
    x = random.randint(1,GRID_COL)-1
    y = random.randint(1,GRID_ROW)-1
    block = Block(x,y,RED)

    return block

def main():
    pg.init()
    SCREEN = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    
    gameOver = False
    score = 0
    dir = 'D'
    head_x,head_y = int(GRID_COL/2), int(GRID_ROW/2)
    foodBlock = generateFood()

    snack = Snack(BLUE,head_x,head_y)

    drawer = Draw(SCREEN,BLOCK_SIZE)

    fps = pg.time.Clock()

    drawer.drawGrid(GRID_ROW,GRID_COL,WHITE)
    drawer.drawFood(foodBlock)
    drawer.drawSnack(snack.getPieces())
    pg.display.update()

    while(gameOver == False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                dir = changeDir(dir,event.key)
        
        head_x,head_y = move(dir,head_x,head_y)
 
        if(head_x == foodBlock.getX() and head_y == foodBlock.getY()):
            foodBlock = generateFood()
            score += 1
        else:
            snack.pop()

        if(validateMove(head_x,head_y,snack.getPieces()) == False):
            gameOver = True
        
        snack.append(head_x,head_y)

        drawer.drawGrid(GRID_ROW,GRID_COL,WHITE)
        drawer.drawFood(foodBlock)
        drawer.drawSnack(snack.getPieces())

        pg.display.update()
        fps.tick(SPEED)
    
    print("game over")

if __name__ == "__main__":
    main()