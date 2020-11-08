import pygame
from api.Game import*

class Nivel(object):
    def __init__(self):
        self.background = None

    def setBackground(self, background):
        self.background = pygame.image.load(background)
        self.background = self.background.convert()

    def render(self, screen, h, v):
        screen.blit(self.background, (h, v))

    def destroy(self):
        self.background = None