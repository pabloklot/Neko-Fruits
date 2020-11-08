import pygame

class Cuerpos ():
    SIGUE = 0
    CHOCA = 1
    LOOP = 2

    def __init__(self):
        #coordenadas
        self.horizontal = 0
        self.vertical = 0
        self.velocidadH = 0
        self.velocidadV = 0
        self.minH = 0
        self.maxH = 0
        self.minV = 0
        self.maxV = 0
        #comportamiento de los cuerpos contra el borde
        self.bordesAccion = Cuerpos.SIGUE
        #indica si esta muerto o no
        self.estaMuerto = False

    # get coordenadas
    def getHorizontal(self):
        return self.horizontal

    def getVertical(self):
        return self.vertical

    #set coordenadas
    def setCoordenadas(self,coordHorizontal,coordVertical):
        self.horizontal = coordHorizontal
        self.vertical = coordVertical

    #set velocidad horizontal
    def setVelocidadH(self, velH):
        self.velocidadH = velH

    #set velocidad vertical
    def setVelocidadV(self,velV):
        self.velocidadV = velV

    #set limites
    def setlimites(self, minH, maxH, minV , maxV):
        self.minH = minH
        self.maxH = maxH
        self.minV = minV
        self.maxV = maxV

    #set comportamiento al chocar contra el borde
    def setBordeAccion(self, bordeAccion):
        self.bordesAccion = bordeAccion

    #ve el chequeo con los bordes y hace el comportamiento correcto al chocar
    def verBordes(self):
        #si es sigue no chequea bordes
        if (self.bordesAccion == Cuerpos.SIGUE):
            return
        #saber que borde esta tocando el objeto
        izquierda = (self.horizontal < self.minH)
        derecha = (self.horizontal > self.maxH)
        arriba = (self.vertical < self.minV)
        abajo = (self.vertical > self.maxV)
        #si no toca los bordes no hace nada
        if (not (izquierda or derecha or arriba or abajo)):
            return
        #corregir la posicion del objeto
        #loop
        if (self.bordesAccion == Cuerpos.LOOP):
            if(izquierda):
                self.horizontal = self.maxH
            if(derecha):
                self.horizontal = self.minH
            if(arriba):
                self.vertical = self.maxV
            if(abajo):
                self.vertical = self.minV
        #choca y rebotar evita que salgan del mapa
        else:
            if(izquierda):
                self.horizontal = self.minH
            if(derecha):
                self.horizontal = self.maxH
            if(arriba):
                self.vertical = self.minV
            if(abajo):
                self.vertical = self.maxV
        #para choca el objeto se detiene
        if(self.bordesAccion == Cuerpos.CHOCA):
            self.velocidadH = 0

    #update
    def update(self):
        self.horizontal += self.velocidadH
        self.vertical += self.velocidadV
        #comportamiento con el borde
        self.verBordes()

    #destroy
    def destroy(self):
        self=None