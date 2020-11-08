import pygame
from api.Sprite import*
from api.Keyboard import*

class MenuActualizado(Sprite):
    START = 1
    EXIT = 2
    def __init__(self):
        Sprite.__init__(self)
        fondoMenu = pygame.image.load("assets/images/menu-neko1.png")
        fondoMenu = fondoMenu.convert_alpha()
        self.setImg(fondoMenu)
        self.setCoordenadas(210, 215)
        self.estado = self.START

    def getEstadoMenu(self):
        return self.estado

    # Cambia la pantalla del MENU
    def opcionMenu(self):
        if (Keyboard.inst().wApretada()):
            self.setCoordenadas(210, 215)
            self.estado = self.START
        if (Keyboard.inst().sApretada()):
            self.setCoordenadas(210, 360)
            self.estado = self.EXIT

    def update(self):
        self.opcionMenu()
        Sprite.update(self)

    def render(self, screen):
        Sprite.render(self, screen)

    def destroy(self):
        Sprite.destroy(self)