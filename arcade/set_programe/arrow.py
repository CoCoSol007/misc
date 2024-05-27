import pygame
import random


class Arrow(pygame.sprite.Sprite) : 
    
    def __init__(self,path) :
        super().__init__()
        
        self.direction = random.choice([">", "<"])

        self.images = [pygame.image.load(path+"/set/arrow.png")]
        image = pygame.transform.flip(self.images[0], True, False)
        self.images.append(image)
        self.images[0] = pygame.transform.scale(self.images[0], (64,64))
        self.images[1] = pygame.transform.scale(self.images[1], (64,64))

        self.mouvement = random.randint(2, 3)
        
        if self.direction == '>':
            self.image = self.images[0]
            self.rect = self.image.get_rect() 
            self.rect.centerx = 0
        else:
            self.image = self.images[1]
            self.rect = self.image.get_rect() 
            self.rect.centerx = 1080

        self.rect.centery = 650

    def update(self) :

        if self.direction == ">":
        
            self.rect.move_ip(self.mouvement,0)
            if self.rect.centerx > 1100:
                self.kill()

        else:

            self.rect.move_ip(-1*self.mouvement,0)
            if self.rect.centerx < -100:
                self.kill()
