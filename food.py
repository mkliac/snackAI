import random
import config as cf
from block import Block

class Food:
    def __init__(self,length):
        self.foodBlocks = []
        for i in range(length):
            self.foodBlocks.append(self.generateFood())

    def generateFood(self):
        x = random.randint(1,cf.GRID_COL)-1
        y = random.randint(1,cf.GRID_ROW)-1
        block = Block(x,y,cf.RED)

        return block

    def newFood(self,index):
        self.foodBlocks[index] = self.generateFood()

    def getBlocks(self):
        return self.foodBlocks