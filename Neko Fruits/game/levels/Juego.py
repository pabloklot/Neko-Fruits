import pygame
from game.Gato import *
from game.GameData import *
from game.Deco import *
from game.Fruta import *
from api.Nivel import *
from api.Game import *
from api.FrutaManager import*

class Juego(Nivel):
    gato = None
    deco = None
    def __init__(self):
        Nivel.__init__(self)
        self.setBackground("assets/images/bg1.png")
        GameData.inst().setScore(0)
        GameData.inst().setVidas(3)
        self.gato = Gato()
        self.deco = Deco()

    def update(self, spawnDeFrutas):
        self.gato.update()
        self.deco.update()
        # aparicion de las frutas
        if (spawnDeFrutas ==  0):
            Fruta()
        FrutaManager.inst().update(self.gato)
        #print("Score: " + str(GameData.inst().getScore()))
        #print("Vidas: " + str(GameData.inst().getVidas()))

    def render(self, screen):
        Nivel.render(self, screen, 0, 0)
        self.gato.render(screen)
        FrutaManager.inst().render(screen)
        self.deco.render(screen)

    def destroy(self):
        Nivel.destroy(self)
        self.gato.destroy()
        self.gato = None
        self.deco.destroy()
        self.deco = None
        FrutaManager.inst().destroy()
        Nivel.destroy(self)