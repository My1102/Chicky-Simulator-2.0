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
def caution(c, lvl, username, coin, pull):
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
                    tutorial2(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    choose_level(c, lvl, username, coin, pull)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def tutorial1(c, lvl, username, coin, pull):
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
                    caution(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    choose_level(c, lvl, username, coin, pull)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()        


def tutorial2(c, lvl, username, coin, pull):
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
                    leveltest(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    choose_level(c, lvl, username, coin, pull)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()   


def tutorial4(c, lvl, username, coin, pull):
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
                    level3(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    choose_level(c, lvl, username, coin, pull)

        pygame.display.update()   


def tutorial3(c, lvl, username, coin, pull):
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
                    level2(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    choose_level(c, lvl, username, coin, pull)

        pygame.display.update()   


def leveltest(c, lvl, username, coin, pull):
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
    UI_REFRESH_RATE = clock.tick(60)/1000

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
        def __init__(self,x,y):
                    chic = pygame.image.load(c)
                    self.image = pygame.transform.scale(chic,(30,30))
                    self.rect = self.image.get_rect(center=(17,17))
                    self.rect.x = x
                    self.rect.y = y

        def update(self,gameover):
            dx = 0 
            dy = 0 

            if gameover == 0:
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
                    if self.rect.y>height :
                        self.rect.y=height
                if key[pygame.K_d]:
                    dx += 3
                    if self.rect.x>width :
                        self.rect.x=width
                
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
                            
                # collision with monsters(This one jy use sprite collide becoz they are moving objects)
                if pygame.sprite.spritecollide(self,yuen_group,False):
                    gameover = -1
                if pygame.sprite.spritecollide(self,jy_group,False):
                    gameover = -1
                if pygame.sprite.spritecollide(self,puolin_group,False):
                    gameover = -1

            elif gameover == -1 :
                self.rect.x = 35
                self.rect.y = 35
            
            self.rect.x += dx
            self.rect.y += dy

            screen.blit(self.image,self.rect)

            return gameover

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
                        yuen = Monster1(col_count * tile_size,row_count * tile_size)
                        yuen_group.add(yuen)
                        
                    if tile == 4 :
                        jy = Monster3(col_count * tile_size,row_count * tile_size)
                        jy_group.add(jy)

                    if tile == 5 :
                        puolin = Monster2(col_count * tile_size,row_count * tile_size)
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
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster1.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
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

    class Monster2(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster2.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
                    

    class Monster3(pygame.sprite.Sprite):
        def __init__(self,x,y):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster3.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0
            
        def update(self):
            self.rect.y += self.move_direction
            self.move_counter += 1
            if self.move_counter > 250 :
                self.move_direction *= -1
                self.move_counter *= -1

    class Exit(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('graphic/bananacat.png')
            self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            
    Chicky = chicky(35,35)

    yuen_group = pygame.sprite.Group()
    puolin_group = pygame.sprite.Group()
    jy_group = pygame.sprite.Group()  
    exit_group = pygame.sprite.Group() 

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

        # if main_menu == True:
        #     if exit_button.draw():
        #         run = False
        #     if start_button.draw():
        #         main_menu = False

        # else:
        world.draw()

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

        if gameover == 0:
            jy_group.update()
            yuen_group.update()
            puolin_group.update()

        jy_group.draw(screen)
        yuen_group.draw(screen)
        puolin_group.draw(screen)
        # coin_group.draw(screen)
        # exit_group.draw(screen)

        gameover = Chicky.update(gameover)

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
                Chicky = chicky(35,35)
                gameover = 0
                update_level(username, lvl)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()


def level1(c, lvl, username, coin, pull): # This one easier to read
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
                            win(c, lvl, username, levl, coin, pull)
                            
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


def level2(c, lvl, username, coin, pull):
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
                            win(c, lvl, username, levl, coin, pull)
                            
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


def level3(c, lvl, username, coin, pull):
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
                            win(c, lvl, username, levl, coin, pull)
                            
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


def level4(c, lvl, username, coin, pull):
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
                            win(c, lvl, username, levl, coin, pull)
                            
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


def level5(c, lvl, username, coin, pull):
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
                            win5(c, lvl, username, coin, pull)
                            
                            
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


def win5(c, lvl, username, coin, pull):
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
                    choose_level(c, lvl, username, coin, pull)

                if rank_button.check_input(pos_mouse):
                    ranking(username, lvl, coin, pull)

        pygame.display.update()


def win(c, lvl, username, levl, coin, pull):
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
                    choose_level(c, lvl, username, coin, pull)

                if next_button.check_input(pos_mouse): #changed later
                    if levl == 2:
                        tutorial3(c, lvl, username, coin, pull)
                    elif levl == 3:
                        tutorial4(c, lvl, username, coin, pull)
                    elif levl == 4:
                        level4(c, lvl, username, coin, pull)
                    elif levl == 5:
                        level5(c, lvl, username, coin, pull)

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


def items(username, lvl, coin, times, itemget, pull):

    while True:
        pygame.display.set_caption('Chicky Simulator - Items Get')
        screen.blit(ranking_image,(0,0))

        wish_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Items Get', True, 'white')
        wish_text_rect = wish_text.get_rect(center = (450,100))
        screen.blit(wish_text, wish_text_rect)

        wishing_surface = pygame.Surface((700,350))
        wishing_surface.fill('white')
        wishing_surface.set_alpha(150)
        wishing_surface_rect = wishing_surface.get_rect(center=(width/2,350))
        screen.blit(wishing_surface, wishing_surface_rect)

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
                    wish(username, lvl, coin, pull)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def shooting_stars(username, lvl, coin, times, itemget, pull):

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
                            items(username, lvl, coin, times, itemget, pull)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull)

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
                            items(username, lvl, coin, times, itemget, pull)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull)

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
                            items(username, lvl, coin, times, itemget, pull)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull)

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
                            items(username, lvl, coin, times, itemget, pull)
                
                vid.close()
                items(username, lvl, coin, times, itemget, pull)

        pygame.display.update()


def wish(username, lvl, coin, pull):

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

        item = ('coin5','coin5',
                'coin10','coin10','coin10',
                'coin15','coin15','coin15','coin15',
                'coin20','coin20','coin20','coin20','coin20',
                'coin25','coin25','coin25','coin25','coin25',
                'coin30','coin30','coin30','coin30','coin30','coin30',
                'coin35','coin35','coin35','coin35','coin35',
                'coin40','coin40','coin40','coin40','coin40',
                'coin45','coin45','coin45','coin45',
                'coin50','coin50','coin50',
                'coin75','coin75',
                'coin90','kitty','tanker','worrier','speedy','magnet')
        
        chicky = ('kitty','tanker','worrier','speedy','magnet')

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull)

                if one_pull_button.check_input(pos_mouse):
                    if coin >= 100:
                        times = 1
                        coin -= 100
                        pull += 1

                        if pull < 50:
                            itemget = random.choice(item)
                            if itemget in chicky:
                                pull = 0
                        else:
                            pull = 0
                            itemget = random.choice(chicky)
                        
                        update_pull(username, pull)
                        update_coin(username, coin)
                        shooting_stars(username, lvl, coin, times, itemget, pull)
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
                            if pull < 50:
                                itemget = random.choice(item)
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
                        shooting_stars(username, lvl, coin, times, itemsget, pull)
                    else:
                        break

            Manager.process_events(event)

        pygame.display.update()


def ranking(username, lvl, coin, pull):
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
            for rank, (Username, Password, Level, Time, Coin, Pull) in enumerate(sorted_data[0:9], start=1):
                first = Ranking(130+(rank*50), str(rank), Username, Time)
                first.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def chick(username, lvl, coin, pull):
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
                    choose_level(c, lvl, username, coin, pull)

                if chick2_button.check_input(pos_mouse):
                    c = 'graphic/geekchic.png'
                    choose_level(c, lvl, username, coin, pull)

                if chick3_button.check_input(pos_mouse):
                    c = 'graphic/pinkchic.png'
                    choose_level(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull)

                Manager.process_events(event)
            
            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def choose_level(c, lvl, username, coin, pull):
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
                    tutorial1(c, lvl, username, coin, pull)

                if lvl2_button.check_input(pos_mouse):
                    if lock2_con == True:
                        tutorial3(c, lvl, username, coin, pull)

                if lvl3_button.check_input(pos_mouse):
                    if lock3_con == True:
                        tutorial4(c, lvl, username, coin, pull)

                if lvl4_button.check_input(pos_mouse):
                    if lock4_con == True:
                        level4(c, lvl, username, coin, pull)

                if lvl5_button.check_input(pos_mouse):
                    if lock5_con == True:
                        level5(c, lvl, username, coin, pull)

                if back_button.check_input(pos_mouse):
                    chick(username, lvl, coin, pull)
                
                if next_button.check_input(pos_mouse):
                    arcade_lobby(c,username, lvl, coin, pull)
            
            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def lobby(username, lvl, coin, pull):


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

        pos_mouse = pygame.mouse.get_pos()

        # get user events (their selections)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(pos_mouse):
                    chick(username, lvl, coin, pull)  

                if rank_button.check_input(pos_mouse):
                    ranking(username, lvl, coin, pull)
                
                if wish_button.check_input(pos_mouse):
                    wish(username, lvl, coin, pull)
                
                if back_button.check_input(pos_mouse):
                    log_or_reg()
                
                if store_button.check_input(pos_mouse):
                    store(username, lvl, coin, pull)

                if quit_button.check_input(pos_mouse):
                    pygame.quit()
                    sys.exit()

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def read_userinput(username, password):
    # checking username and password for login part - by my
    while True:
        file = open('user_details.txt', 'r')
        for i in file:
            Username, Password, Level, Time, Coin, Pull, = i.split(",")
            Password = Password.strip()
            Level = Level.strip()
            Coin = Coin.strip()
            Pull = Pull.strip()
            if (Username == username and Password == password):
                return Level, Coin, Pull
            
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
            Username, Password, Level, Time, Coin, Pull = i.strip().split(",")

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
            file.write(f'{username}, {password}, 1, 10000, 0, 0' + '\n')
            # username, password, level, time, coin, pull
            file.close()

            file2 = open('user_backpack.txt', 'a')
            file2.write(f'{username}, normal, no, no')
            file2.close()

            lvl = 1
            coin = 0
            pull = 0
            return lvl, coin, pull
        
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


def welcome_user(username, lvl, coin, pull):
    # screen display after user done with login/register part - my
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                lobby(username, lvl, coin, pull)

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
                    lvl, coin, pull = read_userinput(username_input.text, password_input.text)
                    welcome_user(username_input.text, int(lvl), int(coin), int(pull))
            
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

def update_weapon(username, weapon):
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


def update_equipment(username, equipments):
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_backpack = line.strip().split(", ")
        if user_backpack[0] == username:
            equipments_list = user_backpack[3].split('/')
            if equipments_list[0] == 'no':
                del equipments_list[0]
                equipments_list.append(f'{equipments}')
            elif equipments in equipments_list:
                break
            else:
                equipments_list.append(f'{equipments}')
            equipments_str = '/'.join(equipments_list)
            user_backpack[3] = str(equipments_str)
            lines[i] = ', '.join(user_backpack) + '\n'
            break

    with open('user_backpack.txt', 'w') as file:
        file.writelines(lines)
    return

def check_weapon(username,weapon) :
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_backpack = line.strip().split(", ")
        if user_backpack[0] == username:
            weapon_list = user_backpack[2].split('/')
            if weapon in weapon_list:
                yo = False
            weapon_str = '/'.join(weapon_list)
            user_backpack[2] = str(weapon_str)
            lines[i] = ', '.join(user_backpack) + '\n'
            break

    # with open('user_backpack.txt', 'w') as file:
    #     file.writelines(lines)
    return



def store(username, lvl, coin, pull):
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
        screen.blit(sword,(85,130))
        screen.blit(shield,(380,130))
        screen.blit(bow,(680,130))
        screen.blit(x_bow,(85,375))
        screen.blit(hammer,(380,375))
        screen.blit(axe,(680,375))
        #################

        #PRICE
        #####sword####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,305))
        screen.blit(price_text, text_rect)
        ######Shield######
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,305))
        screen.blit(price_text, text_rect)
        ######bow######
        price_text = font.render(f"{75}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,305))
        screen.blit(price_text, text_rect)
        ####x-bow#####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,555))
        screen.blit(price_text, text_rect)
        ######hammer#####        
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,555))
        screen.blit(price_text, text_rect)
        #######axe#########        
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,555))
        screen.blit(price_text, text_rect)


        #BUTTONS
        buy_button1 = Button('graphic/button2.png', 150, 350, 0.15, "BUY")
        buy_button1.draw(screen)
        buy_button2 = Button('graphic/button2.png', 450, 350, 0.15, "BUY")
        buy_button2.draw(screen)
        buy_button3 = Button('graphic/button2.png', 750, 350, 0.15, "BUY")
        buy_button3.draw(screen)
        buy_button4 = Button('graphic/button2.png', 150, 600, 0.15, "BUY")
        buy_button4.draw(screen)
        buy_button5 = Button('graphic/button2.png', 450, 600, 0.15, "BUY")
        buy_button5.draw(screen)
        buy_button6 = Button('graphic/button2.png', 750, 600, 0.15, "BUY")
        buy_button6.draw(screen)
        #########

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #To store data
        weapon = ('sword','shield','bow','x-bow','hammer','axe')
        
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    if coin >= 100:
                        coin -= 100
                        update_coin(username, coin)
                        update_weapon(username,weapon[0])
                        bought1(username, lvl, coin, pull)
                            
                    else :
                        no_money(username, lvl, coin, pull)
                    
                if buy_button2.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
                        update_coin(username, coin)
                        update_weapon(username,weapon[1])

                        if buy :
                            buy = False
                        else :
                            buy = True
                    else :
                        if no :
                            no = False
                        else :
                            no = True      
                if buy_button3.check_input(pos_mouse):
                    if coin >= 75 :
                        coin -= 75
                        update_coin(username, coin)
                        update_weapon(username,weapon[2])
                        if buy :
                            buy = False
                        else :
                            buy = True
                    else :
                            if no :
                                no = False
                            else :
                                no = True
                if buy_button4.check_input(pos_mouse):
                    if coin >= 100 :
                        coin -= 100
                        update_coin(username, coin)
                        update_weapon(username,weapon[3])
                        if buy :
                            buy = False
                        else :
                            buy = True                                        
                    else :
                        if no :
                            no = False
                        else :
                            no = True
                if buy_button5.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
                        update_coin(username, coin)
                        update_weapon(username,weapon[4])
                        if buy :
                            buy = False
                        else :
                            buy = True
                    else :
                        if no :
                            no = False
                        else :
                            no = True
                if buy_button6.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
                        update_coin(username, coin)
                        update_weapon(username,weapon[5])
                        if buy :
                            buy = False
                        else :
                            buy = True
                    else :
                        if no :
                            no = False
                        else :
                            no = True
                if next_button.check_input(pos_mouse):
                    equipment(username, lvl, coin, pull)
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull)           

        if buy :
            bought1(username, lvl, coin, pull)
        elif no :
            no_money(username, lvl, coin, pull)
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def alr_have(username,lvl, coin, pull):
    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You already have one.',True,'white'),(230,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)
            
        Manager.update(UI_REFRESH_RATE)
        pygame.display.update()

def bought1(username, lvl, coin, pull) :
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
                store(username, lvl, coin, pull)

            Manager.process_events(event)
        
        Manager.update(UI_REFRESH_RATE)
        pygame.display.flip()


def bought2(username, lvl, coin, pull) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You bought an item.',True,'white'),(280,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def bought3(username, lvl, coin, pull) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You bought an item.',True,'white'),(280,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))

    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def no_money(username, lvl, coin, pull) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                store(username, lvl, coin, pull)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def no_money2(username, lvl, coin, pull) :
    #puopuo did this too

    pygame.display.set_caption('Chicky Simulator - Store')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment(username, lvl, coin, pull)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def no_money3(username, lvl, coin, pull) :
    #puopuo did this too

    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                equipment2(username, lvl, coin, pull)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


def equipment(username, lvl, coin, pull) :
    #puopuo did this also
    on = True
    buy = False
    no = False
    hand = pygame.image.load("graphic/hand.png")
    noob_hand = pygame.image.load("graphic/noob hand.png")
    armor = pygame.image.load("graphic/armor.png")
    helmet = pygame.image.load("graphic/helmet.png")
    leg= pygame.image.load("graphic/leg.png")
    noob_leg= pygame.image.load("graphic/noob leg.png")
                            
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
        screen.blit(hand,(85,130))
        screen.blit(armor,(380,130))
        screen.blit(noob_hand,(680,130))
        screen.blit(noob_leg,(85,375))
        screen.blit(helmet,(380,375))
        screen.blit(leg,(680,375))
        #################

        #PRICE
        #####hand####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,305))
        screen.blit(price_text, text_rect)
        ######armor######
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,305))
        screen.blit(price_text, text_rect)
        ######noob hand######
        price_text = font.render(f"{75}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,305))
        screen.blit(price_text, text_rect)
        ####noob leg#####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,555))
        screen.blit(price_text, text_rect)
        ######helmet#####        
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,555))
        screen.blit(price_text, text_rect)
        #######leg#########        
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,555))
        screen.blit(price_text, text_rect)


        # BUY BUTTONS
        buy_button1 = Button('graphic/button2.png', 150, 350, 0.15, "BUY")
        buy_button1.draw(screen)
        buy_button2 = Button('graphic/button2.png', 450, 350, 0.15, "BUY")
        buy_button2.draw(screen)
        buy_button3 = Button('graphic/button2.png', 750, 350, 0.15, "BUY")
        buy_button3.draw(screen)
        buy_button4 = Button('graphic/button2.png', 150, 600, 0.15, "BUY")
        buy_button4.draw(screen)
        buy_button5 = Button('graphic/button2.png', 450, 600, 0.15, "BUY")
        buy_button5.draw(screen)
        buy_button6 = Button('graphic/button2.png', 750, 600, 0.15, "BUY")
        buy_button6.draw(screen)
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Next page button#
        next_button = Button('graphic/botton1.png', 850, 70, 0.6, ">>")
        next_button.draw(screen)

        #SAving Data
        equipments = ('hand','noob_hand','armor','helmet','leg','noob_leg')
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    if coin >= 100 :
                        coin -= 100
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
                if buy_button2.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
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
                if buy_button3.check_input(pos_mouse):
                    if coin >= 75 :
                        coin -= 75
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
                if buy_button4.check_input(pos_mouse):
                    if coin >= 100 :
                        coin -= 100
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
                if buy_button5.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
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
                if buy_button6.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
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
                if back_button.check_input(pos_mouse):
                    store(username, lvl, coin, pull)
                if next_button.check_input(pos_mouse):
                    equipment2(username, lvl, coin, pull)

        if buy :
            bought2(username, lvl, coin, pull)
        elif no :
            no_money2(username, lvl, coin, pull)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def equipment2(username, lvl, coin, pull) :
    #puopuo also did this
    on = True
    buy = False
    no = False
    noob_helmet = pygame.image.load("graphic/noob helmet.png")
    noob_armor = pygame.image.load("graphic/noob armor.png")
    helmet3 = pygame.image.load("graphic/helmet3.png")
                            
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
        screen.blit(noob_armor,(85,130))
        screen.blit(helmet3,(385,130))
        screen.blit(noob_helmet,(680,130))
        #################

        #PRICE
        #####noob helmet####
        price_text = font.render(f"{100}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(150,305))
        screen.blit(price_text, text_rect)
        ######noob armor######
        price_text = font.render(f"{150}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(450,305))
        screen.blit(price_text, text_rect)
        ######helmet 3######
        price_text = font.render(f"{75}", True, (255,255,255))
        text_rect = price_text.get_rect(center =(750,305))
        screen.blit(price_text, text_rect)


        # BUY BUTTONS
        buy_button1 = Button('graphic/button2.png', 150, 350,0.15, "BUY")
        buy_button1.draw(screen)
        buy_button2 = Button('graphic/button2.png', 450, 350,0.15, "BUY")
        buy_button2.draw(screen)
        buy_button3 = Button('graphic/button2.png', 750, 350, 0.15, "BUY")
        buy_button3.draw(screen)
        #########

        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)

        #Data saving
        equipments =('noob_helmet','helmet3','noob_armor')
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if buy_button1.check_input(pos_mouse):
                    if coin >= 100 :
                        coin -= 100
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
                        
                if buy_button2.check_input(pos_mouse):
                    if coin >= 150 :
                        coin -= 150
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
                if buy_button3.check_input(pos_mouse):
                    if coin >= 75 :
                        coin -= 75
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
                if back_button.check_input(pos_mouse):
                    equipment(username, lvl, coin, pull)
        if buy :
            bought3(username, lvl, coin, pull)
        elif no :
            no_money3(username, lvl, coin, pull)

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def arcade_lobby(c,username, lvl, coin, pull):
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
        play_button1 = Button('graphic/button2.png', 150, 500, 0.16, "PLAY")
        play_button1.draw(screen)
        play_button2 = Button('graphic/button2.png', 450, 500, 0.16, "PLAY")
        play_button2.draw(screen)
        play_button3 = Button('graphic/button2.png', 750, 500, 0.16, "PLAY")
        play_button3.draw(screen)
        #########

        #Back page button#
        back_button = Button('graphic/button2.png', 50, 35, 0.13, "Back")
        back_button.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button1.check_input(pos_mouse):
                    snake_lobby(c, username, lvl, coin, pull)                                   
                        
                if play_button2.check_input(pos_mouse):
                    dunno1_lobby(c, username, lvl, coin, pull)

                if play_button3.check_input(pos_mouse):
                    dunno2_lobby(c, username, lvl, coin, pull)

                if back_button.check_input(pos_mouse):
                    choose_level(c, username, lvl, coin, pull)           

        pygame.display.flip()

    pygame.quit()
    sys.exit()


def snake_lobby(c,username, lvl, coin, pull) :
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
                    arcade_lobby(c,username, lvl, coin, pull)
        
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def dunno1_lobby(c,username, lvl, coin, pull) :
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
                    arcade_lobby(c, username, lvl, coin, pull)
        
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


def dunno2_lobby(c,username, lvl, coin, pull) :
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
                    arcade_lobby(c, username, lvl, coin, pull)
        
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


log_or_reg()
