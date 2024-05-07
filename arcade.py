import pygame
import sys
import pygame_gui
import os
from button import Button
from random import randint
from main import chick

def arcade() :
    width, height = 500, 500
    screen = pygame.display.set_mode((width,height))
    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    pygame.display.set_caption('Chicky Simulator - Level 3')
    board2 = pygame.image.load('graphic/10x10map.jpg')
    Manager = pygame_gui.UIManager((width,height))
    UI_REFRESH_RATE = clock.tick(60)/1000
    tile_size=50
    

    time = 0
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    clock = pygame.time.Clock()

    class coin():
        x = 0
        y = 0
        step = 50
 
        def __init__(self,x,y):
            self.x = x * self.step
            self.y = y * self.step
 
        def draw(self, surface, image):
            surface.blit(image,(self.x, self.y))

    class chicken() :
        
        def __init__(self,x,y):
            chic = pygame.image.load('graphic/kunchic.png')
            self.image = pygame.transform.scale(chic,(50,50))
            self.rect = self.image.get_rect(center=(25,25))
            self.rect.x = x
            self.rect.y = y

        def update(self):
            dx = 0
            dy = 0

            key = pygame.key.get_pressed()
            if key[pygame.K_w]:
                dy -= 3
                if self.rect.y<0 :
                    self.rect.y=0
            if key[pygame.K_a]:
                dx -= 3
                if self.rect.x<0 :
                    self.rect.x=0
            if key[pygame.K_s]:
                dy += 3
                if self.rect.y>450 :
                    self.rect.y=450
            if key[pygame.K_d]:
                dx += 3
                if self.rect.x>450 :
                    self.rect.x=450
    while on == True :

        screen.blit(board2,(0,0))


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT + 1:
                time += 1

            Manager.process_events(event)

        timer_text = font.render(f"{time}", True, (255,255,255))
        text_rect = timer_text.get_rect(center = (width//2,50))
        screen.blit(timer_text, text_rect)