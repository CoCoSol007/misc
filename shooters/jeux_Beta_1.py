
import random
import pygame


pygame.init()


pygame.mixer.init()


sond = {
    "shoot" : pygame.mixer.Sound("shoot.ogg"),
    "coins" : pygame.mixer.Sound("coins.ogg"),
    "hit" : pygame.mixer.Sound("hit.ogg"),
    "hit_knight" : pygame.mixer.Sound("ouil.wav"),
    "ultime" : pygame.mixer.Sound("boom7.wav"),
    "launche" : pygame.mixer.Sound("launche.wav"),
    "start" : pygame.mixer.Sound("_start.wav"),
    "hit_archer" : pygame.mixer.Sound("hit_archer.wav"),
    "mega_arow" : pygame.mixer.Sound("tir_mega_arow.ogg"),
    "PlusDeMana" : pygame.mixer.Sound("mana.mp3")
}

class game():

    def colition( sprit , group ):
        return pygame.sprite.spritecollide(sprit , group , True , pygame.sprite.collide_mask)

class archer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.mouvement = (0,0)
        self.vitesse = 10
        self.images ={}
        self.images[">"] = pygame.image.load("archer_.png")
        self.images["<"] = pygame.transform.flip(self.images[">"] , True , False)
        self.image = pygame.transform.scale(self.images[">"], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (100, 400) 
        self.ancien_co = self.rect.center
        self.score = 0
        
        self.all_players = pygame.sprite.Group()
        self.direction = ">"
        
        

    def update(self):

        self.image = self.images[self.direction]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.ancien_co = self.rect.center
        
        

        
            
        Wall
        self.rect.move_ip( self.mouvement )
        if not self.colition(self.all_players):
            self.rect.center = self.ancien_co
        
        if len(pygame.sprite.spritecollide(self, Knife.all_coutau, True)) == 1:
            self.hit()

        

        
    def hit(self):
        self.score -= 0.5
        self.rect.x -= 10
        sond["hit_archer"].play()


        
    def launche_Arows(self):
        sond["shoot"].play()
        Arow.all_arow.add(arow(self, self.direction))
        

    def launche_Arows_special(self):
        if self.score >= 10:
            self.score -= 10
            Arow.special(self)
            sond["ultime"].play()
        else:
            sond["PlusDeMana"].play()

    def colition(self ,object):
        a = 0
        for WALL in Wall.all_wall:
            if not Wall.verification_player(WALL, object):
                a += 1
        
        if a == 0 : 
            return True
                
class arow(pygame.sprite.Sprite):
    def __init__(self, lancer , direction):
        super().__init__()
        self.vitesse = 40
        self.images = {}
        self.images[">"] = pygame.image.load("arow_.png")
        self.images["<"] = pygame.transform.flip(self.images[">"] , True , False)
        self.image = self.images[">"]
        self.rect = self.image.get_rect()
        self.rect.center = (Archer.mouvement) 
        if direction == ">":
            self.rect.x = lancer.rect.x + 60
        else:
            self.rect.x = lancer.rect.x - 30
        self.rect.y = lancer.rect.y + 20
        self.lancer = lancer
        self.all_arow = pygame.sprite.Group()
        self.direction = direction
        self.renvoi = False
        
        
        
    def mouv(self):
        if self.direction == "<":
            self.image = self.images["<"]
            self.rect.x -= self.vitesse
            if Mirror.miroir_actif:
                if len(pygame.sprite.spritecollide(self , Mirror.miror , False)) == 1:
                    self.direction = ">"
                    self.renvoi = True

        else: 
            self.rect.x += self.vitesse
            self.image = self.images[">"]
            if Mirror.miroir_actif:
                if len(pygame.sprite.spritecollide(self , Mirror.miror , False)) == 1:
                    self.direction = "<"
                    self.renvoi = True
            
        self.image = pygame.transform.scale(self.image, (32, 32))
        if self.rect.x > 1366 or self.rect.x < 0:
            self.remove(Arow.all_arow)

        if len(game.colition(knights , Arow.all_arow )) == 1:
            if self.direction == "<":
                knights.hit(-100)
            else:
                knights.hit(100)

        if self.renvoi:
            if len(game.colition(Archer , Arow.all_arow )) == 1:
                Archer.hit()
        
            
    def special(self, lanceur):
        sond["shoot"].play
        list_special_arows = []
        
        for i in range(0, 10):
            Arow1 = arow(lanceur , Archer.direction)

            Arow1.rect.y += -250 + i * 50
                

            list_special_arows.append(Arow1)
           
            
        self.all_arow.add(list_special_arows)

class Mega_Arow(pygame.sprite.Sprite):
    def __init__(self  ):
        super().__init__()
        self.images = {}
        self.images[">"] = pygame.image.load("arow_.png")
        self.images["<"] = pygame.transform.flip( self.images[">"] , True , False )
        self.image = self.images[">"]
        self.image = pygame.transform.scale( self.image , (400,1000))
        self.rect = self.image.get_rect()
        self.velocyty = 20
        self.rect.center = Archer.rect.center
        self.mega_arow = pygame.sprite.Group()
        self.tuch = True
    
    def spawn(self ):
        sond["mega_arow"].play()
        Archer.score -= 20

        MegaArow = Mega_Arow()
        Arow.all_arow.add(MegaArow)
        MegaArow.all_arow.add(MegaArow)

    def mouv(self):
        self.rect.x += self.velocyty
        
            
        if pygame.sprite.spritecollide(knights , self.mega_arow  , True , pygame.sprite.collide_mask):
            if self.tuch:
                piece1.score -= 20
                self.tuch = False
            sond["hit_knight"].play()
            
class knight(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vitesse = 10
        self.mouvement = (0,0)
        self.images = {}
        self.images["<"] = pygame.image.load("_knight.png")
        self.images[">"] = pygame.transform.flip(self.images["<"] , True , False)
        self.image = self.images["<"]
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (1100, 400) 
        self.all_players = pygame.sprite.Group()
        self.direction = "<"
        self.ancien_co = self.rect.center
        

    def update(self):
        self.ancien_co = self.rect.center

        if self.direction == "<":
            self.image = self.images["<"]
        else:
            self.image = self.images[">"]
        if not Sheild.protection and not Mirror.miroir_actif:
            
            self.rect.move_ip( self.mouvement )
            if not Archer.colition(self.all_players):
                self.rect.center = self.ancien_co
            

        self.image = pygame.transform.scale(self.image , (64, 64))

        

    def hit(self, rollback):
        if not Sheild.protection:
            self.rect.x = self.rect.x + rollback
            Archer.score += 1
            sond["hit_knight"].play()
            if Archer.score % 10 == 0:
                piece1.score -= 10
        else:
            sond["hit"].play()

    def launche_knife(self):
        if not Sheild.protection:
            Knife.spawn()
                
class sheild(pygame.sprite.Sprite):
    def __init__(self , porteur):
        super().__init__()
        self.image = pygame.image.load("sheild.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.rect = self.image.get_rect()
        self.rect.center = (knights.mouvement) 
        self.all_sheild = pygame.sprite.Group()
        self.rect.x = porteur.rect.x - 25
        self.rect.y = porteur.rect.y - 100
        self.protection = False

    
        

    def dessiner(self , porteur):
        self.rect.x = porteur.rect.x-20
        self.rect.y = porteur.rect.y
        self.all_sheild.draw(ecran)

class coutau(pygame.sprite.Sprite):
    def __init__(self , lancer):
        super().__init__()
        self.vitesse = 25
        self.image = pygame.image.load("axe.png")
        self.image = pygame.transform.scale(self.image, (32, 32))
        self.rect = self.image.get_rect()
        self.rect.center = (0,0) 
        self.rect.x = lancer.rect.x 
        self.rect.y = lancer.rect.y + 20
        self.lancer = lancer
        self.all_coutau = pygame.sprite.Group()
        self.origine_image = self.image
        self.angle = 0

    def spawn(self):
        if piece1.score >= 2:
            sond["launche"].play()
            self.all_coutau.add(coutau( knights))
            piece1.score -= 2


    def mouv(self):
        
        self.rect.x -= self.vitesse
        self.angle += 10
        self.image = pygame.transform.rotate(self.origine_image , self.angle )
        if self.rect.x < 0:
            self.remove(Arow.all_arow)

class mirror(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Mirror.png")
        self.image = pygame.transform.scale(self.image, (126, 126))
        self.rect = self.image.get_rect()
        self.rect.center = (knights.mouvement) 
        self.miror = pygame.sprite.Group()
        self.rect.x -= 400
        self.rect.y = knights.rect.y  
        self.miroir_actif = False


    def dessiner(self , porteur):
        temps_depui_debut = pygame.time.get_ticks()
        self.rect.x = porteur.rect.x - 100
        self.rect.y = porteur.rect.y - 25
        self.miror.draw(ecran)
        if Mirror.miroir_actif:
            piece1.score -= 0.25

class gold(pygame.sprite.Sprite):
    def __init__(self , nombre , positionX , positionY) :
        super().__init__()
        self.score = 0
        if nombre == 1:
            self.image = pygame.image.load("gold.png")
            self.image = pygame.transform.scale(self.image, (64, 64))
            self.rect = self.image.get_rect()
            self.rect.center = (knights.mouvement) 
            self.all_piece = pygame.sprite.Group()
            self.valu = 1
            self.rect.x = positionX
            self.rect.y = positionY
        
        
        
    def ramaser(self):
        if pygame.sprite.spritecollide(knights , self.all_piece  , True , pygame.sprite.collide_mask):
            sond["coins"].play()
            self.score += 1
            piece = gold(1 , random.randint(800 , 1150) , random.randint(100 , 500) )
            piece1.all_piece.add(piece)

class wall(pygame.sprite.Sprite):
    def __init__(self , place):
        super().__init__()
        self.duability = 10
        self.image = pygame.image.load("wall.png")
        self.image = pygame.transform.scale(self.image , (50,50))
        self.rect = self.image.get_rect()
        self.rect.center = place
        self.all_wall = pygame.sprite.Group()

    def verification_wapon(self , objec) :
        if pygame.sprite.spritecollide(self , objec  , True , pygame.sprite.collide_mask):
            pass
    
    def verification_player(self , Wall , player):

        
        
        if pygame.sprite.spritecollide(Wall , player  , False , pygame.sprite.collide_mask):
            return False
        else:
            return True 


Archer = archer() 
Archer.all_players.add(Archer)

Game = game()


knights = knight() 
knights.all_players.add(knights)

Arow = arow(Archer , ">")

Sheild = sheild(knights)
Sheild.all_sheild.add(Sheild)

Wall = wall((600,500))
Wall2 = wall((650,500))

Wall.all_wall.add(Wall , Wall2)

Mirror = mirror()
Mirror.miror.add(Mirror)

mega_arow = pygame.sprite.Group()

Knife = coutau(knights)

piece1 = gold(1 , 1, 1)

for i in range(1,100):

    piece1.all_piece.add(gold(1 , random.randint(800 , 1150) , random.randint(50 , 500) ))

horloge = pygame.time.Clock()
temps_depui_debut = pygame.time.get_ticks()

ecran = pygame.display.set_mode( (1366, 768), )
interface = pygame.Surface( (800 , 50), pygame.SRCALPHA )
myfont = pygame.font.SysFont("arial", 30)
fond = pygame.image.load("fond.png"  )
fond = pygame.transform.scale(fond, (1366, 768))

sond["start"].play()

marche = True

while marche:
    evenement = pygame.event.get()

    for event in evenement:
        if event.type == pygame.QUIT:
            marche = False
        
        elif event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_ESCAPE:
                marche = False

            

            if event.key == pygame.K_i:
                Sheild.protection = True

            if event.key == pygame.K_p:
                knights.launche_knife()

            if event.key == pygame.K_r:
                if Archer.score >= 20:
                    Mega_Arow.spawn(Archer)
                else:
                    sond["PlusDeMana"].play()


            if event.key == pygame.K_e:
                Archer.launche_Arows()

            if event.key == pygame.K_u:
                if piece1.score >= 0.5:
                    Mirror.miroir_actif = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_i:
                Sheild.protection = False
            if event.key == pygame.K_a:
                Archer.launche_Arows_special()
           
            if event.key == pygame.K_u:
                Mirror.miroir_actif = False
               

    touches = pygame.key.get_pressed()
    mouvementX = 0
    mouvementY = 0
    mouvementX_k = 0
    mouvementY_k = 0

    if touches[pygame.K_q]:
        mouvementX = -1 * Archer.vitesse
        
        Archer.direction = "<"
    
    elif touches[pygame.K_d]:
        mouvementX = Archer.vitesse
        
        Archer.direction = ">"


    if touches[pygame.K_z]:
        mouvementY = -1 * Archer.vitesse
 
    elif touches[pygame.K_s]:
        mouvementY = Archer.vitesse
       

    if touches[pygame.K_k]:
        mouvementX_k = -1 * knights.vitesse
        knights.direction = "<"
       
    elif touches[pygame.K_m]:
        mouvementX_k = knights.vitesse
        knights.direction = ">"
        

    if touches[pygame.K_o]:
        mouvementY_k = -1 * knights.vitesse
        
    elif touches[pygame.K_l]:
        mouvementY_k = knights.vitesse


    
    knights.mouvement = (mouvementX_k, mouvementY_k)
    Archer.mouvement = (mouvementX, mouvementY)
    

    if piece1.score == 0:
        Mirror.miroir_actif = False
        
    for i in range(1,3):
        if i == 1 :
            personag = Archer
        elif i == 2:
            personag = knights
        if personag.rect.x < 0:
            personag.rect.centerx = 35
        elif personag.rect.x > 1320:
            personag.rect.centerx = 1350
        if personag.rect.y < 0:
            personag.rect.centery = 35
        elif personag.rect.y > 705:
            personag.rect.centery = 735
        
    for i in range(1,3):
        if i == 1:
            groupe = Arow.all_arow
        else:
            groupe = Knife.all_coutau
        Wall.verification_wapon(groupe)
    

    for progectile in Arow.all_arow:
        progectile.mouv()

    for progectile in Knife.all_coutau:
        progectile.mouv()





    discour_1 = "Tu A : " + str(Archer.score) + " De Mana !"
    discour_knight = "Tu As: "+ str (piece1.score) + " Coins !"
   
    
    piece1.ramaser()
    

    Archer.update()
    knights.update()

    ecran.fill((0,0,0))
    interface.fill((0,0,0,0))
    
    
    score_display_Archer = myfont.render( discour_1, 100, (0,0,0))
    score_display_Knight = myfont.render( discour_knight, 100, (0,0,0))

    ecran.blit(fond , (0,0))
    

    piece1.all_piece.draw(ecran)
    Wall.all_wall.draw(ecran)
    Knife.all_coutau.draw(ecran)
    Archer.all_players.draw(ecran)
    knights.all_players.draw(ecran)
    Arow.all_arow.draw(ecran)

    interface.blit(score_display_Archer, (0,0))

    ecran.blit(score_display_Knight, (1000, 100))
    

    if Sheild.protection:
        Sheild.dessiner(knights)

    if Mirror.miroir_actif:
        Mirror.dessiner(knights)

    

    ecran.blit(interface , (100,100))
    pygame.display.update()

    horloge.tick(30)

