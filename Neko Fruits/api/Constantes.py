import pygame

class Constantes (object):
    instance = None
    initialized = False
    RESOLUCIONH = 600
    RESOLUCIONV = 800
    RESOLUCION = (RESOLUCIONV, RESOLUCIONH)

    def __new__(cls, *args, **kwargs):
        if (Constantes.instance is None):
            Constantes.instance = object.__new__(cls, *args, **kwargs)
            cls.init(Constantes.instance)
        else:
            print("cuidado: Constantes(): no deberia instanciar mas de una vez esta clase, usar Constantes.inst()")
        return Constantes.instance
    @classmethod
    def inst(cls):
        if (not cls.instance):
            return cls()
        return cls.instance

    def init(self):
        if (Constantes.initialized):
            return