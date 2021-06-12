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
        button("GO!",680,200,100,50,green,bright_green,game_loop)
        button("Quit",680,280,100,50,red,bright_red,quitgame)
        
        
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
