
import pygame
import random
import time
import sys
from tkinter import *
from os import path
from pygame.locals import *
from tilessettings import *
from tilessprites import *
from tilemap import *


from settings import *
from sprites import *




black =(0,0,0)
white=(255,255,255)
red = (200, 0,0)
green =(0,200,0)
bright_green = (0,255,0)
bright_red = (255,0,0)
orange = (255,165,0)
bright_orange = (255,140,0)
yellow = (255,215,0)
bright_yellow = (255,255,0)
blue = (0,0,200)
bright_blue = (0,0,255)
violet = (147,112,219)
bright_violet = (160,32,240)



pygame.init()
pygame.mixer.init()

display_width = 900
display_height = 563

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('GAME DEN')
clock = pygame.time.Clock()

backtile_img = pygame.image.load('zoombiee.jpg')
backtile_img_rect = backtile_img.get_rect() 
backtile_img1 = pygame.image.load('ballgameback.jpg')
backtile_img_rect1 = backtile_img1.get_rect()
backtile_img2 = pygame.image.load('shoot.jpg')
backtile_img_rect2 = backtile_img2.get_rect()
startpage_img = pygame.image.load('gamestart.jpg')
startpage_img_rect = startpage_img.get_rect()
logo_img = pygame.image.load('logo1.png')
logo_img_rect = logo_img.get_rect()
beginpage_img = pygame.image.load('beginpage.png')
beginpage_img_rect = beginpage_img.get_rect()
inst_img = pygame.image.load('ballinst.png')
inst_img_rect = inst_img.get_rect()
inst_img1 = pygame.image.load('pictureinst.png')
inst_img_rect1 = inst_img1.get_rect()
inst_img2 = pygame.image.load('carinst.png')
inst_img_rect2 = inst_img2.get_rect()
inst_img3 = pygame.image.load('shootinst.png')
inst_img_rect3 = inst_img3.get_rect()                                                
inst_img4 = pygame.image.load('zoimbeeinst.png')
inst_img_rect4 = inst_img4.get_rect()                                


def button(msg,x,y,w,h,ic,ac,action = None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
    smallText = pygame.font.Font('freesansbold.ttf',20)

    textSurf,textRect = text_objects(msg,smallText)
    textRect.center =((x+(w/2)),(y+(h/2)))
    gameDisplay.blit(textSurf, textRect)


def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        logo_img_rect.center = (470,300)
        gameDisplay.blit(logo_img,logo_img_rect)
        
        largeText = pygame.font.Font('freesansbold.ttf',60)
        
        
        pygame.display.update()
        time.sleep(2)
        game_den()
        clock.tick(15)


def game_den():
    den = True
    while den:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(startpage_img,startpage_img_rect)
        button("BEGIN",230,470,100,50,green,bright_green,beginpage)

        pygame.display.update()
        clock.tick(15)

def beginpage():
    begin = True
    while begin:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(beginpage_img,beginpage_img_rect)
        button("BALL Vs BALL",407,204,170,35,red,bright_red,ballgame_intro)
        button("PICTURE PUZZLE",407,249,170,35,orange,bright_orange,picturepuzzle)
        button("JUMPY",407,294,170,35,yellow,bright_yellow,jumpy)
        button("A BIT RACEY",407,339,170,35,green,bright_green,cargame)
        button("SHMUP!",407,384,170,35,blue,bright_blue,shooting_intro)
        button("ZOIMBIEE",407,429,170,35,violet,bright_violet,tilegame_intro)
        button("ROLL DIE",697,138,100,35,green,bright_green,rollgame)
        button("QUIT",697,183,100,35,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)
    




    
def quitgame():
    pygame.quit()
    quit()

def shooting_intro():
        shooting = True
        while shooting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(white)
            gameDisplay.blit(backtile_img2,backtile_img_rect2)
            largeText = pygame.font.Font('freesansbold.ttf',60)
            TextSurf, TextRect = text_objects("SHMUP!",largeText)
            TextRect.center = ((display_width / 2 - 125 ),(display_height / 2  + 50))
            gameDisplay.blit(TextSurf, TextRect)
            button("GO",520,280,150,35,green,bright_green,shootgame)
            button("INSTRUCTIONS",520,330,150,35,yellow,bright_yellow,inst4)
            button("QUIT",520,380,150,35,red,bright_red,quitgame)

            pygame.display.update()
            clock.tick(15)


def inst4():
    
    inst4 = True
    while inst4:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(inst_img3,inst_img_rect3)
        button("BACK",300,500,70,35,yellow,bright_yellow,shooting_intro)
        button("PLAY",470,500,70,35,green,bright_green,shootgame)

        
        
        pygame.display.update()
        clock.tick(15)
        
def shootgame():
    # shmup game
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Art from Kenney.nl
    import pygame
    import random
    from os import path

    img_dir = path.join(path.dirname(__file__), 'img')
    snd_dir = path.join(path.dirname(__file__), 'snd')

    WIDTH = 480
    HEIGHT = 600
    FPS = 60
    POWERUP_TIME = 5000

    # define colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)
    YELLOW = (255, 255, 0)

    # initialize pygame and create window
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Shmup!")
    clock = pygame.time.Clock()
    font_name = pygame.font.match_font('arial')



    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, WHITE)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surf.blit(text_surface, text_rect)

    def newmob():
          m = Mob()
          all_sprites.add(m)
          mobs.add(m)

    def draw_shield_bar(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 10
        fill = (pct / 100) * BAR_LENGTH
        outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
        pygame.draw.rect(surf, GREEN, fill_rect)
        pygame.draw.rect(surf, WHITE, outline_rect, 2)

    def draw_lives(surf, x, y, lives, img):
        for i in range(lives):
            img_rect = img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)
           


    class Player(pygame.sprite.Sprite):        
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.transform.scale(player_img, (50, 38))
            self.image.set_colorkey(BLACK)
            
            self.rect = self.image.get_rect()
            self.radius = 20
            # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.centerx = WIDTH / 2
            self.rect.bottom = HEIGHT - 10
            self.speedx = 0
            self.shield = 100
            self.shoot_delay = 250
            self.last_shot = pygame.time.get_ticks()
            self.lives = 3
            self.hidden = False
            self.hide_timer = pygame.time.get_ticks()
            self.power = 1
            self.power_time = pygame.time.get_ticks()
            

        def update(self):
            # timeout for powerups
            if self.power >= 2 and pygame.time.get_ticks() - self.power_time > POWERUP_TIME:
                self.power -= 1
                self.power_time = pygame.time.get_ticks()
                
            # unhide if hidden
            if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
                self.hidden = False
                self.rect.centerx = WIDTH / 2
                self.rect.bottom = HEIGHT - 10
                
            self.speedx = 0
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_LEFT]:
                self.speedx = -8
            if keystate[pygame.K_RIGHT]:
                self.speedx = 8
            if keystate[pygame.K_SPACE]:
                self.shoot()
            self.rect.x += self.speedx
            if self.rect.right > WIDTH:
                self.rect.right = WIDTH
            if self.rect.left < 0:
                self.rect.left = 0

        def powerup(self):
            self.power += 1
            self.power_time = pygame.time.get_ticks()
        
                
        def shoot(self):
            now = pygame.time.get_ticks()
            if now - self.last_shot > self.shoot_delay:
                self.last_shot = now
                if self.power == 1:
                    bullet = Bullet(self.rect.centerx, self.rect.top)
                    all_sprites.add(bullet)
                    bullets.add(bullet)
                    shoot_sound.play()
                if self.power == 2:
                    bullet1 = Bullet(self.rect.left, self.rect.centery)
                    bullet2 = Bullet(self.rect.right, self.rect.centery)
                    all_sprites.add(bullet1)
                    all_sprites.add(bullet2)
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                    shoot_sound.play()

                if self.power >= 3:
                    bullet1 = Bullet(self.rect.left, self.rect.centery)
                    bullet2 = Bullet(self.rect.right, self.rect.centery)
                    bullet3 = Bullet(self.rect.centerx, self.rect.centery)
                    all_sprites.add(bullet1)
                    all_sprites.add(bullet2)
                    all_sprites.add(bullet3)
                    bullets.add(bullet1)
                    bullets.add(bullet2)
                    bullets.add(bullet3)
                    shoot_sound.play()

                  
        def hide(self):
            # hide the player temporarily
            self.hidden = True
            self.hide_timer = pygame.time.get_ticks()
            self.rect.center = (WIDTH / 2,HEIGHT + 200)
            
    class Mob(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)
            self.image_orig = random.choice(meteor_images)
            self.image_orig.set_colorkey(BLACK)
            self.image = self.image_orig.copy()
            self.rect = self.image.get_rect()
            self.radius = int(self.rect.width * 0.85 / 2)
            # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)
            self.speedx = random.randrange(-3, 3)
            self.rot = 0
            self.rot_speed = random.randrange(-8, 8)
            self.last_update = pygame.time.get_ticks()

        def rotate(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > 50:
                self.last_update = now
                self.rot = (self.rot + self.rot_speed) % 360
                new_image = pygame.transform.rotate(self.image_orig, self.rot)
                old_center = self.rect.center
                self.image = new_image
                self.rect = self.image.get_rect()
                self.rect.center = old_center

        def update(self):
            self.rotate()
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
                self.rect.x = random.randrange(WIDTH - self.rect.width)
                self.rect.y = random.randrange(-100, -40)
                self.speedy = random.randrange(1, 8)

                
    class Bullet(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            self.image = laser_img
            self.image.set_colorkey(BLACK)
            
            self.rect = self.image.get_rect()
            self.rect.bottom = y
            self.rect.centerx = x
            self.speedy = -10
     
        def update(self):
            self.rect.y += self.speedy
            # kill if it moves off the top of the screen
            if self.rect.bottom < 0:
                self.kill()
    class Pow(pygame.sprite.Sprite):
        def __init__(self, center):
            pygame.sprite.Sprite.__init__(self)
            self.type = random.choice(['shield', 'gun'])
            self.image = powerup_images[self.type]
            self.image.set_colorkey(BLACK)
            
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.speedy = 5
     
        def update(self):
            self.rect.y += self.speedy
            # kill if it moves off the top of the screen
            if self.rect.top > HEIGHT:
                self.kill()
                

                
    class Explosion(pygame.sprite.Sprite):
        def __init__(self, center, size):
            pygame.sprite.Sprite.__init__(self)
            self.size = size
            self.image = explosion_anim[self.size][0]
            self.rect = self.image.get_rect()
            self.rect.center = center
            self.frame = 0
            self.last_update = pygame.time.get_ticks()
            self.frame_rate = 75

        def update(self):
            now = pygame.time.get_ticks()
            if now - self.last_update > self.frame_rate:
                self.last_update = now
                self.frame += 1
                if self.frame == len(explosion_anim[self.size]):
                    self.kill()
                else:
                    center = self.rect.center
                    self.image = explosion_anim[self.size][self.frame]
                    self.rect = self.image.get_rect()
                    self.rect.center = center

    def show_go_screen():
        screen.blit(frontpage, frontpage_rect)
        draw_text(screen, "SHMUP!", 64, WIDTH / 2, HEIGHT / 4 - 100)
        draw_text(screen, "GAME OVER", 40, WIDTH / 2, HEIGHT / 2 - 50)
        draw_text(screen, "Arrow keys : MOVE", 15, WIDTH / 2, HEIGHT - 20)
        draw_text(screen, "Space key : FIRE", 15, WIDTH / 2, HEIGHT - 40)
        draw_text(screen, "START GAME", 30, WIDTH / 2, HEIGHT * 3 / 4 - 60)
        draw_text(screen, "press enter", 10, WIDTH / 2, HEIGHT * 3 / 4 - 30)
        draw_text(screen, "SCORE:" + str(score), 22, WIDTH / 2, HEIGHT / 2)
    
        
                  

        pygame.display.flip()
        waiting = True
        while waiting:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_KP_ENTER:   
                        waiting = False


    # Load all game graphics
    frontpage = pygame.image.load(path.join(img_dir, "s2.jpg")).convert()
    frontpage_rect = frontpage.get_rect()
    background = pygame.image.load(path.join(img_dir, "spac3.jpg")).convert()
    background_rect = background.get_rect()
    player_img = pygame.image.load(path.join(img_dir, "playerShip2_orange.png")).convert()
    player_mini_img = pygame.transform.scale(player_img, (25, 19))
    player_mini_img.set_colorkey(BLACK)
    laser_img = pygame.image.load(path.join(img_dir, "laserRed01.png")).convert()
    meteor_images = []
    meteor_list = ['meteorBrown_med1.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png', 
                   'meteorGrey_med1.png', 'meteorGrey_med2.png', 'meteorBrown_big3.png',
                   'meteorGrey_small1.png', 'meteorBrown_med3.png', 
                   'meteorBrown_big4.png', 'meteorBrown_tiny1.png', 'fire0.png',
                   'fire2.png', 'fire3.png', 'fire4.png', 'fire5.png', 'fire6.png']
    for img in meteor_list:
        meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())
    explosion_anim = {}
    explosion_anim['lg'] = []
    explosion_anim['sm'] = []
    explosion_anim['player'] = []
    for i in range(8):
        filename = 'exp{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img.set_colorkey(BLACK)
        img_lg = pygame.transform.scale(img, (75, 75))
        explosion_anim['lg'].append(img_lg)
        img_sm = pygame.transform.scale(img, (32, 32))
        explosion_anim['sm'].append(img_sm)
        filename = 'exp0{}.png'.format(i)
        img = pygame.image.load(path.join(img_dir, filename)).convert()
        img.set_colorkey(BLACK)
        img = pygame.transform.scale(img, (200, 200))
        explosion_anim['player'].append(img)
    powerup_images = {}
    powerup_images['shield'] = pygame.image.load(path.join(img_dir, 'shield_gold.png')).convert()
    powerup_images['gun'] = pygame.image.load(path.join(img_dir, 'bolt_gold.png')).convert()



    # Load all game sounds
    shoot_sound = pygame.mixer.Sound(path.join(snd_dir, 'Laser_Shoot6.wav'))
    shield_sound = pygame.mixer.Sound(path.join(snd_dir, 'Pow6.wav'))
    power_sound = pygame.mixer.Sound(path.join(snd_dir, 'Pow5.wav'))
    expl_sounds = []
    for snd in ['Explosion.wav', 'Explosion4.wav']:
        expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir, snd)))
    player_die_sound = pygame.mixer.Sound(path.join(snd_dir, 'Explosion40.wav'))
    pygame.mixer.music.load(path.join(snd_dir, 'tgfcoder-FrozenJam-SeamlessLoop.mp3'))
    pygame.mixer.music.set_volume(1)
    pygame.mixer.music.play(loops=-1)

    # Game loop
    game_over = True
    running = True
    while running:
        if game_over:
            game_over = False
            all_sprites = pygame.sprite.Group()
            mobs = pygame.sprite.Group()
            bullets = pygame.sprite.Group()
            powerups = pygame.sprite.Group()
            player = Player()
            all_sprites.add(player)
            for i in range(8):
                newmob()
        
            score = 0 
            
           
            
        # keep loop running at the right speed
        clock.tick(FPS)
        # Process input(event)
        
        for event in   pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            
        # Update
        all_sprites.update()

        # check to see if a bullet hit a mob
        hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
        for hit in hits:
            score += 50 - hit.radius
            random.choice(expl_sounds).play()
            expl = Explosion(hit.rect.center, 'lg')
            all_sprites.add(expl)
            if random.random() > 0.9:
                pow = Pow(hit.rect.center)
                all_sprites.add(pow)
                powerups.add(pow)
            newmob()
            
        # check to see if a mob hit the player
        hits = pygame.sprite.spritecollide(player, mobs, True, pygame.sprite.collide_circle)
        for hit in hits:
            player.shield -= hit.radius * 2
            expl = Explosion(hit.rect.center, 'sm')
            all_sprites.add(expl)
            newmob()
            if player.shield<=0:
                player_die_sound.play()
                death_explosion = Explosion(player.rect.center, 'player')
                all_sprites.add(death_explosion)
                player.hide()
                player.lives -=1
                player.shield = 100

        # check to see if player hit a powerup
        hits = pygame.sprite.spritecollide(player, powerups, True)
        for hit in hits:
            if hit.type == 'shield':
                player.shield += random.randrange(10, 30)
                shield_sound.play()
                if player.shield >= 100:
                    player.shield = 100
            if hit.type == 'gun':
                player.powerup()
                power_sound.play()
            

        # if the player died and the explosion has finished playing
        if player.lives == 0 and not death_explosion.alive():
            game_over = True
            show_go_screen() 
            
        # Draw / render
        screen.fill(BLACK)
        screen.blit(background,background_rect)
        all_sprites.draw(screen)
        draw_text(screen, str(score), 18, WIDTH / 2, 10)
        draw_shield_bar(screen, 5, 5, player.shield)
        draw_lives(screen, WIDTH - 100, 5, player.lives, player_mini_img)
        
        # *after* drawing everything, flip the display
        pygame.display.flip()

    pygame.quit()
    quit()
    
    


def picturepuzzle():
    import pygame
    import time
    import random
    import sys


    pygame.init()
    pygame.mixer.init()

    display_width = 600
    display_height = 600


    black =(0,0,0)
    white=(255,255,255)
    red = (200, 0,0)
    green =(0,200,0)
    bright_green = (0,255,0)
    bright_red = (255,0,0)

    gameDisplay = pygame.display.set_mode((display_width,display_height))
    pygame.display.set_caption('Picture puzzle')
    clock = pygame.time.Clock()
    myfont = pygame.font.SysFont('freesansbold.ttf',15)
    font_name = pygame.font.match_font('arial')

    cong_img = pygame.image.load('congb.jpg')
    cong_img_rect = cong_img.get_rect()
    cong_img1 = pygame.image.load('cong1.jpg')
    cong_img_rect1 = cong_img1.get_rect()
    cong_img2 = pygame.image.load('cong2.jpg')
    cong_img_rect2 = cong_img2.get_rect()
    cong_img3= pygame.image.load('cong3.jpg')
    cong_img_rect3 = cong_img3.get_rect()


    back_img = pygame.image.load('back2.jpg')
    back_img_rect = back_img.get_rect()
    back_img1 = pygame.image.load('featured1.jpg')
    back_img_rect1 = back_img.get_rect()
    back_img2 = pygame.image.load('back5.jpg')
    back_img_rect2 = back_img.get_rect()
    back_img3= pygame.image.load('back6.jpg')
    back_img_rect3 = back_img.get_rect()
    back_img4= pygame.image.load('back7.jpg')
    back_img_rect4 = back_img.get_rect()
    back_img5= pygame.image.load('back8.jpg')
    back_img_rect5= back_img.get_rect()
    back_img6= pygame.image.load('back9.jpg')
    back_img_rect6= back_img.get_rect()
    back_img7= pygame.image.load('back10.jpg')
    back_img_rect7= back_img.get_rect()
    back_img8= pygame.image.load('back11.jpg')
    back_img_rect8= back_img.get_rect()
    back_img9= pygame.image.load('back12.jpg')
    back_img_rect9= back_img.get_rect()
    back_img10= pygame.image.load('back13.png')
    back_img_rect10= back_img.get_rect()
    back_img11= pygame.image.load('back14.jpg')
    back_img_rect11= back_img.get_rect()
    back_img12= pygame.image.load('back15.jpg')
    back_img_rect12= back_img.get_rect()
    back_img13= pygame.image.load('back16.jpg')
    back_img_rect13= back_img.get_rect()
    back_img14= pygame.image.load('back17.jpg')
    back_img_rect14= back_img.get_rect()
    back_img15= pygame.image.load('back18.jpg')
    back_img_rect15= back_img.get_rect()
    back_img16= pygame.image.load('back19.jpg')
    back_img_rect16= back_img.get_rect()
    back_img17= pygame.image.load('back20.jpg')
    back_img_rect17= back_img.get_rect()
    back_img18= pygame.image.load('back21.jpg')
    back_img_rect18= back_img.get_rect()
    back_img19= pygame.image.load('back22.jpg')
    back_img_rect19= back_img.get_rect()
    back_img20= pygame.image.load('back23.jpg')
    back_img_rect20= back_img.get_rect()
    back_img21= pygame.image.load('back24.jpg')
    back_img_rect21= back_img.get_rect()
    back_img22= pygame.image.load('back25.jpg')
    back_img_rect22= back_img.get_rect()
    back_img23= pygame.image.load('back26.jpg')
    back_img_rect23= back_img.get_rect()
    back_img24= pygame.image.load('back27.jpg')
    back_img_rect24= back_img.get_rect()
    back_img25= pygame.image.load('back28.jpg')
    back_img_rect25= back_img.get_rect()
    back_img26= pygame.image.load('back29.jpg')
    back_img_rect26= back_img.get_rect()
    back_img27= pygame.image.load('back20.jpg')
    back_img_rect27= back_img.get_rect()
    back_img28= pygame.image.load('back31.jpg')
    back_img_rect28= back_img.get_rect()
    back_img29= pygame.image.load('back32.jpg')
    back_img_rect29= back_img.get_rect()
    back_img30= pygame.image.load('back33.jpg')
    back_img_rect30= back_img.get_rect()
    back_img31= pygame.image.load('back34.jpg')
    back_img_rect31= back_img.get_rect()
    back_img32= pygame.image.load('back35.jpg')
    back_img_rect32= back_img.get_rect()
    back_img33= pygame.image.load('back36.jpg')
    back_img_rect33= back_img.get_rect()
    back_img34= pygame.image.load('back37.jpg')
    back_img_rect34= back_img.get_rect()
    back_img35= pygame.image.load('back38.jpg')
    back_img_rect35= back_img.get_rect()
    back_img36= pygame.image.load('back39.jpg')
    back_img_rect36= back_img.get_rect()
    back_img37= pygame.image.load('back40.jpg')
    back_img_rect37= back_img.get_rect()
    back_img38= pygame.image.load('back41.jpg')
    back_img_rect38= back_img.get_rect()
    back_img39= pygame.image.load('back42.jpg')
    back_img_rect39= back_img.get_rect()
    back_img40= pygame.image.load('back43.jpg')
    back_img_rect40= back_img.get_rect()
    back_img41= pygame.image.load('back44.jpg')
    back_img_rect41= back_img.get_rect()
    back_img42= pygame.image.load('back45.jpg')
    back_img_rect42= back_img.get_rect()
    back_img43= pygame.image.load('back46.jpg')
    back_img_rect43= back_img.get_rect()
    back_img44= pygame.image.load('back47.jpg')
    back_img_rect44= back_img.get_rect()
    back_img45= pygame.image.load('back48.jpg')
    back_img_rect45= back_img.get_rect()
    back_img46= pygame.image.load('back21.jpg')
    back_img_rect46= back_img.get_rect()
    back_img47= pygame.image.load('back22.jpg')
    back_img_rect47= back_img.get_rect()
    back_img48= pygame.image.load('back23.jpg')
    back_img_rect48= back_img.get_rect()
    back_img49= pygame.image.load('back24.jpg')
    back_img_rect49= back_img.get_rect()
    back_img50= pygame.image.load('back25.jpg')
    back_img_rect50= back_img.get_rect()
    back_img51= pygame.image.load('back26.jpg')
    back_img_rect51= back_img.get_rect()
    back_img52= pygame.image.load('back27.jpg')
    back_img_rect52= back_img.get_rect()
    back_img53= pygame.image.load('back28.jpg')
    back_img_rect53= back_img.get_rect()
    back_img54= pygame.image.load('back29.jpg')
    back_img_rect54= back_img.get_rect()
    back_img55= pygame.image.load('back30.jpg')
    back_img_rect55= back_img.get_rect()
    back_img56= pygame.image.load('back31.jpg')
    back_img_rect56= back_img.get_rect()
    back_img57= pygame.image.load('back32.jpg')
    back_img_rect57= back_img.get_rect()
    back_img58= pygame.image.load('back33.jpg')
    back_img_rect58= back_img.get_rect()
    back_img59= pygame.image.load('back34.jpg')
    back_img_rect59= back_img.get_rect()
    back_img60= pygame.image.load('back35.jpg')
    back_img_rect60= back_img.get_rect()
    back_img61= pygame.image.load('back36.jpg')
    back_img_rect61= back_img.get_rect()









    frontpage  =pygame.image.load('acura.jpg')
    frontpage_rect = frontpage.get_rect()
    frontpage1  =pygame.image.load('acura1.png')
    frontpage_rect1 = frontpage.get_rect()
    frontpage2  =pygame.image.load('apache.png')
    frontpage_rect2 = frontpage.get_rect()
    frontpage3  =pygame.image.load('apache2.jpg')
    frontpage_rect3 = frontpage.get_rect()
    frontpage4  =pygame.image.load('axis.jpg')
    frontpage_rect4 = frontpage.get_rect()
    frontpage5  =pygame.image.load('axis1.jpg')
    frontpage_rect5= frontpage.get_rect()
    frontpage6  =pygame.image.load('bestbuy.jpg')
    frontpage_rect6= frontpage.get_rect()
    frontpage7  =pygame.image.load('bestbuy2.jpg')
    frontpage_rect7= frontpage.get_rect()
    frontpage8  =pygame.image.load('bmw.png')
    frontpage_rect8= frontpage.get_rect()
    frontpage9  =pygame.image.load('bmw1.jpg')
    frontpage_rect9= frontpage.get_rect()
    frontpage10  =pygame.image.load('bootstrap.jpg')
    frontpage_rect10= frontpage.get_rect()
    frontpage11  =pygame.image.load('bootstrap2.jpg')
    frontpage_rect11= frontpage.get_rect()
    frontpage12  =pygame.image.load('buick.jpg')
    frontpage_rect12= frontpage.get_rect()
    frontpage13  =pygame.image.load('buick1.jpg')
    frontpage_rect13= frontpage.get_rect()
    frontpage14  =pygame.image.load('cococola.jpg')
    frontpage_rect14= frontpage.get_rect()
    frontpage15  =pygame.image.load('cococola1.png')
    frontpage_rect15= frontpage.get_rect()
    frontpage16  =pygame.image.load('dominos.png')
    frontpage_rect16= frontpage.get_rect()
    frontpage17  =pygame.image.load('dominos2.png')
    frontpage_rect17= frontpage.get_rect()
    frontpage18  =pygame.image.load('dream.png')
    frontpage_rect18= frontpage.get_rect()
    frontpage19  =pygame.image.load('dream2.jpg')
    frontpage_rect19= frontpage.get_rect()
    frontpage20  =pygame.image.load('ebay.png')
    frontpage_rect20= frontpage.get_rect()
    frontpage21  =pygame.image.load('ebay1.png')
    frontpage_rect21= frontpage.get_rect()
    frontpage22  =pygame.image.load('iot.jpg')
    frontpage_rect22= frontpage.get_rect()
    frontpage23  =pygame.image.load('iot1.jpg')
    frontpage_rect23= frontpage.get_rect()
    frontpage24  =pygame.image.load('ford.jpg')
    frontpage_rect24= frontpage.get_rect()
    frontpage25  =pygame.image.load('ford1.jpg')
    frontpage_rect25= frontpage.get_rect()
    frontpage26  =pygame.image.load('arjun.jpg')
    frontpage_rect26= frontpage.get_rect()
    frontpage27  =pygame.image.load('arjun2.jpg')
    frontpage_rect27= frontpage.get_rect()
    frontpage28  =pygame.image.load('intel.png')
    frontpage_rect28= frontpage.get_rect()
    frontpage29  =pygame.image.load('intel1.png')
    frontpage_rect29= frontpage.get_rect()
    frontpage30  =pygame.image.load('jaguar.jpg')
    frontpage_rect30= frontpage.get_rect()
    frontpage31  =pygame.image.load('jaguar2.jpg')
    frontpage_rect31= frontpage.get_rect()
    frontpage32  =pygame.image.load('java.png')
    frontpage_rect32= frontpage.get_rect()
    frontpage33  =pygame.image.load('java1.jpg')
    frontpage_rect33= frontpage.get_rect()
    frontpage34  =pygame.image.load('lays.jpg')
    frontpage_rect34= frontpage.get_rect()
    frontpage35  =pygame.image.load('lays1.png')
    frontpage_rect35= frontpage.get_rect()
    frontpage36  =pygame.image.load('lego.jpg')
    frontpage_rect36= frontpage.get_rect()
    frontpage37  =pygame.image.load('lego1.png')
    frontpage_rect37= frontpage.get_rect()
    frontpage38  =pygame.image.load('linked.jpg')
    frontpage_rect38= frontpage.get_rect()
    frontpage39  =pygame.image.load('linked1.jpg')
    frontpage_rect39= frontpage.get_rect()
    frontpage40  =pygame.image.load('linux.jpg')
    frontpage_rect40= frontpage.get_rect()
    frontpage41  =pygame.image.load('linux1.jpg')
    frontpage_rect41= frontpage.get_rect()
    frontpage42  =pygame.image.load('nbc.png')
    frontpage_rect42= frontpage.get_rect()
    frontpage43  =pygame.image.load('nbc1.png')
    frontpage_rect43= frontpage.get_rect()
    frontpage44  =pygame.image.load('nestle.jpg')
    frontpage_rect44= frontpage.get_rect()
    frontpage45  =pygame.image.load('nestle1.png')
    frontpage_rect45= frontpage.get_rect()
    frontpage46  =pygame.image.load('nike.jpg')
    frontpage_rect46= frontpage.get_rect()
    frontpage47  =pygame.image.load('nike1.png')
    frontpage_rect47= frontpage.get_rect()
    frontpage48  =pygame.image.load('python.jpg')
    frontpage_rect48= frontpage.get_rect()
    frontpage49  =pygame.image.load('python1.png')
    frontpage_rect49= frontpage.get_rect()
    frontpage50  =pygame.image.load('micromax.jpg')
    frontpage_rect50= frontpage.get_rect()
    frontpage51  =pygame.image.load('micromax1.png')
    frontpage_rect51= frontpage.get_rect()
    frontpage52  =pygame.image.load('sonyer.png')
    frontpage_rect52= frontpage.get_rect()
    frontpage53  =pygame.image.load('sonyer1.jpg')
    frontpage_rect53= frontpage.get_rect()
    frontpage54  =pygame.image.load('starbucks.png')
    frontpage_rect54= frontpage.get_rect()
    frontpage55  =pygame.image.load('starbucks1.jpg')
    frontpage_rect55= frontpage.get_rect()
    frontpage56  =pygame.image.load('versace.jpg')
    frontpage_rect56= frontpage.get_rect()
    frontpage57 =pygame.image.load('versace1.png')
    frontpage_rect57= frontpage.get_rect()
    frontpage58  =pygame.image.load('volkswagen.jpg')
    frontpage_rect58= frontpage.get_rect()
    frontpage59  =pygame.image.load('volkswagen1.jpg')
    frontpage_rect59= frontpage.get_rect()









    lost_img = pygame.image.load('lostgame.png')
    lost_img_rect = lost_img.get_rect()

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def label():
        pass

        
    def button(msg,x,y,w,h,ic,ac,action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()

        else:
            pygame.draw.rect(gameDisplay, ic,(x,y,w,h))
        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf,textRect = text_objects(msg,smallText)
        textRect.center =((x+(w/2)),(y+(h/2)))
        gameDisplay.blit(textSurf, textRect)
        
    def quitgame():
        pygame.quit()
        quit()
        
        
        
    def game_intro():
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(white)
            gameDisplay.blit(back_img,back_img_rect)
            largeText = pygame.font.Font('freesansbold.ttf',60)
            TextSurf, TextRect = text_objects("PICTURE PUZZLE",largeText)
            TextRect.center = ((display_width / 2  ),(display_height / 2 - 180))
            gameDisplay.blit(TextSurf, TextRect)
            button("GO",420,220,130,35,green,bright_green,game_loop)
            button("Instructions",420,270,130,35,yellow,bright_yellow,inst2)
            button("Quit",420,320,130,35,red,bright_red,quitgame)

            pygame.display.update()

            clock.tick(15)


    def inst2():
        inst = True
        while inst:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(white)
            gameDisplay.blit(inst_img1,inst_img_rect1)
            button("BACK",200,500,70,35,yellow,bright_yellow,picturepuzzle)
            button("PLAY",330,500,70,35,green,bright_green,game_loop)

        
        
            pygame.display.update()
            clock.tick(15)
        

    def next_loop():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img4,back_img_rect4)
            frontpage_rect2.center = ((display_width/2 - 40, display_height / 2 - 100))
            gameDisplay.blit(frontpage2, frontpage_rect2)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.UBUNTU",120,350,150,50,green,bright_green,lost_loop)
            button("2.ANSE",370,350,150,50,green,bright_green,lost_loop)
            button("3.APACHE",120,420,150,50,green,bright_green,sol_loop1)
            button("4.ASME",370,420,150,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop1():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img5,back_img_rect5)
            frontpage_rect4.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage4, frontpage_rect4)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("ABN.AMRO BANK",70,350,190,50,green,bright_green,lost_loop)
            button("AXIS BANK",370,350,180,50,green,bright_green,sol_loop2)
            button("ALLAHABAD BANK",70,420,190,50,green,bright_green,lost_loop)
            button("ANDHRA BANK",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop2():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img8,back_img_rect8)
            frontpage_rect6.center = ((display_width/2 - 110 , display_height / 2 - 150))
            gameDisplay.blit(frontpage6, frontpage_rect6)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.BEST BUY",70,350,190,50,green,bright_green,sol_loop3)
            button("2.BLUE DART",370,350,180,50,green,bright_green,lost_loop)
            button("3.BIG BAZAR",70,420,190,50,green,bright_green,lost_loop)
            button("4.BALENO",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()

        

    def next_loop3():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img9,back_img_rect9)
            frontpage_rect8.center = ((display_width/2  , display_height / 2 - 180))
            gameDisplay.blit(frontpage8, frontpage_rect8)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.BMW",70,350,190,50,green,bright_green,sol_loop4)
            button("2.BUGGATTI",370,350,180,50,green,bright_green,lost_loop)
            button("3.BENTLEY",70,420,190,50,green,bright_green,lost_loop)
            button("4.NISSAN",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop4():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img11,back_img_rect11)
            frontpage_rect10.center = ((display_width/2  , display_height / 2 - 180))
            gameDisplay.blit(frontpage10, frontpage_rect10)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.BITBUCKET",70,350,190,50,green,bright_green,lost_loop)
            button("2.BOOTSTRAP",370,350,180,50,green,bright_green,sol_loop5)
            button("3.BIG DATA",70,420,190,50,green,bright_green,lost_loop)
            button("4.BEHANCE",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop5():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img13,back_img_rect13)
            frontpage_rect12.center = ((display_width/2  , display_height / 2 - 180))
            gameDisplay.blit(frontpage12, frontpage_rect12)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.BUICK",70,350,190,50,green,bright_green,sol_loop6)
            button("2.FARGO",370,350,180,50,green,bright_green,lost_loop)
            button("3.IMPERIAL",70,420,190,50,green,bright_green,lost_loop)
            button("4.MARQUETTE",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()



    def next_loop6():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img15,back_img_rect15)
            frontpage_rect14.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage14, frontpage_rect14)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.COCO COLA",70,350,190,50,green,bright_green,sol_loop7)
            button("2.PEPSI",370,350,180,50,green,bright_green,lost_loop)
            button("3.CARIBA",70,420,190,50,green,bright_green,lost_loop)
            button("4.TROPICANA",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop7():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img18,back_img_rect18)
            frontpage_rect16.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage16, frontpage_rect16)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.PIZZA HUT",70,350,190,50,green,bright_green,lost_loop)
            button("2.DOMNIOS PIZZA",370,350,180,50,green,bright_green,sol_loop8)
            button("3.MC DONALDS",70,420,190,50,green,bright_green,lost_loop)
            button("4.PAPA JOHNS'S",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop8():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img20,back_img_rect20)
            frontpage_rect18.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage18, frontpage_rect18)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.DROP BOX",70,350,190,50,green,bright_green,lost_loop)
            button("2.DREAM WEAVER",370,350,180,50,green,bright_green,sol_loop9)
            button("3.DREAM WORKS",70,420,190,50,green,bright_green,lost_loop)
            button("4.DRUPAL",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop9():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img22,back_img_rect22)
            frontpage_rect20.center = ((display_width/2  , display_height / 2 - 50))
            gameDisplay.blit(frontpage20, frontpage_rect20)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.EBAY",70,350,190,50,green,bright_green,sol_loop10)
            button("2.AMAZON",370,350,180,50,green,bright_green,lost_loop)
            button("3.FLIPKART",70,420,190,50,green,bright_green,lost_loop)
            button("4.ENWOMB",370,420,180,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop10():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img24,back_img_rect24)
            frontpage_rect22.center = ((display_width/2  , display_height / 2 - 110))
            gameDisplay.blit(frontpage22, frontpage_rect22)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("PINTEREST",50,350,210,50,green,bright_green,lost_loop)
            button("IOT",370,350,200,50,green,bright_green,sol_loop11)
            button("EMBEDDED SYSTEMS",50,420,210,50,green,bright_green,lost_loop)
            button("CONNECTED WORLD",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop11():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img26,back_img_rect26)
            frontpage_rect24.center = ((display_width/2  , display_height / 2 - 80))
            gameDisplay.blit(frontpage24, frontpage_rect24)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.FORD",50,350,210,50,green,bright_green,sol_loop12)
            button("2.FABCAR",370,350,200,50,green,bright_green,lost_loop)
            button("3.FERRARI",50,420,210,50,green,bright_green,lost_loop)
            button("4.FERNANDA",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop12():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img28,back_img_rect28)
            frontpage_rect26.center = ((display_width/2  , display_height / 2 - 80))
            gameDisplay.blit(frontpage26, frontpage_rect26)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("AJIM PREMJI",50,350,210,50,green,bright_green,lost_loop)
            button("ARJUN MALHOTRA",370,350,200,50,green,bright_green,sol_loop13)
            button("ANAND MAHINDRA",50,420,210,50,green,bright_green,lost_loop)
            button("LARRY PAGE",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop13():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img30,back_img_rect30)
            frontpage_rect28.center = ((display_width/2  , display_height / 2 - 100))
            gameDisplay.blit(frontpage28, frontpage_rect28)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.NESPRESSO",50,350,210,50,green,bright_green,lost_loop)
            button("2.NICHOLLOS",370,350,200,50,green,bright_green,lost_loop)
            button("3.INTEL",50,420,210,50,green,bright_green,sol_loop14)
            button("4.INDESIT",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop14():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img32,back_img_rect32)
            frontpage_rect30.center = ((display_width/2 - 40 , display_height / 2 - 120))
            gameDisplay.blit(frontpage30, frontpage_rect30)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.CHEETAH X-15",50,350,210,50,green,bright_green,lost_loop)
            button("2.JAGUAR",370,350,200,50,green,bright_green,sol_loop15)
            button("3.BENIBILLIONS",50,420,210,50,green,bright_green,lost_loop)
            button("4.XERXES",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop15():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img34,back_img_rect34)
            frontpage_rect32.center = ((display_width/2 + 30, display_height / 2 - 120))
            gameDisplay.blit(frontpage32, frontpage_rect32)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.JML",50,350,210,50,green,bright_green,lost_loop)
            button("2.JQUERY",370,350,200,50,green,bright_green,lost_loop)
            button("3.JAVA",50,420,210,50,green,bright_green,sol_loop16)
            button("4.JTA",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop16():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img36,back_img_rect36)
            frontpage_rect34.center = ((display_width/2 , display_height / 2 - 120))
            gameDisplay.blit(frontpage34, frontpage_rect34)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.CHEETOS",50,350,210,50,green,bright_green,lost_loop)
            button("2.KURKURE",370,350,200,50,green,bright_green,lost_loop)
            button("3.BINGO",50,420,210,50,green,bright_green,lost_loop)
            button("4.LAYS",370,420,200,50,green,bright_green,sol_loop17)
            pygame.display.flip()

    def next_loop17():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img38,back_img_rect38)
            frontpage_rect36.center = ((display_width/2 + 30, display_height / 2 - 120))
            gameDisplay.blit(frontpage36, frontpage_rect36)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.LEGO",50,350,210,50,green,bright_green,sol_loop18)
            button("2.LEGENDZ",370,350,200,50,green,bright_green,lost_loop)
            button("3.LIMA",50,420,210,50,green,bright_green,lost_loop)
            button("4.HOT WHEELS",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop18():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img40,back_img_rect40)
            frontpage_rect38.center = ((display_width/2 + 30, display_height / 2 - 120))
            gameDisplay.blit(frontpage38, frontpage_rect38)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.LINKED IN",50,350,210,50,green,bright_green,sol_loop19)
            button("2.FLICKR",370,350,200,50,green,bright_green,lost_loop)
            button("3.FOTOLOG",50,420,210,50,green,bright_green,lost_loop)
            button("4.IBIBO",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop19():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img42,back_img_rect42)
            frontpage_rect40.center = ((display_width/2 + 30, display_height / 2 - 120))
            gameDisplay.blit(frontpage40, frontpage_rect40)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.ECLIPSE",50,350,210,50,green,bright_green,lost_loop)
            button("2.LINUX",370,350,200,50,green,bright_green,sol_loop20)
            button("3.TURBO C",50,420,210,50,green,bright_green,lost_loop)
            button("4.JRE",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop20():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img44,back_img_rect44)
            frontpage_rect42.center = ((display_width/2 , display_height / 2 - 120))
            gameDisplay.blit(frontpage42, frontpage_rect42)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.NDTV",50,350,210,50,green,bright_green,lost_loop)
            button("2.NBC",370,350,200,50,green,bright_green,sol_loop21)
            button("3.NEWS 9",50,420,210,50,green,bright_green,lost_loop)
            button("4.TIMES NOW",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


        
    def  next_loop21():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img46,back_img_rect46)
            frontpage_rect44.center = ((display_width/2 , display_height / 2 - 120))
            gameDisplay.blit(frontpage44, frontpage_rect44)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.UNILEVER",50,350,210,50,green,bright_green,lost_loop)
            button("2.NESTLE",370,350,200,50,green,bright_green,sol_loop22)
            button("3.AMWAY",50,420,210,50,green,bright_green,lost_loop)
            button("4.BRITANNIA",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop22():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img48,back_img_rect48)
            frontpage_rect46.center = ((display_width/2 , display_height / 2 - 120))
            gameDisplay.blit(frontpage46, frontpage_rect46)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.PUMA",50,350,210,50,green,bright_green,lost_loop)
            button("2.NIKE",370,350,200,50,green,bright_green,sol_loop23)
            button("3.REEBOK",50,420,210,50,green,bright_green,lost_loop)
            button("4.ADIDAS",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()


    def next_loop23():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img50,back_img_rect50)
            frontpage_rect48.center = ((display_width/2 , display_height / 2 - 120))
            gameDisplay.blit(frontpage48, frontpage_rect48)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.JAVA SCRIPT",50,350,210,50,green,bright_green,lost_loop)
            button("2.PHP",370,350,200,50,green,bright_green,lost_loop)
            button("3.RUBY",50,420,210,50,green,bright_green,lost_loop)
            button("4.PYTHON",370,420,200,50,green,bright_green,sol_loop24)
            pygame.display.flip()

    def next_loop24():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img52,back_img_rect52)
            frontpage_rect50.center = ((display_width/2 , display_height / 2 - 160))
            gameDisplay.blit(frontpage50, frontpage_rect50)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.MICROMAX",50,350,210,50,green,bright_green,sol_loop25)
            button("2.ONE PLUS",370,350,200,50,green,bright_green,lost_loop)
            button("3.OPPO",50,420,210,50,green,bright_green,lost_loop)
            button("4.XIAOMI",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop25():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img54,back_img_rect54)
            frontpage_rect52.center = ((display_width/2 , display_height / 2 - 160))
            gameDisplay.blit(frontpage52, frontpage_rect52)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("FOXCONN",50,350,210,50,green,bright_green,lost_loop)
            button("SONY",370,350,200,50,green,bright_green,lost_loop)
            button("SONY ERICCSON",50,420,210,50,green,bright_green,sol_loop26)
            button("LAVA",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def next_loop26():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img56,back_img_rect56)
            frontpage_rect54.center = ((display_width/2 , display_height / 2 - 160))
            gameDisplay.blit(frontpage54, frontpage_rect54)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("DUNKIN DONUTS",50,350,210,50,green,bright_green,lost_loop)
            button("STARBUCKS",370,350,200,50,green,bright_green,sol_loop27)
            button("COFFEE BEANERY",50,420,210,50,green,bright_green,lost_loop)
            button("GLORIA JEAN'S",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

        
        
    def next_loop27():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img58,back_img_rect58)
            frontpage_rect56.center = ((display_width/2 , display_height / 2 - 160))
            gameDisplay.blit(frontpage56, frontpage_rect56)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.EVINE",50,350,210,50,green,bright_green,lost_loop)
            button("2.GUCCI",370,350,200,50,green,bright_green,lost_loop)
            button("3.VERSACE",50,420,210,50,green,bright_green,sol_loop28)
            button("4.NELLY",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()



    def next_loop28():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img60,back_img_rect60)
            frontpage_rect58.center = ((display_width/2 , display_height / 2 - 160))
            gameDisplay.blit(frontpage58, frontpage_rect58)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.MAHINDRA",50,350,210,50,green,bright_green,lost_loop)
            button("2.SAN MOTORS",370,350,200,50,green,bright_green,lost_loop)
            button("3.VOLKSWAGEN",50,420,210,50,green,bright_green,sol_loop29)
            button("4.SKODA",370,420,200,50,green,bright_green,lost_loop)
            pygame.display.flip()

    def congo_loop():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(cong_img, cong_img_rect)
            cong_img_rect1.center = ((display_width/2 , 380))
            gameDisplay.blit(cong_img1, cong_img_rect1)
            cong_img_rect2.center = ((display_width/2 , 100))
            gameDisplay.blit(cong_img3, cong_img_rect3)
            gameDisplay.blit(cong_img2, cong_img_rect2)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("PLAY AGAIN",90,530,150,50,green,bright_green,game_intro)
            button("QUIT",450,530,70,50,red,bright_red,quitgame)
            pygame.display.flip()

            
    def sol_loop29():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img61, back_img_rect61)
            frontpage_rect59.center = ((display_width/2 +20, display_height / 2 - 150))
            gameDisplay.blit(frontpage59, frontpage_rect59)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,congo_loop)
            draw_text(gameDisplay,"VOLKSWAGEN",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:10000",40,display_width/2,400)
            pygame.display.flip()

        
    def sol_loop28():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img59, back_img_rect59)
            frontpage_rect57.center = ((display_width/2 +20, display_height / 2 - 200))
            gameDisplay.blit(frontpage57, frontpage_rect57)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop28)
            draw_text(gameDisplay,"VERSACE",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:8760",40,display_width/2,400)
            pygame.display.flip()

       
    def sol_loop27():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img57, back_img_rect57)
            frontpage_rect55.center = ((display_width/2 , display_height / 2 - 130))
            gameDisplay.blit(frontpage55, frontpage_rect55)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop27)
            draw_text(gameDisplay,"STARBUCKS",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:8120",40,display_width/2,400)
            pygame.display.flip()

        
        
    def sol_loop26():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img55, back_img_rect55)
            frontpage_rect53.center = ((display_width/2 , display_height / 2 - 130))
            gameDisplay.blit(frontpage53, frontpage_rect53)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop26)
            draw_text(gameDisplay,"SONY ERICCSON",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:7480",40,display_width/2,400)
            pygame.display.flip()

        

    def sol_loop25():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img53, back_img_rect53)
            frontpage_rect51.center = ((display_width/2 , display_height / 2 - 30))
            gameDisplay.blit(frontpage51, frontpage_rect51)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop25)
            draw_text(gameDisplay,"MICROMAX",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:6840",40,display_width/2,400)
            pygame.display.flip()

        
    def sol_loop24():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img51, back_img_rect51)
            frontpage_rect49.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage49, frontpage_rect49)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop24)
            draw_text(gameDisplay,"PYTHON",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"BONUS:1600",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:6200",40,display_width/2,450)
            pygame.display.flip()


    def sol_loop23():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img16, back_img_rect16)
            frontpage_rect47.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage47, frontpage_rect47)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop23)
            draw_text(gameDisplay,"NIKE",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:4280",40,display_width/2,400)
            pygame.display.flip()

    def sol_loop22():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img47, back_img_rect47)
            frontpage_rect45.center = ((display_width/2 + 30, display_height / 2 - 150))
            gameDisplay.blit(frontpage45, frontpage_rect45)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop22)
            draw_text(gameDisplay,"NESTLE",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:3960",40,display_width/2,400)
            pygame.display.flip()

    def sol_loop21():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img45, back_img_rect45)
            frontpage_rect43.center = ((display_width/2 + 30, display_height / 2 - 100))
            gameDisplay.blit(frontpage43, frontpage_rect43)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop21)
            draw_text(gameDisplay,"NBC",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:3640",40,display_width/2,400)
            pygame.display.flip()
     
    def sol_loop20():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img43, back_img_rect43)
            frontpage_rect41.center = ((display_width/2, display_height / 2 - 100))
            gameDisplay.blit(frontpage41, frontpage_rect41)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop20)
            draw_text(gameDisplay,"LINUX",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:3320",40,display_width/2,400)
            pygame.display.flip()
     
    def sol_loop19():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img41, back_img_rect41)
            frontpage_rect39.center = ((display_width/2 + 30, display_height / 2 - 100))
            gameDisplay.blit(frontpage39, frontpage_rect39)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop19)
            draw_text(gameDisplay,"LINKED IN",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"BONUS:800",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:3000",40,display_width/2,450)
            pygame.display.flip()
     
    def sol_loop18():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img39, back_img_rect39)
            frontpage_rect37.center = ((display_width/2 + 30, display_height / 2 - 150))
            gameDisplay.blit(frontpage37, frontpage_rect37)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop18)
            draw_text(gameDisplay,"LEGO",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:2040",40,display_width/2,400)
            pygame.display.flip()
     
    def sol_loop17():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img37, back_img_rect37)
            frontpage_rect35.center = ((display_width/2 + 30, display_height / 2 - 100))
            gameDisplay.blit(frontpage35, frontpage_rect35)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop17)
            draw_text(gameDisplay,"LAYS",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:1880",40,display_width/2,400)
            pygame.display.flip()
     

    def sol_loop16():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img35, back_img_rect35)
            frontpage_rect33.center = ((display_width/2 , display_height / 2 - 150))
            gameDisplay.blit(frontpage33, frontpage_rect33)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop16)
            draw_text(gameDisplay,"JAVA",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:1720",40,display_width/2,400)
            pygame.display.flip()
     
        
        
    def sol_loop15():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img33, back_img_rect33)
            frontpage_rect31.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage31, frontpage_rect31)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop15)
            draw_text(gameDisplay,"JAGUAR",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:1560",40,display_width/2,400)
            pygame.display.flip()
     

    def sol_loop14():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img31, back_img_rect31)
            frontpage_rect29.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage29, frontpage_rect29)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop14)
            draw_text(gameDisplay,"INTEL",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"BONUS:400",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:1400",40,display_width/2,450)
            pygame.display.flip()
        


    def sol_loop13():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img29, back_img_rect29)
            frontpage_rect27.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage27, frontpage_rect27)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop13)
            draw_text(gameDisplay,"ARJUN MALHOTRA",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:920",40,display_width/2,400)
            pygame.display.flip()
        

    def sol_loop12():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img27, back_img_rect27)
            frontpage_rect25.center = ((display_width/2 - 20 , display_height / 2 - 80))
            gameDisplay.blit(frontpage25, frontpage_rect25)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop12)
            draw_text(gameDisplay,"FORD",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:840",40,display_width/2,400)
            pygame.display.flip()
        
        
    def sol_loop11():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img25, back_img_rect25)
            frontpage_rect23.center = ((display_width/2 , display_height / 2 - 110))
            gameDisplay.blit(frontpage23, frontpage_rect23)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop11)
            draw_text(gameDisplay,"IOT",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:760",40,display_width/2,400)
            pygame.display.flip()
        
    def sol_loop10():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img23, back_img_rect23)
            frontpage_rect21.center = ((display_width/2 + 20, display_height / 2 - 50))
            gameDisplay.blit(frontpage21, frontpage_rect21)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop10)
            draw_text(gameDisplay,"EBAY",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:680",40,display_width/2,400)
            pygame.display.flip()
        
    def sol_loop9():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img19, back_img_rect19)
            frontpage_rect19.center = ((display_width/2 , display_height / 2 - 150))
            gameDisplay.blit(frontpage19, frontpage_rect19)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop9)
            draw_text(gameDisplay,"DREAM WEAVER",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"BONUS:200",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:600",40,display_width/2,450)
            pygame.display.flip()
    def sol_loop8():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img19, back_img_rect19)
            frontpage_rect17.center = ((display_width/2 + 30 , display_height / 2 - 100))
            gameDisplay.blit(frontpage17, frontpage_rect17)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop8)
            draw_text(gameDisplay,"DOMINOS PIZZA",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:360",40,display_width/2,400)
            pygame.display.flip()

        
    def sol_loop7():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img16, back_img_rect16)
            frontpage_rect15.center = ((display_width/2  , display_height / 2 - 100))
            gameDisplay.blit(frontpage15, frontpage_rect15)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop7)
            draw_text(gameDisplay,"COCO COLA",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:320",40,display_width/2,400)
            pygame.display.flip()

    def sol_loop6():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img14, back_img_rect14)
            frontpage_rect13.center = ((display_width/2  , display_height / 2 - 100))
            gameDisplay.blit(frontpage13, frontpage_rect13)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop6)
            draw_text(gameDisplay,"BUICK",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:280",40,display_width/2,400)
            pygame.display.flip()

        
    def sol_loop5():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img12, back_img_rect12)
            frontpage_rect11.center = ((display_width/2  , display_height / 2 - 150))
            gameDisplay.blit(frontpage11, frontpage_rect11)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop5)
            draw_text(gameDisplay,"BOOTSTRAP",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:240",40,display_width/2,400)
            pygame.display.flip()
        
        
    def sol_loop4():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img10, back_img_rect10)
            frontpage_rect9.center = ((display_width/2  , display_height / 2 - 180))
            gameDisplay.blit(frontpage9, frontpage_rect9)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop4)
            draw_text(gameDisplay,"BMW",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"BONUS:100",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:200",40,display_width/2,450)
            pygame.display.flip()
        
        
    def sol_loop3():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img7, back_img_rect7)
            frontpage_rect7.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage7, frontpage_rect7)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop3)
            draw_text(gameDisplay,"BEST BUY",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:80",40,display_width/2,400)
            pygame.display.flip()
        
    def sol_loop2():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img6, back_img_rect6)
            frontpage_rect3.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage5, frontpage_rect5)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,450,100,50,green,bright_green,next_loop2)
            draw_text(gameDisplay,"AXIS BANK",40,display_width/2,300)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,350)
            draw_text(gameDisplay,"SCORE:60",40,display_width/2,400)
            pygame.display.flip()
    def sol_loop1():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img2, back_img_rect2)
            frontpage_rect3.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage3, frontpage_rect3)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop1)
            draw_text(gameDisplay,"APACHE",40,display_width/2,350)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:40",40,display_width/2,450)
            pygame.display.flip()

    def sol_loop():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img2, back_img_rect2)
            
            gameDisplay.blit(frontpage1, frontpage_rect1)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()

            button("NEXT",display_width/2-50,500,100,50,green,bright_green,next_loop)
            draw_text(gameDisplay,"ACURA",40,display_width/2,350)
            draw_text(gameDisplay,"CONGO!!",40,display_width/2,400)
            draw_text(gameDisplay,"SCORE:20",40,display_width/2,450)
            pygame.display.flip()

    def lost_loop():
        gameExit = False
        while not gameExit:
            gameDisplay.fill(white)
            
            gameDisplay.blit(back_img3, back_img_rect3)
            lost_img_rect.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(lost_img, lost_img_rect)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            button("PLAY AGAIN",display_width/2 -75,350,150,35,green,bright_green,game_intro)
            button("BACK",display_width/2 - 35,400,70,35,yellow,bright_yellow,beginpage) 
            button("QUIT",display_width/2 - 35,450,70,35,red,bright_red,quitgame) 
            pygame.display.flip()
                
    def draw_text(surf, text, size, x, y):
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, black)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        surf.blit(text_surface, text_rect)

        
    def game_loop():
        gameExit = False
        while  not  gameExit:
            gameDisplay.fill(white)
            gameDisplay.blit(back_img1, back_img_rect1)
            frontpage_rect.center = ((display_width/2 , display_height / 2 - 100))
            gameDisplay.blit(frontpage, frontpage_rect)        
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quitgame()
            
                
                        
        
            button("1.ACURA",100,350,150,50,green,bright_green,sol_loop)
            button("2.CHRYSLER",370,350,150,50,green,bright_green,lost_loop)
            button("3.LINCOLLN",100,420,150,50,green,bright_green,lost_loop)
            button("4.CADILLAC",370,420,150,50,green,bright_green,lost_loop)
            pygame.display.flip()
           
    game_intro()
    game_loop()


def jumpy():
    



    import pygame as pg
    import random
    
    from os import path

    img_dir = path.join(path.dirname(__file__), 'img')
    gameDisplay = pg.display.set_mode((WIDTH, HEIGHT))

    
        
    class Game:
        def __init__(self):
            #initialize game window,etc
            #pass says do nothinpygame.init()
            pg.init()
            pg.mixer.init()
            self.screen = pg.display.set_mode((WIDTH,HEIGHT))
            pg.display.set_caption(TITLE)
            self.clock = pg.time.Clock()
            self.running = True
            self.font_name = pg.font.match_font(FONT_NAME)
            self.load_data()

        def load_data(self):
            #load high score
            self.dir = path.dirname(__file__)
            with open(path.join(self.dir,HS_FILE), 'w') as f:
                try:
                    self.highscore = int(f.read())
                except:
                    self.highscore = 0
            #load spritesheet image
            img_dir = path.join(self.dir, 'img')
            self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
            # cloud images
            self.cloud_images = []
            for i in range(1, 4):
                self.cloud_images.append(pg.image.load(path.join(img_dir, 'cloud1.png'.format(1))).convert())

            # load sounds
            self.snd_dir = path.join(self.dir, 'snd')
            self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Jump.wav'))
            self.boost_sound = pg.mixer.Sound(path.join(self.snd_dir, 'Powerup20.wav'))
                
        def new(self):
            #start a new game
            self.score = 0
            self.all_sprites = pg.sprite.LayeredUpdates()
            self.platforms = pg.sprite.Group()
            self.powerups = pg.sprite.Group()
            self.mobs = pg.sprite.Group()
            self.clouds = pg.sprite.Group()
            self.player = Player(self)
            for plat in PLATFORM_LIST:
                 Platform(self, *plat)
            self.mob_timer = 0
            pg.mixer.music.load(path.join(self.snd_dir, 'Happytune.wav'))
            for i in range(8):
                c = Cloud(self)
                c.rect.y += 500
            self.run()

        def run(self):
            #game - loop
            pg.mixer.music.play(loops=-1)
            self.playing = True
            while self.playing:
                self.clock.tick(FPS)
                self.events()
                self.update()
                self.draw()
            pg.mixer.music.fadeout(500)

        def update(self):
             # game loop -update
            self.all_sprites.update()

            #spawn a mob?
            now = pg.time.get_ticks()
            if now - self.mob_timer > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
                self.mob_timer = now
                Mob(self)

            #hit mobs?
            mob_hits = pg.sprite.spritecollide(self.player, self.mobs,False,pg.sprite.collide_mask)
            if mob_hits:
                self.playing = False
                
            #check if player hits a platform only if falling
            if self.player.vel.y >0:
                hits = pg.sprite.spritecollide(self.player, self.platforms, False)
                if hits:
                    lowest = hits[0]
                    for hit in hits:
                        if hit.rect.bottom > lowest.rect.bottom:
                            lowest = hit
                    if self.player.pos.x < lowest.rect.right + 10 and \
                       self.player.pos.x > lowest.rect.left :
                       if self.player.pos.y < lowest.rect.centery:
                        self.player.pos.y = lowest.rect.top
                        self.player.vel.y = 0
                        self.player.jumping = False
                        
             # if player reaches top 1/4 of sccreen
            if self.player.rect.top <= HEIGHT /4 :
                if random.randrange(100) < 15:
                    Cloud(self)
                self.player.pos.y += max(abs(self.player.vel.y), 2)
                for cloud in self.clouds:
                    cloud.rect.y += max(abs(self.player.vel.y / 2),2)
                for mob in self.mobs:
                    mob.rect.y += max(abs(self.player.vel.y), 2)
                for plat in self.platforms:
                    plat.rect.y += max(abs(self.player.vel.y), 2)
                    if plat.rect.top >= HEIGHT:
                        plat.kill()
                        self.score += 10

             # if player hits powerup
            pow_hits = pg.sprite.spritecollide(self.player, self.powerups, True)
            for pow in pow_hits:
                if pow.type =='boost':
                    self.boost_sound.play()
                    self.player.vel.y = -BOOST_POWER
                    self.player.jumping = False
                    
             #die
            if self.player.rect.bottom > HEIGHT:
                for sprite in self.all_sprites:
                    sprite.rect.y -= max(self.player.vel.y, 10)
                    if sprite.rect.bottom < 0:
                        sprite.kill()
            if len(self.platforms) == 0:
                self.playing = False
                

            # spawn new platforms to keep same average number platforms
            while len(self.platforms) < 6:
                width = random.randrange(50, 100)
                Platform(self, random.randrange(0, WIDTH-width),
                         random.randrange(-75, -30))
                

        def events(self):
            #game loop - events
            for event in pg.event.get():
            #check for closing window
             if event.type == pg.QUIT:
                 if self.playing:
                     self.playing = False
                 self.running = False
             if event.type == pg.KEYDOWN:
                  if event.key == pg.K_SPACE:
                      self.player.jump()
                      
             if event.type == pg.KEYUP:
                  if event.key == pg.K_SPACE:
                        self.player.jump_cut()

        def draw(self):
            # game loop- draw
            self.screen.fill(BGCOLOR)
            self.all_sprites.draw(self.screen)
            self.draw_text(str(self.score), 22,WHITE, WIDTH / 2, 15)
            # *after* drawing everything ,flip the display
            pg.display.flip()


        def show_start_screen(self):
            #game splash/start screen
            pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.wav'))
            pg.mixer.music.play(loops=-1)
            
            frontimg = pg.image.load(path.join(img_dir,'front1.jpg')).convert()
            frontimg_rect = frontimg.get_rect()
            gameDisplay.blit(frontimg, frontimg_rect)
            #self.screen.fill(BGCOLOR)
            self.draw_text(TITLE, 48, RED, WIDTH / 2, HEIGHT / 4)
            self.draw_text("Arrows to move,space to jump", 22, BLACK,WIDTH / 2,HEIGHT / 2)
            self.draw_text("Press any key to play", 22, BLACK, WIDTH / 2, HEIGHT * 3 /4)
            self.draw_text("High score : " + str(self.highscore), 22, BLACK, WIDTH / 2, 15)            
            pg.display.flip()
            self.wait_for_key()
            pg.mixer.music.fadeout(500)

        def show_go_screen(self):
            #game over/continue
            if not self.running:
                return
            pg.mixer.music.load(path.join(self.snd_dir, 'Yippee.wav'))
            pg.mixer.music.play(loops=-1)
            backimg = pg.image.load(path.join(img_dir,'gameover.jpg')).convert()
            backimg_rect = backimg.get_rect()
            gameDisplay.blit(backimg, backimg_rect)
            #self.screen.fill(BGCOLOR)
            self.draw_text("Game over", 48,WHITE, WIDTH / 2, HEIGHT / 4)
            self.draw_text("Score :" + str(self.score), 22, WHITE,WIDTH / 2,HEIGHT / 2)
            self.draw_text("Press any key to play", 22, WHITE, WIDTH / 2, HEIGHT * 3 /4)
            if self.score > self.highscore:
                self.highscore = self.score
                self.draw_text("NEW HIGH SCORE", 22,WHITE, WIDTH / 2, HEIGHT / 2 +40)
                with open(path.join(self.dir, HS_FILE), 'w') as f:
                    f.write(str(self.score))
            else:
                self.draw_text("High score: " + str(self.highscore), 22, WHITE, WIDTH / 2, HEIGHT / 2 +40)
            pg.display.flip()
            self.wait_for_key()
            pg.mixer.music.fadeout(500)

        def wait_for_key(self):
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        self.runnin = False
                    if event.type == pg.KEYUP:
                        waiting = False
                


        
            
        def draw_text(self, text, size, color, x, y):
            font = pg.font.Font(self.font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            text_rect.midtop = (x,y)
            self.screen.blit(text_surface,text_rect)
        
    g=Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.show_go_screen()

    pg.quit()
    quit()


def cargame():
    import pygame
    import time
    import random

    pygame.init()
    pygame.mixer.init()


    display_width = 840
    display_height = 650
    car_width = 23
    car_height = 47


    black = (0,0,0)
    white = (255,255,255)
    red = (200,0,0)
    green = (0,200,0)

    bright_red = (255, 0, 0)
    bright_green = (0, 255, 0)

    gameDisplay = pygame.display.set_mode((display_width, display_height))
    pygame.display.set_caption('Car Game')
    clock = pygame.time.Clock()

    carImg = pygame.image.load('car2.png')


    back_img = pygame.image.load('background-1.png')
    back_img_rect = back_img.get_rect()
    front_img = pygame.image.load('sri.jpg')
    front_img_rect = front_img.get_rect()

    car_images = []
    car_list = ['car1.png','car3.png','car4.jpg','car5.jpg','car6.jpg','car7.jpg',
                'car8.jpg','car9.jpg','car10.jpg','car11.jpg','car12.jpg','car13.jpg']
    for img in car_list:
        car_images.append(pygame.image.load(img))


    crash_sound = pygame.mixer.Sound('crash2.wav')


    pause = False

    def things_dodged(count):
        font = pygame.font.SysFont(None, 60)
        text = font.render("SCORE:"+str(count), True, red)
        gameDisplay.blit(text, (display_width / 2 - 85,0))
        

    def car(x,y):
        gameDisplay.blit(carImg,(x,y))

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    ##def message_display(text,x,y):
    ##    largeText = pygame.font.Font('freesansbold.ttf',115)
    ##    TextSurf, TextRect = text_objects(text, largeText)
    ##    TextRect.center = ((x / 2 ),(y/ 2))
    ##    gameDisplay.blit(TextSurf, TextRect)
    ##
    ##    pygame.display.update()
    ##    
    ##    time.sleep(2)
    ##    game_loop()
    ##    

    def crash():

        pygame.mixer.music.stop()
        pygame.mixer.Sound.play(crash_sound)
        pygame.mixer.music.load('Racing-Menu.mp3')
        pygame.mixer.music.set_volume(0.6)
        pygame.mixer.music.play(-1)
        crash = True
        while crash:
            for event in pygame.event.get():
            # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #gameDisplay.fill(white)
            #gameDisplay.blit(front_img, front_img_rect)
            largeText = pygame.font.Font('freesansbold.ttf',80)
            TextSurf, TextRect = text_objects('YOU CRASHED',largeText)
            
            TextRect.center = ((display_width / 2),(display_height / 2 - 180))
            gameDisplay.blit(TextSurf, TextRect)
            button("Play Again",299,280,110,50,green,bright_green,game_loop)
            button("Quit",430,280,110,50,red,bright_red,quitgame)
            button("Back",378,350,70,35,yellow,bright_yellow,beginpage)
            
            
            pygame.display.update()
            clock.tick(15)



    def button(msg,x,y,w,h,ic,ac,action = None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        #print(click)
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(gameDisplay, ac, (x,y,w,h))
            if click[0] == 1 and action != None:
                action()
    ##            if action == "play":
    ##                game_loop()
    ##            elif action == "quit":
    ##                pygame.quit()
    ##                quit()


        else:
            pygame.draw.rect(gameDisplay, ic, (x,y,w,h))

        smallText = pygame.font.Font('freesansbold.ttf',20)
        textSurf,textRect = text_objects(msg, smallText)
        textRect.center =((x +(w/2)),(y+(h/2)))
        gameDisplay.blit(textSurf, textRect)



           
    def unpause():
        global pause
        pygame.mixer.music.unpause()
        pause = False
        
    def paused():
        pygame.mixer.music.pause()
        while pause:
            
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            #gameDisplay.fill(white)
            gameDisplay.blit(front_img, front_img_rect)
            largeText = pygame.font.Font('freesansbold.ttf',80)
            TextSurf, TextRect = text_objects("Paused", largeText)
            TextRect.center = ((display_width / 2 - 100),(display_height / 2 - 120))
            gameDisplay.blit(TextSurf, TextRect)
            
            button("Continue",680,200,100,50,green,bright_green,unpause)
            button("Quit",680,280,100,50,red,bright_red,quitgame)
            
            
            pygame.display.update()
            clock.tick(15)

    def quitgame():
        pygame.quit()
        quit()

    def game_intro():
        pygame.mixer.music.load('music2.mp3')
        pygame.mixer.music.play(-1)
        intro = True
        while intro:
            
            
            for event in pygame.event.get():
                # print(event)
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(white)
            gameDisplay.blit(front_img, front_img_rect)
            largeText = pygame.font.Font('freesansbold.ttf',80)
            TextSurf, TextRect = text_objects("A BIT RACEY", largeText)
            TextRect.center = ((display_width / 2 - 100),(display_height / 2 - 120))
            gameDisplay.blit(TextSurf, TextRect)
            button("GO!",680,200,150,35,green,bright_green,game_loop)
            button("INSTRUCTIONS",680,245,150,35,yellow,bright_yellow,inst3)
            button("QUIT",680,290,150,35,red,bright_red,quitgame)
            
            
            pygame.display.update()
            clock.tick(15)

    def inst3():
        inst3 = True
        while inst3:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            gameDisplay.fill(white)
            gameDisplay.blit(inst_img2,inst_img_rect2)
            button("BACK",400,500,70,35,yellow,bright_yellow,cargame)
            button("PLAY",400,450,70,35,green,bright_green,game_loop)

        
        
            pygame.display.update()
            clock.tick(15)
        

    def game_loop():
        global pause
        pygame.mixer.music.load('carrace.mp3') 
        pygame.mixer.music.play(-1)
        
        x = (display_width * 0.488)
        y = (display_height * 0.8)

        x_change = 0
        thing_img = random.choice(car_images)
        thing_img.set_colorkey(black)
        thing_img_rect = thing_img.get_rect()
        
        t_img2= random.choice(car_images)
        t_img2_rect = t_img2.get_rect()

        t_img3= random.choice(car_images)
        t_img3_rect = t_img3.get_rect()

        t_img4= random.choice(car_images)
        t_img4_rect = t_img4.get_rect()
            

        thing_img_rect.x = random.randrange(139, 260)
        t_img2_rect.x= random.randrange(280, 400)
        t_img3_rect.x = random.randrange(420, 540) 
        t_img4_rect.x = random.randrange(560, 680)
        thing_img_rect.y= -600
        t_img2_rect.y = -400
        t_img2_rect.y = -1000
        t_img2_rect.y  = -300
        thing_speed = random.randrange(7,20)
        thing_speed2=random.randrange(6,12)
        thing_speed3 = random.randrange(8,16)
        thing_speed4 = random.randrange(4,15)
        thing_width = 30
        thing_height = 30

        score = 0
        maxlives = 3
        gameExit = False
        while not gameExit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x_change = -5
                    if event.key == pygame.K_RIGHT:
                        x_change = 5
                    if event.key == pygame.K_p:
                        pause = True
                        paused()

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        x_change = 0 

            x += x_change

            gameDisplay.fill(white)
            gameDisplay.blit(back_img,back_img_rect)
            gameDisplay.blit(thing_img,thing_img_rect)
            thing_img_rect.y += thing_speed
            
            gameDisplay.blit(t_img2,t_img2_rect)
            t_img2_rect.y += thing_speed2
            gameDisplay.blit(t_img3,t_img3_rect)
            t_img3_rect.y += thing_speed3
            gameDisplay.blit(t_img4,t_img4_rect)
            t_img4_rect.y += thing_speed4
            
            
            car(x, y)
            things_dodged(score)
            
            

            if x > display_width - 159 or x < 139:
                crash()


            if thing_img_rect.y > display_height:
                thing_img= random.choice(car_images)
                thing_img.set_colorkey(black)
                thing_img_rect = thing_img.get_rect()
                thing_img_rect.y = 0 - thing_height
                thing_img_rect.x = random.randrange(139, 260)
                thing_speed = random.randrange(7, 25)
                score += 10
                
            if t_img2_rect.y > display_height:
                t_img2= random.choice(car_images)
                t_img2_rect = t_img2.get_rect()
                t_img2_rect.y = 0 - thing_height
                t_img2_rect.x = random.randrange(280, 400)
                thing_speed2 = random.randrange(9, 25)
                score += 10
                
            if t_img3_rect.y > display_height:
                t_img3= random.choice(car_images)
                t_img3_rect = t_img3.get_rect()
                t_img3_rect.y = 0 - thing_height
                t_img3_rect.x = random.randrange(420, 540)
                thing_speed3 = random.randrange(8, 22)
                score += 10
                
            if t_img4_rect.y > display_height:
                t_img4= random.choice(car_images)
                t_img4_rect = t_img4.get_rect()
                t_img4_rect.y = 0 - thing_height
                t_img4_rect.x = random.randrange(560, 680)
                thing_speed4 = random.randrange(9, 23)
                score += 10
                
            
            if y < thing_img_rect.y + thing_height and y + car_height > thing_img_rect.y:
                if (x > thing_img_rect.x and x < thing_img_rect.x + thing_width) or (x + car_width > thing_img_rect.x and x + car_width< thing_img_rect.x + thing_width):
                    crash()
                    
            if y < t_img2_rect.y + thing_height and y + car_height > t_img2_rect.y:
                if (x > t_img2_rect.x and x < t_img2_rect.x + thing_width) or (x + car_width> t_img2_rect.x  and x + car_width< t_img2_rect.x + thing_width):
                    crash()
            
            if y < t_img3_rect.y + thing_height and y + car_height > t_img3_rect.y:
                if (x > t_img3_rect.x and x < t_img3_rect.x + thing_width) or (x + car_width> t_img3_rect.x  and x + car_width< t_img3_rect.x + thing_width):
                    crash()
                
            if y < t_img4_rect.y + thing_height and y + car_height  > t_img4_rect.y:
                if (x > t_img4_rect.x and x < t_img4_rect.x + thing_width) or (x + car_width > t_img4_rect.x and x + car_width< t_img4_rect.x + thing_width):
                    #crash()
                    print(iam)


                     
            pygame.display.update()
            clock.tick(60)




                    
           
    game_intro()
    game_loop()
    pygame.quit()
    quit()

    

        
def ballgame_intro():
    ballintro = True
    while ballintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(backtile_img1,backtile_img_rect1)
        largeText = pygame.font.Font('freesansbold.ttf',60)
        TextSurf, TextRect = text_objects("BALL VS BALL",largeText)
        TextRect.center = ((display_width / 2  ),(display_height / 2 ))
        gameDisplay.blit(TextSurf, TextRect)
        button("GO",450,470,100,35,green,bright_green,ballgame)
        button("Instructions",580,470,130,35,yellow,bright_yellow,ballgameinst)
        button("Quit",740,470,100,35,red,bright_red,quitgame)

        pygame.display.update()
        
        clock.tick(15)


def ballgameinst():
    inst = True
    while inst:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(inst_img,inst_img_rect)
        button("BACK",750,100,70,35,yellow,bright_yellow,ballgame_intro)
        button("PLAY",750,50,70,35,green,bright_green,ballgame)

        
        
        pygame.display.update()
        clock.tick(15)
        
def ballgame():
    ## A bubble shooter game built with pygame.
## Music by Steven O'Brien



    import math, pygame, sys, os, copy, time, random
    import pygame.gfxdraw
    
    ## Constants, yo ##

    FPS          = 120
    WINDOWWIDTH  = 640
    WINDOWHEIGHT = 480
    TEXTHEIGHT   = 20
    BUBBLERADIUS = 20
    BUBBLEWIDTH  = BUBBLERADIUS * 2
    BUBBLELAYERS = 5
    BUBBLEYADJUST = 5
    STARTX = WINDOWWIDTH / 2
    STARTY = WINDOWHEIGHT - 27
    ARRAYWIDTH = 16
    ARRAYHEIGHT = 14


    RIGHT = 'right'
    LEFT  = 'left'
    BLANK = '.'

    ## COLORS ##

    #            R    G    B
    GRAY     = (100, 100, 100)
    NAVYBLUE = ( 60,  60, 100)
    WHITE    = (255, 255, 255)
    RED      = (255,   0,   0)
    GREEN    = (  0, 255,   0)
    BLUE     = (  0,   0, 255)
    YELLOW   = (255, 255,   0)
    ORANGE   = (255, 128,   0)
    PURPLE   = (255,   0, 255)
    CYAN     = (  0, 255, 255)
    BLACK    = (  0,   0,   0)
    COMBLUE  = (233, 232, 255)

    BGCOLOR    = WHITE
    COLORLIST = [RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN]
         

    class Bubble(pygame.sprite.Sprite):
        def __init__(self, color, row=0, column=0):
            pygame.sprite.Sprite.__init__(self)

            self.rect = pygame.Rect(0, 0, 30, 30)
            self.rect.centerx = STARTX
            self.rect.centery = STARTY
            self.speed = 10
            self.color = color
            self.radius = BUBBLERADIUS
            self.angle = 0
            self.row = row
            self.column = column
            
        def update(self):

            if self.angle == 90:
                xmove = 0
                ymove = self.speed * -1
            elif self.angle < 90:
                xmove = self.xcalculate(self.angle)
                ymove = self.ycalculate(self.angle)
            elif self.angle > 90:
                xmove = self.xcalculate(180 - self.angle) * -1
                ymove = self.ycalculate(180 - self.angle)
            

            self.rect.x += xmove
            self.rect.y += ymove


        def draw(self):
            pygame.gfxdraw.filled_circle(DISPLAYSURF, self.rect.centerx, self.rect.centery, self.radius, self.color)
            pygame.gfxdraw.aacircle(DISPLAYSURF, self.rect.centerx, self.rect.centery, self.radius, GRAY)
            


        def xcalculate(self, angle):
            radians = math.radians(angle)
            
            xmove = math.cos(radians)*(self.speed)
            return xmove

        def ycalculate(self, angle):
            radians = math.radians(angle)
            
            ymove = math.sin(radians)*(self.speed) * -1
            return ymove




    class Arrow(pygame.sprite.Sprite):
        def __init__(self):
            pygame.sprite.Sprite.__init__(self)

            self.angle = 90
            arrowImage = pygame.image.load('Arrow.png')
            arrowImage.convert_alpha()
            arrowRect = arrowImage.get_rect()
            self.image = arrowImage
            self.transformImage = self.image
            self.rect = arrowRect
            self.rect.centerx = STARTX 
            self.rect.centery = STARTY
            


        def update(self, direction):
            
            if direction == LEFT and self.angle < 180:
                self.angle += 2
            elif direction == RIGHT and self.angle > 0:        
                self.angle -= 2

            self.transformImage = pygame.transform.rotate(self.image, self.angle)
            self.rect = self.transformImage.get_rect()
            self.rect.centerx = STARTX 
            self.rect.centery = STARTY

            
        def draw(self):
            DISPLAYSURF.blit(self.transformImage, self.rect)


    class Score(object):
        def __init__(self):
            self.total = 0
            self.font = pygame.font.SysFont('Times new roman', 15)
            self.render = self.font.render('Score: ' + str(self.total), True, BLACK, WHITE)
            self.rect = self.render.get_rect()
            self.rect.left = 5
            self.rect.bottom = WINDOWHEIGHT - 5
            
            
        def update(self, deleteList):
            self.total += ((len(deleteList)) * 10)
            self.render = self.font.render('Score: ' + str(self.total), True, BLACK, WHITE)

        def draw(self):
            DISPLAYSURF.blit(self.render, self.rect)



    def main():
        global FPSCLOCK, DISPLAYSURF, DISPLAYRECT, MAINFONT
        pygame.init()
        FPSCLOCK = pygame.time.Clock()
        pygame.display.set_caption('Puzzle Bobble')
        MAINFONT = pygame.font.SysFont('Helvetica', TEXTHEIGHT)
        DISPLAYSURF, DISPLAYRECT = makeDisplay()
        
        

        while True:
            score, winorlose = runGame()
            endScreen(score, winorlose)



    def runGame():
        musicList =['bgmusic.ogg', 'Utopian_Theme.ogg', 'Goofy_Theme.ogg']
        pygame.mixer.music.load(musicList[0])
        pygame.mixer.music.play()
        track = 0
        gameColorList = copy.deepcopy(COLORLIST)
        direction = None
        launchBubble = False
        newBubble = None
        
        
        
        arrow = Arrow()
        bubbleArray = makeBlankBoard()
        setBubbles(bubbleArray, gameColorList)
        
        nextBubble = Bubble(gameColorList[0])
        nextBubble.rect.right = WINDOWWIDTH - 5
        nextBubble.rect.bottom = WINDOWHEIGHT - 5

        score = Score()
        
        
        
       
        while True:
            frontpage = pygame.image.load('image/bubble1.jpg')
            frontpage_rect = frontpage.get_rect()
            DISPLAYSURF.blit(frontpage, frontpage_rect)

            
            
            #DISPLAYSURF.fill(BGCOLOR)
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                    
                elif event.type == KEYDOWN:
                    if (event.key == K_LEFT):
                        direction = LEFT
                    elif (event.key == K_RIGHT):
                        direction = RIGHT
                        
                elif event.type == KEYUP:
                    direction = None
                    if event.key == K_SPACE:
                        launchBubble = True
                    elif event.key == K_ESCAPE:
                        terminate()

            if launchBubble == True:
                if newBubble == None:
                    newBubble = Bubble(nextBubble.color)
                    newBubble.angle = arrow.angle
                    

                newBubble.update()
                newBubble.draw()
                
                
                if newBubble.rect.right >= WINDOWWIDTH - 5:
                    newBubble.angle = 180 - newBubble.angle
                elif newBubble.rect.left <= 5:
                    newBubble.angle = 180 - newBubble.angle


                launchBubble, newBubble, score = stopBubble(bubbleArray, newBubble, launchBubble, score)

                finalBubbleList = []
                for row in range(len(bubbleArray)):
                    for column in range(len(bubbleArray[0])):
                        if bubbleArray[row][column] != BLANK:
                            finalBubbleList.append(bubbleArray[row][column])
                            if bubbleArray[row][column].rect.bottom > (WINDOWHEIGHT - arrow.rect.height - 10):
                                return score.total, 'lose'

                
                
                if len(finalBubbleList) < 1:
                    return score.total, 'win'
                                            
                            
                
                gameColorList = updateColorList(bubbleArray)
                random.shuffle(gameColorList)
                
                        
                                
                if launchBubble == False:
                    
                    nextBubble = Bubble(gameColorList[0])
                    nextBubble.rect.right = WINDOWWIDTH - 5
                    nextBubble.rect.bottom = WINDOWHEIGHT - 5

            
            
                                
            nextBubble.draw()
            if launchBubble == True:
                coverNextBubble()
            
            arrow.update(direction)
            arrow.draw()


            
            setArrayPos(bubbleArray)
            drawBubbleArray(bubbleArray)

            score.draw()

            if pygame.mixer.music.get_busy() == False:
                if track == len(musicList) - 1:
                    track = 0
                else:
                    track += 1

                pygame.mixer.music.load(musicList[track])
                pygame.mixer.music.play()

                
            
            pygame.display.update()
            FPSCLOCK.tick(FPS)




    def makeBlankBoard():
        array = []
        
        for row in range(ARRAYHEIGHT):
            column = []
            for i in range(ARRAYWIDTH):
                column.append(BLANK)
            array.append(column)

        return array




    def setBubbles(array, gameColorList):
        for row in range(BUBBLELAYERS):
            for column in range(len(array[row])):
                random.shuffle(gameColorList)
                newBubble = Bubble(gameColorList[0], row, column)
                array[row][column] = newBubble 
                
        setArrayPos(array)





    def setArrayPos(array):
        for row in range(ARRAYHEIGHT):
            for column in range(len(array[row])):
                if array[row][column] != BLANK:
                    array[row][column].rect.x = (BUBBLEWIDTH * column) + 5
                    array[row][column].rect.y = (BUBBLEWIDTH * row) + 5

        for row in range(1, ARRAYHEIGHT, 2):
            for column in range(len(array[row])):
                if array[row][column] != BLANK:
                    array[row][column].rect.x += BUBBLERADIUS
                    

        for row in range(1, ARRAYHEIGHT):
            for column in range(len(array[row])):
                if array[row][column] != BLANK:
                    array[row][column].rect.y -= (BUBBLEYADJUST * row)

        deleteExtraBubbles(array)



    def deleteExtraBubbles(array):
        for row in range(ARRAYHEIGHT):
            for column in range(len(array[row])):
                if array[row][column] != BLANK:
                    if array[row][column].rect.right > WINDOWWIDTH:
                        array[row][column] = BLANK



    def updateColorList(bubbleArray):
        newColorList = []

        for row in range(len(bubbleArray)):
            for column in range(len(bubbleArray[0])):
                if bubbleArray[row][column] != BLANK:
                    newColorList.append(bubbleArray[row][column].color)

        colorSet = set(newColorList)

        if len(colorSet) < 1:
            colorList = []
            colorList.append(WHITE)
            return colorList

        else:

            return list(colorSet)
        
        



    def checkForFloaters(bubbleArray):
        bubbleList = [column for column in range(len(bubbleArray[0]))
                             if bubbleArray[0][column] != BLANK]

        newBubbleList = []

        for i in range(len(bubbleList)):
            if i == 0:
                newBubbleList.append(bubbleList[i])
            elif bubbleList[i] > bubbleList[i - 1] + 1:
                newBubbleList.append(bubbleList[i])

        copyOfBoard = copy.deepcopy(bubbleArray)

        for row in range(len(bubbleArray)):
            for column in range(len(bubbleArray[0])):
                bubbleArray[row][column] = BLANK
        

        for column in newBubbleList:
            popFloaters(bubbleArray, copyOfBoard, column)



    def popFloaters(bubbleArray, copyOfBoard, column, row=0):
        if (row < 0 or row > (len(bubbleArray)-1)
                    or column < 0 or column > (len(bubbleArray[0])-1)):
            return
        
        elif copyOfBoard[row][column] == BLANK:
            return

        elif bubbleArray[row][column] == copyOfBoard[row][column]:
            return

        bubbleArray[row][column] = copyOfBoard[row][column]
        

        if row == 0:
            popFloaters(bubbleArray, copyOfBoard, column + 1, row    )
            popFloaters(bubbleArray, copyOfBoard, column - 1, row    )
            popFloaters(bubbleArray, copyOfBoard, column,     row + 1)
            popFloaters(bubbleArray, copyOfBoard, column - 1, row + 1)

        elif row % 2 == 0:
            popFloaters(bubbleArray, copyOfBoard, column + 1, row    )
            popFloaters(bubbleArray, copyOfBoard, column - 1, row    )
            popFloaters(bubbleArray, copyOfBoard, column,     row + 1)
            popFloaters(bubbleArray, copyOfBoard, column - 1, row + 1)
            popFloaters(bubbleArray, copyOfBoard, column,     row - 1)
            popFloaters(bubbleArray, copyOfBoard, column - 1, row - 1)

        else:
            popFloaters(bubbleArray, copyOfBoard, column + 1, row    )
            popFloaters(bubbleArray, copyOfBoard, column - 1, row    )
            popFloaters(bubbleArray, copyOfBoard, column,     row + 1)
            popFloaters(bubbleArray, copyOfBoard, column + 1, row + 1)
            popFloaters(bubbleArray, copyOfBoard, column,     row - 1)
            popFloaters(bubbleArray, copyOfBoard, column + 1, row - 1)
            


    def stopBubble(bubbleArray, newBubble, launchBubble, score):
        deleteList = []
        popSound = pygame.mixer.Sound('popcork.ogg')
        
        for row in range(len(bubbleArray)):
            for column in range(len(bubbleArray[row])):
                
                if (bubbleArray[row][column] != BLANK and newBubble != None):
                    if (pygame.sprite.collide_rect(newBubble, bubbleArray[row][column])) or newBubble.rect.top < 0:
                        if newBubble.rect.top < 0:
                            newRow, newColumn = addBubbleToTop(bubbleArray, newBubble)
                            
                        elif newBubble.rect.centery >= bubbleArray[row][column].rect.centery:

                            if newBubble.rect.centerx >= bubbleArray[row][column].rect.centerx:
                                if row == 0 or (row) % 2 == 0:
                                    newRow = row + 1
                                    newColumn = column
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow - 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                    
                                else:
                                    newRow = row + 1
                                    newColumn = column + 1
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow - 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                                        
                            elif newBubble.rect.centerx < bubbleArray[row][column].rect.centerx:
                                if row == 0 or row % 2 == 0:
                                    newRow = row + 1
                                    newColumn = column - 1
                                    if newColumn < 0:
                                        newColumn = 0
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow - 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                else:
                                    newRow = row + 1
                                    newColumn = column
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow - 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                    
                                
                        elif newBubble.rect.centery < bubbleArray[row][column].rect.centery:
                            if newBubble.rect.centerx >= bubbleArray[row][column].rect.centerx:
                                if row == 0 or row % 2 == 0:
                                    newRow = row - 1
                                    newColumn = column
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow + 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                else:
                                    newRow = row - 1
                                    newColumn = column + 1
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow + 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                
                            elif newBubble.rect.centerx <= bubbleArray[row][column].rect.centerx:
                                if row == 0 or row % 2 == 0:
                                    newRow = row - 1
                                    newColumn = column - 1
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow + 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn
                                    
                                else:
                                    newRow = row - 1
                                    newColumn = column
                                    if bubbleArray[newRow][newColumn] != BLANK:
                                        newRow = newRow + 1
                                    bubbleArray[newRow][newColumn] = copy.copy(newBubble)
                                    bubbleArray[newRow][newColumn].row = newRow
                                    bubbleArray[newRow][newColumn].column = newColumn


                        popBubbles(bubbleArray, newRow, newColumn, newBubble.color, deleteList)
                        
                        
                        if len(deleteList) >= 3:
                            for pos in deleteList:
                                popSound.play()
                                row = pos[0]
                                column = pos[1]
                                bubbleArray[row][column] = BLANK
                            checkForFloaters(bubbleArray)
                            
                            score.update(deleteList)

                        launchBubble = False
                        newBubble = None

        return launchBubble, newBubble, score

                        

    def addBubbleToTop(bubbleArray, bubble):
        posx = bubble.rect.centerx
        leftSidex = posx - BUBBLERADIUS

        columnDivision = math.modf(float(leftSidex) / float(BUBBLEWIDTH))
        column = int(columnDivision[1])

        if columnDivision[0] < 0.5:
            bubbleArray[0][column] = copy.copy(bubble)
        else:
            column += 1
            bubbleArray[0][column] = copy.copy(bubble)

        row = 0
        

        return row, column
        
        


    def popBubbles(bubbleArray, row, column, color, deleteList):
        if row < 0 or column < 0 or row > (len(bubbleArray)-1) or column > (len(bubbleArray[0])-1):
            return

        elif bubbleArray[row][column] == BLANK:
            return
        
        elif bubbleArray[row][column].color != color:
            return

        for bubble in deleteList:
            if bubbleArray[bubble[0]][bubble[1]] == bubbleArray[row][column]:
                return

        deleteList.append((row, column))

        if row == 0:
            popBubbles(bubbleArray, row,     column - 1, color, deleteList)
            popBubbles(bubbleArray, row,     column + 1, color, deleteList)
            popBubbles(bubbleArray, row + 1, column,     color, deleteList)
            popBubbles(bubbleArray, row + 1, column - 1, color, deleteList)

        elif row % 2 == 0:
            
            popBubbles(bubbleArray, row + 1, column,         color, deleteList)
            popBubbles(bubbleArray, row + 1, column - 1,     color, deleteList)
            popBubbles(bubbleArray, row - 1, column,         color, deleteList)
            popBubbles(bubbleArray, row - 1, column - 1,     color, deleteList)
            popBubbles(bubbleArray, row,     column + 1,     color, deleteList)
            popBubbles(bubbleArray, row,     column - 1,     color, deleteList)

        else:
            popBubbles(bubbleArray, row - 1, column,     color, deleteList)
            popBubbles(bubbleArray, row - 1, column + 1, color, deleteList)
            popBubbles(bubbleArray, row + 1, column,     color, deleteList)
            popBubbles(bubbleArray, row + 1, column + 1, color, deleteList)
            popBubbles(bubbleArray, row,     column + 1, color, deleteList)
            popBubbles(bubbleArray, row,     column - 1, color, deleteList)
                


    def drawBubbleArray(array):
        for row in range(ARRAYHEIGHT):
            for column in range(len(array[row])):
                if array[row][column] != BLANK:
                    array[row][column].draw()


                        

    def makeDisplay():
        DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        DISPLAYRECT = DISPLAYSURF.get_rect()
        DISPLAYSURF.fill(BGCOLOR)
        DISPLAYSURF.convert()
        pygame.display.update()

        return DISPLAYSURF, DISPLAYRECT
        
     
    def terminate():
        pygame.quit()
        quit()


    def coverNextBubble():
        whiteRect = pygame.Rect(0, 0, BUBBLEWIDTH, BUBBLEWIDTH)
        whiteRect.bottom = WINDOWHEIGHT
        whiteRect.right = WINDOWWIDTH
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, whiteRect)



    def endScreen(score, winorlose):
        endFont = pygame.font.SysFont('Times new roman', 29)
        endMessage1 = endFont.render('You ' + winorlose + '! Your Score is ' + str(score) + '. Press Enter to Play Again.', True, WHITE )
        endMessage1Rect = endMessage1.get_rect()
        

        endPage = pygame.image.load('image/bubbles6.jpg')
        endPage_rect = endPage.get_rect()
        windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
        windowSurface.blit(endPage, endPage_rect)
        DISPLAYSURF.blit(endMessage1, endMessage1Rect)
        pygame.display.update()

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    terminate()
                elif event.type == KEYUP:
                    if event.key == K_RETURN:
                        return
                    elif event.key == K_ESCAPE:
                        terminate()
            
            
    if __name__ == '__main__':
        main()


def tilegame_intro():
    tileintro = True
    while tileintro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
        gameDisplay.fill(white)
        gameDisplay.blit(backtile_img,backtile_img_rect)
        button("GO",700,100,150,35,green,bright_green,tilegame)
        button("INSTRUCTIONS",700,145,150,35,yellow,bright_yellow,inst5)
        button("Quit",700,190,150,35,red,bright_red,quitgame)

        pygame.display.update()
        
        clock.tick(15)

def inst5():
    inst5 = True
    while inst5:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        gameDisplay.fill(white)
        gameDisplay.blit(inst_img4,inst_img_rect4)
        button("BACK",300,500,70,35,yellow,bright_yellow,tilegame_intro)
        button("PLAY",470,500,70,35,green,bright_green,tilegame)

        
        
        pygame.display.update()
        clock.tick(15)
   
def tilegame():
    #TILE MAP DEMO
    import pygame as pg
    import sys
    from random import choice, random
    from os import path
    import tilessettings
    import tilessprites
    import tilemap






    #HUD functions
    def draw_player_health(surf, x, y, pct):
        if pct < 0:
            pct = 0
        BAR_LENGTH = 100
        BAR_HEIGHT = 20
        fill = pct * BAR_LENGTH
        outline_rect = pg.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
        fill_rect = pg.Rect(x, y, fill, BAR_HEIGHT)
        if pct > 0.6:
            col = GREEN
        elif pct > 0.3:
            col = YELLOW
        else:
            col = RED
        pg.draw.rect(surf, col, fill_rect)
        pg.draw.rect(surf, WHITE, outline_rect, 2)

    class Game:
        def __init__(self):
            pg.mixer.pre_init(44100, -16, 1, 2048)
            pg.init()
            self.screen = pg.display.set_mode((1024, 768))
            pg.display.set_caption(TITLE)
            self.clock = pg.time.Clock()
            pg.key.set_repeat(500, 100)
            self.load_data()
            self.running = True

        def draw_text(self, text, font_name, size, color, x, y, align="nw"):
            font = pg.font.Font(font_name, size)
            text_surface = font.render(text, True, color)
            text_rect = text_surface.get_rect()
            if align == "nw":
                text_rect.topleft = (x, y)
            if align == "ne":
                text_rect.topright = (x, y)
            if align == "sw":
                text_rect.bottomleft = (x, y)
            if align == "se":
                text_rect.bottomright = (x, y)
            if align == "n":
                text_rect.midtop = (x, y)
            if align == "s":
                text_rect.midbottom = (x, y)
            if align == "e":
                text_rect.midright = (x, y)
            if align == "w":
                text_rect.midleft = (x, y)
            if align == "center":
                text_rect.center = (x, y)
            self.screen.blit(text_surface, text_rect)
            
        def load_data(self):
            mazegame_folder = path.dirname(__file__)
            img_folder = path.join(mazegame_folder, 'img')
            snd_folder = path.join(mazegame_folder, 'snd')
            music_folder = path.join(mazegame_folder, 'music')
            self.map_folder = path.join(mazegame_folder, 'maps')
            self.title_font = path.join(img_folder, 'ZOMBIE.TTF')
            self.hud_font = path.join(img_folder, 'Impacted2.0.ttf')
            self.dim_screen = pg.Surface(self.screen.get_size()).convert_alpha()
            self.dim_screen.fill((0, 0, 0, 180))
            self.player_img = pg.image.load(path.join(img_folder, PLAYER_IMG)).convert_alpha()
            self.bullet_images = {}
            self.bullet_images['lg'] = pg.image.load(path.join(img_folder, BULLET_IMG)).convert_alpha()
            self.bullet_images['sm'] = pg.transform.scale(self.bullet_images['lg'], (10, 10))
            self.mob_img = pg.image.load(path.join(img_folder, MOB_IMG)).convert_alpha()
            self.wall_img = pg.image.load(path.join(img_folder, WALL_IMG)).convert_alpha()                
            self.wall_img = pg.transform.scale(self.wall_img, (TILESIZE, TILESIZE))
            self.splat = pg.image.load(path.join(img_folder, SPLAT)).convert_alpha()
            self.splat = pg.transform.scale(self.splat, (64, 64))
            self.gun_flashes = []
            for img in MUZZLE_FLASHES:
                self.gun_flashes.append(pg.image.load(path.join(img_folder, img)).convert_alpha())
            self.item_images = {}
            for item in ITEM_IMAGES:
                self.item_images[item] = pg.image.load(path.join(img_folder, ITEM_IMAGES[item])).convert_alpha()
            # Sound loading
            pg.mixer.music.load(path.join(music_folder, BG_MUSIC))
            self.effects_sounds = {}
            for type in EFFECTS_SOUNDS:
                self.effects_sounds[type] = pg.mixer.Sound(path.join(snd_folder, EFFECTS_SOUNDS[type]))
            self.weapon_sounds = {}
            for weapon in WEAPON_SOUNDS:
                self.weapon_sounds[weapon] = []
                for snd in WEAPON_SOUNDS[weapon]:
                    s = pg.mixer.Sound(path.join(snd_folder, snd))
                    s.set_volume(0.3)
                    self.weapon_sounds[weapon].append(s)
            self.zombie_moan_sounds = []
            for snd in ZOMBIE_MOAN_SOUNDS:
                s = pg.mixer.Sound(path.join(snd_folder,snd))
                s.set_volume(0.2)
                self.zombie_moan_sounds.append(s)
            self.player_hit_sounds = []
            for snd in PLAYER_HIT_SOUNDS:
                self.player_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd)))  
            self.zombie_hit_sounds = []
            for snd in ZOMBIE_HIT_SOUNDS:
                self.zombie_hit_sounds.append(pg.mixer.Sound(path.join(snd_folder, snd))) 

        def new(self):
            #initilaise all variables and do all the setup for a new game
            self.all_sprites = pg.sprite.LayeredUpdates()
            self.walls = pg.sprite.Group()
            self.mobs = pg.sprite.Group()
            self.bullets = pg.sprite.Group()
            self.items = pg.sprite.Group()
            self.map = TiledMap(path.join(self.map_folder, 'tiled2.tmx'))
            self.map_img = self.map.make_map()
            self.map_rect = self.map_img.get_rect()
            #for row, tiles in enumerate(self.map.data):
                #for col, tile in enumerate(tiles):
                    #if tile == '1':
                        #Wall(self, col, row)
                    #if tile == 'M':
                        #Mob(self, col, row)
                    #if tile == 'P':
                        #self.player = Player(self, col, row)
            for tile_object in self.map.tmxdata.objects:
                obj_center = vec(tile_object.x + tile_object.width / 2,
                                 tile_object.y + tile_object.height / 2)
                
                if tile_object.name == 'player':
                    self.player = Player1(self, obj_center.x, obj_center.y)
                if tile_object.name == 'zoimbie':
                    Mob1(self, obj_center.x, obj_center.y)
                if tile_object.name == 'wall':
                    Obstacle(self, tile_object.x, tile_object.y,
                             tile_object.width, tile_object.height)
                if tile_object.name in['health', 'shotgun']:
                    Item(self, obj_center, tile_object.name)
            self.camera = Camera(self.map.width, self.map.height)
            self.draw_debug = False
            self.paused = False
            self.effects_sounds['level_start'].play()
                
                

        def run(self):
            #game loop - set self.playing = false to the game
            self.playing = True
            pg.mixer.music.play(loops=-1)
            while self.playing:
                self.dt = self.clock.tick(FPS) / 1000
                self.events()
                if not self.paused:
                    self.update()
                self.draw()

        def quit(self):
            pg.quit()
            quit()

        def update(self):
            #update portion of the game loop
            self.all_sprites.update()
            self.camera.update(self.player)
            # game over
            if len(self.mobs) == 0:
                self.playing = False
                
            
            #player hits items
            hits = pg.sprite.spritecollide(self.player, self.items, False)
            for hit in hits:
                if hit.type == 'health' and self.player.health < PLAYER_HEALTH:
                    hit.kill()
                    self.effects_sounds['health_up'].play()
                    self.player.add_health(HEALTH_PACK_AMOUNT)
                if hit.type == 'shotgun':
                    hit.kill()
                    self.effects_sounds['gun_pickup'].play()
                    self.player.weapon = 'shotgun'
                    

            # mobs hit player
            hits = pg.sprite.spritecollide(self.player, self.mobs, False, collide_hit_rect)
            for hit in hits:
                if random() < 0.7:
                    choice(self.player_hit_sounds).play()
                self.player.health -= MOB_DAMAGE
                hit.vel = vec(0, 0)
                if self.player.health <=0:
                    self.playing = False
                if hits:
                    self.player.hit()
                    self.player.pos += vec(MOB_KNOCKBACK, 0).rotate(-hits[0].rot)
            # bullets hit mobs
            hits = pg.sprite.groupcollide(self.mobs, self.bullets, False, True)
            for mob in hits:
                #hit.health -= WEAPONS[self.player.weapon]['damage'] * len(hits[hit])
                for bullet in hits[mob]:
                    mob.health -= bullet.damage
                mob.vel = vec(0, 0)

        def draw_grid(self):
            for x in range(0, 1024, TILESIZE):
                pg.draw.line(self.screen, LIGHTGREY, (x,0), (x, 768))
            for y in range(0, 768, TILESIZE):
                pg.draw.line(self.screen, LIGHTGREY, (0,y), (1024, y))
            

        def draw(self):
            pg.display.set_caption("{:.2f}".format(self.clock.get_fps()))
            #self.screen.fill(BGCOLOR)
            self.screen.blit(self.map_img, self.camera.apply_rect(self.map_rect))
            #self.draw_grid()
            for sprite in self.all_sprites:
                if isinstance(sprite, Mob1):
                    sprite.draw_health()
                self.screen.blit(sprite.image, self.camera.apply(sprite))
                if self.draw_debug:
                    pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(sprite.hit_rect), 1)
            if self.draw_debug:
                for wall in self.walls:
                    pg.draw.rect(self.screen, CYAN, self.camera.apply_rect(wall.rect), 1)
                    
            #pg.draw.rect(self.screen, WHITE, self.player.hit_rect, 2)
            #HUD functions
            draw_player_health(self.screen, 10, 10, self.player.health / PLAYER_HEALTH)
            self.draw_text('Zombies: {}'.format(len(self.mobs)), self.hud_font, 30, WHITE,
                            1024 - 10, 10, align="ne")
            if self.paused:
                self.screen.blit(self.dim_screen, (0, 0))
                self.draw_text("PAUSED", self.title_font, 105, RED, 1024 / 2, 768/ 2, align="nw")
            pg.display.flip()

       
       
        def events(self):
            #catch all events here
            for event in pg.event.get():
                #check for closing window
                if event.type == pg.QUIT:
                    quitgame()
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_ESCAPE:
                        quitgame()
                    if event.key == pg.K_h:
                        self.draw_debug = not self.draw_debug
                    if event.key == pg.K_p:
                        self.paused = not self.paused

        def show_start_screen(self):
            #game splash/start screen
            pass
        def show_go_screen(self):
            #game over/continue
            self.screen.fill(BLACK)
            self.draw_text("GAME OVER", self.title_font, 100, RED,
                            1024 / 2,768 / 2, align="center")
            self.draw_text("Press a key to start", self.title_font, 75, WHITE,
                             1024 / 2, 768 * 3 / 4, align="center")
            pg.display.flip()
            self.wait_for_key()

        def wait_for_key(self):
            pg.event.wait()
            waiting = True
            while waiting:
                self.clock.tick(FPS)
                for event in pg.event.get():
                    if event.type == pg.QUIT:
                        waiting = False
                        quitgame()
                    if event.type == pg.KEYUP:
                        waiting = False
        
    g = Game()
    g.show_start_screen()
    while g.running:
        g.new()
        g.run()
        g.show_go_screen()

    pg.quit()
    quit()

    
    
    
def rollgame():
    import tkinter as tk  # use tk namespace for Tkinter items
    import random
    import pygame as pg
    def create_dice():
        """
        create the dice canvas list as dice[0] to dice[6]
        """
        dice = []
        dice.append(draw_dice('dot0'))   # empty
        dice.append(draw_dice('dot5'))   # center dot --> 1
        dice.append(draw_dice('dot4', 'dot6'))
        dice.append(draw_dice('dot3', 'dot5', 'dot7'))
        dice.append(draw_dice('dot1', 'dot3', 'dot7', 'dot9'))
        dice.append(draw_dice('dot1', 'dot3', 'dot5', 'dot7', 'dot9'))
        dice.append(draw_dice('dot1', 'dot3', 'dot4', 'dot6', 'dot7', 'dot9'))
        return dice
    def draw_dice(*arg):
        """
        draws the 7 different dice dots on the canvas
        """
        w = 200
        h = 200
        c = tk.Canvas(root, width=w+30, height=h+30)
        my_image = PhotoImage(file='C:\\Users\\dell\\Desktop\\Sri Harshitha\\game project\\linkinggames\\lavatube.gif')    
        c.create_image(0, 0, anchor = NW, image = my_image)
        c.my_image = my_image
                   
        # set the dot specs
        x = 20
        y = 20
        r = 50
        if 'dot1' in arg:
            dot1 = c.create_oval(x, y, x+r, y+r, fill='black')
        x = w/2
        x = 180
        if 'dot3' in arg:
            dot3 = c.create_oval(x, y, x+r, y+r, fill='black')
        x = 20
        y = h/2
        if 'dot4' in arg:
            dot4 = c.create_oval(x, y, x+r, y+r, fill='black')
        x = w/2
        if 'dot5' in arg:
            dot5 = c.create_oval(x, y, x+r, y+r, fill='black')
        x = 180
        if 'dot6' in arg:
            dot6 = c.create_oval(x, y, x+r, y+r, fill='black')
        x = 20
        y = 180
        if 'dot7' in arg:
            dot7 = c.create_oval(x, y, x+r, y+r, fill='black')
        x = w/2
        x = 180
        if 'dot9' in arg:
            dot9 = c.create_oval(x, y, x+r, y+r, fill='black')
        if 'dot0' in arg:
            pass
        return c
    def click():
        """
        display a randomly selected dice value
        """
        # start with a time delay of 100 ms and increase it as the dice rolls
        t = 100
        stop = random.randint(13, 18)
        for x in range(stop):
            dice_index = x%6 + 1
            root.title(str(dice_index))  # test
            dice_list[dice_index].grid(row=1, column=0, pady=5)
            root.update()
            if x == stop-1:
                # final result available via var1.get()
                var1.set(str(x%6 + 1))
                if(x%6 + 1 == 5):
                    shooting_intro()
                elif(x%6 + 1 == 2):
                    picturepuzzle()
                elif(x%6 + 1 == 3):
                    jumpy()
                elif(x % 6 + 1 == 4):
                    cargame()
                elif(x % 6 + 1 == 1):
                    ballgame_intro()
                elif(x % 6 + 1 == 6):
                    tilegame_intro()
                    
                
                break
            root.after(t, dice_list[dice_index].grid_forget())
            t += 25
        
    # create the window form
    root = tk.Tk()

    # StringVar() updates result label automatically
    var1 = tk.StringVar()
    # set initial value
    var1.set("")
    # create the result label
    result = tk.Label(root, textvariable=var1, fg='red')
    result.grid(row=3, column=0, columnspan=3)
    dice_list = create_dice()
    # start with an empty canvas
    dice_list[0].grid(row=1, column=0, pady=5)
    button1 = tk.Button(root, text="Press me", command=click)
    button1.grid(row=2, column=0, pady=3)
    # start of program event loop
    root.mainloop()


game_intro()
