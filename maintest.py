import pygame
import sys
import pygame_gui
from button import Button # library by my
from rank import Ranking # library by my
from lock import Lock # library by my
import pickle
from os import path

pygame.init()

width, height = 700, 700
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
level = 1
maxlevel = 30
main_menu = 0

username_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,320), (300,50)), manager = Manager, object_id = '#username')
password_input = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((300,450), (300,50)), manager = Manager, object_id = '#password')

time = 0
fps = 60
pygame.time.set_timer(pygame.USEREVENT+1, 1000)
clock = pygame.time.Clock()
time_use =[]

def reset_level(level):
    
    jy_group.empty()
    yuen_group.empty()
    puolin_group.empty()

    if path.exists(f'level{level}_data'):
        pickle_in = open(f'level{level}_data', 'rb')
        world_data = pickle.load(pickle_in)
    world = World(world_data)

    return world

class chicky():
    def __init__(self,x,y):
                chic = pygame.image.load('graphic/geekchic.png')
                self.image = pygame.transform.scale(chic,(30,30))
                self.rect = self.image.get_rect(center=(17,17))
                self.rect.x = x
                self.rect.y = y

    def update(self,gameover):
        dx = 0 # Willie : teacher teacher what is this
        dy = 0 # Jy : Change in position of player, we nid this to do collision ltr

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

if path.exists(f'level{level}_data'):
    pickle_in = open(f'level{level}_data', 'rb')
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
            world = reset_level(level)
            gameover = 0

    if gameover == 1:
        #reset game and go to next level
        level += 1
        if level <= maxlevel:
            #reset level
            world_data = []
            world = reset_level(level)
            Chicky = chicky(35,35)
            gameover = 0
        # else:
        #     # if restart_button.draw(screen):
        #         level = 1
        #         #reset level
        #         world_data = []
        #         world = reset_level(level)
        #         gameover = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if chick1_button.check_input(pos_mouse):
        #             c = 'graphic/kunchic.png' # link to later use
        #             level(c, lvl, username)


    pygame.display.update()

pygame.quit()