import pygame
from api.Sprite import*
from game.GameData import*

class Deco(Sprite):
    # Manejo de corazones
    def corazones(self):
        if(GameData.inst().getVidas() == 3):
            img = "assets/images/vidas4.png"
        if (GameData.inst().getVidas() == 2):
            img = "assets/images/vidas3.png"
        if (GameData.inst().getVidas() == 1):
            img = "assets/images/vidas2.png"
        if (GameData.inst().getVidas() == 0):
            img = "assets/images/vidas1.png"
        # carga imagen
        imgDeco = pygame.image.load(img)
        imgDeco = imgDeco.convert_alpha()
        self.setImg(imgDeco)

    # Manejo de score
    def score(self, screen, x, y, mensage, size, color):
        font = pygame.font.Font("assets/font/LemonMilklight.otf", size)
        imgTxt = font.render(mensage, True, color)
        screen.blit(imgTxt, (x , y))

    def __init__(self):
        Sprite.__init__(self)
        imgDeco = pygame.image.load("assets/images/vidas4.png")
        imgDeco = imgDeco.convert_alpha()
        self.setImg(imgDeco)
        self.setCoordenadas(20, 20)

    def update(self):
        self.corazones()
        Sprite.update(self)

    def render(self, screen):
        self.score(screen, 300, 10, "Score: " + str(GameData.inst().getScore()), 36, (122 ,152 ,165))
        Sprite.render(self, screen)

    def destroy(self):
        Sprite.destroy(self)