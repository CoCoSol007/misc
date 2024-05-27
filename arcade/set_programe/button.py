import random 
import pygame




class Button(pygame.sprite.Sprite) :

    def __init__(self, style, co,path) :
        super().__init__()
        
        if style == "start" :
            
            self.image = pygame.image.load(path+"/set/button_start.png")
            self.image = pygame.transform.scale(self.image,(256, 128))

            
            

        elif style == "re-start" : 
            self.image = pygame.image.load(path+"/set/re-start.png")
            self.image = pygame.transform.scale(self.image,(128, 128))

        elif style == "menu" : 
            self.image = pygame.image.load(path+"/set/menu.png")
            self.image = pygame.transform.scale(self.image,(256, 200))
        elif style == "settings" : 
            self.image = pygame.image.load(path+"/set/settings.png")
            self.image = pygame.transform.scale(self.image,(256, 100))
        elif style == "Plus" : 
            self.image = pygame.image.load(path+"/set/Son_Plus.png")
            self.image = pygame.transform.scale(self.image,(128,128))
        elif style == "Moin" : 
            self.image = pygame.image.load(path+"/set/Son_Moin.png")
            self.image = pygame.transform.scale(self.image,(128,128))

        self.rect = self.image.get_rect()
        self.rect.center = co