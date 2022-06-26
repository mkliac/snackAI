import pygame as pg

class Draw:
    def __init__(self,screen,block_size,text_font):
        self.screen = screen
        self.block_size = block_size
        self.text_font = text_font

    def drawGrid(self,row,col,border_color):
        for x in range(col):
            for y in range(row):
                rect = pg.Rect(x*self.block_size,y*self.block_size,self.block_size,self.block_size)
                pg.draw.rect(self.screen,border_color,rect,1)

    def drawSnack(self,snakePieces):
        for block in snakePieces:
            rect = pg.Rect(block.getX()*self.block_size,block.getY()*self.block_size,self.block_size,self.block_size)
            pg.draw.rect(self.screen,block.getColor(),rect,1)

    def drawFood(self,food_block):
        rect = pg.Rect(food_block.getX()*self.block_size,food_block.getY()*self.block_size,self.block_size,self.block_size)
        pg.draw.rect(self.screen,food_block.getColor(),rect,1)

    def showText(self,message,x,y):
        text = self.text_font.render(message,1,(200,200,200))
        self.screen.blit(text,(x,y))

    def screenClear(self):
        self.screen.fill((0,0,0))

