import pygame
import sys
from button import Button

pygame.init()



width, height = 900, 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chicky Simulator')
background_image = pygame.image.load('graphic/bgimg.png')
font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)


def store():
    on = True
    buy = False
    sword = pygame.image.load("graphic/sword.png")
    shield = pygame.image.load("graphic/shield.png")
    bow = pygame.image.load("graphic/bow.png")
    x_bow = pygame.image.load("graphic/x-bow.png")
    hammer= pygame.image.load("graphic/hammer.png")
    axe= pygame.image.load("graphic/axe.png")
                               
    while on:
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #EQUIPMENT DIsPLAY
        screen.blit(sword,(75,35))
        screen.blit(shield,(390,35))
        screen.blit(bow,(680,35))
        screen.blit(x_bow,(75,370))
        screen.blit(hammer,(390,370))
        screen.blit(axe,(680,370))
        #################

        #PRICE
        #####sword####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,215))
        screen.blit(price_text, text_rect)
        ######Shield######
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,215))
        screen.blit(price_text, text_rect)
        ######bow######
        price_text = font.render(f"{75}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,215))
        screen.blit(price_text, text_rect)
        ####x-bow#####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,215))
        screen.blit(price_text, text_rect)
        ######hammer#####        
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,215))
        screen.blit(price_text, text_rect)
        #######axe#########        
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,215))
        screen.blit(price_text, text_rect)


        #BUTTONS
        buy_button1 = Button('graphic/botton1.png', 150, 300, 1, "BUY")
        buy_button1.draw(screen)
        buy_button2 = Button('graphic/botton1.png', 450, 300, 1, "BUY")
        buy_button2.draw(screen)
        buy_button3 = Button('graphic/botton1.png', 750, 300, 1, "BUY")
        buy_button3.draw(screen)
        buy_button4 = Button('graphic/botton1.png', 150, 600, 1, "BUY")
        buy_button4.draw(screen)
        buy_button5 = Button('graphic/botton1.png', 450, 600, 1, "BUY")
        buy_button5.draw(screen)
        buy_button6 = Button('graphic/botton1.png', 750, 600, 1, "BUY")
        buy_button6.draw(screen)
        #########
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    if buy :
                        buy = False
                    else :
                        buy = True                                        
                        
                if buy_button2.check_input(pos_mouse):
                    if buy :
                        buy = False
                    else :
                        buy = True      
                if buy_button3.check_input(pos_mouse):
                    if buy :
                        buy = False
                    else :
                        buy = True
                if buy_button4.check_input(pos_mouse):
                    if buy :
                        buy = False
                    else :
                        buy = True                                        
                        
                if buy_button5.check_input(pos_mouse):
                    if buy :
                        buy = False
                    else :
                        buy = True      
                if buy_button6.check_input(pos_mouse):
                    if buy :
                        buy = False
                    else :
                        buy = True            

        if buy :
            bought()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

def bought() :
    surface =  pygame.Surface((width,height))
    surface.blit(background_image,(0,0))
    surface.blit(font.render('You bought an item.',True,'white'),(100,150))
    surface.blit(font.render('Click anywhere to go back.',True,'white'),(100,200))
    screen.blit(surface,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            store()
        if event.type == pygame.quit:
            pygame.quit()
            sys.exit()

    pygame.display.flip()

store()
