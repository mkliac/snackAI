from snackBody import Snack
from draw import Draw
from block import Block
from food import Food
import config as cf
import pygame as pg
import random
import time

def validateMove(snackBody):
    head_x = snackBody[0].getX()
    head_y = snackBody[0].getY()

    if(head_x < 0 or head_y < 0 or head_x >= cf.GRID_COL or head_y >= cf.GRID_ROW):
        return False

    i = 0
    for block in snackBody:
        i = i + 1
        if i == 1:
            continue # skip head
        if block.getX() == head_x and block.getY() == head_y:
            return False

    return True

def move(dir,head_x,head_y,wall):
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
    
    if(wall == False):
        rx = rx % cf.GRID_COL
        ry = ry % cf.GRID_ROW

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

def eatFood(snackBody,foods):
    for idx, food in enumerate(foods.getBlocks()):
        for block in snackBody.getBlocks():
            if(block.getX() == food.getX() and block.getY() == food.getY()):
                foods.newFood(idx)
                return True

    return False

def main():
    pg.init()
    SCREEN = pg.display.set_mode((cf.WINDOW_WIDTH, cf.WINDOW_HEIGHT))
    text_font = pg.font.SysFont("monospace", 16)

    highest_score = 0
    gameOver = False
    score = 0
    dir = 'D'
    head_x,head_y = int(cf.GRID_COL/2), int(cf.GRID_ROW/2)
    foodHandler = Food(cf.NUM_FOOD)
    snackHandler = Snack(cf.BLUE,head_x,head_y)
    drawer = Draw(SCREEN,cf.BLOCK_SIZE,text_font)
    fps = pg.time.Clock()

    while(gameOver == False):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYDOWN:
                dir = changeDir(dir,event.key)
        
        head_x,head_y = move(dir,head_x,head_y,cf.WALL)

        snackHandler.append(head_x,head_y)

        if(eatFood(snackHandler,foodHandler) == True): #eat food
            score += 1
        else:
            snackHandler.pop()

        if(validateMove(snackHandler.getBlocks()) == False):
            gameOver = True

        drawer.screenClear()
        drawer.drawGrid(cf.GRID_ROW,cf.GRID_COL,cf.WHITE)
        drawer.drawBlocks(foodHandler.getBlocks())
        drawer.drawBlocks(snackHandler.getBlocks())
        drawer.showText("Score: {0}".format(score),cf.WINDOW_WIDTH/2,0)
        pg.display.update()
        fps.tick(cf.SPEED)

if __name__ == "__main__":
    main()