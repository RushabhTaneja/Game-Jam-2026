import pygame
import random 
import math 

def draw(self, surface):
    radius =150
    pygame.draw.circle(surface, (0,0,0), self.center, radius, 3)