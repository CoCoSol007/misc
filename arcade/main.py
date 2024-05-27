#boucle principale

import os

# Getting the path of the current file.
path = os.path.dirname(__file__)



# On importe le module pygame
import pygame
# Importing the class `Health` from the file `GameManager.py` in the folder `set_programe`.
from set_programe.GameManager import Health





# On initialise pygame
pygame.init()

# On créé une horloge (pour les FPS)
horloge = pygame.time.Clock()


# On créé un écran pour notre programme (= une fenêtre)
ecran = pygame.display.set_mode( (1080, 720) )

pygame.display.set_caption('Game Made By Raph & CoCo')
pygame.display.set_icon(pygame.image.load(path+"/set/logo.png"))


# On définit le taux de rafraîchissement de la fenêtre
fps = 120

# A variable that is used to animate the character.
tic_animation = 1
tic = 1
tic_dash = 1 
tic_remain_dash = 180
tic_coins_anilation = 0
tic_respiration = 0

# Creating an instance of the class `Health` 
GameManager = Health(path)
GameManager.all_object_to_draw_fix.add(GameManager)



GAME_FONT = pygame.freetype.Font(path+"/set/fast99.ttf", 50)
fond = pygame.image.load(path+"/set/fond.jpg")

# Creating three coins.
for i in range(1,4):
    GameManager.NewCoin()
   


# Changing the value of the variable `Game` to `"Menu"`.
Game = "Menu"

# On créé une variable pour sortir de la boucle principale
marche = True

# On met en place la boucle principale d'affichage
while marche:

    if Game == "Run":

        # Checking if the player has lost all his lives.
        if GameManager.life == 1:
            Game = "Game Over"

        if GameManager.score == 15 and GameManager.level == 1 :
            GameManager.level = 2
            GameManager.score = 0
            
        # Checking if the player has collected 15 coins and if the level is 1. If both conditions are
        # true, the level will be changed to 2.
        elif GameManager.score == 15 and GameManager.level == 2 :
            GameManager.level = 3
            GameManager.score = 0
        elif GameManager.score == 20 and GameManager.level == 3 :
            GameManager.level = 4
            GameManager.score = 0
        elif GameManager.score == 30 and GameManager.level == 4 :
            GameManager.level = 5
            GameManager.score = 0
        elif GameManager.score == 40 and GameManager.level == 5 :
            Game = "Win"


        
            
        
        # Used to animate the character.
        tic += 1
        tic_animation += 0.125 
        if tic_animation == 7:
            tic_animation = 1
        tic_coins_anilation += 0.0625
        if tic_coins_anilation == 6:
            tic_coins_anilation = 0
        tic_respiration += 0.0625
        if tic_respiration == 3:
            tic_respiration = 0
        


        # On récupère la liste des évènements actuels
        evenements = pygame.event.get()

        # On fait le tour de la liste des évènements
        for evenement in evenements:
            # Si l'évènement actuel est de type QUIT
            if evenement.type == pygame.QUIT:
                # On sort de la boucle
                marche = False

            # Si on a appuyé sur une touche du clavier
            elif evenement.type == pygame.KEYDOWN:
                # Si on a appuyé sur la touche Echap (Esc)
                if evenement.key == pygame.K_ESCAPE:
                    # On sort de la boucle
                    Game = "Menu"
            
                elif evenement.key == pygame.K_SPACE and tic_remain_dash > 180:
                    GameManager.Hero.dash()

                elif evenement.key == pygame.K_z and GameManager.Hero.rect.centery == 650 :
                    GameManager.Hero.saut()
                    


    # On récupère les touches actuellement appuyées
        touches = pygame.key.get_pressed()


        # On se sert de variables pour le mouvement
        mouvementX = 0
    

        # On teste les touches appuyées
        if touches[pygame.K_q] and not touches[pygame.K_d] and GameManager.Hero.rect.x > 0:
            # Le héros se déplacera vers la gauche à sa prochaine update
            mouvementX = -1 * GameManager.Hero.vitesse
            GameManager.Hero.direction = ">"
        elif touches[pygame.K_d] and not touches[pygame.K_q] and GameManager.Hero.rect.x < 995:
            mouvementX = GameManager.Hero.vitesse
            GameManager.Hero.direction = "<"

        # On assigne les variables au tuple de mouvement du héros
        GameManager.Hero.mouvement = mouvementX
        


        # Checking if the player is dashing.
        if GameManager.Hero.sprint :
            tic_dash += 1
            tic_remain_dash = 1
            if tic_dash == GameManager.Hero.temps_dash :
                GameManager.Hero.sprint = False
                GameManager.Hero.vitesse = GameManager.Hero.vitesse_walk
                tic_dash = 1 
            
        # Used to check if the player isn't dashing.
        if not GameManager.Hero.sprint :
            tic_remain_dash += 1 


        # Used to spawn the items.
        GameManager.spawn_item(tic)

        # On efface l'écran
        

        ecran.blit(fond, (-100,0))                                                                  # On afiche le fond d ecran     
        
        # Updating the position of the coins.
        GameManager.update()
        GameManager.Hero.update(tic_animation, tic_respiration)
        GameManager.all_coins.update(tic_coins_anilation,GameManager.all_coins ,GameManager.Hero)
        GameManager.coins_icon.update(tic_coins_anilation)
        GameManager.all_bombe.update()                                                              # On update tout les bombes
        GameManager.all_arrow.update()
        GameManager.all_malus.update(tic_coins_anilation)
        GameManager.all_apple.update()

        # Drawing all the objects that are in the group `all_object_to_draw_mobile` on the screen.
        GameManager.all_object_to_draw_mobile.draw(ecran) 
        GameManager.all_object_to_draw_fix.draw(ecran)                                                  # On afiche tout les objet a dessiner
        
        text_surface, rect = GAME_FONT.render(str(GameManager.score), (140, 82, 70))                # On afiche le score
        ecran.blit(text_surface,(80, 25)  )
        text_surface, rect = GAME_FONT.render("level : " + str(GameManager.level), (140, 82, 70))   # On afiche le lvl
        ecran.blit(text_surface,(15, 90)  )



    
    elif Game == "Menu":
        # On récupère la liste des évènements actuels
        evenements = pygame.event.get()

        # On fait le tour de la liste des évènements
        for evenement in evenements:
            # Si l'évènement actuel est de type QUIT
            if evenement.type == pygame.QUIT:
                # On sort de la boucle
                marche = False

            # Si on a appuyé sur une touche du clavier
            elif evenement.type == pygame.KEYDOWN:
                # Si on a appuyé sur la touche Echap (Esc)
                if evenement.key == pygame.K_ESCAPE:
                    # On sort de la boucle
                    marche = False
            
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if GameManager.start_button.rect.collidepoint(evenement.pos):
                    GameManager.score = 0
                    GameManager.level = 1
                    GameManager.life = 11
                    for ellement in GameManager.all_object_to_draw_mobile:
                        if not ellement == GameManager.Hero or GameManager.coins_icon or GameManager:
                            ellement.kill()
                    
                    Game = "Run"
                    

                if GameManager.settings_buttom.rect.collidepoint(evenement.pos):
                    Game = "Setings"

        ecran.blit(fond, (-100,0))                                                                  # On afiche le fond d ecran     
        GameManager.all_object_to_draw_menu.draw(ecran)

    elif Game == "Setings":
        # On récupère la liste des évènements actuels
        evenements = pygame.event.get()

        # On fait le tour de la liste des évènements
        for evenement in evenements:
            # Si l'évènement actuel est de type QUIT
            if evenement.type == pygame.QUIT:
                # On sort de la boucle
                marche = False

            # Si on a appuyé sur une touche du clavier
            elif evenement.type == pygame.KEYDOWN:
                # Si on a appuyé sur la touche Echap (Esc)
                if evenement.key == pygame.K_ESCAPE:
                    # On sort de la boucle
                    marche = False
            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if GameManager.menu_button.rect.collidepoint(evenement.pos):
                    Game = "Menu"
                elif GameManager.button_Moin.rect.collidepoint(evenement.pos):
                    if GameManager.volume_sons > 0:
                        GameManager.volume_sons -= 0.1
                        for son in GameManager.son:
                            pygame.mixer.Sound.set_volume(GameManager.son[son], GameManager.volume_sons)
                        GameManager.son["pop"].play()

                elif GameManager.button_plus.rect.collidepoint(evenement.pos):
                    if GameManager.volume_sons < 1:
                        GameManager.volume_sons += 0.1
                        for son in GameManager.son:
                            pygame.mixer.Sound.set_volume(GameManager.son[son], GameManager.volume_sons)
                            GameManager.son["pop"].play()
                        
                            
            
            
            

        ecran.blit(fond, (-100,0))  
        GameManager.all_object_to_draw_settings.draw(ecran) 

    else:
        

        # On récupère la liste des évènements actuels
        evenements = pygame.event.get()

        # On fait le tour de la liste des évènements
        for evenement in evenements:
            # Si l'évènement actuel est de type QUIT
            if evenement.type == pygame.QUIT:
                # On sort de la boucle
                marche = False

            # Si on a appuyé sur une touche du clavier
            elif evenement.type == pygame.KEYDOWN:
                # Si on a appuyé sur la touche Echap (Esc)
                if evenement.key == pygame.K_ESCAPE:
                    # On sort de la boucle
                    marche = False

            elif evenement.type == pygame.MOUSEBUTTONDOWN:
                if GameManager.re_start_button.rect.collidepoint(evenement.pos):
                    GameManager.score = 0
                    GameManager.level = 1
                    GameManager.life = 11
                    for ellement in GameManager.all_object_to_draw_mobile:
                        if not ellement == GameManager.Hero or GameManager.coins_icon or GameManager:
                            ellement.kill()
        
                    Game = "Run"
                    
                elif GameManager.menu_button.rect.collidepoint(evenement.pos):
                    Game = "Menu"


        if Game == "Game Over":

            ecran.fill((255, 0, 0))

            text_surface, rect = GAME_FONT.render("Game Over !" , (255, 255, 255))   # On afiche le lvl

        elif Game == "Win":

            ecran.fill((147, 208, 0))

            text_surface, rect = GAME_FONT.render("Win !" , (255, 255, 255))   # On afiche le lvl


        ecran.blit(text_surface,(380, 340)  ) 
        GameManager.all_object_to_draw_menu_Win_and_Over.draw(ecran)



                                                                   # On afiche le fond d ecran     
        





    pygame.display.update()
    horloge.tick(fps)

