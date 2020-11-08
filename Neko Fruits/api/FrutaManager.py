import pygame
from api.Constantes import*
from game.Fruta import *
from game.GameData import *

class FrutaManager(object):
    instance = None
    initialized = False
    #lista de frutas
    frutas = None
    def __new__(self, *args, **kwargs):
        if (FrutaManager.instance is None):
            FrutaManager.instance = object.__new__(self, *args, **kwargs)
            self.init(FrutaManager.instance)
        else:
            print("Cuidado: FrutaManager(): No se debería instanciar más de una vez esta clase. Usar FrutaManager.inst().")
        return self.instance
    @classmethod
    def inst(cls):
        if (not cls.instance):
            return cls()
        return cls.instance

    def init(self):
        if(FrutaManager.initialized):
            return
        FrutaManager.initialized = True
        #crea la lista de frutas
        FrutaManager.frutas = []

    #retorna true si choca con el gato
    def coliciones(self,sprite):
        i = 0
        while(i < len(self.frutas)):
            if(sprite.coliciones(self.frutas[i])):
                return self.frutas[i]
            i = i+1
        return None

    def update(self, gato):
        #recorre el array de frutas
        for i in range(0, len(FrutaManager.inst().frutas)-1):
            try:
                f = FrutaManager.inst().frutas[i]
                #este if evita que se caiga si un lugar de la lista esta vacia
                if(f.getTipoDeFruta != None):
                    #si una fruta choca contra el gato se suma los puntos de la fruta al score o la accion correspondiente
                    if(f.coliciones(gato)):
                        #si tiene menos de 3 vidas al comer un chocolate se le suma 1 vida
                        if(GameData.inst().getVidas() != 3 and f.getTipoDeFruta() == 3):
                            GameData.inst().addVidas(1)
                        else:
                            GameData.inst().addScore(f.getPuntosFruta())
                    #perder vidas
                    if(f.getVertical() > Constantes.RESOLUCIONV-205 and 3 > f.getTipoDeFruta()):
                        GameData.inst().addVidas(-1)
                #al chocar con el gato o salir de la pantalla se elimina las frutas
                if(f.getVertical() > Constantes.RESOLUCIONV-205 or f.coliciones(gato)):
                    f.destroy()
                    FrutaManager.inst().frutas.pop(i)
                else:
                    f.update()
            except:
                pass

    def render(self, pantalla):
        for f in FrutaManager.inst().frutas:
            f.render(pantalla)

    def addFruta(self, frutas):
        FrutaManager.inst().frutas.append(frutas)

    def destroy(self):
        i = len(FrutaManager.inst().frutas)
        while (i > 0):
            FrutaManager.frutas[i-1].destroy()
            FrutaManager.frutas.pop(i-1)
            i = i-1
        FrutaManager.instance = None