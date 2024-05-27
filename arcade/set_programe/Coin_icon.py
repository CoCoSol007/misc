import pygame



class Coin(pygame.sprite.Sprite) :

    def __init__(self,path) :
        super().__init__()
        self.images = [
            pygame.image.load(path+"/set/coins_animation\star coin shine\star coin 1.png"),
            pygame.image.load(path+"/set/coins_animation\star coin shine\star coin 2.png"),
            pygame.image.load(path+"/set/coins_animation\star coin shine\star coin 3.png"),
            pygame.image.load(path+"/set/coins_animation\star coin shine\star coin 4.png"),
            pygame.image.load(path+"/set/coins_animation\star coin shine\star coin 5.png"),
            pygame.image.load(path+"/set/coins_animation\star coin shine\star coin 6.png")
        ]

        for i in range(0,6):
            self.images[i] = pygame.transform.scale(self.images[i], (64,64))        





        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (40, 40)
        
        

    def update(self, tic):
        if tic % 1 == 0:

            self.image = self.images[int(tic)] 
            

        