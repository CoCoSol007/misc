import random 
import pygame




class Apple(pygame.sprite.Sprite) :

    def __init__(self,path) :
        super().__init__()
            

        self.image = pygame.image.load(path+"/set/apple.png")
        self.image = pygame.transform.scale(self.image, (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,1040), 0)
        self.gravity = random.randint(1,3)
        

    
    def update(self):
        

        self.rect.move_ip(0,self.gravity)

        if self.rect.centery > 740:
            self.kill()


        
            

    