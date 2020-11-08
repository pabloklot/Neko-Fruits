import pygame
from api.Nivel import*
from api.Keyboard import*
from game.levels.Juego import*
from game.levels.Portada import*
from game.levels.Menu import*
from api.Constantes import*
from game.levels.Pausa import*
from game.GameData import*

class Game(object):
    # Def de tipo api
    screen = None
    fullscreen = False
    clock = None
    # Def de tipo game
    PORTADA = 0
    MENU = 1
    JUEGO = 2
    PAUSA = 3
    nivelActual = 0
    portada = None
    menu = None
    juego = None
    pausa = None
    spawnDeFrutas = 30
    salir = False

    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Neko Fruits")
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(Constantes.RESOLUCION)
        self.fullscreen = False
        self.clock = pygame.time.Clock()
        self.nivelActual = 0
        self.portada = None
        self.menu = None
        self.juego = None
        self.pausa = None
        self.spawnDeFrutas = 30
        self.salir = False

    def loopJuego(self):
        self.salir = False
        self.portada = Portada()
        self.menu = Menu()
        self.portada.init()
        while (not self.salir):
            # Frames
            self.clock.tick(30)
            # TECLADO GAME
            for event in pygame.event.get():
                # Quit(X)
                if (event.type == pygame.QUIT):
                    self.salir = True
                # Fullscreen(F)
                if (event.type == pygame.KEYDOWN):
                    Keyboard.inst().keyDown(event.key)
                    if (event.key == pygame.K_f):
                        self.fullscreen = not self.fullscreen
                        if (self.fullscreen):
                            self.screen = pygame.display.set_mode(Constantes.RESOLUCION, pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode(Constantes.RESOLUCION)
                # TECLADO PAUSA
                elif (Keyboard.inst().spaceApretado() and self.nivelActual == self.PAUSA):
                    # 1-Jugar 2-Salir / Exit
                    if (self.pausa.getEleccion() == 2 and Keyboard.inst().spaceApretado() ):
                        self.juego.destroy()
                        self.juego = None
                        self.nivelActual = self.MENU
                        self.menu = Menu()
                    # Regresa al juego
                    else:
                        self.nivelActual = self.JUEGO
                    # Sale de la pausa
                    self.pausa.destroy()
                    self.pausa = None
                # TECLADO MENU
                elif(self.nivelActual == self.MENU):
                    # 1 - Jugar
                    if(Keyboard.inst().spaceApretado() and self.menu.getEleccion() == 1):
                        self.menu.destroy()
                        self.menu = None
                        self.nivelActual = self.JUEGO
                        self.juego = Juego()
                        GameData.instance = None
                    elif(Keyboard.inst().spaceApretado() and self.menu.getEleccion() == 2):
                        self.salir = True
                # TECLADO DE PORTADA
                elif (Keyboard.inst().spaceApretado() or Keyboard.inst().dApretada() or Keyboard.inst().aApretada()):
                    # Si se apr seta SPACE, A o D se va al MENU (hace destroy de portada, cambia el nivel actual a MENU y lo inicia)
                    if (self.nivelActual == self.PORTADA):
                        self.portada.destroy()
                        self.portada = None
                        self.nivelActual = self.MENU
                # ESC
                elif (Keyboard.inst().escApretado()):
                    # En caso de PORTADA y MENU se sale del juego
                    if (self.nivelActual == self.PORTADA or self.nivelActual == self.MENU):
                        self.salir = True
                    # En caso JUEGO entra en PAUSA y se detiene el update de juego
                    if(self.nivelActual == self.JUEGO):
                        self.nivelActual = self.PAUSA
                        self.pausa = Pausa()
                # REINICIA EL TECLADO (Deja las teclas apretadas en False)
                if(event.type == pygame.KEYUP):
                    Keyboard.inst().keyUp(event.key)
            # LOGICA DE LOS NIVELES DEL JUEGO (1-PORTADA 2-MENU 3-JUEGO)
            # PORTADA
            if (self.nivelActual == self.PORTADA):
                self.portada.render(self.screen)
            # MENU
            if(self.nivelActual == self.MENU):
                self.menu.update()
                self.menu.render(self.screen)
            # JUEGO
            if(self.nivelActual == self.JUEGO):
                self.juego.update(self.spawnDeFrutas)
                # LLUVIA DE FRUTAS
                if (self.spawnDeFrutas > 0):
                    self.spawnDeFrutas = self.spawnDeFrutas - 1
                else:
                    self.spawnDeFrutas = random.randint(15, 30)
                self.juego.render(self.screen)
                # GAME OVER
                if(GameData.inst().getVidas() == 0):
                    self.juego.destroy()
                    self.juego = None
                    self.nivelActual = self.MENU
                    self.menu = Menu()
            # PAUSA el render de juego esta dentro de pausa asi las animaciones del juego continuan en su lugar
            if(self.nivelActual == self.PAUSA):
                self.juego.render(self.screen)
                self.pausa.update()
                self.pausa.render(self.screen)
            #actualiza la pantalla
            pygame.display.flip()
        # Destroy
        pygame.mouse.set_visible(True)
        pygame.quit()