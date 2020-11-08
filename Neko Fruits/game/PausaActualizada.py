import pygame
from api.Sprite import*
from api.Keyboard import*

class PausaActualizada(Sprite):
    PLAY = 1
    EXIT = 2
    def __init__(self):
        Sprite.__init__(self)
        fondoPausa = pygame.image.load("assets/images/neko-pausa1.png")
        fondoPausa = fondoPausa.convert_alpha()
        self.setImg(fondoPausa)
        self.setCoordenadas(235, 275)
        self.estado = self.PLAY

    def getEstadoPausa(self):
        return self.estado

    # Cambia la pantalla del MENU
    def opcionPausa(self):
        if (Keyboard.inst().wApretada()):
            self.setCoordenadas(235, 275)
            self.estado = self.PLAY
        if (Keyboard.inst().sApretada()):
            self.setCoordenadas(235, 370)
            self.estado = self.EXIT

    def update(self):
        self.opcionPausa()
        Sprite.update(self)

    def render(self, screen):
        Sprite.render(self, screen)

    def destroy(self):
        Sprite.destroy(self)