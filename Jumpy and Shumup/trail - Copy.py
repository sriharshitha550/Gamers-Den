# select a dice image at random using Tkinter
# tested with Python24     vegaseat      23dec2006

import tkinter as tk  # use tk namespace for Tkinter items
import random
import pygame
from os import path 

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
    c = tk.Canvas(root, width=w+30, height=h+30, bg='yellow')
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
            if (x%6 +1 == 1):
                game1()
            break
        root.after(t, dice_list[dice_index].grid_forget())
        t += 25

def game1():
    # shmup game
# Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3
# Art from Kenny

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
