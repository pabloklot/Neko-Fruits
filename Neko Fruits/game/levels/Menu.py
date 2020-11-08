import pygame
from api.Keyboard import*
from api.Game import*
from api.Nivel import*
from game.MenuActualizado import*

class Menu(Nivel):
    def __init__(self):
        Nivel.__init__(self)
        self.setBackground("assets/images/menu1.png")
        self.menuAyuda = MenuActualizado()

    # 1-Jugar 2-Exit
    def getEleccion(self):
        self.eleccion = self.menuAyuda.getEstadoMenu()
        return self.eleccion

    def update(self):
        self.menuAyuda.update()

    def render(self, screen):
        Nivel.render(self, screen, 0, 0)
        self.menuAyuda.render(screen)


    def destroy(self):
        Nivel.destroy(self)
        self.menuAyuda.destroy()