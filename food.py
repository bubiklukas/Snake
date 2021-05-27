import pygame
import random
class Food(object):
    
    def __init__(self):
        self.count = 1
        self.width = 10
        self.x = 0
        self.y = 0
        self.color = 255, 0, 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.width))

    def randomize(self, WIDTH, HEIGHT):
        self.x = random.randrange(3 * self.width, (WIDTH - 3 * self.width)/10) * self.width
        self.y = random.randrange(3 * self.width, (HEIGHT - 3 * self.width)/10) * self.width

    

