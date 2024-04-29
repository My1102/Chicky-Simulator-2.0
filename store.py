import pygame
import sys
from button import Button

pygame.init()



width, height = 900, 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chicky Simulator')
background_image = pygame.image.load('graphic/bgimg.png')
sword = pygame.image.load("graphic/sword.png")
shield = pygame.image.load("graphic/shield.png")
potion = pygame.image.load("graphic/potion.png")
font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
coin = 100



def market():
    on = True
    
    while on:
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()
        times =1
        

        #EQUIPMENT DIsPLAY
        screen.blit(sword,(75,35))
        screen.blit(shield,(390,35))
        screen.blit(potion,(710,35))
        #################

        #PRICE
        #####sword####
        price_text = font.render(f"{50}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,215))
        screen.blit(price_text, text_rect)
        ######Shield######
        price_text = font.render(f"{60}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,215))
        screen.blit(price_text, text_rect)
        ######potion######
        price_text = font.render(f"{30}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,215))
        screen.blit(price_text, text_rect)


        #BUTTONS
        buy_button1 = Button('graphic/botton1.png', 150, 300, 1, "BUY")
        buy_button1.draw(screen)
        buy_button2 = Button('graphic/botton1.png', 450, 300, 1, "BUY")
        buy_button2.draw(screen)
        buy_button3 = Button('graphic/botton1.png', 750, 300, 1, "BUY")
        buy_button3.draw(screen)
        #########
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    # if   times >= 1:
                        print("You bought a sword.")
                    #     times = times -1
                    # if times < 1:
                        # print("You already have one.")
                        

                if buy_button2.check_input(pos_mouse):
                    print("You bought a shield.")
                if buy_button3.check_input(pos_mouse):
                    print("You bought a potion.")

        pygame.display.flip()

    pygame.quit()
    sys.exit()

market()
