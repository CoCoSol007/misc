import pygame
from set_programe.dl_image import download


class Hero(pygame.sprite.Sprite) :

    def __init__(self,path) :
        super().__init__()
        self.images, self.image_respiration = download(path)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center =(540, 650)
        self.mouvement = (0, 0)
        self.direction = ">"
        self.vitesse = 2
        self.vitesse_saut = 10
        self.vitesse_walk = 2 
        self.sprint = False
        self.temps_dash = 30
        self.gravity = 0.25
        self.puissant_saut_max = 10
        self.Saut = False
        self.puissant_saut = 0
        
        
        

    def update(self, tic, tic_respiration) :

        

        if tic % 1 == 0:

            

            if self.mouvement == 0:
                if self.direction == "<":
                
                    self.image = self.image_respiration[int(tic_respiration)]
                    
                else : 
                    self.image = self.image_respiration[int(tic_respiration)+ 3]

            elif self.direction == "<":
                self.image = self.images[int(tic)]
            else:
                tic += 7
                self.image = self.images[int(tic)]

            

           
            
               
                
            


        if self.Saut:
            self.puissant_saut -= self.gravity

            self.rect.move_ip((self.mouvement, -1*self.puissant_saut))
        
            if self.rect.centery >= 650:
                self.puissant_saut = 0
                self.Saut = False
                self.rect.centery = 650 

            
            
        else:
            self.rect.move_ip((self.mouvement, 0))





    def dash(self ) :
        self.sprint = True
        self.vitesse = self.vitesse_saut

        
    def saut(self):
        self.Saut = True
        self.puissant_saut = self.puissant_saut_max