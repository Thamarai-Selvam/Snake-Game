#imports needed 
import pygame
import tkinter as tk

import random
import math

dim = [500, 500]#width and height of game box
game_dim = [30, 30] # width and height of actual game / rows and cols

class cube():
    
    rows = game_dim[1]
    width = dim[1]

    def __init__ (self, start,x=1, y=0,color=(255, 0, 0)):
        self.pos = start
        self.x = x
        self.y = y
        self.color = color
    
    def draw(self, surface):
        dis = self.width // self.rows
        row = self.pow[0]
        col = self.pow[1]
        pygame.draw.rect(surface, self.color, (row * dis+1, col * dis+1, dis - 2, dis - 2))

    def move():
        self.x = x
        self.y = y
        self.pos = (self.pos[0] + self.x, self.pos[1] + self.y)

class snake():
    body = []
    turns = {}


    def __init__(self, color, pos):
        
        self.color = color
        self.head = cube(pos)
        self.body.append(self.head)
        self.x = 0
        self.y = 1

    def draw(self, surface):
        for i, c in enumerate(self.body):
                c.draw(surface)
    def reDraw():
        global root
        root.fill(0,0,0)
        s.draw(root)
        egg.draw(root)
        pygame.display.update()

    def drawGrid(cols, rows, surface):
        gap = cols //  rows

        x,y = 0,0
        for i in range(rows):
            x,y = x + gap, y + gap
            pygame.draw.line(surface, WHITE, (x, 0), (x, cols))
            pygame.draw.line(surface, WHITE, (0, y), (cols, y))
        
    def move(self):














