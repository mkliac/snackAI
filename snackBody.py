from collections import deque
from block import Block
class Snack():
    def __init__(self,color,x = 0,y = 0):
        self.head_x = x
        self.head_y = y
        self.color = color

        head_block = Block(self.head_x,self.head_y,self.color)
        self.pieces = deque([head_block])

    # append new head pos at front
    def append(self,new_head_x,new_head_y):
        self.head_x = new_head_x
        self.head_y = new_head_y

        head_block = Block(self.head_x,self.head_y,self.color)
        self.pieces.appendleft(head_block)

    # pop tail
    def pop(self):
        self.pieces.pop()

    def getPieces(self):
        return self.pieces

