import pygame

class Mouse(object):
    instance = None
    initialized = False
    leftPressed = False
    rightPressed = False
    centerPressed = False
    leftPressedPreviousFrame = False
    def __new__(self, *args, **kwargs):
        if(Mouse.instance is None):
            Mouse.instance = object.__new__(self, *args, **kwargs)
            self.init(Mouse.instance)
        else:
            print("Cuidado: Mouse no se debería instanciar más de una vez esta clase. Usar Mouse.inst().")
        return Mouse.instance
    @classmethod
    def inst(cls):
        if(not cls.instance):
            return cls()
        return cls.instance

    def init(self):
        if(Mouse.initialized):
            return
        Mouse.initialized = True
        Mouse.leftPressed = False
        Mouse.rightPressed = False
        Mouse.centerPressed = False
        Mouse.leftPressedPreviousFrame = False

    def update(self):
        Mouse.leftPressedPreviousFrame = Mouse.leftPressed
        Mouse.leftPressed = pygame.mouse.get_pressed()[0]
        Mouse.centerPressed = pygame.mouse.get_pressed()[1]
        Mouse.rightPressed = pygame.mouse.get_pressed()[2]

    def leftPressed(self):
        return Mouse.leftPressed

    def rightPressed(self):
        return Mouse.rightPressed

    def centerPressed(self):
        return Mouse.centerPressed

    def click(self):
        return Mouse.leftPressed == False and Mouse.leftPressedPreviousFrame == True

    def getPos(self):
        return pygame.mouse.get_pos()

    #horizontal
    def getX(self):
        return pygame.mouse.get_pos()[0]

    #vertical
    def getY(self):
        return pygame.mouse.get_pos()[1]

    def destroy(self):
        Mouse.instance = None