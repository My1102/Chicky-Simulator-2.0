# *********************************************************
# Program: main.py
# Course: PSP0101 PROBLEM SOLVING AND PROGRAM DESIGN
# Class: TL10-7
# Year: 2023/24 Trimester 1
# Names: LIM MIN YUEN | TAN JIA YING | TAN PUO LIN
# IDs: 1221107408 | 1221107413 | 1221169360
# Emails: 1221107408@student.mmu.edu.my | 1221107413@student.mmu.edu.my | 1221169360@student.mmu.edu.my
# Phones: 010-5268328 | 012-9331640 | 012-9873238
# *********************************************************

# The things we changed / added
# 1.Caution for the steps counter 
# 2.Navigation between lvl 
# 3.Our explanation comment

# importing libraries 
import pygame
import sys
import pygame_gui
import random
import os
from pyvidplayer2 import Video
from button import Button # library by my
from rank import Ranking # library by my
from lock import Lock # library by my
from backpack import Item, Slot, Info
from os import path
import pickle


pygame.init()

FFMPEG_PATH = 'ffmpeg-7.0-essentials_build/ffmpeg-7.0-essentials_build/bin'
os.environ['PATH'] += os.pathsep + FFMPEG_PATH

# program setup / screen display
width, height = 900, 700
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Chicky Simulator')
background_image = pygame.image.load('graphic/bgimg.png')
ranking_image = pygame.image.load('graphic/garden.png')
level_image = pygame.image.load('graphic/garden.png')
clock = pygame.time.Clock()
Manager = pygame_gui.UIManager((width,height))
UI_REFRESH_RATE = clock.tick(60)/1000
font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)

# let user enter their username and password (using pygame_gui manager) - by my
# learn from tutorial
username_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,320), (300,50)), manager = Manager, object_id = '#username')
password_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,450), (300,50)), manager = Manager, object_id = '#password')

# added later
def caution(lvl, username, coin, pull, c, equip, stats):
    while True:
        #program setup / screen display
        pygame.display.set_caption('Chicky Simulator - Caution')
        screen.blit(level_image, (0,0))

        w, h = 600, 400
        caution = pygame.image.load('graphic/caution.PNG')
        caution = pygame.transform.scale(caution,(w,h))
        caution_rect = caution.get_rect(center = (width/2, height/2))
        screen.blit(caution, caution_rect)

        next_button = Button('graphic/botton1.png', 630, 470, 0.6, ">>")
        next_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        #checking for user events 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.check_input(pos_mouse):
                    tutorial2(lvl, username, coin, pull, c, equip, stats)

                if back_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def tutorial1(lvl, username, coin, pull, c, equip, stats):
    while True:
        #program setup / screen display
        pygame.display.set_caption('Chicky Simulator - Tutorial')
        screen.blit(level_image, (0,0))

        w, h = 600, 400
        tuto1 = pygame.image.load('graphic/tuto1.PNG')
        tuto1 = pygame.transform.scale(tuto1,(w,h))
        tuto1_rect = tuto1.get_rect(center = (width/2, height/2))
        screen.blit(tuto1, tuto1_rect)

        next_button = Button('graphic/botton1.png', 630, 470, 0.6, ">>")
        next_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        #checking for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.check_input(pos_mouse):
                    caution(lvl, username, coin, pull, c, equip, stats)

                if back_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()        


def tutorial2(lvl, username, coin, pull, c, equip, stats):
    while True:
        #program setup /screen display
        pygame.display.set_caption('Chicky Simulator - Tutorial')
        screen.blit(level_image, (0,0))

        w, h = 600, 400
        tuto2 = pygame.image.load('graphic/tuto2.PNG')
        tuto2 = pygame.transform.scale(tuto2,(w,h))
        tuto2_rect = tuto2.get_rect(center = (width/2, height/2))
        screen.blit(tuto2, tuto2_rect)

        start_button = Button('graphic/button2.png', 620, 470, 0.2, "START")
        start_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        #checking for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_input(pos_mouse):
                    leveltest(lvl, username, coin, pull, c, equip, stats)

                if back_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()   


def tutorial4(lvl, username, coin, pull, c, equip, stats):
    #screen display / program setup
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator - Tutorial')
    screen.blit(level_image, (0,0))
    
    while True:

        w, h = 600, 400
        tuto4 = pygame.image.load('graphic/tuto4.PNG')
        tuto4 = pygame.transform.scale(tuto4,(w,h))
        tuto4_rect = tuto4.get_rect(center = (width/2, height/2))
        screen.blit(tuto4, tuto4_rect)

        start_button = Button('graphic/button2.png', 620, 475, 0.2, "START")
        start_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        #checking for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_input(pos_mouse):
                    level3(lvl, username, coin, pull, c, equip, stats)

                if back_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

        pygame.display.update()   


def tutorial3(lvl, username, coin, pull, c, equip, stats):
    #screen display / program setup
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator - Toutorial')
    screen.blit(level_image, (0,0))    
    
    while True:

        w, h = 600, 400
        tuto3 = pygame.image.load('graphic/tuto3.PNG')
        tuto3 = pygame.transform.scale(tuto3,(w,h))
        tuto3_rect = tuto3.get_rect(center = (width/2, height/2))
        screen.blit(tuto3, tuto3_rect)

        start_button = Button('graphic/button2.png', 620, 475, 0.2, "START")
        start_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        #checking for user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if start_button.check_input(pos_mouse):
                    level2(lvl, username, coin, pull, c, equip, stats)

                if back_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

        pygame.display.update()   


def leveltest(lvl, username, coin, pull, c, equip, stats):
    width, height = 900, 700
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator')
    background_image = pygame.image.load('graphic/map.jpg')
    pygame.transform.scale(background_image,(700,700))
    ranking_image = pygame.image.load('graphic/garden.png')
    level_image = pygame.image.load('graphic/garden.png')
    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    clock = pygame.time.Clock()
    Manager = pygame_gui.UIManager((width,height))
    UI_REFRESH_RATE = clock.tick(60)
    # info = pygame.image.load('graphic/brown.png')
    # pygame.transform.scale(info,(200,700))

    red = (255,0,0)
    green = (0, 255, 0)

    tile_size = 35
    gameover = 0
    lvl = 1
    maxlevel = 30
   
    
    username_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,320), (300,50)), manager = Manager, object_id = '#username')
    password_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,450), (300,50)), manager = Manager, object_id = '#password')

    time = 0
    fps = 60
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    clock = pygame.time.Clock()
    time_use =[]

    def reset_level(lvl):
        
        jy_group.empty()
        yuen_group.empty()
        puolin_group.empty()

        if path.exists(f'level{lvl}_data'):
            pickle_in = open(f'level{lvl}_data', 'rb')
            world_data = pickle.load(pickle_in)
        world = World(world_data)

        return world

    class chicky():
        def __init__(self,x,y,max_hp,damage,cd):
            # chic = pygame.image.load(c)
            # self.image = pygame.transform.scale(chic,(30,30))
            self.images_right = []
            self.images_left = []
            self.index = 0
            self.counter = 0
            for num in range(1, 6):
                img_right = pygame.image.load(f'graphic/chickytest/{num}.png')
                img_right = pygame.transform.scale(img_right, (30, 30))
                img_left = pygame.transform.flip(img_right, True, False)
                self.images_right.append(img_right)
                self.images_left.append(img_left)
                print(f"Loaded image {num}.png")

                
            self.image = self.images_right[self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.max_hp = max_hp
            self.hp = max_hp
            self.damage = damage
            self.cd = cd
            self.last_attack_time = 0
            self.direction = 0

        def attack(self):
            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time > self.cd:
                # Perform attack
                for yuen in pygame.sprite.spritecollide(self, yuen_group, False):
                    yuen.hp -= self.damage
                    print(yuen.hp)
                for jy in pygame.sprite.spritecollide(self, jy_group, False):
                    jy.hp -= self.damage
                for puolin in pygame.sprite.spritecollide(self, puolin_group, False):
                    puolin.hp -= self.damage
                # Set last attack time
                self.last_attack_time = current_time


        def update(self,gameover):
            dx = 0 
            dy = 0 
            walk_cooldown = 0
            

            if gameover == 0:
                key = pygame.key.get_pressed()
                if key[pygame.K_w]:
                    dy -= 3
                    #self.counter += 1
                    # if self.rect.y<0 :
                    #     self.rect.y=0
                if key[pygame.K_a]:
                    dx -= 3
                    self.counter += 1
                    self.direction = -1
                    # if self.rect.x<0 :
                    #     self.rect.x=0
                        
                if key[pygame.K_s]:
                    dy += 3
                    # self.counter += 1
                    # if self.rect.y>height :
                    #     self.rect.y=height

                if key[pygame.K_d]:
                    dx += 3
                    self.counter += 1
                    # print(self.images_right)
                    self.direction = 1 
                    # if self.rect.x>width :
                    #     self.rect.x=width

                if key[pygame.K_SPACE]:
                    Chicky.attack()

                if key[pygame.K_LEFT] == False and key[pygame.K_RIGHT] == False:
                    self.counter = 0
                    self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

                
                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index +- 1
                    if self.index >= len(self.images_right):
                        self.index = 0
                    if self.direction == 1:
                        self.image = self.images_right[self.index]
                    if self.direction == -1:
                        self.image = self.images_left[self.index]

               

                
                # collision with blocks
                for item in world.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        dx = 0
                        dy = 0
                # collision with coins
                for item in world.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        world.coin_list.remove(item)
                        if world.coin_list == [] :
                            # set timer stop 
                            pygame.time.set_timer(pygame.USEREVENT, 0)
                            # save in list 
                            time_use.append(time)
                            gameover = 1
                            # win(c,lvl,username,coin)
                            
                # collision with monsters
                # for yuen in pygame.sprite.spritecollide(Chicky, yuen_group, False):
                
                #     Chicky.hp -= yuen.damage
                    
                # for jy in pygame.sprite.spritecollide(Chicky, jy_group, False):
                    
                #     Chicky.hp -= jy.damage
                # for puolin in pygame.sprite.spritecollide(Chicky, puolin_group, False):
                    
                #     Chicky.hp -= puolin.damage
                # if pygame.sprite.spritecollide(self, yuen_group, False):
        
                #     self.hp -= yuen.damage
                # elif pygame.sprite.spritecollide(self, jy_group, False):
                    
                #     self.hp -= jy.damage
                # elif pygame.sprite.spritecollide(self, puolin_group, False):
                    
                #     self.hp -= puolin.damage
                # if self.hp <= 0:
                #     gameover = -1    

                # return gameover 

                # if pygame.sprite.spritecollide(self,yuen_group,False):
                #     # gameover = -1
                #     key = pygame.key.get_pressed()
                #     if key[pygame.K_SPACE]:
                #         yuen_group.update.hp -= self.damage
                # if pygame.sprite.spritecollide(self,jy_group,False):
                #     gameover = -1
                # if pygame.sprite.spritecollide(self,puolin_group,False):
                #     gameover = -1

            elif gameover == -1 :
                self.rect.x = 35
                self.rect.y = 35
            
            self.rect.x += dx
            self.rect.y += dy

            screen.blit(self.image,self.rect)

            return gameover
        
    class HealthBar():
        def __init__(self,x,y,hp,max_hp):
            self.x = x
            self.y =y 
            self.hp = hp
            self.max_hp = max_hp

        def draw(self,hp):
            self.hp = hp
            ratio = self.hp/self.max_hp
            pygame.draw.rect(screen,red,(self.x,self.y,60,200))
            pygame.draw.rect(screen,green,(self.x,self.y,60,200*ratio))
            
    
    class World():
        def __init__(self,data):
            self.block_list = [ ] 
            self.coin_list = [ ] 


            block = pygame.image.load('graphic/block.png')
            coin = pygame.image.load('graphic/coin.png')

            row_count = 0
            for row in data:
                col_count = 0
                for tile in row:
                    if tile == 1 :
                        block = pygame. transform. scale(block, (tile_size, tile_size))
                        block_rect = block.get_rect()
                        block_rect.x = col_count * tile_size
                        block_rect.y = row_count * tile_size
                        item = (block, block_rect) 
                        self.block_list.append(item) 
                    if tile == 2 :
                        coin = pygame. transform. scale(coin, (tile_size, tile_size))
                        coin_rect = block.get_rect()
                        coin_rect.x = col_count * tile_size
                        coin_rect.y = row_count * tile_size
                        item = (coin, coin_rect)
                        self.coin_list.append(item)
                        
                    if tile == 3 :
                        yuen = Monster1(col_count * tile_size,row_count * tile_size,100,100,15,5)
                        yuen_group.add(yuen)
                        
                    if tile == 4 :
                        jy = Monster3(col_count * tile_size,row_count * tile_size,75,75,30)
                        jy_group.add(jy)

                    if tile == 5 :
                        puolin = Monster2(col_count * tile_size,row_count * tile_size,150,150,5)
                        puolin_group.add(puolin)

                    # if tile == 6:
                    #     exit = Exit(col_count * tile_size, row_count * tile_size - (tile_size // 2))
                    #     exit_group.add(exit)
                    col_count += 1
                row_count += 1
        def draw(self):
            for item in self.block_list:
                screen.blit(item[0],item[1]) 
            for item in self.coin_list:
                screen.blit(item[0],item[1])

    class Monster1(pygame.sprite.Sprite):
        def __init__(self,x,y,hp,max_hp,damage,cd):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster1.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0
            self.hp = hp
            self.max_hp = max_hp
            self.damage = damage
            self.cd = cd
            self.last_attack_time = 0
            
        def update(self,hp,max_hp,damage):
            current_time = pygame.time.get_ticks()
            self.rect.x += self.move_direction
            self.move_counter += 1
            if self.move_counter > 100 :
                self.move_direction *= -1
                self.move_counter *= -1
            self.hp = hp
            self.max_hp = max_hp
            self.damage = damage
            if current_time - self.last_attack_time > self.cd:
                for yuen in pygame.sprite.spritecollide(Chicky, yuen_group, False):
                    Chicky.hp -= self.damage
                    
            ratio = self.hp/self.max_hp
            pygame.draw.rect(screen,red,(self.rect.x ,self.rect.y -5 ,35,5))
            pygame.draw.rect(screen,green,(self.rect.x*ratio ,self.rect.y -5 ,35,5))
            
            # if pygame.sprite.collide_rect(self,Chicky):
            #     Chicky.hp -= yuen_group.damage
                

    class Monster2(pygame.sprite.Sprite):
        def __init__(self,x,y,hp,max_hp,damage):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster2.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.hp = hp
            self.max_hp = max_hp
            self.damage = damage

        def update(self,hp,max_hp,damage):
            self.hp = hp
            self.max_hp = max_hp
            self.damage = damage
            ratio = self.hp/self.max_hp
            pygame.draw.rect(screen,red,(self.rect.x ,self.rect.y -5 ,35,5))
            pygame.draw.rect(screen,green,(self.rect.x ,self.rect.y -5 ,35*ratio,5))

    class Monster3(pygame.sprite.Sprite):
        def __init__(self,x,y,hp,max_hp,damage):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster3.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0
            self.hp = hp
            self.max_hp = max_hp
            self.damage = damage
            
        def update(self,hp,max_hp,damage):
            self.rect.y += self.move_direction
            self.move_counter += 1
            if self.move_counter > 250 :
                self.move_direction *= -1
                self.move_counter *= -1
            self.hp = hp
            self.max_hp = max_hp
            self.damage = damage
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen,red,(self.rect.x ,self.rect.y -5 ,35,5))
            pygame.draw.rect(screen,green,(self.rect.x ,self.rect.y -5 ,35*ratio,5))


    class Exit(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('graphic/bananacat.png')
            self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            
    Chicky = chicky(35,35,100,10,5)

    yuen_group = pygame.sprite.Group()
    puolin_group = pygame.sprite.Group()
    jy_group = pygame.sprite.Group()  
    exit_group = pygame.sprite.Group() 

    chicky_health_bar = HealthBar(750,200,Chicky.hp,Chicky.max_hp)
    

    if path.exists(f'level{lvl}_data'):
        pickle_in = open(f'level{lvl}_data', 'rb')
        world_data = pickle.load(pickle_in)
        print('yes im here')
    world = World(world_data)

    # restart_button = Button('graphic/button2.png', width // 2 - 50, height//2 + 100, 0.35, "restart")
    # start_button = Button('graphic/button2.png', width // 2 - 250, height // 2, 0.35,'start')
    # exit_button = Button('graphic/button2.png', width // 2 + 100, height // 2,0.35, 'exit')


    run = True
    while run:
        
        clock.tick(fps)
        screen.blit(background_image,(0,0))
        
        world.draw()
        gameover = Chicky.update(gameover)

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
        chicky_health_bar.draw(Chicky.hp)
        

        if gameover == 0:
            for jy in jy_group:
                jy.update(75,75,15)
            for yuen in yuen_group:
                yuen.update(100, 100, 10)
            for puolin in puolin_group:
                puolin.update(150, 150, 5)
            


        jy_group.draw(screen)
        yuen_group.draw(screen)
        puolin_group.draw(screen)
            # coin_group.draw(screen)
            # exit_group.draw(screen)

        if gameover == -1:
            # if restart_button.draw(screen):
                world_data = []
                world = reset_level(lvl)
                gameover = 0

        if gameover == 1:
            lvl += 1
            #reset game and go to next level
            
            if lvl <= maxlevel:
                
                #reset level
                world_data = []
                world = reset_level(lvl)
                Chicky = chicky(35,35,100,10,5)
                gameover = 0
                update_level(username, lvl)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


def level1(lvl, username, coin, pull, c, equip, stats): # This one easier to read
    # by 'Puo Puo'(Puo Lin) & Jia Ying
    import pygame as pg # change pygame to pg 

    # screen display / program setup
    width, height = 500, 500
    screen = pg.display.set_mode((width,height))
    font = pg.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    pg.display.set_caption('Chicky Simulator - Level 1')
    board2 = pg.image.load('graphic/10x10map.jpg')
    tile_size=50

    # timer part refers tutorial https://www.pygame.org/docs/ref/time.html#pygame.time.set_timer told by handsome Mr.Willie)
    time = 0
    pg.time.set_timer(pg.USEREVENT+1, 1000)
    clock = pg.time.Clock()
    time_use =[]
    
    while True:
        
        class chicky():
            def __init__(self,x,y):
                chic = pygame.image.load(c)
                self.image = pg.transform.scale(chic,(50,50))
                self.rect = self.image.get_rect(center=(25,25))
                self.rect.x = x
                self.rect.y = y

            def update(self):
                dx = 0 # Willie : teacher teacher what is this
                dy = 0 # Jy : Change in position of player, we nid this to do collision ltr

                key = pg.key.get_pressed()
                if key[pg.K_w]:
                    dy -= 3
                    if self.rect.y<0 :
                        self.rect.y=0
                if key[pg.K_a]:
                    dx -= 3
                    if self.rect.x<0 :
                        self.rect.x=0
                if key[pg.K_s]:
                    dy += 3
                    if self.rect.y>450 :
                        self.rect.y=450
                if key[pg.K_d]:
                    dx += 3
                    if self.rect.x>450 :
                        self.rect.x=450
                
                # collision with blocks
                for item in level.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        dx = 0
                        dy = 0
                # collision with coins
                for item in level.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        level.coin_list.remove(item)
                        if level.coin_list == [] :
                            # set timer stop 
                            pg.time.set_timer(pg.USEREVENT, 0)
                            # save in list 
                            time_use.append(time)
                            levl = 2 #added later  #for navigation in win - by my
                            win(lvl, username, levl, coin, pull, c, equip, stats)
                            
                # collision with monsters(This one jy use sprite collide becoz they are moving objects)
                if pg.sprite.spritecollide(self,yuen_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,jy_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,puolin_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                
                self.rect.x += dx
                self.rect.y += dy

                screen.blit(self.image,self.rect)

        # define fixed information(NPC/Blocks/Coin) - by jy
        class lvel():
            def __init__(self,data):
                self.block_list = [ ] 
                self.coin_list = [ ] 
                
                block = pg.image.load('graphic/block.png')
                coin = pg.image.load('graphic/coin.png')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1 :
                            block = pg. transform. scale(block, (tile_size, tile_size))
                            block_rect = block.get_rect()
                            block_rect.x = col_count * tile_size
                            block_rect.y = row_count * tile_size
                            item = (block, block_rect) 
                            self.block_list.append(item) 
                        if tile == 2 :
                            coin = pg. transform. scale(coin, (tile_size, tile_size))
                            coin_rect = block.get_rect()
                            coin_rect.x = col_count * tile_size
                            coin_rect.y = row_count * tile_size
                            item = (coin, coin_rect)
                            self.coin_list.append(item)
                            
                        if tile == 3 :
                            yuen = Monster1(col_count * tile_size,row_count * tile_size)
                            yuen_group.add(yuen)
                            
                        if tile == 4 :
                            jy = Monster3(col_count * tile_size,row_count * tile_size)
                            jy_group.add(jy)

                        if tile == 5 :
                            puolin = Monster2(col_count * tile_size,row_count * tile_size)
                            puolin_group.add(puolin)
                        col_count += 1
                    row_count += 1

            def draw(self):
                for item in self.block_list:
                    screen.blit(item[0],item[1]) 
                for item in self.coin_list:
                    screen.blit(item[0],item[1])

        # http://www.codingwithruss.com/pygame/sprite-class-and-sprite-groups-explained/ 
        # jy learned how to create sprite groups from this 
        class Monster1(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster1.png') 
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1
            # Willie : how u display this on screen u don't even write a funtion for display 
            # jy : sprite got build in draw funtion hehe
                    
        class Monster2(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster2.png') 
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                
        class Monster3(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster3.png') 
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.y += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        
        lvl1_data=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,1,1,0,1,1,1,0,0],
        [0,1,1,2,1,1,2,1,1,0],
        [0,1,2,0,1,0,0,2,1,0],
        [0,1,1,0,0,0,2,1,1,0],
        [0,0,1,1,0,0,1,1,0,0],
        [0,0,0,1,0,1,1,0,0,0],
        [0,0,0,0,2,1,0,0,0,0],
        [0,0,0,5,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]

        # user spawning point
        Chicky = chicky(0,0)
        # group created for collision use
        yuen_group = pg.sprite.Group()
        puolin_group = pg.sprite.Group()
        jy_group = pg.sprite.Group()  

        level = lvel(lvl1_data)

        # start program in loop
        on = True
        while on == True :

            screen.blit(board2,(0,0))

            level.draw() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    on = False
                    pygame.quit()
                    sys.exit()

                if event.type == pg.USEREVENT + 1:
                    time += 1

                Manager.process_events(event)
                    
            timer_text = font.render(f"{time}", True, (255,255,255))
            text_rect = timer_text.get_rect(center = (width//2,50))
            screen.blit(timer_text, text_rect)

            yuen_group.update()
            yuen_group.draw(screen)

            jy_group.update()
            jy_group.draw(screen)

            puolin_group.draw(screen)
            Chicky.update()
            
            clock.tick(60)
            pg.display.update()        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)
        pygame.display.update()


def level2(lvl, username, coin, pull, c, equip, stats):
    # by 'Puo Puo'(Puo Lin) & Jia Ying
    import pygame as pg #change pygame to pg 

    #screen display / program setup

    width, height = 500, 500
    screen = pg.display.set_mode((width,height))
    font = pg.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    pg.display.set_caption('Chicky Simulator - Level 2')
    board2 = pg.image.load('graphic/10x10map.jpg')
    tile_size=50

    time = 0
    pg.time.set_timer(pg.USEREVENT+1, 1000)
    clock = pg.time.Clock()
    time_use =[]
    
    while True:

        class chicky():
            def __init__(self,x,y):
                chic = pygame.image.load(c)
                self.image = pg.transform.scale(chic,(50,50))
                self.rect = self.image.get_rect(center=(25,25))
                self.rect.x = x
                self.rect.y = y

            def update(self):
                dx = 0
                dy = 0

                key = pg.key.get_pressed()
                if key[pg.K_w]:
                    dy -= 3
                    if self.rect.y<0 :
                        self.rect.y=0
                if key[pg.K_a]:
                    dx -= 3
                    if self.rect.x<0 :
                        self.rect.x=0
                if key[pg.K_s]:
                    dy += 3
                    if self.rect.y>450 :
                        self.rect.y=450
                if key[pg.K_d]:
                    dx += 3
                    if self.rect.x>450 :
                        self.rect.x=450
                
                #collision with blocks
                for item in level.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        dx = 0
                        dy = 0
                #collision with coins
                for item in level.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        level.coin_list.remove(item)
                        if level.coin_list == [] :
                            # make time stop
                            pg.time.set_timer(pg.USEREVENT, 0)
                            # save time
                            time_use.append(time)
                            levl = 3
                            win(lvl, username, levl, coin, pull, c, equip, stats)
                            
                #collision with monsters
                if pg.sprite.spritecollide(self,yuen_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,jy_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,puolin_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                
                self.rect.x += dx
                self.rect.y += dy

                screen.blit(self.image,self.rect)
        
        #define fixed information(NPC/Blocks/Coin)
        class lvel():
            def __init__(self,data):
                self.block_list = [ ] 
                self.coin_list = [ ] 


                block = pg.image.load('graphic/block.png')
                coin = pg.image.load('graphic/coin.png')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1 :
                            block = pg. transform. scale(block, (tile_size, tile_size))
                            block_rect = block.get_rect()
                            block_rect.x = col_count * tile_size
                            block_rect.y = row_count * tile_size
                            item = (block, block_rect) 
                            self.block_list.append(item) 
                        if tile == 2 :
                            coin = pg. transform. scale(coin, (tile_size, tile_size))
                            coin_rect = block.get_rect()
                            coin_rect.x = col_count * tile_size
                            coin_rect.y = row_count * tile_size
                            item = (coin, coin_rect)
                            self.coin_list.append(item)
                            
                        if tile == 3 :
                            yuen = Monster1(col_count * tile_size,row_count * tile_size)
                            yuen_group.add(yuen)
                            
                        if tile == 4 :
                            jy = Monster3(col_count * tile_size,row_count * tile_size)
                            jy_group.add(jy)

                        if tile == 5 :
                            puolin = Monster2(col_count * tile_size,row_count * tile_size)
                            puolin_group.add(puolin)
                        col_count += 1
                    row_count += 1

            def draw(self):
                for item in self.block_list:
                    screen.blit(item[0],item[1]) 
                for item in self.coin_list:
                    screen.blit(item[0],item[1])

        class Monster1(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster1.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1


        class Monster2(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster2.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                
        class Monster3(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster3.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.y += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        lvl2_data=[
        [0,0,0,0,0,0,3,0,0,0],
        [0,0,3,0,0,0,0,3,0,0],
        [0,0,0,0,0,0,3,0,0,0],
        [0,0,0,3,0,0,0,0,3,0],
        [3,0,0,0,3,0,0,0,0,3],
        [0,0,3,0,0,0,0,3,0,0],
        [0,0,0,0,0,3,0,0,0,2],
        [0,3,0,0,0,0,0,3,0,2],
        [0,0,0,0,0,0,0,0,0,2],
        [0,0,0,0,3,0,0,2,2,2]
        ] 
        #spawn point
        Chicky = chicky(0,0)
        #group for collision
        yuen_group = pg.sprite.Group()
        puolin_group = pg.sprite.Group()
        jy_group = pg.sprite.Group()  

        level = lvel(lvl2_data)
        #run loop
        on = True
        while on == True :

            screen.blit(board2,(0,0))

            level.draw() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    on = False
                    pygame.quit()
                    sys.exit()
                if event.type == pg.USEREVENT + 1:
                    time += 1

                Manager.process_events(event)

            timer_text = font.render(f"{time}", True, (255,255,255))
            text_rect = timer_text.get_rect(center = (width//2,50))
            screen.blit(timer_text, text_rect)

            yuen_group.update()
            yuen_group.draw(screen)

            jy_group.update()
            jy_group.draw(screen)

            puolin_group.draw(screen)
            Chicky.update()
            
            clock.tick(60)
            pg.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)
        pygame.display.update()


def level3(lvl, username, coin, pull, c, equip, stats):
    # by 'Puo Puo'(Puo Lin) & Jia Ying
    import pygame as pg #change pg

    #screen display /setup
    width, height = 500, 500
    screen = pg.display.set_mode((width,height))
    font = pg.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    pg.display.set_caption('Chicky Simulator - Level 3')
    board2 = pg.image.load('graphic/10x10map.jpg')
    tile_size=50

    time = 0
    pg.time.set_timer(pg.USEREVENT+1, 1000)
    clock = pg.time.Clock()
    time_use =[]
    
    while True:

        class chicky():
            def __init__(self,x,y):
                chic = pygame.image.load(c)
                self.image = pg.transform.scale(chic,(50,50))
                self.rect = self.image.get_rect(center=(25,25))
                self.rect.x = x
                self.rect.y = y

            def update(self):
                dx = 0
                dy = 0

                key = pg.key.get_pressed()
                if key[pg.K_w]:
                    dy -= 3
                    if self.rect.y<0 :
                        self.rect.y=0
                if key[pg.K_a]:
                    dx -= 3
                    if self.rect.x<0 :
                        self.rect.x=0
                if key[pg.K_s]:
                    dy += 3
                    if self.rect.y>450 :
                        self.rect.y=450
                if key[pg.K_d]:
                    dx += 3
                    if self.rect.x>450 :
                        self.rect.x=450
                
                #collision with blocks
                for item in level.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        dx = 0
                        dy = 0
                #collision with coins
                for item in level.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        level.coin_list.remove(item)
                        if level.coin_list == [] :
                            # make time stop
                            pg.time.set_timer(pg.USEREVENT, 0)
                            # save in list 
                            time_use.append(time)
                            levl = 4
                            win(lvl, username, levl, coin, pull, c, equip, stats)
                            
                #collision with monsters
                if pg.sprite.spritecollide(self,yuen_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,jy_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,puolin_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                
                self.rect.x += dx
                self.rect.y += dy

                screen.blit(self.image,self.rect)

         #define fixed information(NPC/Blocks/Coin)
        class lvel():
            def __init__(self,data):
                self.block_list = [ ] 
                self.coin_list = [ ] 


                block = pg.image.load('graphic/block.png')
                coin = pg.image.load('graphic/coin.png')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1 :
                            block = pg. transform. scale(block, (tile_size, tile_size))
                            block_rect = block.get_rect()
                            block_rect.x = col_count * tile_size
                            block_rect.y = row_count * tile_size
                            item = (block, block_rect) 
                            self.block_list.append(item) 
                        if tile == 2 :
                            coin = pg. transform. scale(coin, (tile_size, tile_size))
                            coin_rect = block.get_rect()
                            coin_rect.x = col_count * tile_size
                            coin_rect.y = row_count * tile_size
                            item = (coin, coin_rect)
                            self.coin_list.append(item)
                            
                        if tile == 3 :
                            yuen = Monster1(col_count * tile_size,row_count * tile_size)
                            yuen_group.add(yuen)
                            
                        if tile == 4 :
                            jy = Monster3(col_count * tile_size,row_count * tile_size)
                            jy_group.add(jy)

                        if tile == 5 :
                            puolin = Monster2(col_count * tile_size,row_count * tile_size)
                            puolin_group.add(puolin)
                        col_count += 1
                    row_count += 1

            def draw(self):
                for item in self.block_list:
                    screen.blit(item[0],item[1]) 
                for item in self.coin_list:
                    screen.blit(item[0],item[1])

        class Monster1(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster1.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        class Monster2(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster2.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                
        class Monster3(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster3.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.y += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        lvl3_data=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,1,1,0],
        [0,1,1,1,0,1,4,0,1,0],
        [0,2,5,1,0,1,0,0,1,0],
        [0,1,1,1,0,1,0,0,1,0],
        [0,1,5,0,0,1,2,1,1,0],
        [0,1,1,0,1,1,1,1,0,0],
        [0,1,2,0,1,5,2,0,0,0],
        [0,1,1,1,1,1,1,0,1,0],
        [0,0,0,2,5,1,0,0,1,2]
        ] 
        #spawn point
        Chicky = chicky(0,0)
        #group for collision
        yuen_group = pg.sprite.Group()
        puolin_group = pg.sprite.Group()
        jy_group = pg.sprite.Group()  

        level = lvel(lvl3_data)


        #run loop
        on = True
        while on == True :

            screen.blit(board2,(0,0))

            level.draw() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    on = False
                    pygame.quit()
                    sys.exit()
                if event.type == pg.USEREVENT + 1:
                    time += 1

                Manager.process_events(event)

            timer_text = font.render(f"{time}", True, (255,255,255))
            text_rect = timer_text.get_rect(center = (width//2,50))
            screen.blit(timer_text, text_rect)

            yuen_group.update()
            yuen_group.draw(screen)

            jy_group.update()
            jy_group.draw(screen)

            puolin_group.draw(screen)
            Chicky.update()
            
            clock.tick(60)
            pg.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)
        pygame.display.update()


def level4(lvl, username, coin, pull, c, equip, stats):
    # by 'Puo Puo'(Puo Lin) & Jia Ying
    import pygame as pg #change pg

    #screen display /setup

    width, height = 500, 500
    screen = pg.display.set_mode((width,height))
    font = pg.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    pg.display.set_caption('Chicky Simulator - Level 4')
    board2 = pg.image.load('graphic/10x10map.jpg')
    tile_size=50

    time = 0
    # count = False
    pg.time.set_timer(pg.USEREVENT+1, 1000)
    clock = pg.time.Clock()
    time_use =[]
    
    while True:

        class chicky():
            def __init__(self,x,y):
                chic = pygame.image.load(c)
                self.image = pg.transform.scale(chic,(50,50))
                self.rect = self.image.get_rect(center=(25,25))
                self.rect.x = x
                self.rect.y = y

            def update(self):
                dx = 0
                dy = 0

                key = pg.key.get_pressed()
                if key[pg.K_w]:
                    dy -= 3
                    if self.rect.y<0 :
                        self.rect.y=0
                if key[pg.K_a]:
                    dx -= 3
                    if self.rect.x<0 :
                        self.rect.x=0
                if key[pg.K_s]:
                    dy += 3
                    if self.rect.y>450 :
                        self.rect.y=450
                if key[pg.K_d]:
                    dx += 3
                    if self.rect.x>450 :
                        self.rect.x=450
                
                #collision with blocks
                for item in level.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        dx = 0
                        dy = 0
                #collision with coins
                for item in level.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        level.coin_list.remove(item)
                        if level.coin_list == [] :
                            # make time stop
                            pg.time.set_timer(pg.USEREVENT, 0)
                            # save in list 
                            time_use.append(time)
                            levl = 5
                            win(lvl, username, levl, coin, pull, c, equip, stats)
                            
                #collision with monsters
                if pg.sprite.spritecollide(self,yuen_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,jy_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,puolin_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                
                self.rect.x += dx
                self.rect.y += dy

                screen.blit(self.image,self.rect)

        #define fixed information(NPC/Blocks/Coin)
        class lvel():
            def __init__(self,data):
                self.block_list = [ ] 
                self.coin_list = [ ] 


                block = pg.image.load('graphic/block.png')
                coin = pg.image.load('graphic/coin.png')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1 :
                            block = pg. transform. scale(block, (tile_size, tile_size))
                            block_rect = block.get_rect()
                            block_rect.x = col_count * tile_size
                            block_rect.y = row_count * tile_size
                            item = (block, block_rect) 
                            self.block_list.append(item) 
                        if tile == 2 :
                            coin = pg. transform. scale(coin, (tile_size, tile_size))
                            coin_rect = block.get_rect()
                            coin_rect.x = col_count * tile_size
                            coin_rect.y = row_count * tile_size
                            item = (coin, coin_rect)
                            self.coin_list.append(item)
                            
                        if tile == 3 :
                            yuen = Monster1(col_count * tile_size,row_count * tile_size)
                            yuen_group.add(yuen)
                            
                        if tile == 4 :
                            jy = Monster3(col_count * tile_size,row_count * tile_size)
                            jy_group.add(jy)

                        if tile == 5 :
                            puolin = Monster2(col_count * tile_size,row_count * tile_size)
                            puolin_group.add(puolin)
                        col_count += 1
                    row_count += 1

            def draw(self):
                for item in self.block_list:
                    screen.blit(item[0],item[1]) 
                for item in self.coin_list:
                    screen.blit(item[0],item[1])

        class Monster1(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster1.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        class Monster2(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster2.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                

        class Monster3(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster3.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.y += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        lvl4_data=[
        [0,1,1,1,1,0,1,1,1,0],
        [0,1,0,0,1,0,0,2,1,0],
        [0,1,0,0,1,0,1,1,1,0],
        [0,1,1,1,1,4,0,0,1,0],
        [4,0,0,0,0,0,1,1,1,0],
        [0,1,1,1,1,0,0,3,0,0],
        [0,0,2,5,1,0,1,0,1,0],
        [0,1,1,1,1,0,1,2,1,0],
        [0,1,2,0,0,0,1,1,1,0],
        [2,1,1,1,1,5,0,0,1,2]
        ] 

        Chicky = chicky(0,0)

        yuen_group = pg.sprite.Group()
        puolin_group = pg.sprite.Group()
        jy_group = pg.sprite.Group()  

        level = lvel(lvl4_data)

        on = True
        while on == True :

            screen.blit(board2,(0,0))

            level.draw() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    on = False
                    pygame.quit()
                    sys.exit()
                if event.type == pg.USEREVENT + 1:
                    time += 1

                Manager.process_events(event)
                
            timer_text = font.render(f"{time}", True, (255,255,255))
            text_rect = timer_text.get_rect(center = (width//2,50))
            screen.blit(timer_text, text_rect)

            yuen_group.update()
            yuen_group.draw(screen)

            jy_group.update()
            jy_group.draw(screen)

            puolin_group.draw(screen)
            Chicky.update()
                
            clock.tick(60)
            pg.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)
        pygame.display.update()


def level5(lvl, username, coin, pull, c, equip, stats):
    # by 'Puo Puo'(Puo Lin) & Jia Ying
    import pygame as pg #change pg

    #screen display /setup

    width, height = 500, 500
    screen = pg.display.set_mode((width,height))
    font = pg.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    pg.display.set_caption('Chicky Simulator - Level 5')
    board2 = pg.image.load('graphic/10x10map.jpg')
    tile_size=50

    time = 0
    # count = False
    pg.time.set_timer(pg.USEREVENT+1, 1000)
    clock = pg.time.Clock()
    time_use =[]
    
    while True:

        class chicky():
            def __init__(self,x,y):
                chic = pygame.image.load(c)
                self.image = pg.transform.scale(chic,(50,50))
                self.rect = self.image.get_rect(center=(25,25))
                self.rect.x = x
                self.rect.y = y

            def update(self):
                dx = 0
                dy = 0

                key = pg.key.get_pressed()
                if key[pg.K_w]:
                    dy -= 3
                    if self.rect.y<0 :
                        self.rect.y=0
                if key[pg.K_a]:
                    dx -= 3
                    if self.rect.x<0 :
                        self.rect.x=0
                if key[pg.K_s]:
                    dy += 3
                    if self.rect.y>450 :
                        self.rect.y=450
                if key[pg.K_d]:
                    dx += 3
                    if self.rect.x>450 :
                        self.rect.x=450
                
                #collision with blocks
                for item in level.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        dx = 0
                        dy = 0
                #collision with coins
                for item in level.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20 , 10, 10):
                        level.coin_list.remove(item)
                        if level.coin_list == [] :
                            # make time stop
                            pg.time.set_timer(pg.USEREVENT, 0)
                            # save in list and save in text file
                            time_use.append(time)
                            update_time(username, time_use[0])
                            win5(lvl, username, coin, pull, c, equip, stats)
                            
                            
                #collision with monsters
                if pg.sprite.spritecollide(self,yuen_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,jy_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                if pg.sprite.spritecollide(self,puolin_group,False):
                    self.rect.x = 0
                    self.rect.y = 0
                
                self.rect.x += dx
                self.rect.y += dy

                screen.blit(self.image,self.rect)

        #define fixed information(NPC/Blocks/Coin)
        class lvel():
            def __init__(self,data):
                self.block_list = [ ] 
                self.coin_list = [ ] 


                block = pg.image.load('graphic/block.png')
                coin = pg.image.load('graphic/coin.png')

                row_count = 0
                for row in data:
                    col_count = 0
                    for tile in row:
                        if tile == 1 :
                            block = pg. transform. scale(block, (tile_size, tile_size))
                            block_rect = block.get_rect()
                            block_rect.x = col_count * tile_size
                            block_rect.y = row_count * tile_size
                            item = (block, block_rect) 
                            self.block_list.append(item) 
                        if tile == 2 :
                            coin = pg. transform. scale(coin, (tile_size, tile_size))
                            coin_rect = block.get_rect()
                            coin_rect.x = col_count * tile_size
                            coin_rect.y = row_count * tile_size
                            item = (coin, coin_rect)
                            self.coin_list.append(item)
                            
                        if tile == 3 :
                            yuen = Monster1(col_count * tile_size,row_count * tile_size)
                            yuen_group.add(yuen)
                            
                        if tile == 4 :
                            jy = Monster3(col_count * tile_size,row_count * tile_size)
                            jy_group.add(jy)

                        if tile == 5 :
                            puolin = Monster2(col_count * tile_size,row_count * tile_size)
                            puolin_group.add(puolin)
                        col_count += 1
                    row_count += 1

            def draw(self):
                for item in self.block_list:
                    screen.blit(item[0],item[1]) 
                for item in self.coin_list:
                    screen.blit(item[0],item[1])

        class Monster1(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster1.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.x += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        class Monster2(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster2.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                

        class Monster3(pg.sprite.Sprite):
            def __init__(self,x,y):
                pg.sprite.Sprite.__init__(self)
                self.image = pg.image.load('graphic/monster3.png')
                self.image = pg.transform.scale(self.image, (tile_size, tile_size))
                self.rect = self.image.get_rect()
                self.rect.x = x
                self.rect.y = y
                self.move_direction = 1
                self.move_counter = 0
                
            def update(self):
                self.rect.y += self.move_direction
                self.move_counter += 1
                if self.move_counter > 100 :
                    self.move_direction *= -1
                    self.move_counter *= -1

        lvl5_data=[
        [0,0,0,0,0,0,0,2,5,0],
        [0,0,0,3,0,0,0,3,0,0],
        [0,4,0,2,5,4,0,0,0,4],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,3,0,0,0,3,0,0],
        [4,0,2,0,0,0,2,0,4,0],
        [0,0,0,0,3,0,0,0,0,0],
        [0,4,5,0,0,4,0,0,0,4],
        [0,0,2,0,0,0,0,0,0,0],
        [0,0,3,0,0,0,3,0,0,2]
        ] 
                    
        # lvl5_data=[
        # [0,0,0,0,0,0,0,0,0,0],
        # [0,0,1,1,0,1,1,1,0,0],
        # [0,1,1,2,1,1,2,1,1,0],
        # [0,1,2,0,1,0,0,2,1,0],                    #Backup plan if mr.willie can get through
        # [0,1,1,0,0,0,2,1,1,0],
        # [0,0,1,1,0,0,1,1,0,0],
        # [0,0,0,1,0,1,1,0,0,0],
        # [0,0,0,0,2,1,0,0,0,0],
        # [0,0,0,5,1,0,0,0,0,0],
        # [0,0,0,0,0,0,0,0,0,0]
        # ]

        #spawn point
        Chicky = chicky(0,0)

        #collision group
        yuen_group = pg.sprite.Group()
        puolin_group = pg.sprite.Group()
        jy_group = pg.sprite.Group()  

        level = lvel(lvl5_data)

        #run loop
        on = True
        while on == True :

            screen.blit(board2,(0,0))

            level.draw() 

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    on = False
                    pygame.quit()
                    sys.exit()
                if event.type == pg.USEREVENT + 1:
                    time += 1

                Manager.process_events(event)

            timer_text = font.render(f"{time}", True, (255,255,255))
            text_rect = timer_text.get_rect(center = (width//2,50))
            screen.blit(timer_text, text_rect)

            yuen_group.update()
            yuen_group.draw(screen)

            jy_group.update()
            jy_group.draw(screen)

            puolin_group.draw(screen)
            Chicky.update()

            clock.tick(60)
            pg.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)
        pygame.display.update()


def win5(lvl, username, coin, pull, c, equip, stats):
    # winning condition for lvl 5

    # screen display / setup
    width, height = 900, 700
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator - Congratulations')
    screen.blit(level_image, (0,0))

    while True:

        w, h = 600, 400
        win_image = pygame.image.load('graphic/win.PNG')
        win_image = pygame.transform.scale(win_image,(w,h))
        win_image_rect = win_image.get_rect(center = (width/2, height/2))
        screen.blit(win_image, win_image_rect)

        level_button = Button('graphic/button2.png', 330, 460, 0.25, "LEVEL")
        level_button.draw(screen)

        rank_button = Button('graphic/button2.png', 570, 460, 0.25, "RANKING")
        rank_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                if rank_button.check_input(pos_mouse):
                    ranking(username, lvl, coin, pull, c, equip, stats)

        pygame.display.update()


def win(lvl, username, levl, coin, pull, c, equip, stats):
    # winning condition for lvl 1, 2, 3, 4

    # screen display / setup
    width, height = 900, 700
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator - Congratulations')
    screen.blit(level_image, (0,0))

    # renew user_details with latest lvl   #changed later
    if lvl < 5:
        lvl += 1
        update_level(username, lvl)

    while True:

        w, h = 600, 400
        win_image = pygame.image.load('graphic/win.PNG')
        win_image = pygame.transform.scale(win_image,(w,h))
        win_image_rect = win_image.get_rect(center = (width/2, height/2))
        screen.blit(win_image, win_image_rect)

        level_button = Button('graphic/button2.png', 330, 460, 0.25, "LEVEL")
        level_button.draw(screen)

        next_button = Button('graphic/button2.png', 570, 460, 0.25, "NEXT")
        next_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_button.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                if next_button.check_input(pos_mouse): #changed later
                    if levl == 2:
                        tutorial3(lvl, username, coin, pull, c, equip, stats)
                    elif levl == 3:
                        tutorial4(lvl, username, coin, pull, c, equip, stats)
                    elif levl == 4:
                        level4(lvl, username, coin, pull, c, equip, stats)
                    elif levl == 5:
                        level5(lvl, username, coin, pull, c, equip, stats)

        pygame.display.update()


def update_time(username, time):
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            if int(user_details[3]) > int(time):
                user_details[3] = str(time)
                lines[i] = ', '.join(user_details) + '\n'
                break
            else:
                break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)
    return


def update_level(username, lvl):
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            user_details[2] = str(lvl)
            lines[i] = ', '.join(user_details) + '\n'
            break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)
    return


def update_coin(username, coin):
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            user_details[4] = str(coin)
            lines[i] = ', '.join(user_details) + '\n'
            break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)
    return


def update_pull(username, pull):
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            user_details[5] = str(pull)
            lines[i] = ', '.join(user_details) + '\n'
            break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)
    return


def update_chicky(username, chicky):
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_backpack = line.strip().split(", ")
        if user_backpack[0] == username:
            chicky_list = user_backpack[1].split('/')
            if chicky_list[1] == '0':
                del chicky_list[1]
                chicky_list.append(f'{chicky}')
            elif chicky in chicky_list:
                break
            else:
                chicky_list.append(f'{chicky}')
            chicky_str = '/'.join(chicky_list)
            user_backpack[1] = str(chicky_str)
            lines[i] = ', '.join(user_backpack) + '\n'
            break

    with open('user_backpack.txt', 'w') as file:
        file.writelines(lines)
    return


def update_equipment(username, weapon):
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_backpack = line.strip().split(", ")
        if user_backpack[0] == username:
            weapon_list = user_backpack[2].split('/')
            if weapon_list[0] == 'no':
                del weapon_list[0]
                weapon_list.append(f'{weapon}')
            elif weapon in weapon_list:
                break
            else:
                weapon_list.append(f'{weapon}')
            weapon_str = '/'.join(weapon_list)
            user_backpack[2] = str(weapon_str)
            lines[i] = ', '.join(user_backpack) + '\n'
            break

    with open('user_backpack.txt', 'w') as file:
        file.writelines(lines)
    return


def backpack(username, lvl, coin, pull, chicky, equip, stats):

    FPS = 60
    selected_item = None
    offset_x, offset_y = None, None
    backpack_rows = 5
    backpack_cols = 3
    slot_size = 100
    backpack_slots = []

    for row in range(backpack_rows):
        for col in range(backpack_cols):
            x = 495 + col * (slot_size + 25)
            y = 140 + row * (slot_size + 10)
            backpack_slots.append(Slot(x, y, slot_size, slot_size))

    equip_slots = {
        "sword": Slot(105, 430, slot_size, slot_size),
        "shield": Slot(255, 430, slot_size, slot_size),
        "helmet": Slot(30, 550, slot_size, slot_size),
        "armor": Slot(180, 550, slot_size, slot_size),
        "shoes": Slot(330, 550, slot_size, slot_size)
    }

    equipment_list = []
    with open('user_backpack.txt', 'r') as file1:
        lines = file1.readlines()
        for i, line in enumerate(lines):
            user_backpack = line.split(", ")
            if user_backpack[0] == username:
                equipment_list = user_backpack[2].split('/')
                break

    items = []
    with open('equipment_details.txt', 'r') as file2:
        lines = file2.readlines()
        for line in lines:
            item_details = line.split(", ")
            if item_details[0] in equipment_list:
                item_graphic = (f'{item_details[1]}')
                item_info = (f'{item_details[2]}\n{item_details[3]}')
                item = Item(item_graphic, item_info, 0.65)
                items.append(item)
                
            #items = [Item('Sword', 'graphic/sword.png', 'Sword\nAttack +30', 0.65),
            #Item('Shield', 'graphic/shield.png', 'Wood Shield\nDefence +5', 0.65),
            #Item('Helmet', 'graphic/helmet.png', 'Leather Helmet\nDefence +5', 0.65),
            #Item('Armor', 'graphic/armor.png', 'Leather Armor\nDefence +5', 0.65),
            #Item('Shoes', 'graphic/noob leg.png', 'Leather Shoes\nSpeed +2', 0.65)
            #]

    for i, item in enumerate(items):
        if i <= len(backpack_slots):
            backpack_slots[i].item = item

    #for i,item in enumerate(equips):

    while True:

        pygame.display.set_caption('Chicky Simulator - Backpack')
        screen.blit(ranking_image,(0,0))

        backpack_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Backpack', True, 'white')
        backpack_text_rect = backpack_text.get_rect(center = (450,80))
        screen.blit(backpack_text, backpack_text_rect)

        coinlogo = Lock('graphic/manycoin.png', 700, 80, 0.3)
        coinlogo.draw(screen)

        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (780,80))
        screen.blit(coin_text, coin_text_rect)

        backpack_surface = pygame.Surface((420,550))
        backpack_surface.fill('white')
        backpack_surface.set_alpha(150)
        backpack_surface_rect = backpack_surface.get_rect(center=(670,410))
        screen.blit(backpack_surface, backpack_surface_rect)

        equip_surface = pygame.Surface((420,550))
        equip_surface.fill('white')
        equip_surface.set_alpha(150)
        equip_surface_rect = equip_surface.get_rect(center=(230,410))
        screen.blit(equip_surface, equip_surface_rect)

        back_button = Button('graphic/botton1.png', 100, 80, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for slot in backpack_slots:
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        selected_item.rect.x = pos_mouse[0] + offset_x
                        selected_item.rect.y = pos_mouse[1] + offset_y
                        slot.item = None
                        break

                for slot in list(equip_slots.values()):
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        selected_item.rect.x = pos_mouse[0] + offset_x
                        selected_item.rect.y = pos_mouse[1] + offset_y
                        slot.item = None
                        break
                        #if slot.item == None:
                            #with open('user_details.txt', 'r') as file1:
                                #lines = file1.readlines()
                                #for line in lines:
                                    #user_default = line.strip().split(", ")
                                    #if user_default[0] == username:
                                        #equip_list = user_default[7].split('/')
                                        #with open('equipment_details.txt', 'r') as file2:
                                            #lines = file2.readlines()
                                            #for line in lines:
                                                #item_details = line.split(", ")
                                                #if item_details[0] in equip_list:
                                                    #a, d, s = item_details[4].split('/')
                                                    #Atk -= a
                                                    #Def -= d
                                                    #Spd -= s

                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, chicky, equip, stats)

            elif event.type == pygame.MOUSEMOTION:
                if selected_item:
                    selected_item.rect.x = pos_mouse[0] + offset_x
                    selected_item.rect.y = pos_mouse[1] + offset_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_item:
                    for slot in backpack_slots + list(equip_slots.values()):
                        if (slot.rect.collidepoint(pos_mouse)) and (slot.item is None):
                            slot.item = selected_item
                            selected_item = None
                            offset_x, offset_y = None, None
                            break
                    if selected_item:
                        for slot in backpack_slots:
                            if slot.item is None:
                                slot.item = selected_item
                                selected_item = None
                                offset_x, offset_y = None, None
                                break

        for slot in backpack_slots:
            slot.draw(screen)

        for slot in equip_slots.values():
            slot.draw(screen)

        if selected_item == None:
            Hp,Def,Atk,Spd,Mag = stats.split('/')
            default1 = Info(50, 135, (f'Hp={Hp}\nDef={Def}'))
            default2 = Info(200, 135, (f'Atk={Atk}\nSpd={Spd}'))
            default1.draw_info(screen)
            default2.draw_info(screen)
        else:
            screen.blit(selected_item.image, selected_item.rect.topleft)
            Hp,Def,Atk,Spd,Mag = stats.split('/')
            default1 = Info(50, 135, (f'Hp={Hp}\nDef={Def}'))
            default2 = Info(200, 135, (f'Atk={Atk}\nSpd={Spd}'))
            default1.draw_info(screen)
            default2.draw_info(screen)
            info = Info(50, 330, selected_item.info)
            info.draw_info(screen)

        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.update()


def items(username, lvl, coin, times, itemget, pull, c, equip, stats):

    while True:
        pygame.display.set_caption('Chicky Simulator - Items Get')
        screen.blit(ranking_image,(0,0))

        item_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Items Get', True, 'white')
        item_text_rect = item_text.get_rect(center = (450,100))
        screen.blit(item_text, item_text_rect)

        item_surface = pygame.Surface((700,350))
        item_surface.fill('white')
        item_surface.set_alpha(150)
        item_surface_rect = item_surface.get_rect(center=(width/2,350))
        screen.blit(item_surface, item_surface_rect)

        back_button = Button('graphic/button2.png', 450, 580, 0.3, "BACK")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        if times == 1:
            if itemget == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)
                kitty = Lock('graphic/miaoji.png', width/2, 350, 0.18)
                kitty.draw(screen)

            elif itemget == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)
                tanker = Lock('graphic/tank chic.png', width/2, 350, 0.18)
                tanker.draw(screen)

            elif itemget == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)
                magnet = Lock('graphic/magnetchic.png', width/2, 350, 0.18)
                magnet.draw(screen)

            elif itemget == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)
                speedy = Lock('graphic/speedychic.png', width/2, 350, 0.18)
                speedy.draw(screen)

            elif itemget == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)
                worrier = Lock('graphic/ninjachic.png', width/2, 350, 0.18)
                worrier.draw(screen)

            else:
                coins = Lock('graphic/itemcoin.png', width/2, 350, 1.5)
                coins.draw(screen)

        else:
            item1,item2,item3,item4,item5 = itemget.split(',')
            if item1 == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)
                kitty = Lock('graphic/miaoji.png', 200, 350, 0.18)
                kitty.draw(screen)

            elif item1 == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)
                tanker = Lock('graphic/tank chic.png', 200, 350, 0.18)
                tanker.draw(screen)

            elif item1 == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)
                magnet = Lock('graphic/magnetchic.png', 200, 350, 0.18)
                magnet.draw(screen)

            elif item1 == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)
                speedy = Lock('graphic/speedychic.png', 200, 350, 0.18)
                speedy.draw(screen)

            elif item1 == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)
                worrier = Lock('graphic/ninjachic.png', 200, 350, 0.18)
                worrier.draw(screen)

            else:
                coins = Lock('graphic/itemcoin.png', 200, 350, 1.5)
                coins.draw(screen)

            if item2 == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)
                kitty = Lock('graphic/miaoji.png', 325, 350, 0.18)
                kitty.draw(screen)

            elif item2 == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)
                tanker = Lock('graphic/tank chic.png', 325, 350, 0.18)
                tanker.draw(screen)

            elif item2 == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)
                magnet = Lock('graphic/magnetchic.png', 325, 350, 0.18)
                magnet.draw(screen)

            elif item2 == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)
                speedy = Lock('graphic/speedychic.png', 325, 350, 0.18)
                speedy.draw(screen)

            elif item2 == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)
                worrier = Lock('graphic/ninjachic.png', 325, 350, 0.18)
                worrier.draw(screen)

            else:
                coins = Lock('graphic/itemcoin.png', 325, 350, 1.5)
                coins.draw(screen)

            if item3 == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)
                kitty = Lock('graphic/miaoji.png', width/2, 350, 0.18)
                kitty.draw(screen)

            elif item3 == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)
                tanker = Lock('graphic/tank chic.png', width/2, 350, 0.18)
                tanker.draw(screen)

            elif item3 == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)
                magnet = Lock('graphic/magnetchic.png', width/2, 350, 0.18)
                magnet.draw(screen)

            elif item3 == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)
                speedy = Lock('graphic/speedychic.png', width/2, 350, 0.18)
                speedy.draw(screen)

            elif item3 == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)
                worrier = Lock('graphic/ninjachic.png', width/2, 350, 0.18)
                worrier.draw(screen)

            else:
                coins = Lock('graphic/itemcoin.png', width/2, 350, 1.5)
                coins.draw(screen)

            if item4 == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)
                kitty = Lock('graphic/miaoji.png', 575, 350, 0.18)
                kitty.draw(screen)

            elif item4 == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)
                tanker = Lock('graphic/tank chic.png', 575, 350, 0.18)
                tanker.draw(screen)

            elif item4 == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)
                magnet = Lock('graphic/magnetchic.png', 575, 350, 0.18)
                magnet.draw(screen)

            elif item4 == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)
                speedy = Lock('graphic/speedychic.png', 575, 350, 0.18)
                speedy.draw(screen)

            elif item4 == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)
                worrier = Lock('graphic/ninjachic.png', 575, 350, 0.18)
                worrier.draw(screen)

            else:
                coins = Lock('graphic/itemcoin.png', 575, 350, 1.5)
                coins.draw(screen)
            
            if item5 == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)
                kitty = Lock('graphic/miaoji.png', 700, 350, 0.18)
                kitty.draw(screen)

            elif item5 == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)
                tanker = Lock('graphic/tank chic.png', 700, 350, 0.18)
                tanker.draw(screen)

            elif item5 == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)
                magnet = Lock('graphic/magnetchic.png', 700, 350, 0.18)
                magnet.draw(screen)

            elif item5 == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)
                speedy = Lock('graphic/speedychic.png', 700, 350, 0.18)
                speedy.draw(screen)

            elif item5 == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)
                worrier = Lock('graphic/ninjachic.png', 700, 350, 0.18)
                worrier.draw(screen)
            else:
                coins = Lock('graphic/itemcoin.png', 700, 350, 1.5)
                coins.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    wish(username, lvl, coin, pull, c, equip, stats)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def shooting_stars(username, lvl, coin, times, itemget, pull, c, equip, stats):

    while True:
        chicky = ('kitty','tanker','worrier','speedy','magnet')
        if times == 1:
            if itemget in chicky:
                vid = Video('graphic/onegold.mp4')
                screen = pygame.display.set_mode((width,height))
                pygame.display.set_caption('Chicky Simulator - Wishing')

                while vid.active:
                    vid.set_speed(1.0)
                    if vid.draw(screen, (-360, 0), force_draw=False):
                        pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vid.stop()
                            vid.close()
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            vid.stop()
                            items(username, lvl, coin, times, itemget, pull, c, equip, stats)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull, c, equip, stats)

            else:
                vid = Video('graphic/onepurple.mp4')
                screen = pygame.display.set_mode((width,height))
                pygame.display.set_caption('Chicky Simulator - Wishing')

                while vid.active:
                    vid.set_speed(1.0)
                    if vid.draw(screen, (-360, 0), force_draw=False):
                        pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vid.stop()
                            vid.close()
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            vid.stop()
                            items(username, lvl, coin, times, itemget, pull, c, equip, stats)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull, c, equip, stats)

        else:
            item_list = itemget.split(',')
            # for item in item_list:
            if ((item_list[0] in chicky) or (item_list[1] in chicky) or (item_list[2] in chicky) or (item_list[3] in chicky) or (item_list[4] in chicky)):
                vid = Video('graphic/fivegold.mp4')
                screen = pygame.display.set_mode((width,height))
                pygame.display.set_caption('Chicky Simulator - Wishing')

                while vid.active:
                    vid.set_speed(1.0)
                    if vid.draw(screen, (-360, 0), force_draw=False):
                        pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vid.stop()
                            vid.close()
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            vid.stop()
                            items(username, lvl, coin, times, itemget, pull, c, equip, stats)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull, c, equip, stats)

            else:
                vid = Video('graphic/fivepurple.mp4')
                screen = pygame.display.set_mode((width,height))
                pygame.display.set_caption('Chicky Simulator - Wishing')

                while vid.active:
                    vid.set_speed(1.0)
                    if vid.draw(screen, (-360, 0), force_draw=False):
                        pygame.display.update()

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            vid.stop()
                            vid.close()
                            pygame.quit()
                            sys.exit()

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            vid.stop()
                            items(username, lvl, coin, times, itemget, pull, c, equip, stats)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull, c, equip, stats)

        pygame.display.update()


def wish(username, lvl, coin, pull, c, equip, stats):

    while True:
        pygame.display.set_caption('Chicky Simulator - Wishes')
        screen.blit(ranking_image,(0,0))

        wish_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Wishes', True, 'white')
        wish_text_rect = wish_text.get_rect(center = (450,100))
        screen.blit(wish_text, wish_text_rect)

        wishing_surface = pygame.Surface((700,350))
        wishing_surface.fill('white')
        wishing_surface.set_alpha(150)
        wishing_surface_rect = wishing_surface.get_rect(center=(width/2,350))
        screen.blit(wishing_surface, wishing_surface_rect)

        all_chicky = Lock('graphic/allchicky.png', width/2, 340, 0.9)
        all_chicky.draw(screen)

        coinlogo = Lock('graphic/manycoin.png', 700, 100, 0.3)
        coinlogo.draw(screen)

        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (780,100))
        screen.blit(coin_text, coin_text_rect)

        rpull = 50 - pull
        pull_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render(f'{rpull} Wishes Left', True, 'black')
        pull_text_rect = pull_text.get_rect(center = (240,510))
        screen.blit(pull_text, pull_text_rect)

        one_pull_button = Button('graphic/button2.png', 540, 580, 0.22, "1 Wish")
        one_pull_button.draw(screen)

        scoin = Lock('graphic/coin2.png', 510, 510, 0.12)
        scoin.draw(screen)

        scoin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('100', True, 'black')
        scoin_text_rect = scoin_text.get_rect(center = (560,510))
        screen.blit(scoin_text, scoin_text_rect)

        five_pull_button = Button('graphic/button2.png', 720, 580, 0.22, "5 Wish")
        five_pull_button.draw(screen)

        bcoin = Lock('graphic/coin2.png', 680, 510, 0.12)
        bcoin.draw(screen)

        bcoin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('500', True, 'black')
        bcoin_text_rect = bcoin_text.get_rect(center = (740,510))
        screen.blit(bcoin_text, bcoin_text_rect)

        chicky_button = Button('graphic/chicky.png', 150, 580, 0.11, " ")
        chicky_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        # 1.25%
        item = ('coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin90','kitty','tanker','worrier','speedy','magnet')
        
        pity = ('coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',

                'coin75','coin75','coin75',
                'coin90','coin90',
                'kitty','tanker','worrier','speedy','magnet')
        
        chicky = ('kitty','tanker','worrier','speedy','magnet')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, c, equip, stats)

                if one_pull_button.check_input(pos_mouse):
                    if coin >= 100:
                        times = 1
                        coin -= 100
                        pull += 1

                        if pull < 40:
                            itemget = random.choice(item)
                            if itemget in chicky:
                                pull = 0
                        elif ((pull >= 40) and (pull < 50)):
                            itemget = random.choice(pity)
                            if itemget in chicky:
                                pull = 0
                        else:
                            pull = 0
                            itemget = random.choice(chicky)
                        
                        update_pull(username, pull)
                        update_coin(username, coin)
                        shooting_stars(username, lvl, coin, times, itemget, pull, c, equip, stats)
                    else:
                        break

                if five_pull_button.check_input(pos_mouse):
                    if coin >= 500:
                        times = 5
                        coin -= 500
                        n = 5
                        itemlist = [0]
                        while n > 0:
                            pull += 1
                            n -= 1
                            if pull < 40:
                                itemget = random.choice(item)
                                if itemget in chicky:
                                    pull = 0
                            elif ((pull >= 40) and (pull < 50)):
                                itemget = random.choice(pity)
                                if itemget in chicky:
                                    pull = 0
                            else:
                                pull = 0
                                itemget = random.choice(chicky)

                            itemlist.append(itemget)

                        del itemlist[0]
                        itemsget = str(f'{itemlist[0]},{itemlist[1]},{itemlist[2]},{itemlist[3]},{itemlist[4]}')

                        update_pull(username, pull)
                        update_coin(username, coin)
                        shooting_stars(username, lvl, coin, times, itemsget, pull, c, equip, stats)
                    else:
                        break

            Manager.process_events(event)

        pygame.display.update()


def ranking(username, lvl, coin, pull, chicky, equip, stats):
    # leaderboard functions by my
    while True:

        # screen display / setup
        pygame.display.set_caption('Chicky Simulator - Ranking')
        screen.blit(ranking_image,(0,0))

        rank_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Ranking', True, 'white')
        rank_text_rect = rank_text.get_rect(center = (450,100))
        screen.blit(rank_text, rank_text_rect)

        ranking_surface = pygame.Surface((700,500))
        ranking_surface.fill('white')
        ranking_surface.set_alpha(150)
        ranking_surface_rect = ranking_surface.get_rect(center=(width/2,400))
        screen.blit(ranking_surface, ranking_surface_rect)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        # read file when user press ranking and display out top 9 used least steps - by my
        # modify from tutorial
        # Time means steps
        with open('user_details.txt', 'r') as file:
            data = [tuple(line.strip().split(',')) for line in file]
            sorted_data = sorted(data, key=lambda x:int(x[3])) 
            for rank, (Username, Password, Level, Time, Coin, Pull, Chicky, Equip, Stats) in enumerate(sorted_data[0:9], start=1):
                first = Ranking(130+(rank*50), str(rank), Username, Time)
                first.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def chick(username, lvl, coin, pull, c, equip, stats):
    # let user pick their character - by my

    while True:
        # screen display / setup
        pygame.display.set_caption('Chicky Simulator - Chicky')
        screen.blit(background_image,(0,0))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('What chick you like?', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        chick1_button = Button('graphic/kunchic.png', 150, 350, 0.5, "KunKun")
        chick1_button.draw(screen)

        chick2_button = Button('graphic/geekchic.png', 450, 350, 0.5, "WeeWee")
        chick2_button.draw(screen)

        chick3_button = Button('graphic/pinkchic.png', 750, 350, 0.5, "Honeey")
        chick3_button.draw(screen)

        back_button = Button('graphic/button2.png', 450, 580, 0.35, "BACK")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        # get user's selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if chick1_button.check_input(pos_mouse):
                    c = 'graphic/kunchic.png' # link to later use
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                if chick2_button.check_input(pos_mouse):
                    c = 'graphic/geekchic.png'
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                if chick3_button.check_input(pos_mouse):
                    c = 'graphic/pinkchic.png'
                    choose_level(lvl, username, coin, pull, c, equip, stats)

                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, c, equip, stats)

                Manager.process_events(event)
            
            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def choose_level(lvl, username, coin, pull, chicky, equip, stats):
    # level selection - by my

    while True:
        
        # screen display / setup
        pygame.display.set_caption('Chicky Simulator - Level')
        screen.blit(background_image,(0,0))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('LEVEL', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        lvl1_button = Button('graphic/botton1.png', 150, 350, 1.2, "1")
        lvl1_button.draw(screen)

        lvl2_button = Button('graphic/botton1.png', 300, 350, 1.2, "2")
        lvl2_button.draw(screen)

        lvl3_button = Button('graphic/botton1.png', 450, 350, 1.2, "3")
        lvl3_button.draw(screen)

        lvl4_button = Button('graphic/botton1.png', 600, 350, 1.2, "4")
        lvl4_button.draw(screen)

        lvl5_button = Button('graphic/botton1.png', 750, 350, 1.2, "5")
        lvl5_button.draw(screen)

        back_button = Button('graphic/button2.png', 250, 580, 0.35, "BACK")
        back_button.draw(screen)

        next_button = Button('graphic/button2.png', 650, 580, 0.35, "NEXT")
        next_button.draw(screen)
        
        pos_mouse = pygame.mouse.get_pos()

        lock2 = Lock('graphic/lock.png', 300, 350, 0.25)
        lock3 = Lock('graphic/lock.png', 450, 350, 0.25)
        lock4 = Lock('graphic/lock.png', 600, 350, 0.25)
        lock5 = Lock('graphic/lock.png', 750, 350, 0.25)

        lock2_con = False
        lock3_con = False
        lock4_con = False
        lock5_con = False

        # check if user unlock the level or not
        if lvl == 1:
            lock2.draw(screen)
            lock3.draw(screen)
            lock4.draw(screen)
            lock5.draw(screen)

        elif lvl == 2:
            lock2_con = True
            lock3.draw(screen)
            lock4.draw(screen)
            lock5.draw(screen)

        elif lvl == 3:
            lock2_con = True
            lock3_con = True
            lock4.draw(screen)
            lock5.draw(screen)

        elif lvl == 4:
            lock2_con = True
            lock3_con = True
            lock4_con = True
            lock5.draw(screen)

        else:
            lock2_con = True
            lock3_con = True
            lock4_con = True
            lock5_con = True

        # get user event(selection)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if lvl1_button.check_input(pos_mouse):
                    tutorial1(lvl, username, coin, pull, chicky, equip, stats)

                if lvl2_button.check_input(pos_mouse):
                    if lock2_con == True:
                        tutorial3(lvl, username, coin, pull, chicky, equip, stats)

                if lvl3_button.check_input(pos_mouse):
                    if lock3_con == True:
                        tutorial4(lvl, username, coin, pull, chicky, equip, stats)

                if lvl4_button.check_input(pos_mouse):
                    if lock4_con == True:
                        level4(lvl, username, coin, pull, chicky, equip, stats)

                if lvl5_button.check_input(pos_mouse):
                    if lock5_con == True:
                        level5(lvl, username, coin, pull, chicky, equip, stats)

                if back_button.check_input(pos_mouse):
                    chick(username, lvl, coin, pull, chicky, equip, stats)
                
                if next_button.check_input(pos_mouse):
                    arcade_lobby(lvl,username , coin, pull, chicky, equip, stats)
            
            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def lobby(username, lvl, coin, pull, chicky, equip, stats):


    while True:

        #screen display / setup
        pygame.display.set_caption('Chicky Simulator')
        screen.blit(background_image,(0,0))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        play_button = Button('graphic/button2.png', 450, 320, 0.3, "PLAY")
        play_button.draw(screen)

        rank_button = Button('graphic/button2.png', 450, 450, 0.3, "RANKING")
        rank_button.draw(screen)

        quit_button = Button('graphic/button2.png', 450, 580, 0.3, "QUIT")
        quit_button.draw(screen)

        wish_button = Button('graphic/star.png', 800, 460, 0.2, " ")
        wish_button.draw(screen)

        store_button = Button('graphic/store5.png', 800, 580, 0.6, " ")
        store_button.draw(screen)

        chicky_button = Button('graphic/chicky.png', 100, 460, 0.12, " ")
        chicky_button.draw(screen)

        backpack_button = Button('graphic/backpack3.png', 100, 580, 0.3, " ")
        backpack_button.draw(screen)

        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        collection_button = Button('graphic/botton1.png', 800, 350, 0.6, "?")
        collection_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        # get user events (their selections)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(pos_mouse):
                    chick(username, lvl, coin, pull, chicky, equip, stats)  

                if rank_button.check_input(pos_mouse):
                    ranking(username, lvl, coin, pull, chicky, equip, stats)
                
                if wish_button.check_input(pos_mouse):
                    wish(username, lvl, coin, pull, chicky, equip, stats)
                
                if store_button.check_input(pos_mouse):
                    store(username, lvl, coin, pull, chicky, equip, stats)
                    
                if collection_button.check_input(pos_mouse):
                    collection(username, lvl, coin, pull, chicky, equip, stats)

                if backpack_button.check_input(pos_mouse):
                    backpack(username, lvl, coin, pull, chicky, equip, stats)

                if back_button.check_input(pos_mouse):
                    log_or_reg()

                if quit_button.check_input(pos_mouse):
                    pygame.quit()
                    sys.exit()

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def check_default(username):
    with open('user_details.txt', 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            user_default = line.strip().split(", ")
            if user_default[0] == username:
                chicky = user_default[6]
                if chicky == 'normal':
                    chicky_graphic = 'graphic/chicky.png'
                    Hp, Def, Atk, Spd, Mag = 100, 0, 10, 10, 0
                    break
                elif chicky == 'kitty':
                    chicky_graphic = 'graphic/miaoji.png'
                    Hp, Def, Atk, Spd, Mag = 150, 0, 10, 10, 0
                    break
                elif chicky == 'worrier':
                    chicky_graphic = 'graphic/ninjachic.png'
                    Hp, Def, Atk, Spd, Mag = 75, 0, 20, 10, 0
                    break
                elif chicky == 'magnet':
                    chicky_graphic = 'graphic/magnetchic.png'
                    Hp, Def, Atk, Spd, Mag= 100, 0, 10, 10, 1
                    break
                elif chicky == 'speedy':
                    chicky_graphic = 'graphic/speedychic.png'
                    Hp, Def, Atk, Spd, Mag = 75, 0, 10, 20, 0
                    break
                elif chicky == 'tanker':
                    chicky_graphic = 'graphic/tank chic.png'
                    Hp, Def, Atk, Spd, Mag = 200, 0, 10, 5, 0
                    break

                equip_list = user_default[7].split('/')
                with open('equipment_details.txt', 'r') as file2:
                    lines = file2.readlines()
                    for line in lines:
                        item_details = line.split(", ")
                        if item_details[0] in equip_list:
                            a, d, s = item_details[4].split('/')
                            Atk += a
                            Def += d
                            Spd += s

    stats = str(f'{Hp}/{Def}/{Atk}/{Spd}/{Mag}')
    return stats


def read_userinput(username, password):
    # checking username and password for login part - by my
    while True:
        file = open('user_details.txt', 'r')
        for i in file:
            Username, Password, Level, Time, Coin, Pull, Chicky, Equip= i.split(",")
            Password = Password.strip()
            Level = Level.strip()
            Coin = Coin.strip()
            Pull = Pull.strip()
            Chicky = Chicky.strip()
            Equip = Equip.strip()
            Stats = check_default(username)
            if (Username == username and Password == password):
                return Level, Coin, Pull, Chicky, Equip, Stats
            
            else:
                screen.blit(background_image,(0,0))
            
                title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
                title_text_rect = title_text.get_rect(center = (450,150))
                screen.blit(title_text, title_text_rect)

                incorrect_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Username or password incorrect.', True, 'white')
                incorrect_text_rect = incorrect_text.get_rect(center = (width/2,height/2))
                screen.blit(incorrect_text, incorrect_text_rect)

                tryagain_button = Button('graphic/button2.png', 450, 580, 0.35, "TRY AGAIN")
                tryagain_button.draw(screen)

                pos_mouse = pygame.mouse.get_pos()
            
        file.close()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_button.check_input(pos_mouse):
                    login()

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def save_userinput(username, password):
    # checking and storing username and password for register part - by my
    while True:
        
        file = open('user_details.txt', 'r')
        for i in file:
            #list = i.split(",")
            Username, Password, Level, Time, Coin, Pull, Chicky, Equip = i.strip().split(",")

            # check if the name has been used before
            if username == Username:
                con = 0
                break
            # make sure user type their password
            elif password == ' ':
                con = 1
                break
            # save user details
            else:
                con = 2
                break
            
        if con == 0:
            screen.blit(background_image,(0,0))
            
            title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
            title_text_rect = title_text.get_rect(center = (450,150))
            screen.blit(title_text, title_text_rect)

            incorrect_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Someone had used this name.', True, 'white')
            incorrect_text_rect = incorrect_text.get_rect(center = (width/2,height/2))
            screen.blit(incorrect_text, incorrect_text_rect)

            tryagain_button = Button('graphic/button2.png', 450, 580, 0.35, "TRY AGAIN")
            tryagain_button.draw(screen)

            pos_mouse = pygame.mouse.get_pos()

        elif con == 1:
            screen.blit(background_image,(0,0))
            
            title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
            title_text_rect = title_text.get_rect(center = (450,150))
            screen.blit(title_text, title_text_rect)

            enter_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Please enter your password.', True, 'white')
            enter_text_rect = enter_text.get_rect(center = (width/2,height/2))
            screen.blit(enter_text, enter_text_rect)

            tryagain_button = Button('graphic/button2.png', 450, 580, 0.35, "TRY AGAIN")
            tryagain_button.draw(screen)

            pos_mouse = pygame.mouse.get_pos()

        else:
            file = open('user_details.txt', 'a')
            file.write(f'{username}, {password}, 1, 10000, 0, 0, normal, no' + '\n')
            # username, password, level, time, coin, pull, chicky, equip
            file.close()

            file2 = open('user_backpack.txt', 'a')
            file2.write(f'{username}, normal/0, no')
            file2.close()

            lvl = 1
            coin = 0
            pull = 0
            chicky = 'normal'
            equip = 'no'
            stats = check_default(username)
            return lvl, coin, pull, chicky, equip, stats
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if tryagain_button.check_input(pos_mouse):
                    register()

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def welcome_user(username, lvl, coin, pull, chicky, equip, stats):
    # screen display after user done with login/register part - my
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                lobby(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)

        pygame.display.set_caption('Chicky Simulator')
        screen.blit(background_image,(0,0))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        welcome_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render(f'Hello, {username}!', True, 'white')
        welcom_text_rect = welcome_text.get_rect(center = (width/2,height/2))
        screen.blit(welcome_text, welcom_text_rect)

        click_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Click Anywere To Continue', True, 'white')
        click_text_rect = click_text.get_rect(center = (450,550))
        screen.blit(click_text, click_text_rect)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def login():
    # login page display - by my
    while True:

        pygame.display.set_caption('Chicky Simulator')
        screen.blit(background_image,(0,0))
        
        login_surface = pygame.Surface((400,400))
        login_surface.fill('white')
        login_surface.set_alpha(150)
        screen.blit(login_surface,(250,250))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        name_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Enter your name:', True, 'black')
        name_text_rect = name_text.get_rect(center = (450,300))
        screen.blit(name_text, name_text_rect)

        password_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Enter password:', True, 'black')
        password_text_rect = password_text.get_rect(center = (450,430))
        screen.blit(password_text, password_text_rect)

        back_button = Button('graphic/button2.png', 450, 580, 0.35, "BACK")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        Manager.draw_ui(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if '#username' in username_input.get_object_ids() and '#password' in password_input.get_object_ids():
                    lvl, coin, pull, chicky, equip, stats = read_userinput(username_input.text, password_input.text)
                    welcome_user(username_input.text, int(lvl), int(coin), int(pull), chicky, equip, stats)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    log_or_reg()

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def register():
    # register page display - by my
    while True:
        pygame.display.set_caption('Chicky Simulator')
        screen.blit(background_image,(0,0))
        
        register_surface = pygame.Surface((400,400))
        register_surface.fill('white')
        register_surface.set_alpha(150)
        screen.blit(register_surface,(250,250))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        name_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Enter your name:', True, 'black')
        name_text_rect = name_text.get_rect(center = (450,300))
        screen.blit(name_text, name_text_rect)

        password_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Enter password:', True, 'black')
        password_text_rect = password_text.get_rect(center = (450,430))
        screen.blit(password_text, password_text_rect)

        back_button = Button('graphic/button2.png', 450, 580, 0.35, "BACK")
        back_button.draw(screen)
        pos_mouse = pygame.mouse.get_pos()

        Manager.draw_ui(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED:
                if '#username' in username_input.get_object_ids() and '#password' in password_input.get_object_ids():
                    lvl, coin, pull = save_userinput(username_input.text, password_input.text) # link to later use
                    welcome_user(username_input.text, int(lvl), int(coin), int(pull))
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    log_or_reg()

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def log_or_reg():


    # login or register screen display - by my
    while True:
        pygame.display.set_caption('Chicky Simulator')
        screen.blit(background_image,(0,0))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky Simulator', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        login_button = Button('graphic/button2.png', 450, 350, 0.35, "LOG IN")
        login_button.draw(screen)

        register_button = Button('graphic/button2.png', 450, 550, 0.35, "REGISTER")
        register_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if login_button.check_input(pos_mouse):
                    login()

                if register_button.check_input(pos_mouse):
                    register()
                
                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def store(username, lvl, coin, pull, chicky, equip, stats):
    ##puo puo did this
    on = True
    buy = False
    no = False
    axe= Button("graphic/axe.png",150,205,1,'')
    hammer = Button("graphic/hammer.png",450,205,1,'')
    sword = Button("graphic/sword.png",750,205,1,'')
    shield3 = Button("graphic/shield.png",150,460,1,'')
    shield4= Button("graphic/shield.png",450,460,1,'')
    shield5= Button("graphic/shield.png",750,460,1,'')

    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)

                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Store')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #Coin Display
        coinlogo = Lock('graphic/manycoin.png', 660, 70, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (750,70))
        screen.blit(coin_text, coin_text_rect)
        ###############

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Store', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(150)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        axe.draw(screen)
        hammer.draw(screen)
        sword.draw(screen)
        shield3.draw(screen)
        shield4.draw(screen)
        shield5.draw(screen)
        #################

        #PRICE
        #####sword####
        price_text = font.render(f"{500}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,305))
        screen.blit(price_text, text_rect)
        ######Shield######
        price_text = font.render(f"{1000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,305))
        screen.blit(price_text, text_rect)
        ######bow######
        price_text = font.render(f"{2000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,305))
        screen.blit(price_text, text_rect)
        ####x-bow#####
        price_text = font.render(f"{500}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,555))
        screen.blit(price_text, text_rect)
        ######hammer#####        
        price_text = font.render(f"{1000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,555))
        screen.blit(price_text, text_rect)
        #######axe#########        
        price_text = font.render(f"{2000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,555))
        screen.blit(price_text, text_rect)


        #BUTTONS
        buy_button1 = Button('graphic/button2.png', 150, 350, 0.15, "BUY")
        buy_button2 = Button('graphic/button2.png', 450, 350, 0.15, "BUY")
        buy_button3 = Button('graphic/button2.png', 750, 350, 0.15, "BUY")
        buy_button4 = Button('graphic/button2.png', 150, 600, 0.15, "BUY")
        buy_button5 = Button('graphic/button2.png', 450, 600, 0.15, "BUY")
        buy_button6 = Button('graphic/button2.png', 750, 600, 0.15, "BUY")
        #########

        #view button#
        view_button1 = Button('graphic/button2.png', 150, 350, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 350, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 350, 0.15, "VIEW")
        view_button4 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button5 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button6 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #############

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #To store data
        weapon = ('axe','hammer','sword','shield3','shield4','shield5')

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    weapon_list = user_backpack[2].split('/')
                    if 'axe' in weapon_list :
                        view_button1.draw(screen)
                    elif 'axe' not in weapon_list :
                        buy_button1.draw(screen)
                    if 'hammer' in weapon_list :
                        view_button2.draw(screen)
                    elif 'hammer' not in weapon_list :
                        buy_button2.draw(screen)
                    if 'sword' in weapon_list :
                        view_button3.draw(screen)
                    elif 'sword' not in weapon_list :
                        buy_button3.draw(screen)
                    if 'shield3' in weapon_list :
                        view_button4.draw(screen)
                    elif 'shield3' not in weapon_list :
                        buy_button4.draw(screen)
                    if 'shield4' in weapon_list :
                        view_button5.draw(screen)
                    elif 'shield4' not in weapon_list :
                        buy_button5.draw(screen)
                    if 'shield5' in weapon_list :
                        view_button6.draw(screen)
                    elif 'shield5' not in weapon_list :
                        buy_button6.draw(screen)

                weapon_str = '/'.join(weapon_list)
                user_backpack[2] = str(weapon_str)
                lines[i] = ', '.join(user_backpack) + '\n'
                break  

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if axe.check_input(pos_mouse):
                    axe_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if hammer.check_input(pos_mouse):
                    hammer_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if sword.check_input(pos_mouse):
                    sword_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shield3.check_input(pos_mouse):
                    shield3_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shield4.check_input(pos_mouse):
                    shield4_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shield5.check_input(pos_mouse):
                    shield5_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            weapon_list = user_backpack[2].split('/')
                            if 'axe' in weapon_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 500:
                                    coin -= 500
                                    update_coin(username, coin)
                                    update_equipment(username,weapon[0])

                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True 
                            weapon_str = '/'.join(weapon_list)
                            user_backpack[2] = str(weapon_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            weapon_list = user_backpack[2].split('/')
                            if 'hammer' in weapon_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 1000 :
                                    coin -= 1000
                                    update_coin(username, coin)
                                    update_equipment(username,weapon[1])

                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True   


                            weapon_str = '/'.join(weapon_list)
                            user_backpack[2] = str(weapon_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if buy_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            weapon_list = user_backpack[2].split('/')
                            if 'sword' in weapon_list :
                                backpack(username, lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 2000 :
                                    coin -= 2000
                                    update_coin(username, coin)
                                    update_equipment(username,weapon[2])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                        if no :
                                            no = False
                                        else :
                                            no = True

                            weapon_str = '/'.join(weapon_list)
                            user_backpack[2] = str(weapon_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button4.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            weapon_list = user_backpack[2].split('/')
                            if 'shield3' in weapon_list :
                                backpack(username, lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 500 :
                                    coin -= 500
                                    update_coin(username, coin)
                                    update_equipment(username,weapon[3])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True                                        
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            weapon_str = '/'.join(weapon_list)
                            user_backpack[2] = str(weapon_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button5.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            weapon_list = user_backpack[2].split('/')
                            if 'shield4' in weapon_list :
                                backpack(username, lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 1000 :
                                    coin -= 1000
                                    update_coin(username, coin)
                                    update_equipment(username,weapon[4])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            weapon_str = '/'.join(weapon_list)
                            user_backpack[2] = str(weapon_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button6.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            weapon_list = user_backpack[2].split('/')
                            if 'shield5' in weapon_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 2000 :
                                    coin -= 2000
                                    update_coin(username, coin)
                                    update_equipment(username,weapon[5])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            weapon_str = '/'.join(weapon_list)
                            user_backpack[2] = str(weapon_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if next_button.check_input(pos_mouse):
                    equipment(username, lvl, coin, pull, chicky, equip, stats)
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, chicky, equip, stats)           

        if buy :
            bought1(username, lvl, coin, pull, chicky, equip, stats)
        elif no :
            no_money(username, lvl, coin, pull, chicky, equip, stats)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def bought1(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You bought an item.',True,'white'),(280,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    on = True
    while on :
        for event in pygame.event.get():
            if event.type == pygame.quit:
                on = False
                pygame.quit()
                sys.exit()      
                      
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)
        
        Manager.update(UI_REFRESH_RATE)
        pygame.display.flip()


def bought2(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You bought an item.',True,'white'),(280,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def bought3(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You bought an item.',True,'white'),(280,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))

    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def no_money(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def no_money2(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def no_money3(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this too

    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def equipment(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo did this also
    on = True
    buy = False
    no = False
    armor3 = Button("graphic/noob armor.png",150,205,1,'')
    armor4= Button("graphic/noob armor.png",450,205,1,'')
    armor5= Button("graphic/noob armor.png",750,205,1,'')
    shoe3 = Button("graphic/leg.png",150,460,1,'')
    shoe4= Button("graphic/leg.png",450,460,1,'')
    shoe5= Button("graphic/noob leg.png",750,460,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Store')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #Coin Display
        coinlogo = Lock('graphic/manycoin.png', 660, 70, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (750,70))
        screen.blit(coin_text, coin_text_rect)
        ###############

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Store', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(150)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        armor3.draw(screen)
        armor4.draw(screen)
        armor5.draw(screen)
        shoe3.draw(screen)
        shoe4.draw(screen)
        shoe5.draw(screen)
        #################

        #PRICE
        ####armor3#####
        price_text = font.render(f"{500}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,305))
        screen.blit(price_text, text_rect)
        ######armor4#####        
        price_text = font.render(f"{1000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,305))
        screen.blit(price_text, text_rect)
        #######aRmor5#########        
        price_text = font.render(f"{2000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,305))
        screen.blit(price_text, text_rect)
        ####nleg1#####
        price_text = font.render(f"{500}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,555))
        screen.blit(price_text, text_rect)
        ######leg2#####        
        price_text = font.render(f"{1000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,555))
        screen.blit(price_text, text_rect)
        #######leg3#########        
        price_text = font.render(f"{2000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,555))
        screen.blit(price_text, text_rect)


        # BUY BUTTONS
        buy_button1 = Button('graphic/button2.png', 150, 350, 0.15, "BUY")
        buy_button2 = Button('graphic/button2.png', 450, 350, 0.15, "BUY")
        buy_button3 = Button('graphic/button2.png', 750, 350, 0.15, "BUY")
        buy_button4 = Button('graphic/button2.png', 150, 600, 0.15, "BUY")
        buy_button5 = Button('graphic/button2.png', 450, 600, 0.15, "BUY")
        buy_button6 = Button('graphic/button2.png', 750, 600, 0.15, "BUY")
        #########

        #view button#
        view_button1 = Button('graphic/button2.png', 150, 350, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 350, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 350, 0.15, "VIEW")
        view_button4 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button5 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button6 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #############

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #SAving Data
        equipments = ('armor3','armor4','armor5','shoe3','shoe4','shoe5')

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[2].split('/')
                    if 'armor3' in equipments_list :
                        view_button1.draw(screen)
                    elif 'armor3' not in equipments_list :
                        buy_button1.draw(screen)
                    if 'armor4' in equipments_list :
                        view_button2.draw(screen)
                    elif 'armor4' not in equipments_list :
                        buy_button2.draw(screen)
                    if 'armor5' in equipments_list :
                        view_button3.draw(screen)
                    elif 'armor5' not in equipments_list :
                        buy_button3.draw(screen)
                    if 'shoe3' in equipments_list :
                        view_button4.draw(screen)
                    elif 'shoe3' not in equipments_list :
                        buy_button4.draw(screen)
                    if 'shoe4' in equipments_list :
                        view_button5.draw(screen)
                    elif 'shoe4' not in equipments_list :
                        buy_button5.draw(screen)
                    if 'shoe5' in equipments_list :
                        view_button6.draw(screen)
                    elif 'shoe5' not in equipments_list :
                        buy_button6.draw(screen)

                weapon_str = '/'.join(equipments_list)
                user_backpack[3] = str(weapon_str)
                lines[i] = ', '.join(user_backpack) + '\n'
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if armor3.check_input(pos_mouse):
                    armor3_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if armor4.check_input(pos_mouse):
                    armor4_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if armor5.check_input(pos_mouse):
                    armor5_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shoe3.check_input(pos_mouse):
                    shoe3_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shoe4.check_input(pos_mouse):
                    shoe4_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if shoe5.check_input(pos_mouse):
                    shoe5_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'armor3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 500 :
                                    coin -= 500
                                    update_coin(username, coin)
                                    update_equipment(username, equipments[0])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'armor4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 1000 :
                                    coin -= 1000
                                    update_coin(username, coin)
                                    update_equipment(username, equipments[1])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if buy_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'armor5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 2000 :
                                    coin -= 2000
                                    update_coin(username, coin)
                                    update_equipment(username, equipments[2])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if buy_button4.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'shoe3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 500 :
                                    coin -= 500
                                    update_coin(username, coin)
                                    update_equipment(username, equipments[3])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button5.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'shoe4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 1000 :
                                    coin -= 1000
                                    update_coin(username, coin)
                                    update_equipment(username, equipments[4])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if buy_button6.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'shoe5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 2000 :
                                    coin -= 2000
                                    update_coin(username, coin)
                                    update_equipment(username, equipments[5])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if back_button.check_input(pos_mouse):
                    store(username, lvl, coin, pull, chicky, equip, stats)
                if next_button.check_input(pos_mouse):
                    equipment2(username, lvl, coin, pull, chicky, equip, stats)

        if buy :
            bought2(username, lvl, coin, pull)
        elif no :
            no_money2(username, lvl, coin, pull)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def equipment2(username, lvl, coin, pull, chicky, equip, stats) :
    #puopuo also did this
    on = True
    buy = False
    no = False
    helmet3= Button("graphic/noob helmet.png",150,205,1,'')
    helmet4 = Button("graphic/noob helmet.png",450,205,1,'')
    helmet5 = Button("graphic/noob helmet.png",750,205,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Store')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #Coin Display
        coinlogo = Lock('graphic/manycoin.png', 660, 70, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (750,70))
        screen.blit(coin_text, coin_text_rect)
        ###############

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Store', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(150)
        wishing_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, wishing_surface_rect)

        #EQUIPMENT DIsPLAY
        helmet3.draw(screen)
        helmet4.draw(screen)
        helmet5.draw(screen)

        #################

        #PRICE
        #####helmet3####
        price_text = font.render(f"{500}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,305))
        screen.blit(price_text, text_rect)
        ######helmet4######
        price_text = font.render(f"{1000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,305))
        screen.blit(price_text, text_rect)
        ######helmet 5######
        price_text = font.render(f"{2000}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,305))
        screen.blit(price_text, text_rect)

        # BUY BUTTONS
        buy_button1 = Button('graphic/button2.png', 150, 350, 0.15, "BUY")
        buy_button2 = Button('graphic/button2.png', 450, 350, 0.15, "BUY")
        buy_button3 = Button('graphic/button2.png', 750, 350, 0.15, "BUY")
        #########

        #view button#
        view_button1 = Button('graphic/button2.png', 150, 350, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 350, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 350, 0.15, "VIEW")
        #############

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Data saving
        equipments2 =('helmet3','helmet4','helmet5')

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[2].split('/')
                    if 'helmet3' in equipments_list :
                        view_button1.draw(screen)
                    elif 'helmet3' not in equipments_list :
                        buy_button1.draw(screen)
                    if 'helmet4' in equipments_list :
                        view_button2.draw(screen)
                    elif 'helmet4' not in equipments_list :
                        buy_button2.draw(screen)
                    if 'helmet5' in equipments_list :
                        view_button3.draw(screen)
                    elif 'helmet5' not in equipments_list :
                        buy_button3.draw(screen)

                weapon_str = '/'.join(equipments_list)
                user_backpack[3] = str(weapon_str)
                lines[i] = ', '.join(user_backpack) + '\n'
                break
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if helmet3.check_input(pos_mouse):
                    helmet3_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if helmet4.check_input(pos_mouse):
                    helmet4_info(username, lvl, coin, pull, chicky, equip, stats)

            if event.type == pygame.MOUSEBUTTONDOWN:
                if helmet5.check_input(pos_mouse):
                    helmet5_info(username, lvl, coin, pull, chicky, equip, stats)

            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'helmet3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 500 :
                                    coin -= 500
                                    update_coin(username, coin)
                                    update_equipment(username, equipments2[0])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                                                         
                        
                if buy_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'helmet4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 1000 :
                                    coin -= 1000
                                    update_coin(username, coin)
                                    update_equipment(username, equipments2[1])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'helmet5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                if coin >= 2000 :
                                    coin -= 2000
                                    update_coin(username, coin)
                                    update_equipment(username, equipments2[2])
                                    if buy :
                                        buy = False
                                    else :
                                        buy = True
                                else :
                                    if no :
                                        no = False
                                    else :
                                        no = True

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                

                if back_button.check_input(pos_mouse):
                    equipment(username, lvl, coin, pull, chicky, equip, stats)
                
        if buy :
            bought3(username, lvl, coin, pull, chicky, equip, stats)
        elif no :
            no_money3(username, lvl, coin, pull, chicky, equip, stats)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def arcade_lobby(username, lvl, coin, pull, chicky, equip, stats):
    ## also puo puo did this
    on = True
    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)
                            
    while on:
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('ARCADE', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        #MODE Display#

        #BUTTONS
        play_button1 = Button('graphic/button2.png', 250, 500, 0.2, "PLAY")
        play_button1.draw(screen)
        play_button2 = Button('graphic/button2.png', 650, 500, 0.2, "PLAY")
        play_button2.draw(screen)
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button1.check_input(pos_mouse):
                    snake_lobby(username, lvl, coin, pull, chicky, equip, stats)                                   
                        
                if play_button2.check_input(pos_mouse):
                    dunno1_lobby(username, lvl, coin, pull, chicky, equip, stats)

                if back_button.check_input(pos_mouse):
                    choose_level(username, lvl, coin, pull, chicky, equip, stats)           

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def snake_lobby(username, lvl, coin, pull, chicky, equip, stats) :
    # puo puo did also this
    on = True
    while on :
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption('Chicky Simulator - Chick Game')
        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('Chick Game', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,100))
        screen.blit(title_text, title_text_rect)

        #buttons#
        back_button = Button('graphic/botton1.png', 50, 35, 0.5, "<<")
        back_button.draw(screen)
        play_button = Button('graphic/button2.png', 450, 600, 0.3, "START")
        play_button.draw(screen)

        #tutorial


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if back_button.check_input(pos_mouse):
                    arcade_lobby(username, lvl, coin, pull, chicky, equip, stats)
                if play_button.check_input(pos_mouse):
                    snake(username, lvl, coin, pull, chicky, equip, stats)
        
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def dunno1_lobby(username, lvl, coin, pull, chicky, equip, stats) :
    # puo puo did also this
    on = True
    while on :
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption('Chicky Simulator - Unnamed yet')
        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('Unnamed', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,100))
        screen.blit(title_text, title_text_rect)

        #buttons#
        back_button = Button('graphic/botton1.png', 50, 35, 0.5, "<<")
        back_button.draw(screen)
        play_button = Button('graphic/button2.png', 450, 600, 0.3, "START")
        play_button.draw(screen)

        #tutorial


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if back_button.check_input(pos_mouse):
                    arcade_lobby(username, lvl, coin, pull, chicky, equip, stats)
        
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def collection(username, lvl, coin, pull, chicky, equip, stats) :
    ##puo puo did this
    on = True
    buy = False
    no = False
    sword = pygame.image.load("graphic/sword.png")
    shield = pygame.image.load("graphic/shield.png")
    bow = pygame.image.load("graphic/bow.png")
    x_bow = pygame.image.load("graphic/x-bow.png")
    hammer= pygame.image.load("graphic/hammer.png")
    axe= pygame.image.load("graphic/axe.png")
    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)

    while on:
        pygame.display.set_caption('Chicky Simulator - Collection')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #####Text Display
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Collection', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(150)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)
        #########

        #EQUIPMENT DisPLAY
        screen.blit(sword,(85,130))
        screen.blit(shield,(380,130))
        screen.blit(bow,(680,130))
        screen.blit(x_bow,(85,375))
        screen.blit(hammer,(380,375))
        screen.blit(axe,(680,375))
        #################

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if sword.check_input(pos_mouse):
                    sword(username, lvl, coin, pull, chicky, equip, stats)


def axe_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Axe\n3-Star\nATK+10',True,'white'),(5,5))
        screen.blit(surface,(80,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def hammer_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Hammer\n4-Star\nATK+20',True,'white'),(5,5))
        screen.blit(surface,(380,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def sword_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Sword\n5-Star\nATK+30',True,'white'),(5,5))
        screen.blit(surface,(680,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def shoe3_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Boots\n3-Star\nSPEED+2',True,'white'),(5,5))
        screen.blit(surface,(80,375))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def shoe4_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Boots\n4-Star\nSPEED+4',True,'white'),(5,5))
        screen.blit(surface,(380,375))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def shoe5_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Boots\n5-Star\nSPEED+6',True,'white'),(5,5))
        screen.blit(surface,(680,375))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def shield3_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Shield\n3-Star\nDEF+5',True,'white'),(5,5))
        screen.blit(surface,(80,375))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def shield4_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Shield\n4-Star\nDEF+7',True,'white'),(5,5))
        screen.blit(surface,(380,375))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def shield5_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Shield\n5-Star\nDEF+10',True,'white'),(5,5))
        screen.blit(surface,(680,375))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def helmet3_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Helmet\n3-Star\nDEF+5',True,'white'),(5,5))
        screen.blit(surface,(80,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def helmet4_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Helmet\n4-Star\nDEF+7',True,'white'),(5,5))
        screen.blit(surface,(380,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def helmet5_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Helmet\n5-Star\nDEF+10',True,'white'),(5,5))
        screen.blit(surface,(680,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def armor3_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Armor\n3-Star\nDEF+5',True,'white'),(5,5))
        screen.blit(surface,(80,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def armor4_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Armor\n4-Star\nDEF+7',True,'white'),(5,5))
        screen.blit(surface,(380,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def armor5_info(username, lvl, coin, pull, chicky, equip, stats) :

    while True :

        surface = pygame.Surface((175,195))
        surface.blit(ranking_image,(0,0))
        surface.blit(font.render('Armor\n5-Star\nDEF+10',True,'white'),(5,5))
        screen.blit(surface,(680,130))

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull, chicky, equip, stats)
            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def collection(username, lvl, coin, pull, chicky, equip, stats):
    on = True
    armor3 = Button("graphic/noob armor.png",150,205,1,'')
    armor4= Button("graphic/noob armor.png",450,205,1,'')
    armor5= Button("graphic/noob armor.png",750,205,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Collection')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Collections', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface big
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(140)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(150,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(450,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(750,450))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        armor3.draw(screen)
        armor4.draw(screen)
        armor5.draw(screen)
        #################

        ####armor3#####
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Leather Armor', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('3-Star Armor\nMade by Leather\nBeginner Friendly\nIncrease max HP\nBest in level 1-9\n\n        DEF+5', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,450))
        screen.blit(info_text, text_rect)
        ######armor4#####        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Iron Armor', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('4-Star Armor\nMade by Iron\nMid-Tier Armor\nIncrease max HP\nBest in level 1-19\n\n        DEF+7', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,450))
        screen.blit(info_text, text_rect)
        #######aRmor5#########        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Diamond Armor', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('5-Star Armor\nMade by DIAMOND\nTop-Tier Armor\nIncrease max HP\nit\'s Perfect!!!\nit\'s Unstoppable in\n all level\n\n        DEF+10', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,450))
        screen.blit(info_text, text_rect)

        # Get BUTTONS
        get_button1 = Button('graphic/button2.png', 150, 600, 0.15, "GET")
        get_button2 = Button('graphic/button2.png', 450, 600, 0.15, "GET")
        get_button3 = Button('graphic/button2.png', 750, 600, 0.15, "GET")
        #########

        # view BUTTONS
        view_button1 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[3].split('/')
                    if 'armor3' in equipments_list :
                        view_button1.draw(screen)
                    elif 'armor3' not in equipments_list :
                        get_button1.draw(screen)
                    if 'armor4' in equipments_list :
                        view_button2.draw(screen)
                    elif 'armor4' not in equipments_list :
                        get_button2.draw(screen)
                    if 'armor5' in equipments_list :
                        view_button3.draw(screen)
                    elif 'armor5' not in equipments_list :
                        get_button3.draw(screen)

                weapon_str = '/'.join(equipments_list)
                user_backpack[3] = str(weapon_str)
                lines[i] = ', '.join(user_backpack) + '\n'
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'armor3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)    

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if get_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'armor4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if get_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'armor5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                    
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, chicky, equip, stats)
                if next_button.check_input(pos_mouse):
                    collection2(username, lvl, coin, pull, chicky, equip, stats)


        pygame.display.flip()

    pygame.quit()
    sys.exit()


def collection2(username, lvl, coin, pull, chicky, equip, stats):
    on = True
    helmet3= Button("graphic/noob helmet.png",150,205,1,'')
    helmet4 = Button("graphic/noob helmet.png",450,205,1,'')
    helmet5 = Button("graphic/noob helmet.png",750,205,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Collection')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Collections', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface big
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(140)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(150,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(450,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(750,450))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        helmet3.draw(screen)
        helmet4.draw(screen)
        helmet5.draw(screen)
        #################

        ####armor3#####
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Leather HElmet', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('3-Star Helmet\nMade by Leather\nBeginner Friendly\nProvide Few DEF\nBest in level 1-9\n\n        def+5', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,450))
        screen.blit(info_text, text_rect)
        ######armor4#####        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Iron Helmet', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('4-Star Helmet\nMade by Iron\nMid-Tier Helmet\nProvide More DEF\nBest in level 1-19\n\n        DEF+7', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,450))
        screen.blit(info_text, text_rect)
        #######aRmor5#########        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Diamond Helmet', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('5-Star Helmet\nMade by DIAMOND\nTop-Tier Helmet\nProvide a LOT DEF\nit\'s Perfect!!!\nit\'s Unstoppable in\n all level\n\n        def+10', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,450))
        screen.blit(info_text, text_rect)

        # Get BUTTONS
        get_button1 = Button('graphic/button2.png', 150, 600, 0.15, "GET")
        get_button2 = Button('graphic/button2.png', 450, 600, 0.15, "GET")
        get_button3 = Button('graphic/button2.png', 750, 600, 0.15, "GET")
        #########

        # view BUTTONS
        view_button1 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[3].split('/')
                    if 'helmet3' in equipments_list :
                        view_button1.draw(screen)
                    elif 'helmet3' not in equipments_list :
                        get_button1.draw(screen)
                    if 'helmet4' in equipments_list :
                        view_button2.draw(screen)
                    elif 'helmet4' not in equipments_list :
                        get_button2.draw(screen)
                    if 'helmet5' in equipments_list :
                        view_button3.draw(screen)
                    elif 'helmet5' not in equipments_list :
                        get_button3.draw(screen)

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'helmet3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment2(username, lvl, coin, pull, chicky, equip, stats)    

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if get_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'helmet4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment2(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if get_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'helmet5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment2(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                    
                if back_button.check_input(pos_mouse):
                    collection(username, lvl, coin, pull, chicky, equip, stats)
                if next_button.check_input(pos_mouse):
                    collection3(username, lvl, coin, pull, chicky, equip, stats)


        pygame.display.flip()

    pygame.quit()
    sys.exit()


def collection3(username, lvl, coin, pull, chicky, equip, stats):
    on = True
    shoe3 = Button("graphic/leg.png",150,205,1,'')
    shoe4= Button("graphic/leg.png",450,205,1,'')
    shoe5= Button("graphic/noob leg.png",750,205,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Collection')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Collections', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface big
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(140)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(150,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(450,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(750,450))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        shoe3.draw(screen)
        shoe4.draw(screen)
        shoe5.draw(screen)
        #################

        ####armor3#####
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Leather boots', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('3-Star boots\nMade by Leather\nBeginner Friendly\nfinish 100m in 12sec\nBest in level 1-9\n\n       Speed+2', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,450))
        screen.blit(info_text, text_rect)
        ######armor4#####        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Iron boots', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('4-Star boots\nMade by Iron\nMid-Tier boots\nOMG!usain bolt!\nBest in level 1-19\n\n       Speed+4', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,450))
        screen.blit(info_text, text_rect)
        #######aRmor5#########        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Diamond boots', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('5-Star boots\nMade by DIAMOND\nTop-Tier boots\nThat\'s the flash!!\nit\'s Perfect!!!\nit\'s Unstoppable in\n all level\n\n       Speed+6', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,450))
        screen.blit(info_text, text_rect)

        # Get BUTTONS
        get_button1 = Button('graphic/button2.png', 150, 600, 0.15, "GET")
        get_button2 = Button('graphic/button2.png', 450, 600, 0.15, "GET")
        get_button3 = Button('graphic/button2.png', 750, 600, 0.15, "GET")
        #########

        # view BUTTONS
        view_button1 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[3].split('/')
                    if 'shoe3' in equipments_list :
                        view_button1.draw(screen)
                    elif 'shoe3' not in equipments_list :
                        get_button1.draw(screen)
                    if 'shoe4' in equipments_list :
                        view_button2.draw(screen)
                    elif 'shoe4' not in equipments_list :
                        get_button2.draw(screen)
                    if 'shoe5' in equipments_list :
                        view_button3.draw(screen)
                    elif 'shoe5' not in equipments_list :
                        get_button3.draw(screen)

            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'shoe3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)    

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if get_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'shoe4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if get_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[3].split('/')
                            if 'shoe5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[3] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if back_button.check_input(pos_mouse):
                    collection2(username, lvl, coin, pull, chicky, equip, stats)
                if next_button.check_input(pos_mouse):
                    collection4(username, lvl, coin, pull, chicky, equip, stats)


        pygame.display.flip()

    pygame.quit()
    sys.exit()


def collection4(username, lvl, coin, pull, chicky, equip, stats):
    on = True
    shield3 = Button("graphic/shield.png",150,205,1,'')
    shield4= Button("graphic/shield.png",450,205,1,'')
    shield5= Button("graphic/shield.png",750,205,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Collection')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Collections', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface big
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(140)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(150,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(450,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(750,450))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        shield3.draw(screen)
        shield4.draw(screen)
        shield5.draw(screen)
        #################

        ####armor3#####
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Wooden Shield', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('3-Star shield\nMade by Leather\nBeginner Friendly\nAbsorb few damage\nBest in level 1-9\n\n        DEF+5', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,450))
        screen.blit(info_text, text_rect)
        ######armor4#####        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Iron Shield', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('4-Star shield\nMade by Iron\nMid-Tier shield\nimmune from tyson\nBest in level 1-19\n\n       DEF+7', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,450))
        screen.blit(info_text, text_rect)
        #######aRmor5#########        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Diamond Shield', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('5-Star shield\nMade by DIAMOND\nTop-Tier shield\nWho can kill you?\nit\'s Perfect!!!\nit\'s Unstoppable in\n all level\n\n        DEF+10', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,450))
        screen.blit(info_text, text_rect)

        # Get BUTTONS
        get_button1 = Button('graphic/button2.png', 150, 600, 0.15, "GET")
        get_button2 = Button('graphic/button2.png', 450, 600, 0.15, "GET")
        get_button3 = Button('graphic/button2.png', 750, 600, 0.15, "GET")
        #########

        # view BUTTONS
        view_button1 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[2].split('/')
                    if 'shield3' in equipments_list :
                        view_button1.draw(screen)
                    elif 'shield3' not in equipments_list :
                        get_button1.draw(screen)
                    if 'shield4' in equipments_list :
                        view_button2.draw(screen)
                    elif 'shield4' not in equipments_list :
                        get_button2.draw(screen)
                    if 'shield5' in equipments_list :
                        view_button3.draw(screen)
                    elif 'shield5' not in equipments_list :
                        get_button3.draw(screen)


            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'shield3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                store(username, lvl, coin, pull, chicky, equip, stats)    

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if get_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'shield4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                store(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if get_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'shield5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                store(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if back_button.check_input(pos_mouse):
                    collection3(username, lvl, coin, pull, chicky, equip, stats)
                if next_button.check_input(pos_mouse):
                    collection5(username, lvl, coin, pull, chicky, equip, stats)


        pygame.display.flip()

    pygame.quit()
    sys.exit()


def collection5(username, lvl, coin, pull, chicky, equip, stats):
    on = True
    axe= Button("graphic/axe.png",150,205,1,'')
    hammer = Button("graphic/hammer.png",450,205,1,'')
    sword = Button("graphic/sword.png",750,205,1,'')
                            
    while on:
        pygame.display.set_caption('Chicky Simulator - Collection')
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()

        #####Text Display        
        store_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Collections', True, 'white')
        store_text_rect = store_text.get_rect(center = (450,70))
        screen.blit(store_text, store_text_rect)
        #################

        #white surface big
        store_surface = pygame.Surface((850,500))
        store_surface.fill('white')
        store_surface.set_alpha(140)
        store_surface_rect = store_surface.get_rect(center=(width/2,380))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(150,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(450,450))
        screen.blit(store_surface, store_surface_rect)
        #white surface 1
        store_surface = pygame.Surface((230,240))
        store_surface.fill('white')
        store_surface.set_alpha(200)
        store_surface_rect = store_surface.get_rect(center=(750,450))
        screen.blit(store_surface, store_surface_rect)

        #EQUIPMENT DIsPLAY
        axe.draw(screen)
        hammer.draw(screen)
        sword.draw(screen)
        #################

        ####armor3#####
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('axe', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('3-Star weapon\nMade by iron\nBeginner Friendly\nEasy cutting trees\nBest in level 1-9\n\n        atk+10', True, (0,0,0))
        text_rect = info_text.get_rect(center =(150,450))
        screen.blit(info_text, text_rect)
        ######armor4#####        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('hammer', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('4-Star weapon\nMade by Iron\nMid-Tier weapon\n4 hit to destroy Car\nBest in level 1-19\n\n       atk+20', True, (0,0,0))
        text_rect = info_text.get_rect(center =(450,450))
        screen.blit(info_text, text_rect)
        #######aRmor5#########        
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('sword', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,305))
        screen.blit(info_text, text_rect)
        info_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render('5-Star weapond\nMade by DIAMOND\nTop-Tier weapon\nOnly 1 thing to do:\nKILLLLLLLLL!!!\nit\'s Perfect!!!\nit\'s Unstoppable in\n all level\n        atk+30', True, (0,0,0))
        text_rect = info_text.get_rect(center =(750,450))
        screen.blit(info_text, text_rect)

        # Get BUTTONS
        get_button1 = Button('graphic/button2.png', 150, 600, 0.15, "GET")
        get_button2 = Button('graphic/button2.png', 450, 600, 0.15, "GET")
        get_button3 = Button('graphic/button2.png', 750, 600, 0.15, "GET")
        #########

        # view BUTTONS
        view_button1 = Button('graphic/button2.png', 150, 600, 0.15, "VIEW")
        view_button2 = Button('graphic/button2.png', 450, 600, 0.15, "VIEW")
        view_button3 = Button('graphic/button2.png', 750, 600, 0.15, "VIEW")
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)


        #check user got or no
        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()        
            for i, line in enumerate(lines):
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    equipments_list = user_backpack[2].split('/')
                    if 'axe' in equipments_list :
                        view_button1.draw(screen)
                    elif 'axe' not in equipments_list :
                        get_button1.draw(screen)
                    if 'hammer' in equipments_list :
                        view_button2.draw(screen)
                    elif 'hammer' not in equipments_list :
                        get_button2.draw(screen)
                    if 'sword' in equipments_list :
                        view_button3.draw(screen)
                    elif 'sword' not in equipments_list :
                        get_button3.draw(screen)


            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            

            if event.type == pygame.MOUSEBUTTONDOWN:
                if get_button1.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'axe' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                store(username, lvl, coin, pull, chicky, equip, stats)    

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if get_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'hammer' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                store(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if get_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
                            if 'sword' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                store(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if back_button.check_input(pos_mouse):
                    collection4(username, lvl, coin, pull, chicky, equip, stats)



        pygame.display.flip()

    pygame.quit()
    sys.exit()


def snake(username, lvl, coin, pull, chicky, equip, stats) :

    width, height = 900, 700
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator - Arcade Mode - Chick Game')
    background_image = pygame.image.load('graphic/map.jpg')
    coin_image = pygame.image.load('graphic/manycoin.png')
    coin_image = pygame.transform.scale(coin_image, (50, 50))
    pygame.transform.scale(background_image,(700,700))
    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    clock = pygame.time.Clock()
    Manager = pygame_gui.UIManager((width,height))
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    UI_REFRESH_RATE = clock.tick(60)
    chick_images = [pygame.image.load('graphic/geekchic.png'),
    pygame.image.load('graphic/monster2.png'),
    pygame.image.load('graphic/monster1.png'),
    pygame.image.load('graphic/monster3.png')]
    ticks = pygame.time.get_ticks()


    on = True
    time = 0
    coin = 0
    chick_position = [50, 50]
    chick_speed = 15
    chick_body =[[30,30]]
    direction = 'RIGHT'
    change_to = direction
    coin_position = [random.randrange(1,width//35)* 15,random.randrange(1,height//35)* 15]
    coin_spawn = True
    chick_index = 0
    # [0,0,0]
    
    def game_over(username, lvl, coin, pull, chicky, equip, stats) :
        font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)
        # coin_text = font.render(f"hi", True, (255,255,255))
        # text_rect = coin_text.get_rect(center = (width//2,height//2))
        # text_rect.midtop = (width/2,height/4)
        # screen.blit(coin_text, text_rect)
        # pygame.display.flip()

        on = True

        while on :
            screen.blit(background_image,(0,0))
            screen.blit(font.render(f'Your score is : {coin} ',True,'white'),(280,300))
            screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
            pygame.display.flip()
            # pygame.time.wait(5000)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    lobby(username, lvl, coin, pull, chicky, equip, stats)

                if event.type == pygame.QUIT:
                    on = False
                    sys.exit()

            pygame.display.flip()
    
    while on :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    change_to = 'UP'
                if event.key == pygame.K_s:
                    change_to = 'DOWN'
                if event.key == pygame.K_a:
                    change_to = 'LEFT'
                if event.key == pygame.K_d:
                    change_to = 'RIGHT'
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            chick_position[1] -= 10
        if direction == 'DOWN':
            chick_position[1] += 10
        if direction == 'LEFT':
            chick_position[0] -= 10
        if direction == 'RIGHT':
            chick_position[0] += 10

        chick_body.insert(0, list(chick_position))

        if chick_position[0] == coin_position[0] or chick_position[1] == coin_position[1]:
            coin += 1
            coin_spawn = False
            chick_index =(chick_index + 1) % len(chick_images)
            # new_chick = (chick_index + 1) % len(chick_images)
            # chick_index.insert(0,new_chick)
        else:
            chick_body.pop()
            # chick_index.pop(0)
            
        if not coin_spawn:
            coin_position = [random.randrange(1, (width//35)) * 15, random.randrange(1, (height//35)) * 15]
            
        coin_spawn = True

        screen.blit(background_image,(0,0))

        for index , position in enumerate(chick_body):
            chick_image = pygame.transform.scale(chick_images[chick_index],(50, 50))
            screen.blit(chick_image,pygame.Rect(position[0],position[1],50,50))
            
        screen.blit(coin_image, pygame.Rect(coin_position[0], coin_position[1], 35, 35))
    # [chick_index[index]]
        # Game Over conditions
        #left right
        if chick_position[0] < 0 or chick_position[0] > width-35:
            game_over(username, lvl, coin, pull, chicky, equip, stats)
        #up down
        if chick_position[1] < 0 or chick_position[1] > height-35:
            game_over(username, lvl, coin, pull, chicky, equip, stats)
        
        #timer
        time = 60 - (pygame.time.get_ticks() - ticks) // 1000
        if time <= 0 :
            game_over(username, lvl, coin, pull, chicky, equip, stats)

        #collision
        for block in chick_body[1:]:
            if chick_position == block:
                game_over(username, lvl, coin, pull, chicky, equip, stats)
        
        timer_text = font.render(f"{time}", True, (255,255,255))
        text_rect = timer_text.get_rect(center = (width//2,50))
        screen.blit(timer_text, text_rect)

        coin_text = font.render(f"{coin}", True, (255,255,255))
        text_rect = coin_text.get_rect(center = (750,50))
        screen.blit(coin_text, text_rect)

        pygame.display.update()

        clock.tick(chick_speed)
    

log_or_reg()
