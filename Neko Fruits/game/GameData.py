import pygame

class GameData(object):
    instance = None
    initialized = False
    score = 0
    vidas = 0
    def __new__(self, *args, **kwargs):
        if(GameData.instance is None):
            GameData.instance = object.__new__(self, *args, **kwargs)
            self.init(GameData.instance)
        else:
            print("Cuidado: GameData no se debería instanciar más de una vez esta clase")
        return self.instance
    @classmethod
    def inst(cls):
        if(not cls.instance):
            return cls()
        return cls.instance

    def init(self):
        if(GameData.initialized):
            return
        GameData.initialized = True
        GameData.score = 0
        GameData.vidas = 0

    def setScore(self, score):
        GameData.score = score
        self.controlScore()

    def setVidas(self, vidas):
        GameData.vidas = vidas
        self.controlVidas()

    def getScore(self):
        return GameData.inst().score

    def getVidas(self):
        return GameData.inst().vidas

    def addScore(self, score):
        GameData.inst().score += score
        self.controlScore()

    def addVidas(self, vidas):
        GameData.inst().vidas += vidas
        self.controlVidas()

    def controlScore(self):
        if(GameData.inst().score < 0):
            GameData.inst().score = 0
        if(GameData.inst().score > 99999):
            GameData.inst().score = 99999

    def controlVidas(self):
        if (GameData.inst().vidas < 0):
            GameData.inst().vidas = 0
        if (GameData.inst().vidas > 3):
            GameData.inst().vidas = 3

    def destroy(self):
        GameData.instance = None