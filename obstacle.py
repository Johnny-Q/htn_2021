import pygame
import os
from helpers import normalizeDepth


class Obstacle():
    def __init__(self, img, x, y, lane, depth, isPiano):
        self.image = img
        self.x = x
        self.y = y
        self.lane = lane
        self.depth = depth
        self.isPiano = isPiano

    def render(self, WIN):
        # scale image
        width = 100 + int(round(500*normalizeDepth(self.depth)))
        height = 100 + int(round(500*normalizeDepth(self.depth)))
        #width, height= 2048, 2048
        temp = pygame.transform.scale(self.image, (width, height))
        WIN.blit(temp, (self.x-width/2, self.y))
