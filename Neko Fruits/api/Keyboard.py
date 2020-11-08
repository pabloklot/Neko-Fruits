import pygame

class Keyboard (object):
    instance = None
    initialized = False
    apretoA = False
    apretoW = False
    apretoD = False
    apretoS = False
    apretoSpace = False
    apretoEsc = False

    def __new__(cls, *args, **kwargs):
        if (Keyboard.instance is None):
            Keyboard.instance = object.__new__(cls, *args, **kwargs)
            cls.init(Keyboard.instance)
        else:
            print("cuidado: Keyboard(): no deberia instanciar mas de una vez esta clase, usar Keyboard.inst()")
        return Keyboard.instance

    @classmethod
    def inst(cls):
        if (not cls.instance):
            return cls()
        return cls.instance

    def init(self):
        if (Keyboard.initialized):
            return
        Keyboard.initialized = True
        Keyboard.apretoA = False
        Keyboard.apretoW = False
        Keyboard.apretoD = False
        Keyboard.apretoS = False
        Keyboard.apretoSpace = False
        Keyboard.apretoEsc = False

    def keyDown(self, key):
        if (key == pygame.K_a):
            Keyboard.apretoA = True
        if (key == pygame.K_w):
            Keyboard.apretoW = True
        if (key == pygame.K_d):
            Keyboard.apretoD = True
        if (key == pygame.K_s):
            Keyboard.apretoS = True
        if (key == pygame.K_SPACE):
            Keyboard.apretoSpace = True
        if (key == pygame.K_ESCAPE):
            Keyboard.apretoEsc = True

    def keyUp(self, key):
        if (key == pygame.K_a):
            Keyboard.apretoA = False
        if (key == pygame.K_w):
            Keyboard.apretoW = False
        if (key == pygame.K_d):
            Keyboard.apretoD = False
        if (key == pygame.K_s):
            Keyboard.apretoS = False
        if (key == pygame.K_SPACE):
            Keyboard.apretoSpace = False
        if (key == pygame.K_ESCAPE):
            Keyboard.apretoEsc = False

    def aApretada(self):
        return Keyboard.apretoA

    def wApretada(self):
        return Keyboard.apretoW

    def dApretada(self):
        return Keyboard.apretoD

    def sApretada(self):
        return Keyboard.apretoS

    def spaceApretado(self):
        return  Keyboard.apretoSpace

    def escApretado(self):
        return Keyboard.apretoEsc

    def destroy(self):
        Keyboard.instance = None