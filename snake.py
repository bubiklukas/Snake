import pygame
class Snake(object):

    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.width = 10
        self.children = 10
        self.children_list = []
        self.color = color
        self.pos = self.x, self.y

    def move(self, x, y):
        self.x += self.width * x
        self.y += self.width * y
        self.pos = self.x, self.y

    def position(self):
        return(self.x, self.y)
        
    def draw(self, screen, posx, posy):
        pygame.draw.rect(screen, self.color, pygame.Rect(posx, posy, self.width, self.width))
