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
        button("GO",420,220,100,50,green,bright_green,game_loop)
        button("Quit",420,300,100,50,red,bright_red,quitgame)

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
        button("PLAY AGAIN",display_width/2 -75,350,150,50,green,bright_green,game_intro)
        button("QUIT",display_width/2 - 35,430,70,50,red,bright_red,quitgame) 
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
