import pygame
from api.Sprite import*

class SpriteAnimado(Sprite):
    frameActual = 0
    framePausado = 0
    loop = False

    def setListaParaAnimar(self, lista):
        self.lista = lista

    def getListaParaAnimar(self):
        return self.lista

    def setAccionActual(self, accion):
        self.accion = accion

    def getAccionActual(self):
        return self.accion

    def setDelay(self, delay):
        self.delay = delay

    def getDelay(self):
        return self.delay

    def setLoop(self, loop):
        self.loop = loop

    def getLoop(self):
        return  self.loop

    # carga las imagenes para una lista (numero de frames y el nombre de el frame) o una imagen (si tiene solo 1 frame)
    def iniciaListas(self, numeroDeFrames, nombre):
        i = 0
        lista = []
        while (i <= numeroDeFrames - 1):
            img = pygame.image.load(nombre + str(i + 1) + ".png")
            img = img.convert_alpha()
            lista.append(img)
            i = i + 1
        return lista

    #anima las listas de sprites
    def animacion(self):
        if(self.lista != None):
            largo = len(self.lista)
            if (self.frameActual < largo):
                self.setImg(self.lista[self.frameActual])
            else:
                self.frameActual = 0
            self.framePausado = self.framePausado + 1
            if (self.framePausado > self.delay):
                self.frameActual = self.frameActual + 1
                self.framePausado = 0

    def __init__(self):
        Sprite.__init__(self)

    def update(self):
        Sprite.update(self)

    def render(self, pantalla):
        self.animacion()
        Sprite.render(self, pantalla)

    def destroy(self):
        i = len(self.lista)
        while i > 0:
            self.lista[i - 1] = None
            self.lista.pop(i - 1)
            i = i - 1
        Sprite.destroy(self)