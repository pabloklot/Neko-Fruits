import pygame
from api.SpriteAnimado import*
from api.Keyboard import*
from api.Constantes import*

class Gato(SpriteAnimado):
    # estados del gato
    QUIETO_DERECHA = 0
    QUIETO_IZQUIERDA = 1
    MOV_DERECHA = 2
    MOV_IZQUIERDA = 3
    COMER_DERECHA = 4
    COMER_IZQUIERDA = 5
    ASCO_DERECHA = 6
    ASCO_IZQUIERDA = 7
    MORIR_DERECHA = 8
    MORIR_IZQUIERDA = 9
    lado = True

    # comportamientos del gato
    #quieto
    def quietoDerecha(self):
        self.setVelocidadH(0)
        self.setListaParaAnimar(self.gatoQuietoDerecha)
        self.setAccionActual(self.QUIETO_DERECHA)
        self.setDelay(2.5)

    def quietoIzquierda(self):
        self.setVelocidadH(0)
        self.setListaParaAnimar(self.gatoQuietoIzquierda)
        self.setAccionActual(self.QUIETO_IZQUIERDA)
        self.setDelay(2.5)

    #caminando
    def caminandoDerecha(self):
        self.setLoop(True)
        self.setVelocidadH(12)
        self.setListaParaAnimar(self.gatoMovDerecha)
        self.setAccionActual(self.MOV_DERECHA)
        self.setDelay(1)

    def caminandoIzquierda(self):
        self.setVelocidadH(-12)
        self.setListaParaAnimar(self.gatoMovIzquierda)
        self.setAccionActual(self.MOV_IZQUIERDA)
        self.setDelay(1)

    #comiendo
    def comiendoDerecha(self):
        self.setLoop(True)
        self.setVelocidadH(0)
        self.setListaParaAnimar(self.gatoComerDerecha)
        self.setAccionActual(self.COMER_DERECHA)

    def __init__(self):
        SpriteAnimado.__init__(self)
        #listas de animacion del gato
        self.gatoQuietoDerecha = self.iniciaListas(8, "assets/images/neko-quieto-derecha")
        self.gatoQuietoIzquierda = self.iniciaListas(8, "assets/images/neko-quieto-izquierda")
        self.gatoMovDerecha = self.iniciaListas(8, "assets/images/caminata-derecha-neko")
        self.gatoMovIzquierda = self.iniciaListas(8, "assets/images/neko-caminando-izquierda")
        self.gatoComerDerecha = self.iniciaListas(9, "assets/images/comiendo")
        #comportamiento inicial del gato
        self.setCoordenadas(350, 500)
        self.setlimites(0, Constantes.RESOLUCIONH + 60, 0, Constantes.RESOLUCIONV)
        self.setBordeAccion(Cuerpos.CHOCA)

    def update(self):
        if (not Keyboard.inst().aApretada() and not Keyboard.inst().dApretada()):
            if (self.lado == True):
                self.quietoDerecha()
            else:
                self.quietoIzquierda()
        elif (Keyboard.inst().dApretada()):
            self.caminandoDerecha()
            self.lado = False
        elif (Keyboard.inst().aApretada()):
            self.caminandoIzquierda()
            self.lado = True
        SpriteAnimado.update(self)

    def render(self, pantalla):
        SpriteAnimado.render(self,pantalla)

    def destroy(self):
        self.num = len(self.gatoComerDerecha)
        while self.num > 0:
            self.gatoComerDerecha[self.num - 1] = None
            self.gatoComerDerecha.pop(self.num - 1)
            if (self.num != 9):
                self.gatoQuietoDerecha[self.num - 1] = None
                self.gatoQuietoDerecha.pop(self.num - 1)
                self.gatoQuietoIzquierda[self.num - 1] = None
                self.gatoQuietoIzquierda.pop(self.num - 1)
                self.gatoMovDerecha[self.num - 1] = None
                self.gatoMovDerecha.pop(self.num - 1)
                self.gatoMovIzquierda[self.num - 1] = None
                self.gatoMovIzquierda.pop(self.num - 1)
            self.num = self.num - 1
        SpriteAnimado.destroy(self)