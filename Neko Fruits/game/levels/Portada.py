import pygame
from api.Keyboard import*
from api.Nivel import*

class Portada(Nivel):
    def __init__(self):
        Nivel.__init__(self)

    def init(self):
        self.setBackground("assets/images/portada1.png")

    def render(self, screen):
        Nivel.render(self, screen, 0, 0)

    def destroy(self):
        Nivel.destroy(self)