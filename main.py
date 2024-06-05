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
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)
    time_use =[]
    # info = pygame.image.load('graphic/brown.png')
    # pygame.transform.scale(info,(200,700))

    red = (255,0,0)
    green = (0, 255, 0)

    tile_size = 35
    gameover = 0
    lvl = 1
    maxlevel = 30

    jy_hp = 30
    my_hp =50
    pl_hp =70

    jy_dmg = 20
    my_dmg = 15
    pl_dmg = 10

   
    
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
        def __init__(self, x, y, Hp, Def,Atk,Cd,Mag,c):
            
            self.animation_list = []
            self.index = 0
            self.counter = 0
            self.action = 0 
            self.alive = True
            self.update_time = pygame.time.get_ticks()
            self.c = c

            # Walk = 0
            alist = []
            for num in range(1, 6):
                img = pygame.image.load(f'graphic/{c}/walk/{num}.png')
                img = pygame.transform.scale(img, (35, 35))
                alist.append(img)
            self.animation_list.append(alist)
    
            # Attack = 1
            alist = []
            for num in range(1, 6):
                img = pygame.image.load(f'graphic/{c}/attack/{num}.png')
                img = pygame.transform.scale(img, (35, 35))
                alist.append(img)
            self.animation_list.append(alist)

            # hurt =2
            alist = []
            for num in range(1, 6):
                img = pygame.image.load(f'graphic/{c}/hurt/{num}.png')
                img = pygame.transform.scale(img, (35, 35))
                alist.append(img)
            self.animation_list.append(alist)


            self.image = self.animation_list[self.action][self.index]
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.Hp = Hp
            self.hp = Hp
            self.Def = Def
            self.cdef = Def
            self.Atk = Atk
            self.Cd = Cd
            self.Mag = Mag
            self.last_attack_time = 0
            self.update_time = pygame.time.get_ticks()
            self.direction = 0


        def attack(self, yuen_group, jy_group, puolin_group):
            current_time = pygame.time.get_ticks()
            self.action = 1  # Set action to attack
            self.index = 0
            if current_time - self.last_attack_time > self.Cd:
                # Perform attack
                for yuen in pygame.sprite.spritecollide(self, yuen_group, False):
                    yuen.hp -= self.Atk
                    print(yuen.hp)
                for jy in pygame.sprite.spritecollide(self, jy_group, False):
                    jy.hp -= self.Atk
                for puolin in pygame.sprite.spritecollide(self, puolin_group, False):
                    puolin.hp -= self.Atk

                # Set last attack time
                self.last_attack_time = current_time

        def draw_cooldown_bar(self, screen):
            # Calculate the current cooldown percentage
            current_time = pygame.time.get_ticks()
            elapsed_time = current_time - self.last_attack_time
            cooldown_percentage = max(0, min(1, elapsed_time / self.Cd))

            # Draw the cooldown bar
            bar_width = 50
            bar_height = 5
            filled_width = bar_width * cooldown_percentage
            bar_x = self.rect.x + (self.rect.width // 2) - (bar_width // 2)
            bar_y = self.rect.y - 10

            pygame.draw.rect(screen, (128, 128, 128), (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(screen, (255, 255, 255), (bar_x, bar_y, filled_width, bar_height))
            
        def draw_defense_bar(self, screen):
            # Calculate the current defense percentage
            defense_percentage = max(0, min(1, self.cdef / self.Def))

            # Draw the defense bar
            bar_width = 50
            bar_height = 5
            filled_width = bar_width * defense_percentage
            bar_x = self.rect.x + (self.rect.width // 2) - (bar_width // 2)
            bar_y = self.rect.y - 20

            pygame.draw.rect(screen, (128, 128, 128), (bar_x, bar_y, bar_width, bar_height))
            pygame.draw.rect(screen, (0, 0, 255), (bar_x, bar_y, filled_width, bar_height))
                

        def update(self, gameover):
            current_time = pygame.time.get_ticks()
            if gameover == 0:
                dx, dy = 0, 0
                walk_cooldown = 5
                
                self.image = self.animation_list[self.action][self.index]
                key = pygame.key.get_pressed()
                if key[pygame.K_w]:
                    dy -= 3
                    self.counter += 1
                if key[pygame.K_a]:
                    dx -= 3
                    self.counter += 1
                    self.direction = -1
                if key[pygame.K_s]:
                    dy += 3
                    self.counter += 1
                if key[pygame.K_d]:
                    dx += 3
                    self.counter += 1
                    self.direction = 1
                if key[pygame.K_SPACE]:
                    self.attack(yuen_group, jy_group, puolin_group)
                if not any([key[pygame.K_w], key[pygame.K_a], key[pygame.K_s], key[pygame.K_d]]):
                    self.counter = 0
                    self.action = 0
                    self.index = 0
                    
                if self.counter > walk_cooldown:
                    self.counter = 0
                    self.index += 1
                    if self.index >= len(self.animation_list[self.action]):
                        if self.action == 1:  # Attack animation
                            self.action = 0
                        self.index = 0

                self.image = self.animation_list[self.action][self.index]
                

                # Collision with blocks
                for item in world.block_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20, 10, 10):
                        dx, dy = 0, 0
                # Collision with coins
                for item in world.coin_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20, 10, 10):
                        world.coin_list.remove(item)
                for item in world.exit_list:
                    if item[1].colliderect(self.rect.x + dx + 20, self.rect.y + dy + 20, 10, 10):
                        if not world.coin_list:
                            pygame.time.set_timer(pygame.USEREVENT, 0)
                            time_use.append(time)
                            gameover = 1

                self.rect.x += dx
                self.rect.y += dy

                if self.hp <= 0:
                    gameover = -1

            elif gameover == -1:
                self.rect.x = 35
                self.rect.y = 35


            self.draw_cooldown_bar(screen)
            if self.Def != 0:
                self.draw_defense_bar(screen)
            screen.blit(self.image, self.rect)
            return gameover
        
    class HealthBar():
        def __init__(self,x,y,hp,Hp):
            self.x = x
            self.y =y 
            self.hp = hp
            self.Hp = Hp

        def draw(self,hp):
            self.hp = hp
            ratio = self.hp/self.Hp
            pygame.draw.rect(screen,red,(self.x,self.y,60,200))
            pygame.draw.rect(screen,green,(self.x,self.y,60,200*ratio))

    # class DefBar():
    #     def __init__(self,x,y,cdef,Def):
    #         self.x = x
    #         self.y =y 
    #         self.cdef = cdef
    #         self.Def = Def

    #     def draw(self,cdef):
    #         self.cdef = cdef
    #         ratio = self.cdef/self.Def
    #         bar_width = 50
    #         bar_height = 5
    #         filled_width = bar_width * ratio
    #         bar_x = self.rect.x + (self.rect.width // 2) - (bar_width // 2)
    #         bar_y = self.rect.y - 20

    #         pygame.draw.rect(screen, (128, 128, 128), (bar_x, bar_y, bar_width, bar_height))
    #         pygame.draw.rect(screen, (0, 0, 255), (bar_x, bar_y, filled_width, bar_height))

    class World():
        def __init__(self,data):
            self.block_list = [ ] 
            self.coin_list = [ ] 
            self.exit_list = [ ] 

            block = pygame.image.load('graphic/block.png')
            coin = pygame.image.load('graphic/coin.png')
            exit = pygame.image.load('graphic/bananacat.png')

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
                        coin_rect = coin.get_rect()
                        coin_rect.x = col_count * tile_size
                        coin_rect.y = row_count * tile_size
                        item = (coin, coin_rect)
                        self.coin_list.append(item)
                        
                    if tile == 3 :
                        yuen = Monster1(col_count * tile_size,row_count * tile_size,my_hp,my_dmg,5000)
                        yuen_group.add(yuen)
                        
                    if tile == 4 :
                        jy = Monster3(col_count * tile_size,row_count * tile_size,jy_hp,jy_dmg,5000)
                        jy_group.add(jy)

                    if tile == 5 :
                        puolin = Monster2(col_count * tile_size,row_count * tile_size,pl_hp,pl_dmg,5000)
                        puolin_group.add(puolin)

                    if tile == 6:
                        exit = pygame. transform. scale(exit, (tile_size, tile_size))
                        exit_rect = exit.get_rect()
                        exit_rect.x = col_count * tile_size
                        exit_rect.y = row_count * tile_size
                        item = (exit, exit_rect)
                        self.exit_list.append(item)
                    col_count += 1
                row_count += 1
        def draw(self):
            for item in self.block_list:
                screen.blit(item[0],item[1]) 
            for item in self.coin_list:
                screen.blit(item[0],item[1])
            for item in self.exit_list:
                screen.blit(item[0],item[1])


    class Monster1(pygame.sprite.Sprite):
        def __init__(self, x, y, max_hp, damage, cd):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster1.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0
            self.hp = max_hp
            self.max_hp = max_hp
            self.damage = damage
            self.cd = cd
            self.last_attack_time = 0

        def update(self,max_hp,damage,cd):
            current_time = pygame.time.get_ticks()
            self.rect.x += self.move_direction
            self.move_counter += 1
            if self.move_counter > 100:
                self.move_direction *= -1
                self.move_counter *= -1
            if current_time - self.last_attack_time > self.cd:
                for yuen in pygame.sprite.spritecollide(Chicky, yuen_group, False):
                    Chicky.cdef -=self.damage
                    if Chicky.cdef <= 0 :
                        Chicky.hp -= self.damage
                    self.last_attack_time = current_time
                    
            self.draw_health_bar()
            for yuen in yuen_group:
                if self.hp <= 0:
                    yuen_group.remove(yuen)
          

        def draw_health_bar(self):
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen, red, (self.rect.x, self.rect.y - 5, 35, 5))
            pygame.draw.rect(screen, green, (self.rect.x, self.rect.y - 5, 35 * ratio, 5))
                

    class Monster2(pygame.sprite.Sprite):
        def __init__(self,x,y,max_hp,damage,cd):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster2.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.hp = max_hp
            self.max_hp = max_hp
            self.damage = damage
            self.cd = cd
            self.last_attack_time = 0

        def update(self,max_hp,damage,cd):
            # self.hp = hp
            # self.max_hp = max_hp
            # self.damage = damage
            # ratio = self.hp/self.max_hp
            # pygame.draw.rect(screen,red,(self.rect.x ,self.rect.y -5 ,35,5))
            # pygame.draw.rect(screen,green,(self.rect.x ,self.rect.y -5 ,35*ratio,5))

            current_time = pygame.time.get_ticks()
            if current_time - self.last_attack_time > self.cd:
                for puolin in pygame.sprite.spritecollide(Chicky, puolin_group, False):
                    Chicky.cdef -=self.damage
                    if Chicky.cdef <= 0 :
                        Chicky.hp -= self.damage
                    self.last_attack_time = current_time
                    
            self.draw_health_bar()
            for puolin in puolin_group:
                if self.hp <= 0:
                    puolin_group.remove(puolin)

        def draw_health_bar(self):
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen, red, (self.rect.x, self.rect.y - 5, 35, 5))
            pygame.draw.rect(screen, green, (self.rect.x, self.rect.y - 5, 35 * ratio, 5))

    class Monster3(pygame.sprite.Sprite):
        def __init__(self,x,y,max_hp,damage,cd):
            pygame.sprite.Sprite.__init__(self)
            self.image = pygame.image.load('graphic/monster3.png')
            self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.move_direction = 1
            self.move_counter = 0
            self.hp = max_hp
            self.max_hp = max_hp
            self.damage = damage
            self.cd = cd
            self.last_attack_time = 0
            
        def update(self,max_hp,damage,cd):
            current_time = pygame.time.get_ticks()
            self.rect.y += self.move_direction
            self.move_counter += 1
            if self.move_counter > 250 :
                self.move_direction *= -1
                self.move_counter *= -1
            if current_time - self.last_attack_time > self.cd:
                for jy in pygame.sprite.spritecollide(Chicky, jy_group, False):
                    Chicky.cdef -=self.damage
                    if Chicky.cdef <= 0 :
                        Chicky.hp -= self.damage
                    self.last_attack_time = current_time
                    
            self.draw_health_bar()
            for jy in jy_group:
                if self.hp <= 0:
                    jy_group.remove(jy)

        def draw_health_bar(self):
            ratio = self.hp / self.max_hp
            pygame.draw.rect(screen, red, (self.rect.x, self.rect.y - 5, 35, 5))
            pygame.draw.rect(screen, green, (self.rect.x, self.rect.y - 5, 35 * ratio, 5))


    class Exit(pygame.sprite.Sprite):
        def __init__(self, x, y):
            pygame.sprite.Sprite.__init__(self)
            img = pygame.image.load('graphic/bananacat.png')
            self.image = pygame.transform.scale(img, (tile_size, int(tile_size * 1.5)))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    Hp, Def, Atk, Cd, Mag = map(int, stats.split('/'))
    Chicky = chicky(35,35,Hp, Def, Atk, Cd, Mag,c)
    
    
    
    yuen_group = pygame.sprite.Group()
    puolin_group = pygame.sprite.Group()
    jy_group = pygame.sprite.Group()  

    chicky_health_bar = HealthBar(750,200,Chicky.hp,Chicky.Hp)
  
    

    if path.exists(f'level{lvl}_data'):
        pickle_in = open(f'level{lvl}_data', 'rb')
        world_data = pickle.load(pickle_in)
        print('yes im here')
    world = World(world_data)

    

    run = True
    while run:
        
        clock.tick(fps)
        screen.blit(background_image,(0,0))
        
        world.draw()
        gameover = Chicky.update(gameover)

        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
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
                jy.update(jy_hp,jy_dmg,5000)
            for yuen in yuen_group:
                yuen.update(my_hp,my_dmg,5000)
            for puolin in puolin_group:
                puolin.update(pl_hp, pl_dmg,5000)
            


        jy_group.draw(screen)
        yuen_group.draw(screen)
        puolin_group.draw(screen)
            # coin_group.draw(screen)
            # exit_group.draw(screen)

        if gameover == -1:
            # if restart_button.draw(screen):
            world_data = []
            world = reset_level(lvl)
            Chicky = chicky(35,35,Hp, Def, Atk, Cd, Mag,c)
            gameover = 0
            

        if gameover == 1:
            # set timer stop 
            pygame.time.set_timer(pygame.USEREVENT, 0)
            # save in list 
            time_use.append(time)
            lvl += 1
            #reset game and go to next level
            
            if lvl <= maxlevel:
                
                #reset level
                world_data = []
                world = reset_level(lvl)
                Chicky = chicky(35,35,Hp, Def, Atk, Cd, Mag,c)
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


def update_equipment(username, equip):
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_backpack = line.strip().split(", ")
        if user_backpack[0] == username:
            equip_list = user_backpack[2].split('/')
            if equip_list[0] == 'no':
                del equip_list[0]
                equip_list.append(f'{equip}')
            elif equip in equip_list:
                break
            else:
                equip_list.append(f'{equip}')
            weapon_str = '/'.join(equip_list)
            user_backpack[2] = str(weapon_str)
            lines[i] = ', '.join(user_backpack) + '\n'
            break

    with open('user_backpack.txt', 'w') as file:
        file.writelines(lines)
    return


def update_equip(username, equip):
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            user_details[7] = str(equip)
            lines[i] = ', '.join(user_details) + '\n'
            break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)
    return


def update_equipchick(username, chicky):
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            user_details[6] = str(chicky)
            lines[i] = ', '.join(user_details) + '\n'
            break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)
    return


def check_coinget(username, coin, coinget):
    if coinget == 'coin10':
        coin += 10
        coinsget = int(10)
        update_coin(username, coin)

    elif coinget == 'coin15':
        coin += 15
        coinsget = int(15)
        update_coin(username, coin)

    elif coinget == 'coin20':
        coin += 20
        coinsget = int(20)
        update_coin(username, coin)

    elif coinget == 'coin25':
        coin += 25
        coinsget = int(25)
        update_coin(username, coin)

    elif coinget == 'coin30':
        coin += 30
        coinsget = int(30)
        update_coin(username, coin)

    elif coinget == 'coin35':
        coin += 35
        coinsget = int(35)
        update_coin(username, coin)

    elif coinget == 'coin40':
        coin += 40
        coinsget = int(40)
        update_coin(username, coin)

    elif coinget == 'coin45':
        coin += 45
        coinsget = int(45)
        update_coin(username, coin)

    elif coinget == 'coin50':
        coin += 50
        coinsget = int(50)
        update_coin(username, coin)

    elif coinget == 'coin75':
        coin += 75
        coinsget = int(75)
        update_coin(username, coin)

    elif coinget == 'coin90':
        coin += 90
        coinsget = int(90)
        update_coin(username, coin)

    #update_coin(username, coin)
    return coinsget, coin


def collect_achieve(username, lvl, coin, pull, chicky, equip, stats):
    
    while True:
        pygame.display.set_caption('Chicky Simulator - Achievement')
        screen.blit(ranking_image,(0,0))

        achieve_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Achievement', True, 'white')
        achieve_text_rect = achieve_text.get_rect(center = (450,100))
        screen.blit(achieve_text, achieve_text_rect)

        coinlogo = Lock('graphic/manycoin.png', 750, 100, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (830,100))
        screen.blit(coin_text, coin_text_rect)

        achieve_surface = pygame.Surface((850,520))
        achieve_surface.fill('white')
        achieve_surface.set_alpha(150)
        achieve_surface_rect = achieve_surface.get_rect(center=(width/2,410))
        screen.blit(achieve_surface, achieve_surface_rect)

        a1_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get all the\nweapons\nCoin x500', True, 'black')
        a1_text_rect = a1_text.get_rect(center = (150,210))
        screen.blit(a1_text, a1_text_rect)

        a2_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get all the\nshields\nCoin x500', True, 'black')
        a2_text_rect = a2_text.get_rect(center = (450,210))
        screen.blit(a2_text, a2_text_rect)

        a3_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get all the\nhelmets\nCoin x500', True, 'black')
        a3_text_rect = a3_text.get_rect(center = (750,210))
        screen.blit(a3_text, a3_text_rect)

        a4_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get all the\narmors\nCoin x500', True, 'black')
        a4_text_rect = a4_text.get_rect(center = (150,460))
        screen.blit(a4_text, a4_text_rect)

        a5_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get all the\nshoes\nCoin x500', True, 'black')
        a5_text_rect = a5_text.get_rect(center = (450,460))
        screen.blit(a5_text, a5_text_rect)

        a6_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get all the\nchicky\nCoin x500', True, 'black')
        a6_text_rect = a6_text.get_rect(center = (750,460))
        screen.blit(a6_text, a6_text_rect)

        claim_button1 = Button('graphic/button2.png', 150, 350, 0.25, "Claim")
        claim_button1.draw(screen)
        claim_button2 = Button('graphic/button2.png', 450, 350, 0.25, "Claim")
        claim_button2.draw(screen)
        claim_button3 = Button('graphic/button2.png', 750, 350, 0.25, "Claim")
        claim_button3.draw(screen)
        claim_button4 = Button('graphic/button2.png', 150, 600, 0.25, "Claim")
        claim_button4.draw(screen)
        claim_button5 = Button('graphic/button2.png', 450, 600, 0.25, "Claim")
        claim_button5.draw(screen)
        claim_button6 = Button('graphic/button2.png', 750, 600, 0.25, "Claim")
        claim_button6.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    achievement(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def arcade_achieve(username, lvl, coin, pull, chicky, equip, stats):
    
    while True:
        pygame.display.set_caption('Chicky Simulator - Achievement')
        screen.blit(ranking_image,(0,0))

        achieve_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Achievement', True, 'white')
        achieve_text_rect = achieve_text.get_rect(center = (450,100))
        screen.blit(achieve_text, achieve_text_rect)

        coinlogo = Lock('graphic/manycoin.png', 750, 100, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (830,100))
        screen.blit(coin_text, coin_text_rect)

        achieve_surface = pygame.Surface((850,520))
        achieve_surface.fill('white')
        achieve_surface.set_alpha(150)
        achieve_surface_rect = achieve_surface.get_rect(center=(width/2,410))
        screen.blit(achieve_surface, achieve_surface_rect)

        a1_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get 20 score\nin arcade mode\nCoin x30', True, 'black')
        a1_text_rect = a1_text.get_rect(center = (150,210))
        screen.blit(a1_text, a1_text_rect)

        a2_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get 40 score\nin arcade mode\nCoin x50', True, 'black')
        a2_text_rect = a2_text.get_rect(center = (450,210))
        screen.blit(a2_text, a2_text_rect)

        a3_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Get 60 score\nin arcade mode\nCoin x100', True, 'black')
        a3_text_rect = a3_text.get_rect(center = (750,210))
        screen.blit(a3_text, a3_text_rect)

        a4_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Play arcade \nmode 10 times\nCoin x30', True, 'black')
        a4_text_rect = a4_text.get_rect(center = (150,460))
        screen.blit(a4_text, a4_text_rect)

        a5_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Play arcade \nmode 15 times\nCoin x50', True, 'black')
        a5_text_rect = a5_text.get_rect(center = (450,460))
        screen.blit(a5_text, a5_text_rect)

        a6_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Play arcade \nmode 20 times\nCoin x100', True, 'black')
        a6_text_rect = a6_text.get_rect(center = (750,460))
        screen.blit(a6_text, a6_text_rect)

        claim_button1 = Button('graphic/button2.png', 150, 350, 0.25, "Claim")
        claim_button1.draw(screen)
        claim_button2 = Button('graphic/button2.png', 450, 350, 0.25, "Claim")
        claim_button2.draw(screen)
        claim_button3 = Button('graphic/button2.png', 750, 350, 0.25, "Claim")
        claim_button3.draw(screen)
        claim_button4 = Button('graphic/button2.png', 150, 600, 0.25, "Claim")
        claim_button4.draw(screen)
        claim_button5 = Button('graphic/button2.png', 450, 600, 0.25, "Claim")
        claim_button5.draw(screen)
        claim_button6 = Button('graphic/button2.png', 750, 600, 0.25, "Claim")
        claim_button6.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    achievement(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def level_achieve(username, lvl, coin, pull, chicky, equip, stats):
    
    while True:
        pygame.display.set_caption('Chicky Simulator - Achievement')
        screen.blit(ranking_image,(0,0))

        achieve_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Achievement', True, 'white')
        achieve_text_rect = achieve_text.get_rect(center = (450,100))
        screen.blit(achieve_text, achieve_text_rect)

        coinlogo = Lock('graphic/manycoin.png', 750, 100, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (830,100))
        screen.blit(coin_text, coin_text_rect)

        achieve_surface = pygame.Surface((850,520))
        achieve_surface.fill('white')
        achieve_surface.set_alpha(150)
        achieve_surface_rect = achieve_surface.get_rect(center=(width/2,410))
        screen.blit(achieve_surface, achieve_surface_rect)

        a1_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Clear Level 5\nCoin x30', True, 'black')
        a1_text_rect = a1_text.get_rect(center = (150,210))
        screen.blit(a1_text, a1_text_rect)

        a2_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Clear Level 10\nCoin x50', True, 'black')
        a2_text_rect = a2_text.get_rect(center = (450,210))
        screen.blit(a2_text, a2_text_rect)

        a3_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Clear Level 15\nCoin x75', True, 'black')
        a3_text_rect = a3_text.get_rect(center = (750,210))
        screen.blit(a3_text, a3_text_rect)

        a4_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Clear Level 20\nCoin x100', True, 'black')
        a4_text_rect = a4_text.get_rect(center = (150,460))
        screen.blit(a4_text, a4_text_rect)

        a5_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Clear Level 25\nCoin x150', True, 'black')
        a5_text_rect = a5_text.get_rect(center = (450,460))
        screen.blit(a5_text, a5_text_rect)

        a6_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 35).render('Clear Level 30\nCoin x300', True, 'black')
        a6_text_rect = a6_text.get_rect(center = (750,460))
        screen.blit(a6_text, a6_text_rect)

        claim_button1 = Button('graphic/button2.png', 150, 350, 0.25, "Claim")
        claim_button1.draw(screen)
        claim_button2 = Button('graphic/button2.png', 450, 350, 0.25, "Claim")
        claim_button2.draw(screen)
        claim_button3 = Button('graphic/button2.png', 750, 350, 0.25, "Claim")
        claim_button3.draw(screen)
        claim_button4 = Button('graphic/button2.png', 150, 600, 0.25, "Claim")
        claim_button4.draw(screen)
        claim_button5 = Button('graphic/button2.png', 450, 600, 0.25, "Claim")
        claim_button5.draw(screen)
        claim_button6 = Button('graphic/button2.png', 750, 600, 0.25, "Claim")
        claim_button6.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    achievement(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def achievement(username, lvl, coin, pull, chicky, equip, stats):

    while True:
        pygame.display.set_caption('Chicky Simulator - Achievement')
        screen.blit(ranking_image,(0,0))

        chicky_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Achievement', True, 'white')
        chicky_text_rect = chicky_text.get_rect(center = (450,100))
        screen.blit(chicky_text, chicky_text_rect)

        coinlogo = Lock('graphic/manycoin.png', 700, 100, 0.3)
        coinlogo.draw(screen)
        coin_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{coin}', True, 'white')
        coin_text_rect = coin_text.get_rect(center = (780,100))
        screen.blit(coin_text, coin_text_rect)

        level_button = Button('graphic/button2.png', 180, 350, 0.35, "Level")
        level_button.draw(screen)

        arcade_button = Button('graphic/button2.png', width/2, 350, 0.35, "Arcade")
        arcade_button.draw(screen)

        collect_button = Button('graphic/button2.png', 720, 350, 0.35, "Collection")
        collect_button.draw(screen)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if level_button.check_input(pos_mouse):
                    level_achieve(username, lvl, coin, pull, chicky, equip, stats)
                if arcade_button.check_input(pos_mouse):
                    arcade_achieve(username, lvl, coin, pull, chicky, equip, stats)
                if collect_button.check_input(pos_mouse):
                    collect_achieve(username, lvl, coin, pull, chicky, equip, stats)
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, chicky, equip, stats)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def equip_chick2(username, lvl, coin, pull, chicky, equip, stats):

    while True:
        pygame.display.set_caption('Chicky Simulator - Chicky')
        screen.blit(ranking_image,(0,0))

        chicky_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky', True, 'white')
        chicky_text_rect = chicky_text.get_rect(center = (450,100))
        screen.blit(chicky_text, chicky_text_rect)

        chick1_surface = pygame.Surface((250,500))
        chick1_surface.fill('white')
        chick1_surface.set_alpha(150)
        chick1_surface_rect = chick1_surface.get_rect(center=(180,400))
        screen.blit(chick1_surface, chick1_surface_rect)

        worrier = Lock('graphic/ninjachic.png', 180, 265, 0.29)
        worrier.draw(screen)

        worrier_info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Ninja Chick\nHp = 75\nAtk = 20\nSpd = 10', True, 'black')
        worrier_info_rect = worrier_info.get_rect(center = (180,460))
        screen.blit(worrier_info, worrier_info_rect)

        chick2_surface = pygame.Surface((250,500))
        chick2_surface.fill('white')
        chick2_surface.set_alpha(150)
        chick2_surface_rect = chick2_surface.get_rect(center=(width/2,400))
        screen.blit(chick2_surface, chick2_surface_rect)

        kitty = Lock('graphic/miaoji.png', width/2, 260, 0.29)
        kitty.draw(screen)

        kitty_info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Kitty Chick\nHp = 150\nAtk = 10\nSpd = 10', True, 'black')
        kitty_info_rect = kitty_info.get_rect(center = (width/2,460))
        screen.blit(kitty_info, kitty_info_rect)

        chick3_surface = pygame.Surface((250,500))
        chick3_surface.fill('white')
        chick3_surface.set_alpha(150)
        chick3_surface_rect = chick3_surface.get_rect(center=(720,400))
        screen.blit(chick3_surface, chick3_surface_rect)

        speedy = Lock('graphic/speedychic.png', 720, 260, 0.3)
        speedy.draw(screen)

        speedy_info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Speedy Chick\nHp = 75\nAtk = 10\nSpd = 20', True, 'black')
        speedy_info_rect = speedy_info.get_rect(center = (720,460))
        screen.blit(speedy_info, speedy_info_rect)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        if chicky == 'worrier':
            worrier_button = Button('graphic/button2.png', 180, 590, 0.25, "Using")
            worrier_button.draw(screen)
            kitty_button = Button('graphic/button2.png', width/2, 590, 0.25, "Use")
            kitty_button.draw(screen)
            speedy_button = Button('graphic/button2.png', 720, 590, 0.25, "Use")
            speedy_button.draw(screen)

        elif chicky == 'kitty':
            worrier_button = Button('graphic/button2.png', 180, 590, 0.25, "Use")
            worrier_button.draw(screen)
            kitty_button = Button('graphic/button2.png', width/2, 590, 0.25, "Using")
            kitty_button.draw(screen)
            speedy_button = Button('graphic/button2.png', 720, 590, 0.25, "Use")
            speedy_button.draw(screen)

        elif chicky == 'speedy':
            worrier_button = Button('graphic/button2.png', 180, 590, 0.25, "Use")
            worrier_button.draw(screen)
            kitty_button = Button('graphic/button2.png', width/2, 590, 0.25, "Use")
            kitty_button.draw(screen)
            speedy_button = Button('graphic/button2.png', 720, 590, 0.25, "Using")
            speedy_button.draw(screen)
        else:
            worrier_button = Button('graphic/button2.png', 180, 590, 0.25, "Use")
            worrier_button.draw(screen)
            kitty_button = Button('graphic/button2.png', width/2, 590, 0.25, "Use")
            kitty_button.draw(screen)
            speedy_button = Button('graphic/button2.png', 720, 590, 0.25, "Use")
            speedy_button.draw(screen)

        locknin = Lock('graphic/lock.png', 180, 580, 0.23)
        lockkit = Lock('graphic/lock.png', width/2, 580, 0.23)
        lockspd = Lock('graphic/lock.png', 720, 580, 0.23)

        locknin_con = False
        lockkit_con = False
        lockspd_con = False

        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    chicky_list = user_backpack[1].split('/')
                    if 'worrier' in chicky_list:
                        locknin_con = True
                    if 'kitty' in chicky_list:
                        lockkit_con = True
                    if 'speedy' in chicky_list:
                        lockspd_con = True
                    #chicky_str = '/'.join(chicky_list)
                    #print(str(chicky_str))
                    #print(lockmag_con, locktank_con)
        
        if locknin_con == False:
            locknin.draw(screen)
        if lockkit_con == False:
            lockkit.draw(screen)
        if lockspd_con == False:
            lockspd.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if worrier_button.check_input(pos_mouse):
                    if locknin_con == True:
                        c = str('worrier')
                        update_equipchick(username, c)
                        status = check_default(username)
                        equip_chick2(username, lvl, coin, pull, c, equip, status)

                if kitty_button.check_input(pos_mouse):
                    if lockkit_con == True:
                        c = str('kitty')
                        update_equipchick(username, c)
                        status = check_default(username)
                        equip_chick2(username, lvl, coin, pull, c, equip, status)

                if speedy_button.check_input(pos_mouse):
                    if lockspd_con == True:
                        c = str('speedy')
                        update_equipchick(username, c)
                        status = check_default(username)
                        equip_chick2(username, lvl, coin, pull, c, equip, status)

                if back_button.check_input(pos_mouse):
                    equip_chick(username, lvl, coin, pull, chicky, equip, stats)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def equip_chick(username, lvl, coin, pull, chicky, equip, stats):

    while True:
        pygame.display.set_caption('Chicky Simulator - Chicky')
        screen.blit(ranking_image,(0,0))

        chicky_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100).render('Chicky', True, 'white')
        chicky_text_rect = chicky_text.get_rect(center = (450,100))
        screen.blit(chicky_text, chicky_text_rect)

        chick1_surface = pygame.Surface((250,500))
        chick1_surface.fill('white')
        chick1_surface.set_alpha(150)
        chick1_surface_rect = chick1_surface.get_rect(center=(180,400))
        screen.blit(chick1_surface, chick1_surface_rect)

        normal = Lock('graphic/chicky.png', 180, 270, 0.28)
        normal.draw(screen)

        normal_info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Normal Chick\nHp = 100\nAtk = 10\nSpd = 10', True, 'black')
        normal_info_rect = normal_info.get_rect(center = (180,460))
        screen.blit(normal_info, normal_info_rect)

        chick2_surface = pygame.Surface((250,500))
        chick2_surface.fill('white')
        chick2_surface.set_alpha(150)
        chick2_surface_rect = chick2_surface.get_rect(center=(width/2,400))
        screen.blit(chick2_surface, chick2_surface_rect)

        magnet = Lock('graphic/magnetchic.png', width/2, 260, 0.3)
        magnet.draw(screen)

        magnet_info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Magnet Chick\nHp = 100\nAtk = 10\nSpd = 10', True, 'black')
        magnet_info_rect = magnet_info.get_rect(center = (width/2,460))
        screen.blit(magnet_info, magnet_info_rect)

        chick3_surface = pygame.Surface((250,500))
        chick3_surface.fill('white')
        chick3_surface.set_alpha(150)
        chick3_surface_rect = chick3_surface.get_rect(center=(720,400))
        screen.blit(chick3_surface, chick3_surface_rect)

        tanker = Lock('graphic/tank chic.png', 720, 270, 0.3)
        tanker.draw(screen)

        tanker_info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 40).render('Tanker Chick\nHp = 200\nAtk = 10\nSpd = 5', True, 'black')
        tanker_info_rect = tanker_info.get_rect(center = (720,460))
        screen.blit(tanker_info, tanker_info_rect)

        back_button = Button('graphic/botton1.png', 100, 100, 0.6, "<<")
        back_button.draw(screen)

        next_button = Button('graphic/botton1.png', 800, 100, 0.6, ">>")
        next_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        if chicky == 'normal':
            normal_button = Button('graphic/button2.png', 180, 590, 0.25, "Using")
            normal_button.draw(screen)
            magnet_button = Button('graphic/button2.png', width/2, 590, 0.25, "Use")
            magnet_button.draw(screen)
            tanker_button = Button('graphic/button2.png', 720, 590, 0.25, "Use")
            tanker_button.draw(screen)

        elif chicky == 'magnet':
            normal_button = Button('graphic/button2.png', 180, 590, 0.25, "Use")
            normal_button.draw(screen)
            magnet_button = Button('graphic/button2.png', width/2, 590, 0.25, "Using")
            magnet_button.draw(screen)
            tanker_button = Button('graphic/button2.png', 720, 590, 0.25, "Use")
            tanker_button.draw(screen)

        elif chicky == 'tanker':
            normal_button = Button('graphic/button2.png', 180, 590, 0.25, "Use")
            normal_button.draw(screen)
            magnet_button = Button('graphic/button2.png', width/2, 590, 0.25, "Use")
            magnet_button.draw(screen)
            tanker_button = Button('graphic/button2.png', 720, 590, 0.25, "Using")
            tanker_button.draw(screen)

        else:
            normal_button = Button('graphic/button2.png', 180, 590, 0.25, "Use")
            normal_button.draw(screen)
            magnet_button = Button('graphic/button2.png', width/2, 590, 0.25, "Use")
            magnet_button.draw(screen)
            tanker_button = Button('graphic/button2.png', 720, 590, 0.25, "Use")
            tanker_button.draw(screen)

        lockmag = Lock('graphic/lock.png', width/2, 580, 0.23)
        locktank = Lock('graphic/lock.png', 720, 580, 0.23)

        lockmag_con = False
        locktank_con = False

        with open('user_backpack.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                user_backpack = line.strip().split(", ")
                if user_backpack[0] == username:
                    chicky_list = user_backpack[1].split('/')
                    if 'magnet' in chicky_list:
                        lockmag_con = True
                    if 'tanker' in chicky_list:
                        locktank_con = True
                    #chicky_str = '/'.join(chicky_list)
                    #print(str(chicky_str))
                    #print(lockmag_con, locktank_con)
        
        if lockmag_con == False:
            lockmag.draw(screen)
        if locktank_con == False:
            locktank.draw(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if normal_button.check_input(pos_mouse):
                    c = str('normal')
                    update_equipchick(username, c)
                    status = check_default(username)
                    equip_chick(username, lvl, coin, pull, c, equip, status)

                if magnet_button.check_input(pos_mouse):
                    if lockmag_con == True:
                        c = str('magnet')
                        update_equipchick(username, c)
                        status = check_default(username)
                        equip_chick(username, lvl, coin, pull, c, equip, status)

                if tanker_button.check_input(pos_mouse):
                    if locktank_con == True:
                        c = str('tanker')
                        update_equipchick(username, c)
                        status = check_default(username)
                        equip_chick(username, lvl, coin, pull, c, equip, status)

                if back_button.check_input(pos_mouse):
                    lobby(username, lvl, coin, pull, chicky, equip, stats)

                if next_button.check_input(pos_mouse):
                    equip_chick2(username, lvl, coin, pull, chicky, equip, stats)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)

        pygame.display.update()
    

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

    #equip_slots = {
        #"sword": Slot(105, 430, slot_size, slot_size),
        #"shield": Slot(255, 430, slot_size, slot_size),
        #"helmet": Slot(30, 550, slot_size, slot_size),
        #"armor": Slot(180, 550, slot_size, slot_size),
        #"shoes": Slot(330, 550, slot_size, slot_size)
    #}

    equip_slots = [Slot(105, 430, slot_size, slot_size),
                   Slot(255, 430, slot_size, slot_size),
                   Slot(30, 550, slot_size, slot_size),
                   Slot(180, 550, slot_size, slot_size),
                   Slot(330, 550, slot_size, slot_size)]

    equipments_list = []
    with open('user_backpack.txt', 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            user_backpack = line.split(", ")
            if user_backpack[0] == username:
                equipments_list = user_backpack[2].split('/')
                #print(equipments_list)
                break

    items_list = []
    equips_list= []
    omg_equip_list = equip.split('/')  
    for equipments in equipments_list:
        if equipments in omg_equip_list:
            equips_list.append(equipments)
        else:
            items_list.append(equipments)

    items = []
    equips = []
    with open('equipment_details.txt', 'r') as file2:
        lines = file2.readlines()
        for line in lines:
            item_details = line.split(",")
            for i in items_list:
                if i in item_details[0]:
                    item_graphic = (f'{item_details[1]}')
                    item_info = (f'{item_details[2]}\n{item_details[3]}')
                    item = Item(item_graphic, item_info, 0.65)
                    item_type = (f'{item_details[5]}')
                    items.append(item)
            hoho = ','.join(str(items))
            print(str(hoho))

            for i in equips_list:
                if i in item_details[0]:
                    equip1_graphic = (f'{item_details[1]}')
                    equip1_info = (f'{item_details[2]}\n{item_details[3]}')
                    equip1 = Item(equip1_graphic, equip1_info, 0.65)
                    equip1_type = (f'{item_details[5]}')
                    equips.append(equip1)

    weapon = ['axe','hammer','sword']
    shield = ['shield1','shield2','shield3']
    helmet = ['helmet1','helmet2','helmet3']
    armor = ['armor1','armor2','armor3']
    shoe = ['shoe1','shoe2','shoe3']
    equip_stats = [0,0,0,0,0]
    for equipments in equips_list:
        if equipments in weapon:
            equip_stats[0] = 1
        if equipments in shield:
            equip_stats[1] = 1
        if equipments in helmet:
            equip_stats[2] = 1
        if equipments in armor:
            equip_stats[3] = 1
        if equipments in shoe:
            equip_stats[4] = 1
    #equip_str = str(f'{equip_stats[0]},{equip_stats[1]},{equip_stats[2]},{equip_stats[3]},{equip_stats[4]}')
    #print(equip_str)

    #w_str = ','.join(w)
    #print(str(w_str))
    #shield_str = ','.join(str(shield))
    #print(str(shield_str))
    #h_str = ','.join(str(helmet))
    #print(str(h_str))
    #a_str = ','.join(str(armor))
    #print(str(a_str))
    #s_str = ','.join(str(shoe))
    #print(str(s_str))

    #with open('equipment_details.txt', 'r') as file3:
        #lines = file3.readlines()
        #for line in lines:
            #item_details = line.split(", ")
            #for item in weapon:
                #if item in item_details[0]:
                    #item_graphic = (f'{item_details[1]}')
                    #item_info = (f'{item_details[2]}\n{item_details[3]}')
                    #item = Item(item_graphic, item_info, 0.65)
                    #weapon.append(item)
            #for item in shield:
                #if item in item_details[0]:
                    #item_graphic = (f'{item_details[1]}')
                    #item_info = (f'{item_details[2]}\n{item_details[3]}')
                    #item = Item(item_graphic, item_info, 0.65)
                    #shield.append(item)
            #for item in helmet:
                #if item in item_details[0]:
                    #item_graphic = (f'{item_details[1]}')
                    #item_info = (f'{item_details[2]}\n{item_details[3]}')
                    #item = Item(item_graphic, item_info, 0.65)
                    #helmet.append(item)
            #for item in armor:
                #if item in item_details[0]:
                    #item_graphic = (f'{item_details[1]}')
                    #item_info = (f'{item_details[2]}\n{item_details[3]}')
                    #item = Item(item_graphic, item_info, 0.65)
                    #armor.append(item)
            #for item in shoe:
                #if item in item_details[0]:
                    #item_graphic = (f'{item_details[1]}')
                    #item_info = (f'{item_details[2]}\n{item_details[3]}')
                    #item = Item(item_graphic, item_info, 0.65)
                    #shoe.append(item)

    for i, item in enumerate(items):
        if i <= len(backpack_slots):
            backpack_slots[i].item = item

    for n, equip1 in enumerate(equips):
        if n <= len(equip_slots):
            equip_slots[n].item = equip1

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
                        if slot.item == None:
                            items.remove(selected_item)
                        break

                for slot in equip_slots:
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        selected_item.rect.x = pos_mouse[0] + offset_x
                        selected_item.rect.y = pos_mouse[1] + offset_y
                        slot.item = None
                        #if selected_item in w:
                            #print('True')
                        #else:
                            #print('False')
                        if slot.item == None:
                            if selected_item == weapon:
                                equip_stats[0] = 0
                                equips.remove(selected_item)
                            elif selected_item in shield:
                                equip_stats[1] = 0
                                equips.remove(selected_item)
                            elif selected_item in helmet:
                                equip_stats[2] = 0
                                equips.remove(selected_item)
                            elif selected_item in armor:
                                equip_stats[3] = 0
                                equips.remove(selected_item)
                            elif selected_item in shoe:
                                equip_stats[4] = 0
                                equips.remove(selected_item)
                        equip_str = str(f'{equip_stats[0]},{equip_stats[1]},{equip_stats[2]},{equip_stats[3]},{equip_stats[4]}')
                        print(equip_str)
                        break

                #for slot in list(equip_slots.values()):
                    #if slot.rect.collidepoint(pos_mouse) and slot.item:
                        #selected_item = slot.item
                        #offset_x = slot.rect.x - pos_mouse[0]
                        #offset_y = slot.rect.y - pos_mouse[1]
                        #selected_item.rect.x = pos_mouse[0] + offset_x
                        #selected_item.rect.y = pos_mouse[1] + offset_y
                        #slot.item = None
                        #break
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
                if selected_item != None:
                    for slot in backpack_slots:
                        if (slot.rect.collidepoint(pos_mouse)) and (slot.item is None):
                            slot.item = selected_item
                            selected_item = None
                            offset_x, offset_y = None, None
                            if selected_item == None:
                                items.append(slot.item)
                            break

                    for slot in equip_slots:
                        if (slot.rect.collidepoint(pos_mouse)) and (slot.item is None):
                            slot.item = selected_item
                            selected_item = None
                            offset_x, offset_y = None, None
                            if selected_item == None:
                                if selected_item in weapon:
                                    if equip_stats[0] == 0:
                                        equip_stats[0] = 1
                                        equips.append(slot.item)
                                    else:
                                        slot.item = None

                                elif selected_item in shield:
                                    if equip_stats[1] == 0:
                                        equip_stats[1] = 1
                                        equips.append(slot.item)
                                    else:
                                        slot.item = None

                                elif selected_item in helmet:
                                    if equip_stats[2] == 0:
                                        equip_stats[2] = 1
                                        equips.append(slot.item)
                                    else:
                                        slot.item = None

                                elif selected_item in armor:
                                    if equip_stats[3] == 0:
                                        equip_stats[3] = 1
                                        equips.append(slot.item)
                                    else:
                                        slot.item = None

                                elif selected_item in shoe:
                                    if equip_stats[4] == 0:
                                        equip_stats[4] = 1
                                        equips.append(slot.item)
                                    else:
                                        slot.item = None
                            break

                    if selected_item:
                        for slot in backpack_slots:
                            if slot.item is None:
                                slot.item = selected_item
                                selected_item = None
                                offset_x, offset_y = None, None
                                if selected_item == None:
                                    items.append(slot.item)
                                break

                #if selected_item:
                    #for slot in backpack_slots + list(equip_slots.values()):
                        #if (slot.rect.collidepoint(pos_mouse)) and (slot.item is None):
                            #slot.item = selected_item
                            #selected_item = None
                            #offset_x, offset_y = None, None
                            #break
                    #if selected_item:
                        #for slot in backpack_slots:
                            #if slot.item is None:
                                #slot.item = selected_item
                                #selected_item = None
                                #offset_x, offset_y = None, None
                                #break

        for slot in backpack_slots:
            slot.draw(screen)

        for slot in equip_slots:
            slot.draw(screen)

        if selected_item == None:
            Hp,Def,Atk,Spd,Mag = stats.split('/')
            default = Info(50, 150, (f'Hp={Hp}\nDef={Def}\nAtk={Atk}\nSpd={Spd}'))
            default.draw_info(screen)
        else:
            screen.blit(selected_item.image, selected_item.rect.topleft)
            Hp,Def,Atk,Spd,Mag = stats.split('/')
            default = Info(50, 150, (f'Hp={Hp}\nDef={Def}\nAtk={Atk}\nSpd={Spd}'))
            default.draw_info(screen)
            new_default = Info(250, 150, (f'Hp={Hp}\nDef={Def}\nAtk={Atk}\nSpd={Spd}'))
            new_default.draw_info(screen)
            info = Info(50, 335, selected_item.info)
            info.draw_info(screen)

        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.update()


def items(username, lvl, coin, times, itemget, pull, c, equip, stats):

    if times == 1:
            if itemget == 'kitty':
                chicky = str('kitty')
                update_chicky(username, chicky)

            elif itemget == 'tanker':
                chicky = str('tanker')
                update_chicky(username, chicky)

            elif itemget == 'magnet':
                chicky = str('magnet')
                update_chicky(username, chicky)

            elif itemget == 'speedy':
                chicky = str('speedy')
                update_chicky(username, chicky)

            elif itemget == 'worrier':
                chicky = str('worrier')
                update_chicky(username, chicky)

            else:
                coinget = str(itemget)
                coinsget, ncoin = check_coinget(username, coin, coinget)
                coinsget, ncoin = int(coinsget), int(ncoin)

    else:
        item1,item2,item3,item4,item5 = itemget.split(',')

        if item1 == 'kitty':
            chicky = str('kitty')
            update_chicky(username, chicky)
        elif item1 == 'tanker':
            chicky = str('tanker')
            update_chicky(username, chicky)
        elif item1 == 'magnet':
            chicky = str('magnet')
            update_chicky(username, chicky)
        elif item1 == 'speedy':
            chicky = str('speedy')
            update_chicky(username, chicky)
        elif item1 == 'worrier':
            chicky = str('worrier')
            update_chicky(username, chicky)
        else:
            coinget = str(item1)
            coinsget, ncoin = check_coinget(username, coin, coinget)
            coinsget1, coin = int(coinsget), int(ncoin)

        if item2 == 'kitty':
            chicky = str('kitty')
            update_chicky(username, chicky)
        elif item2 == 'tanker':
            chicky = str('tanker')
            update_chicky(username, chicky)
        elif item2 == 'magnet':
            chicky = str('magnet')
            update_chicky(username, chicky)
        elif item2 == 'speedy':
            chicky = str('speedy')
            update_chicky(username, chicky)
        elif item2 == 'worrier':
            chicky = str('worrier')
            update_chicky(username, chicky)
        else:
            coinget = str(item2)
            coinsget, ncoin = check_coinget(username, coin, coinget)
            coinsget2, coin = int(coinsget), int(ncoin)

        if item3 == 'kitty':
            chicky = str('kitty')
            update_chicky(username, chicky)
        elif item3 == 'tanker':
            chicky = str('tanker')
            update_chicky(username, chicky)
        elif item3 == 'magnet':
            chicky = str('magnet')
            update_chicky(username, chicky)
        elif item3 == 'speedy':
            chicky = str('speedy')
            update_chicky(username, chicky)
        elif item3 == 'worrier':
            chicky = str('worrier')
            update_chicky(username, chicky)
        else:
            coinget = str(item3)
            coinsget, ncoin = check_coinget(username, coin, coinget)
            coinsget3, coin = int(coinsget), int(ncoin)

        if item4 == 'kitty':
            chicky = str('kitty')
            update_chicky(username, chicky)
        elif item4 == 'tanker':
            chicky = str('tanker')
            update_chicky(username, chicky)
        elif item4 == 'magnet':
            chicky = str('magnet')
            update_chicky(username, chicky)
        elif item4 == 'speedy':
            chicky = str('speedy')
            update_chicky(username, chicky)
        elif item4 == 'worrier':
            chicky = str('worrier')
            update_chicky(username, chicky)
        else:
            coinget = str(item4)
            coinsget, ncoin = check_coinget(username, coin, coinget)
            coinsget4, coin = int(coinsget), int(ncoin)
        
        if item5 == 'kitty':
            chicky = str('kitty')
            update_chicky(username, chicky)
        elif item5 == 'tanker':
            chicky = str('tanker')
            update_chicky(username, chicky)
        elif item5 == 'magnet':
            chicky = str('magnet')
            update_chicky(username, chicky)
        elif item5 == 'speedy':
            chicky = str('speedy')
            update_chicky(username, chicky)
        elif item5 == 'worrier':
            chicky = str('worrier')
            update_chicky(username, chicky)
        else:
            coinget = str(item5)
            coinsget, ncoin = check_coinget(username, coin, coinget)
            coinsget5, coin = int(coinsget), int(ncoin)

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

        back_button = Button('graphic/button2.png', 450, 580, 0.25, "BACK")
        back_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        if times == 1:
            if itemget == 'kitty':
                kitty = Lock('graphic/miaoji.png', width/2, 350, 0.18)
                kitty.draw(screen)

            elif itemget == 'tanker':
                tanker = Lock('graphic/tank chic.png', width/2, 350, 0.18)
                tanker.draw(screen)

            elif itemget == 'magnet':
                magnet = Lock('graphic/magnetchic.png', width/2, 350, 0.18)
                magnet.draw(screen)

            elif itemget == 'speedy':
                speedy = Lock('graphic/speedychic.png', width/2, 350, 0.18)
                speedy.draw(screen)

            elif itemget == 'worrier':
                worrier = Lock('graphic/ninjachic.png', width/2, 350, 0.18)
                worrier.draw(screen)

            else:
                coins = Lock('graphic/itemcoin.png', width/2, 350, 1.5)
                coins.draw(screen)
                coinget_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render(f'Coin x{coinsget}', True, 'black')
                coinget_text_rect = coinget_text.get_rect(center = (width/2,420))
                screen.blit(coinget_text, coinget_text_rect)

        else:
            item1,item2,item3,item4,item5 = itemget.split(',')

            if item1 == 'kitty':
                kitty = Lock('graphic/miaoji.png', 200, 350, 0.18)
                kitty.draw(screen)
            elif item1 == 'tanker':
                tanker = Lock('graphic/tank chic.png', 200, 350, 0.18)
                tanker.draw(screen)
            elif item1 == 'magnet':
                magnet = Lock('graphic/magnetchic.png', 200, 350, 0.18)
                magnet.draw(screen)
            elif item1 == 'speedy':
                speedy = Lock('graphic/speedychic.png', 200, 350, 0.18)
                speedy.draw(screen)
            elif item1 == 'worrier':
                worrier = Lock('graphic/ninjachic.png', 200, 350, 0.18)
                worrier.draw(screen)
            else:
                coins = Lock('graphic/itemcoin.png', 200, 350, 1.5)
                coins.draw(screen)
                coinget_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render(f'Coin x{coinsget1}', True, 'black')
                coinget_text_rect = coinget_text.get_rect(center = (200,420))
                screen.blit(coinget_text, coinget_text_rect)

            if item2 == 'kitty':
                kitty = Lock('graphic/miaoji.png', 325, 350, 0.18)
                kitty.draw(screen)
            elif item2 == 'tanker':
                tanker = Lock('graphic/tank chic.png', 325, 350, 0.18)
                tanker.draw(screen)
            elif item2 == 'magnet':
                magnet = Lock('graphic/magnetchic.png', 325, 350, 0.18)
                magnet.draw(screen)
            elif item2 == 'speedy':
                speedy = Lock('graphic/speedychic.png', 325, 350, 0.18)
                speedy.draw(screen)
            elif item2 == 'worrier':
                worrier = Lock('graphic/ninjachic.png', 325, 350, 0.18)
                worrier.draw(screen)
            else:
                coins = Lock('graphic/itemcoin.png', 325, 350, 1.5)
                coins.draw(screen)
                coinget_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render(f'Coin x{coinsget2}', True, 'black')
                coinget_text_rect = coinget_text.get_rect(center = (325,420))
                screen.blit(coinget_text, coinget_text_rect)

            if item3 == 'kitty':
                kitty = Lock('graphic/miaoji.png', width/2, 350, 0.18)
                kitty.draw(screen)
            elif item3 == 'tanker':
                tanker = Lock('graphic/tank chic.png', width/2, 350, 0.18)
                tanker.draw(screen)
            elif item3 == 'magnet':
                magnet = Lock('graphic/magnetchic.png', width/2, 350, 0.18)
                magnet.draw(screen)
            elif item3 == 'speedy':
                speedy = Lock('graphic/speedychic.png', width/2, 350, 0.18)
                speedy.draw(screen)
            elif item3 == 'worrier':
                worrier = Lock('graphic/ninjachic.png', width/2, 350, 0.18)
                worrier.draw(screen)
            else:
                coins = Lock('graphic/itemcoin.png', width/2, 350, 1.5)
                coins.draw(screen)
                coinget_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render(f'Coin x{coinsget3}', True, 'black')
                coinget_text_rect = coinget_text.get_rect(center = (width/2,420))
                screen.blit(coinget_text, coinget_text_rect)

            if item4 == 'kitty':
                kitty = Lock('graphic/miaoji.png', 575, 350, 0.18)
                kitty.draw(screen)
            elif item4 == 'tanker':
                tanker = Lock('graphic/tank chic.png', 575, 350, 0.18)
                tanker.draw(screen)
            elif item4 == 'magnet':
                magnet = Lock('graphic/magnetchic.png', 575, 350, 0.18)
                magnet.draw(screen)
            elif item4 == 'speedy':
                speedy = Lock('graphic/speedychic.png', 575, 350, 0.18)
                speedy.draw(screen)
            elif item4 == 'worrier':
                worrier = Lock('graphic/ninjachic.png', 575, 350, 0.18)
                worrier.draw(screen)
            else:
                coins = Lock('graphic/itemcoin.png', 575, 350, 1.5)
                coins.draw(screen)
                coinget_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render(f'Coin x{coinsget4}', True, 'black')
                coinget_text_rect = coinget_text.get_rect(center = (575,420))
                screen.blit(coinget_text, coinget_text_rect)
            
            if item5 == 'kitty':
                kitty = Lock('graphic/miaoji.png', 700, 350, 0.18)
                kitty.draw(screen)
            elif item5 == 'tanker':
                tanker = Lock('graphic/tank chic.png', 700, 350, 0.18)
                tanker.draw(screen)
            elif item5 == 'magnet':
                magnet = Lock('graphic/magnetchic.png', 700, 350, 0.18)
                magnet.draw(screen)
            elif item5 == 'speedy':
                speedy = Lock('graphic/speedychic.png', 700, 350, 0.18)
                speedy.draw(screen)
            elif item5 == 'worrier':
                worrier = Lock('graphic/ninjachic.png', 700, 350, 0.18)
                worrier.draw(screen)
            else:
                coins = Lock('graphic/itemcoin.png', 700, 350, 1.5)
                coins.draw(screen)
                coinget_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 25).render(f'Coin x{coinsget5}', True, 'black')
                coinget_text_rect = coinget_text.get_rect(center = (700,420))
                screen.blit(coinget_text, coinget_text_rect)

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


def ohno(username, lvl, coin, pull, c, equip, stats) :

    pygame.display.set_caption('Chicky Simulator - Wishes')
    screen.blit(background_image,(0,0))
    screen.blit(font.render('You do not have enough coin.',True,'white'),(180,300))
    screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
    while True :
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                wish(username, lvl, coin, pull, c, equip, stats)

            if event.type == pygame.quit:
                pygame.quit()
                sys.exit()

        pygame.display.flip()


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

                'coin90', 'kitty','tanker','worrier','speedy','magnet')
        
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
                        ohno(username, lvl, coin, pull, c, equip, stats)

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
                        ohno(username, lvl, coin, pull, c, equip, stats)

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


def mode(username, lvl, coin, pull, c, equip, stats):
    # let user pick normal/arcade - by puopuo

    while True:
        # screen display / setup
        pygame.display.set_caption('Chicky Simulator - Chicky')
        screen.blit(background_image,(0,0))

        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('Choose mode', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,150))
        screen.blit(title_text, title_text_rect)

        
        #normal
        play_button1 = Button('graphic/button2.png', 250, 400, 0.3, "Normal")
        play_button1.draw(screen)
        play_button2 = Button('graphic/button2.png', 650, 400, 0.3, "arcade")
        play_button2.draw(screen)
        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)


        pos_mouse = pygame.mouse.get_pos()

        # get user's selection
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button1.check_input(pos_mouse):
                    choose_level(lvl, username, coin, pull, c, equip, stats)
                
                if play_button2.check_input(pos_mouse):
                    arcade_lobby(lvl, username, coin, pull, c, equip, stats)

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
                    mode(username, lvl, coin, pull, chicky, equip, stats)
                
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

        collection_button = Button('graphic/botton1.png', 800, 350, 0.6, "!")
        collection_button.draw(screen)

        achievement_button = Button('graphic/botton1.png', 830, 70, 0.6, "$")
        achievement_button.draw(screen)

        pos_mouse = pygame.mouse.get_pos()

        # get user events (their selections)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.check_input(pos_mouse):
                    mode(username, lvl, coin, pull, chicky, equip, stats)

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

                if chicky_button.check_input(pos_mouse):
                    equip_chick(username, lvl, coin, pull, chicky, equip, stats)

                if achievement_button.check_input(pos_mouse):
                    achievement(username, lvl, coin, pull, chicky, equip, stats)

                if back_button.check_input(pos_mouse):
                    log_or_reg()

                if quit_button.check_input(pos_mouse):
                    pygame.quit()
                    sys.exit()

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
        pygame.display.update()


def check_default(username):
    Hp, Def, Atk, Cd, Mag = 0, 0, 0, 0, 0 # Default initialization
    
    with open('user_details.txt', 'r') as file1:
        lines = file1.readlines()
        for line in lines:
            user_default = line.strip().split(", ")
            if user_default[0] == username:
                chicky = user_default[6]
                if chicky == 'normal':
                    chicky_graphic = 'graphic/chicky.png'
                    Hp, Def, Atk, Cd, Mag = 100, 0, 10, 5000, 0
                    break
                elif chicky == 'kitty':
                    chicky_graphic = 'graphic/miaoji.png'
                    Hp, Def, Atk, Cd, Mag = 150, 0, 10, 5000, 0
                    break
                elif chicky == 'worrier':
                    chicky_graphic = 'graphic/ninjachic.png'
                    Hp, Def, Atk, Cd, Mag = 75, 0, 20, 5000, 0
                    break
                elif chicky == 'magnet':
                    chicky_graphic = 'graphic/magnetchic.png'
                    Hp, Def, Atk, Cd, Mag = 100, 0, 10, 5000, 1
                    break
                elif chicky == 'speedy':
                    chicky_graphic = 'graphic/speedychic.png'
                    Hp, Def, Atk, Cd, Mag = 75, 0, 10, 2500, 0
                    break
                elif chicky == 'tanker':
                    chicky_graphic = 'graphic/tank chic.png'
                    Hp, Def, Atk, Cd, Mag = 200, 20, 10, 10000, 0
                    break

    with open('user_details.txt', 'r') as file2:
        lines = file2.readlines()
        for line in lines:
            user_default = line.strip().split(", ")
            if user_default[0] == username:
                equip_list = user_default[7].split('/')

    with open('equipment_details.txt', 'r') as file3:
        lines = file3.readlines()
        for line in lines:
            item_details = line.split(",")
            for equipments in equip_list:
                if item_details[0] == equipments:
                    a, d, s = item_details[4].split('/')
                    Atk += int(a)
                    Def += int(d)
                    Cd += int(s)

    stats = str(f'{Hp}/{Def}/{Atk}/{Cd}/{Mag}')
    #equip_str = '/'.join(equip_list)
    #print(str(equip_str))
    #print(chicky)
    # print(stats)
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
            file1 = open('user_details.txt', 'a')
            file1.write(f'{username}, {password}, 1, 10000, 0, 0, normal, no/' + '\n')
            # username, password, level, time, coin, pull, chicky, equip
            file1.close()

            file2 = open('user_backpack.txt', 'a')
            file2.write(f'{username}, normal/0, no/, no' + '\n')
            file2.close()

            file3 = open('user_achievement.txt', 'a')
            file3.write(f'{username}, 0/0/0/0/0/0, 0/0/0/0/0/0, 0/0/0/0/0/0' + '\n')
            file3.close()

            lvl = 1
            coin = 0
            pull = 0
            chicky = 'normal'
            equip = 'no/'
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
                    lvl, coin, pull, chicky, equip, stats = save_userinput(username_input.text, password_input.text) # link to later use
                    welcome_user(username_input.text, int(lvl), int(coin), int(pull), chicky, equip, stats)
            
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
                user_backpack[2] = str(weapon_str)
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
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if buy_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
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
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                        
                if buy_button3.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
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
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break

                if buy_button4.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
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
                            user_backpack[2] = str(equipments_str)
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
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                    
                if back_button.check_input(pos_mouse):
                    store(username, lvl, coin, pull, chicky, equip, stats)
                if next_button.check_input(pos_mouse):
                    equipment2(username, lvl, coin, pull, chicky, equip, stats)

        if buy :
            bought2(username, lvl, coin, pull, chicky, equip, stats)
        elif no :
            no_money2(username, lvl, coin, pull, chicky, equip, stats)

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
                user_backpack[2] = str(weapon_str)
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
                            equipments_list = user_backpack[2].split('/')
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
                            user_backpack[2] = str(equipments_str)
                            lines[i] = ', '.join(user_backpack) + '\n'
                            break
                                                         
                        
                if buy_button2.check_input(pos_mouse):
                    with open('user_backpack.txt', 'r') as file:
                        lines = file.readlines()

                    for i, line in enumerate(lines):
                        user_backpack = line.strip().split(", ")
                        if user_backpack[0] == username:
                            equipments_list = user_backpack[2].split('/')
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
                            equipments_list = user_backpack[2].split('/')
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
                            user_backpack[2] = str(equipments_str)
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

        #surface
        store_surface = pygame.Surface((250,250))
        store_surface.fill('black')
        store_surface.set_alpha(150)
        store_surface_rect = store_surface.get_rect(center=(650,350))
        screen.blit(store_surface, store_surface_rect)

        #BUTTONS
        play_button1 = Button('graphic/button2.png', 250, 550, 0.2, "PLAY")
        play_button1.draw(screen)
        #########

        #coming soon
        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render('Coming Soon', True, 'white')
        title_text_rect = title_text.get_rect(center = (650,550))
        screen.blit(title_text, title_text_rect)
        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 75).render('?', True, 'white')
        title_text_rect = title_text.get_rect(center = (650,350))
        screen.blit(title_text, title_text_rect)


        #image
        snake_image = pygame.image.load('graphic/snake.png')
        screen.blit(snake_image,(120,225))



        #Back page button#
        back_button = Button('graphic/botton1.png', 70, 70, 0.6, "<<")
        back_button.draw(screen)
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button1.check_input(pos_mouse):
                    snake_lobby(username, lvl, coin, pull, chicky, equip, stats)                                   
                        

                if back_button.check_input(pos_mouse):
                    mode(username, lvl, coin, pull, chicky, equip, stats)           

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


def crush_lobby(username, lvl, coin, pull, chicky, equip, stats) :
    # puo puo did also this
    on = True
    while on :
        screen.blit(background_image,(0,0))
        pos_mouse = pygame.mouse.get_pos()
        pygame.display.set_caption('Chicky Simulator - Coming Soon')
        title_text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 80).render('Unnamed', True, 'white')
        title_text_rect = title_text.get_rect(center = (450,200))
        screen.blit(title_text, title_text_rect)

        #buttons#
        back_button = Button('graphic/botton1.png', 50, 35, 0.5, "<<")
        back_button.draw(screen)
        # play_button = Button('graphic/button2.png', 450, 600, 0.3, "")
        # play_button.draw(screen)

        #tutorial


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                on = False
            if event.type == pygame.MOUSEBUTTONDOWN :
                if back_button.check_input(pos_mouse):
                    arcade_lobby(username, lvl, coin, pull, chicky, equip, stats)
                # if play_button.check_input(pos_mouse):
                #     crush(username, lvl, coin, pull, chicky, equip, stats)
        
        
        pygame.display.flip()

    pygame.quit()
    sys.exit()


#def collection(username, lvl, coin, pull, chicky, equip, stats) :
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
    #all info made by puopuo

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
    # all collection made by puopuo
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
                    equipments_list = user_backpack[2].split('/')
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
                user_backpack[2] = str(weapon_str)
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
                            equipments_list = user_backpack[2].split('/')
                            if 'armor3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)    

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
                            if 'armor4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

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
                            if 'armor5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
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
                    equipments_list = user_backpack[2].split('/')
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
                            equipments_list = user_backpack[2].split('/')
                            if 'helmet3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment2(username, lvl, coin, pull, chicky, equip, stats)    

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
                            if 'helmet4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment2(username, lvl, coin, pull, chicky, equip, stats)  

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
                            if 'helmet5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment2(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
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
                    equipments_list = user_backpack[2].split('/')
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
                            equipments_list = user_backpack[2].split('/')
                            if 'shoe3' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)    

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
                            if 'shoe4' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

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
                            if 'shoe5' in equipments_list :
                                backpack(username,lvl, coin, pull, chicky, equip, stats)
                            else :
                                equipment(username, lvl, coin, pull, chicky, equip, stats)  

                            equipments_str = '/'.join(equipments_list)
                            user_backpack[2] = str(equipments_str)
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
    #puo puo did

    width, height = 900, 700
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption('Chicky Simulator - Arcade Mode - Chick Game')

    background_image = pygame.image.load('graphic/map.jpg')
    coin_image = pygame.image.load('graphic/coin.png')
    manycoin_image = pygame.image.load('graphic/manycoin.png')
    coin_image = pygame.transform.scale(coin_image, (50, 50))
    manycoin_image = pygame.transform.scale(manycoin_image, (50, 50))
    pygame.transform.scale(background_image,(700,700))

    font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 100)
    clock = pygame.time.Clock()
    ticks = pygame.time.get_ticks()
    pygame.time.set_timer(pygame.USEREVENT+1, 1000)

    chick_images = [pygame.image.load('graphic/geekchic.png'),pygame.image.load('graphic/monster2.png'),pygame.image.load('graphic/monster1.png'),pygame.image.load('graphic/monster3.png')]
    

    on = True
    time = 0
    coins = 0
    played = 0
    chick_position = [50, 50]
    chick_speed = 15
    chick_body =[[50,50]]
    direction = 'RIGHT'
    change_to = direction
    coin_position = [random.randrange(1,width-50),random.randrange(1,height-50)]
    coin_spawn = True
    chick_index = 0


    def game_over(username, lvl, coin, pull, chicky, equip, stats) :
        font = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50)

        on = True
        

        while on :
            screen.blit(background_image,(0,0))
            screen.blit(font.render(f'Your score is : {coins} ',True,'white'),(280,300))
            screen.blit(font.render('Click again to go back.',True,'white'),(230,350))
            pygame.display.flip()


            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    snake_lobby(username, lvl, coin, pull, chicky, equip, stats)
                    if played >= 1:
                        with open('progress.txt', 'r') as file:
                            lines = file.readlines()

                        for i, line in enumerate(lines):
                            user_progress = line.strip().split(", ")
                            if user_progress[0] == username:
                                coin_list = user_progress[1].split('/')
                                if coin_list[0] == 'no':
                                    del coin_list[0]
                                    coin_list.append(f'{coins}')
                                coin_str = '/'.join(coin_list)
                                user_progress[2] = str(coin_str)
                                lines[i] = ', '.join(user_progress) + '\n'
                                break
                        with open('progress.txt', 'w') as file:
                            file.writelines(lines)
                        return
                if event.type == pygame.QUIT:
                    on = False
                    sys.exit()


            pygame.display.flip()
    

    def update_progress(username, lvl, coin, pull, chicky, equip, stats) :

        on = True

        while on :
            
            if coins >=20 and coins <=39 :
                with open('user_score.txt', 'r') as file:
                    lines = file.readlines()

                for i, line in enumerate(lines):
                    user_progress = line.strip().split(", ")
                    if user_progress[0] == username:
                        coin_list = user_progress[1].split('/')
                        if coin_list[0] == 'no':
                            del coin_list[0]
                            coin_list.append(f'{coins}')
                        coin_str = '/'.join(coin_list)
                        user_progress[2] = str(coin_str)
                        lines[i] = ', '.join(user_progress) + '\n'
                        break
                with open('user_score.txt', 'w') as file:
                    file.writelines(lines)
                return
            if coins >= 40 and coins <= 59 :
                with open('user_score.txt', 'r') as file:
                    lines = file.readlines()

                for i, line in enumerate(lines):
                    user_progress = line.strip().split(", ")
                    if user_progress[0] == username:
                        coin_list = str(user_progress[1].split('/'))
                        if coin_list[1] == 'no':
                            del coin_list[1]
                            coin_list.append('1')
                        coin_str = '/'.join(coin_list)
                        user_progress[2] = str(coin_str)
                        lines[i] = ', '.join(user_progress) + '\n'
                        break
                with open('user_score.txt', 'w') as file:
                    file.writelines(lines)
                return
            if coins >= 60 :
                with open('user_score.txt', 'r') as file:
                    lines = file.readlines()

                for i, line in enumerate(lines):
                    user_progress = line.strip().split(", ")
                    if user_progress[0] == username:
                        coin_list = str(user_progress[1].split('/'))
                        if coin_list[2] == 'no':
                            del coin_list[2]
                            coin_list.append('1')
                        coin_str = '/'.join(coin_list)
                        user_progress[2] = str(coin_str)
                        lines[i] = ', '.join(user_progress) + '\n'
                        break

                with open('user_score.txt', 'w') as file:
                    file.writelines(lines)
                return  

    

        with open('user_score.txt', 'w') as file:
            file.writelines(lines)
        return



    while on :
        
        coin_spawn = True
        screen.blit(background_image,(0,0))
        screen.blit(manycoin_image,(650,25))
        screen.blit(coin_image, pygame.Rect(coin_position[0], coin_position[1], 35, 35))

        

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


        
        #make sure no 'u turn' happens
        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            chick_position[1] -= 20
        if direction == 'DOWN':
            chick_position[1] += 20
        if direction == 'LEFT':
            chick_position[0] -= 20
        if direction == 'RIGHT':
            chick_position[0] += 20

        chick_body.insert(0, list(chick_position))

        chick_rect =  pygame.Rect(chick_position[0], chick_position[1], 50, 50)
        coin_rect = pygame.Rect(coin_position[0], coin_position[1], 50, 50)

        #coin collision
        if chick_rect.colliderect(coin_rect):
            
            coin_spawn = False
            coins += 2
            chick_index =(chick_index + 1) % len(chick_images)
        else:
            chick_body.pop()
            
        if not coin_spawn:
            coin_position = [random.randrange(1,width-50),random.randrange(1,height-50)]
            
        #check new added image 
        for index , position in enumerate(chick_body):
            if index == 0:
                chick_image = pygame.transform.scale(chick_images[0], (50,50))
            else :
                chick_image = pygame.transform.scale(chick_images[(chick_index + index - 1) % len(chick_images)],(50, 50))
            screen.blit(chick_image,pygame.Rect(position[0],position[1],50,50))
            
        # Game Over conditions
        #left right
        if chick_position[0] < 0 or chick_position[0] > width-35:
            game_over(username, lvl, coin, pull, chicky, equip, stats)
            
        #up down
        if chick_position[1] < 0 or chick_position[1] > height-35:
            game_over(username, lvl, coin, pull, chicky, equip, stats)
            
        
        #timer
        time = 60 - (pygame.time.get_ticks() - ticks) // 1000
        if time <= 50 :
            played += 1
            game_over(username, lvl, coin, pull, chicky, equip, stats)
            


        #collision with body
        for block in chick_body[1:]:
            if chick_position == block:
                game_over(username, lvl, coin, pull, chicky, equip, stats)
                
        
        

        timer_text = font.render(f"{time}", True, (255,255,255))
        text_rect = timer_text.get_rect(center = (width//2,50))
        screen.blit(timer_text, text_rect)

        coin_text = font.render(f"{coins}", True, (255,255,255))
        text_rect = coin_text.get_rect(center = (750,50))
        screen.blit(coin_text, text_rect)

    

        pygame.display.update()

        clock.tick(chick_speed)


log_or_reg()
