import pygame
from api.Keyboard import*
from api.Game import*
from api.Nivel import*
from game.PausaActualizada import*

class Pausa(Nivel):
    def __init__(self):
        Nivel.__init__(self)
        self.setBackground("assets/images/pausa1.png")
        self.pausaAyuda = PausaActualizada()

    # 1-Jugar 2-Exit
    def getEleccion(self):
        self.eleccion = self.pausaAyuda.getEstadoPausa()
        if(self.eleccion == 1):
            return 1
        if(self.eleccion == 2):
            return 2

    def update(self):
        self.pausaAyuda.update()

    def render(self, screen):
        Nivel.render(self, screen, 170, 120)
        self.pausaAyuda.render(screen)


    def destroy(self):
        Nivel.destroy(self)
        self.pausaAyuda.destroy()