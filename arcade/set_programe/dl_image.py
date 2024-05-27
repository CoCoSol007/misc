
import pygame

pygame.init()

def download(path):
    
    sprit_sheet = pygame.image.load(path+"/set/Oldhero.png")
    
    
    
    all_image = [
        
    
            sprit_sheet.subsurface(1*16,1*16,16,16),

            sprit_sheet.subsurface(1*16,2*16,16,16),
            sprit_sheet.subsurface(2*16,2*16,16,16),
            sprit_sheet.subsurface(3*16,2*16,16,16),
            sprit_sheet.subsurface(4*16,2*16,16,16),
            sprit_sheet.subsurface(5*16,2*16,16,16),
            sprit_sheet.subsurface(6*16,2*16,16,16)
        

        ]

    for i in range(0, 7):                                               # On ajoute les meme sprit mais dans l autre sens 
        image = pygame.transform.flip(all_image[i], True, False)
        all_image.append(image)

    for i in range(-1, len(all_image) - 1 ):                            # On redimentionne les les sprit
        all_image[i] = pygame.transform.scale(all_image[i],(85,85))



   
    respiration = [

            sprit_sheet.subsurface(1*16,1*16,16,16),
            sprit_sheet.subsurface(2*16,1*16,16,16),
            sprit_sheet.subsurface(3*16,1*16,16,16)
        
        ]
    
    for i in range(0, 4):                                               # On ajoute les meme sprit mais dans l autre sens 
        image = pygame.transform.flip(respiration[i], True, False)
        respiration.append(image)

    for i in range(-1, len(respiration) - 1 ):                            # On redimentionne les les sprit
        respiration[i] = pygame.transform.scale(respiration[i],(85,85))
    

    return all_image, respiration


