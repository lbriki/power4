import pygame


class Button:
    def __init__(self, x,y,image,window):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.clicked = False
        self.window = window
    def drawONwindow (self):
        Action = False

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False :
                self.clicked = True
                Action= True
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False

        self.window.blit(self.image,(self.rect.x , self.rect.y))
        return Action