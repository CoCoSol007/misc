import random 
import pygame




class coins(pygame.sprite.Sprite) :

    def __init__(self,path) :
        super().__init__()
        self.images = [
            pygame.image.load(path+"/set/coins_animation\star coin rotate\star coin rotate 1.png"),
            pygame.image.load(path+"/set/coins_animation\star coin rotate\star coin rotate 2.png"),
            pygame.image.load(path+"/set/coins_animation\star coin rotate\star coin rotate 3.png"),
            pygame.image.load(path+"/set/coins_animation\star coin rotate\star coin rotate 4.png")
            
        ]

        self.images.append(pygame.transform.flip(self.images[3],True, False) )   
        self.images.append(pygame.transform.flip(self.images[2],True, False) ) 

        for i in range(0,6):
            self.images[i] = pygame.transform.scale(self.images[i], (50,50))       

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,1040), 0)
        self.gravity = random.randint(1,3)
    
        
        

    def update(self, tic,group_coins, player ):
        if tic % 1 == 0:

            self.image = self.images[int(tic)]

        if self.rect.centery > 740:
            self.rect.center = (random.randint(40,1040), 0)
            self.gravity = random.randint(1,3)

        self.rect.move_ip(0,self.gravity)


        

        