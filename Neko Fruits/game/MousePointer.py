import pygame
from api.Mouse import*
from api.Sprite import*

class MousePointer(Sprite):
    def __init__(self):
        Sprite.__init__(self)
        # carga imagen
        imgMouse = pygame.image.load("assets/images/mouse1.png")
        imgMouse = imgMouse.convert_alpha()
        self.setImg(imgMouse)

    def update(self):
        Sprite.update(self)
        self.setCoordenadas(Mouse.inst().getX(), Mouse.inst().getY())

    def render(self, pantalla):
        Sprite.render(self, pantalla)

    def destroy(self):
        Sprite.destroy(self)