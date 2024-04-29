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
from button import Button # library by my
from rank import Ranking # library by my
from lock import Lock # library by my

pygame.init()

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

# let user enter their username and password (using pygame_gui manager) - by my
# learn from tutorial
username_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,320), (300,50)), manager = Manager, object_id = '#username')
password_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,450), (300,50)), manager = Manager, object_id = '#password')

# added later
def caution(c, lvl, username):
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
                    tutorial2(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    level(c, lvl, username)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
                    
        pygame.display.update()


def tutorial1(c, lvl, username):
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
                    caution(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    level(c, lvl, username)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
                  
        pygame.display.update()        


def tutorial2(c, lvl, username):
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
                    level1(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    level(c, lvl, username)

                Manager.process_events(event)

            Manager.update(UI_REFRESH_RATE)
                    
        pygame.display.update()   


def tutorial4(c, lvl, username):
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
                    level3(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    level(c, lvl, username)
                  
        pygame.display.update()   


def tutorial3(c, lvl, username):
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
                    level2(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    level(c, lvl, username)
                  
        pygame.display.update()   


def level1(c, lvl, username): # This one easier to read
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
                            win(c, lvl, username, levl)
                            
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


def level2(c, lvl, username):
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
                            win(c, lvl, username, levl)
                            
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


def level3(c, lvl, username):
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
                            win(c, lvl, username, levl)
                            
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


def level4(c, lvl, username):
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
                            win(c, lvl, username, levl)
                            
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


def level5(c, lvl, username):
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
                            update_step(username, time_use[0])
                            win5(c, lvl, username)
                            
                            
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


def win5(c, lvl, username):
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
                    level(c, lvl, username)

                if rank_button.check_input(pos_mouse):
                    ranking(username, lvl)
                  
        pygame.display.update()


def win(c, lvl, username, levl):
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
                    level(c, lvl, username)

                if next_button.check_input(pos_mouse): #changed later
                    if levl == 2:
                        tutorial3(c, lvl, username)
                    elif levl == 3:
                        tutorial4(c, lvl, username)
                    elif levl == 4:
                        level4(c, lvl, username)
                    elif levl == 5:
                        level5(c, lvl, username)
                  
        pygame.display.update()


def update_step(username, step):
    # by 'Puo Puo'(Puo Lin)
    # steps used updating
    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    #sort 
    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            if int(user_details[3]) > int(step):
                user_details[3] = str(step)
                lines[i] = ', '.join(user_details) + '\n'
                break
            # user_details[3] = str(step)
            # lines[i] = ', '.join(user_details) + '\n'
            # break
            else:
                break

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)

    return


def update_level(username, lvl):
    # by 'Puo Puo'(Puo Lin) 
    # store lvl user played 
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


def ranking(username, lvl):
    # leaderboard functions by my
    while True:

        # screen display / setup
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
            for rank, (Username, Password, Level, Time) in enumerate(sorted_data[0:9], start=1):
                first = Ranking(130+(rank*50), str(rank), Username, Time)
                first.show(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    lobby(username, lvl)

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def chick(username, lvl):
    # let user pick their character - by my

    while True:
        # screen display / setup
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
                    level(c, lvl, username)

                if chick2_button.check_input(pos_mouse):
                    c = 'graphic/geekchic.png'
                    level(c, lvl, username)

                if chick3_button.check_input(pos_mouse):
                    c = 'graphic/pinkchic.png'
                    level(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    lobby(username, lvl)

                Manager.process_events(event)
            
            Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def level(c, lvl, username):
    # level selection - by my

    while True:
        
        # screen display / setup
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

        back_button = Button('graphic/button2.png', 450, 580, 0.35, "BACK")
        back_button.draw(screen)
        
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
                    tutorial1(c, lvl, username)

                if lvl2_button.check_input(pos_mouse):
                    if lock2_con == True:
                        tutorial3(c, lvl, username)

                if lvl3_button.check_input(pos_mouse):
                    if lock3_con == True:
                        tutorial4(c, lvl, username)

                if lvl4_button.check_input(pos_mouse):
                    if lock4_con == True:
                        level4(c, lvl, username)

                if lvl5_button.check_input(pos_mouse):
                    if lock5_con == True:
                        level5(c, lvl, username)

                if back_button.check_input(pos_mouse):
                    chick(username, lvl)
            
            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def lobby(username, lvl):
    # main lobby when user start - my

    while True:

        #screen display / setup
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
                    chick(username, lvl)  

                if rank_button.check_input(pos_mouse):
                    ranking(username, lvl)

                if back_button.check_input(pos_mouse):
                    log_or_reg()

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
            Username, Password, Level, Time = i.split(",")
            Password = Password.strip()
            Level = Level.strip()
            Time = Time.strip()
            if (Username == username and Password == password):
                return Level # return the user's previous lvl
            
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
            list = i.split(",")

            # check if the name has been used before
            # I test run before it works but now dunno why it not functioning TT
            if username == list[0]:
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

            # make sure user type their password
            elif password == '':
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

            # save user details
            else:
                file = open('user_details.txt', 'a')
                file.write(f'{username}, {password}, 1, 10000' + '\n')
                file.close()
                lvl = 1
                return lvl
            
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


def welcome_user(username, lvl):
    # screen display after user done with login/register part - my
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                lobby(username, lvl)

            Manager.process_events(event)

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
                    lvl = int(read_userinput(username_input.text, password_input.text)) # link to later use
                    welcome_user(username_input.text, lvl)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    log_or_reg()

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def register():
    # register page display - by my
    while True:
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
                    lvl = int(save_userinput(username_input.text, password_input.text)) # link to later use
                    welcome_user(username_input.text, lvl)
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.check_input(pos_mouse):
                    log_or_reg()

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        pygame.display.update()


def log_or_reg():
    # login or register screen display - by my
    while True:
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


log_or_reg()