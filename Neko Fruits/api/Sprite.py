import pygame
from api.Cuerpos import*

class Sprite (Cuerpos):
    def __init__(self):
        Cuerpos.__init__(self)

    def setImg(self, img):
        self.img = img
        # guarda ancho y alto
        self.anchoImg = self.img.get_width()
        self.altoImg = self.img.get_height()

    def getAnchoImg(self):
        return self.anchoImg

    def getAltoImg(self):
        return self.altoImg

    #coliciones
    def coliciones(self,sprite):
        x1 = self.getHorizontal()
        y1 = self.getVertical()
        w1 = self.getAnchoImg()
        h1 = self.getAltoImg()
        x2 = sprite.getHorizontal()
        y2 = sprite.getVertical()
        w2 = sprite.getAnchoImg()
        h2 = sprite.getAltoImg()
        if ((((x1 + w1) > x2) and (x1 < (x2 + w2))) and (((y1 + h1) > y2) and (y1 < (y2 + h2)))):
            return True
        else:
            return False

    def update(self):
        Cuerpos.update(self)

    def render(self, screen):
            screen.blit(self.img, (self.getHorizontal(), self.getVertical()))

    def destroy(self):
        Cuerpos.destroy(self)
        self.img = None