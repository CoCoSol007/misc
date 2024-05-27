import pygame

from set_programe.Coin_icon import Coin
from set_programe.Player import Hero
from set_programe.bomb import bombe
from set_programe.coins import coins
from set_programe.arrow import Arrow
from set_programe.apple import Apple
from set_programe.MalusCoins import Malus
from set_programe.button import Button




class Health(pygame.sprite.Sprite) :

    def __init__(self, path) :
        super().__init__()
        health = pygame.image.load(path+"\set\health.png")
        self.images = [  
        
        health.subsurface(0, 0,244,44),
        health.subsurface(0, 1 * 44,244,44),
        health.subsurface(0, 2 * 44,244,44),
        health.subsurface(0, 3 * 44,244,44),
        health.subsurface(0, 4 * 44,244,44),
        health.subsurface(0, 5 * 44,244,44),
        health.subsurface(0, 6 * 44,244,44),
        health.subsurface(0, 7 * 44,244,44),
        health.subsurface(0, 8 * 44,244,44),
        health.subsurface(0, 9 * 44,244,44),
        health.subsurface(0, 10 * 44,244,44)
        
        ]

        

        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.rect.center = (958,33)
        self.life = 11
        
        self.score = 0
        self.level = 1
        

        self.coins_icon = Coin(path)
        self.Hero = Hero(path)
        self.start_button = Button("start", (540, 317),  path)
        self.re_start_button = Button("re-start", (520, 500), path)
        self.menu_button = Button("menu", (520, 200), path)
        self.settings_buttom = Button("settings", (540, 100), path)
        self.button_plus = Button('Plus', (420, 500), path)
        self.button_Moin = Button('Moin', (630, 500),path)
        
        
        

        self.all_coins = pygame.sprite.Group()
        self.all_bombe = pygame.sprite.Group()
        self.all_arrow = pygame.sprite.Group()
        self.all_apple = pygame.sprite.Group()
        self.all_malus = pygame.sprite.Group()

        self.all_object_to_draw_fix = pygame.sprite.Group(self.coins_icon, self, self.Hero)
        self.all_object_to_draw_mobile = pygame.sprite.Group()
        self.all_object_to_draw_menu = pygame.sprite.Group(self.start_button, self.settings_buttom)   
        self.all_object_to_draw_menu_Win_and_Over = pygame.sprite.Group(self.re_start_button, self.menu_button)
        self.all_object_to_draw_settings = pygame.sprite.Group(self.menu_button, self.button_plus, self.button_Moin)

        self.path = path

        self.son = {
            "boom": pygame.mixer.Sound(path+"/set/boom8.wav"),
            "piece": pygame.mixer.Sound(path+"/set/dropmetalthing.ogg"),
            "hit" : pygame.mixer.Sound(path+"/set/hit.wav"),
            "eat" :pygame.mixer.Sound(path+"/set/eat.ogg"),
            "pop" :pygame.mixer.Sound(path+"/set/pop.flac"),
            #"musique_fond" : pygame.mixer.Sound("musique de fond.mp3")

        }

        self.volume_sons = 0.5

        for son in self.son:
            pygame.mixer.Sound.set_volume(self.son[son], self.volume_sons)

    #pygame.mixer.Sound.set_volume(son["musique_fond"], 0.1)
    #son["musique_fond"].play(-1)
            
        

    def update(self):

        
        
        
        if self.life == 1:
            self.image = self.images[10]
        elif self.life == 2:
            self.image = self.images[9]
        elif self.life == 3:
            self.image = self.images[8]
        elif self.life == 4:
            self.image = self.images[7]
        elif self.life == 5:
            self.image = self.images[6]
        elif self.life == 6:
            self.image = self.images[5]
        elif self.life == 7:
            self.image = self.images[4]
        elif self.life == 8:
            self.image = self.images[3]
        elif self.life == 9:
            self.image = self.images[2]
        elif self.life == 10:
            self.image = self.images[1]
        elif self.life == 11:
            self.image = self.images[0]




     # on gere les colition

        if pygame.sprite.spritecollide(self.Hero ,self.all_coins, True , pygame.sprite.collide_mask):
            self.score += 1
            self.NewCoin()
            self.son["piece"].play()

        if pygame.sprite.spritecollide(self.Hero ,self.all_bombe, True , pygame.sprite.collide_mask):
            
            self.score = max(0,self.score - 1)
            self.son["boom"].play()
            self.NewBombe()
            self.life -= 1


        if pygame.sprite.spritecollide(self.Hero ,self.all_arrow, True , pygame.sprite.collide_mask):
            
            self.score = max(0,self.score - 3)
            self.son["hit"].play()
            self.NewArrow()
            self.life -= 1

        if pygame.sprite.spritecollide(self.Hero ,self.all_apple, True , pygame.sprite.collide_mask):

            self.son["eat"].play()
            self.life += 1
 
            
        if pygame.sprite.spritecollide(self.Hero ,self.all_malus, True , pygame.sprite.collide_mask):

            self.son["piece"].play()
            self.score = 0 


    def NewBombe(self):
        h = bombe(self.path)
        self.all_bombe.add(h)
        self.all_object_to_draw_mobile.add(h)

    def NewCoin(self):
        a = coins(self.path)
        self.all_coins.add(a)
        self.all_object_to_draw_fix.add(a)

    def NewArrow(self):
        a = Arrow(self.path)
        self.all_arrow.add(a)
        self.all_object_to_draw_mobile.add(a)

    def NewApple(self):
        a = Apple(self.path)
        self.all_apple.add(a)
        self.all_object_to_draw_mobile.add(a)

    def NewMalusCoins(self):
        a = Malus(self.path)
        self.all_malus.add(a)
        self.all_object_to_draw_mobile.add(a)


    def spawn_item(self, tick):

        #########
        if self.level == 1:
            pass

        #########
        elif self.level == 2:
            if tick % 300 == 0:
                self.NewBombe()
            

        #########
        elif self.level == 3:
            if tick % 250 == 0:
                self.NewBombe()
            if tick % 720 == 0:
                self.NewArrow()

        #########
        elif self.level == 4:
            if tick % 150 == 0:
                self.NewBombe()
            if tick % 700 == 0:
                self.NewArrow()
            if tick % 800 == 0:
                self.NewApple()
            if tick % 1000 == 0:
                self.NewMalusCoins()


        #########
        elif self.level == 5:
            if tick % 50 == 0:
                self.NewBombe()
            if tick % 650 == 0:
                self.NewArrow()
            if tick % 700 == 0:
                self.NewApple()
                self.NewMalusCoins()
            


        

        