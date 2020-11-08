import pygame
import random
from api.Keyboard import*
from api.FrutaManager import*
from api.Constantes import*
from api.Sprite import*
from game.GameData import*

class Fruta(Sprite):
    TIPO_MANZANA = 0
    TIPO_BANANA = 1
    TIPO_SANDIA = 2
    TIPO_CHOCORETO = 3
    TIPO_PEZ = 4
    TIPO_VENENO = 5
    TIPO_WISHWASH = 6
    TIPO_PESA = 7
    TIPO_ENERGIZANTE = 8
    puntosFruta = 0
    tipoDeFruta = None
    velFruta = 5
    cambiaVel = 500
    imgFruta = None

    # da un numero aleatoreo que corresponda a una fruta y le da los puntos o acciones a cada fruta
    def frutaAleatorea(self):
        aparicion = random.randint(1, 100)
        self.imgFruta = None
        if (aparicion in range(0, 41)):
            self.tipoDeFruta = self.TIPO_MANZANA
            self.imgFruta = "assets/images/manzana1.png"
            self.puntosFruta = 50
        if (aparicion in range(41, 56)):
            self.tipoDeFruta = self.TIPO_BANANA
            self.imgFruta = "assets/images/bananas1.png"
            self.puntosFruta = 100
        if (aparicion in range(56, 68)):
            self.tipoDeFruta = self.TIPO_SANDIA
            self.imgFruta = "assets/images/sandia1.png"
            self.puntosFruta = 200
        if (aparicion in range(68, 71)):
            self.tipoDeFruta = self.TIPO_CHOCORETO
            self.imgFruta = "assets/images/chocoreto1.png"
            self.puntosFruta = 500
        if (aparicion in range(71, 101)):
            self.tipoDeFruta = self.TIPO_PEZ
            self.imgFruta = "assets/images/pez1.png"
            self.puntosFruta = -100
        # carga imagen
        img = pygame.image.load(self.imgFruta)
        img = img.convert_alpha()
        self.setImg(img)

    #cambia la velocidad de la fruta dependiendo de los puntos
    def cambiaVelFruta(self, score):
        if(score > self.cambiaVel):
            self.cambiaVel = self.cambiaVel*2
            self.velFruta += 1

    def __init__(self):
        Sprite.__init__(self)
        self.setlimites(0, Constantes.RESOLUCIONH, 0, Constantes.RESOLUCIONV)
        self.frutaAleatorea()
        self.setCoordenadas(random.randint(0, 700), -150)
        FrutaManager.inst().addFruta(self)

    def getTipoDeFruta(self):
        return self.tipoDeFruta

    def getPuntosFruta(self):
        return self.puntosFruta

    def update(self):
        self.cambiaVelFruta(GameData.inst().getScore())
        self.setVelocidadV(self.velFruta)
        Sprite.update(self)

    def render(self, pantalla):
        Sprite.render(self,pantalla)

    def destroy(self):
        Sprite.destroy(self)