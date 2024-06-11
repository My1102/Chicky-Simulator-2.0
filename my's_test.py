import pygame
import sys

# Constants
FPS = 60
BACKPACK_ROWS = 5
BACKPACK_COLS = 3
SLOT_SIZE = 100
BACKPACK_X_OFFSET = 495
BACKPACK_Y_OFFSET = 140
SLOT_X_GAP = 25
SLOT_Y_GAP = 10
EQUIP_SLOT_COORDS = [(105, 430), (255, 430), (30, 550), (180, 550), (330, 550)]
FONT_PATH = "ThaleahFat/ThaleahFat.ttf"
WHITE = 'white'

# Classes
class Item:
    def __init__(self, graphic, item_type, info, stats, name, scale):
        self.image = pygame.image.load(graphic)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.type = item_type
        self.info = info
        self.name = name
        self.stats = self.ori_stats(stats)

    def ori_stats(self, stats):
        stat_values = stats.split('/')
        return {
            'Atk': int(stat_values[0]),
            'Def': int(stat_values[1]),
            'Spd': int(stat_values[2])
        }

class Slot:
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None
        self.type = None

    def draw(self, screen):
        pygame.draw.rect(screen, 'black', self.rect, 4)
        if self.item:
            screen.blit(self.item.image, self.rect)

class Button:
    # set the parameter
    def __init__(self, image_path, x, y, scale, text):
        image = pygame.image.load(image_path)
        width, height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.pos_x = x
        self.pos_y = y
        self.image_rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
        self.text = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(text, True, 'white')
        self.text_rect = self.text.get_rect(center=(self.pos_x, self.pos_y))
    
    # use to display
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)
        screen.blit(self.text, self.text_rect)

    # check user mouse is in the area or not
    def check_input(self, position):
        # if position[0] in range(self.image_rect.left, self.image_rect.right) and position[1] in range(self.image_rect.top, self.image_rect.bottom):
        if self.image_rect.collidepoint(position):
            return True
        return False

class Info:
    def __init__(self, x, y, info):
        self.info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 45).render(info, True, 'black')
        self.pos_x = x
        self.pos_y = y
        # self.info_rect = self.info.get_rect(center=(self.pos_x, self.pos_y))

    def draw_info(self, screen):
        screen.blit(self.info, (self.pos_x, self.pos_y))

class Lock():
    # set the parameter
    def __init__(self, image_path, x, y, scale):
        image = pygame.image.load(image_path)
        width, height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.pos_x = x
        self.pos_y = y
        self.image_rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
    
    # use to display
    def draw(self, screen):
        screen.blit(self.image, self.image_rect)

def update_equip(username, equip):
    weapon = ['axe','hammer','sword']
    shield = ['shield3','shield4','shield5']
    helmet = ['helmet3','helmet4','helmet5']
    armor = ['armor3','armor4','armor5']
    shoe = ['shoe3','shoe4','shoe5']

    with open('user_details.txt', 'r') as file:
        lines = file.readlines()

    for i, line in enumerate(lines):
        user_details = line.strip().split(", ")
        if user_details[0] == username:
            equip_list = user_details[7].strip().split('/')
            if equip in weapon:
                equip_list[0] = str(f'{equip}')
                break
            elif equip in shield:
                equip_list[1] = str(f'{equip}')
                break
            elif equip in helmet:
                equip_list[2] = str(f'{equip}')
                break
            elif equip in armor:
                equip_list[3] = str(f'{equip}')
                break
            elif equip in shoe:
                equip_list[4] = str(f'{equip}')
                break

    equip_str = '/'.join(equip_list)
    user_details[7] = str(equip_str)
    lines[i] = ', '.join(user_details) + '\n'

    with open('user_details.txt', 'w') as file:
        file.writelines(lines)

    return str(equip_str)

#def update_stats(ori_stats, equips):
    #Hp, Def, Atk, Spd, Mag = ori_stats.split('/')
    #Atk = int(Atk)
    #Def = int(Def)
    #Spd = int(Spd)
    #Hp, Def, Atk, Spd, Mag = [int(stat) for stat in ori_stats.split('/')]
    #for item in equips:
        #for stat, value in item.stats.items():
            #if stat == 'Atk':
                #Atk += value
            #elif stat == 'Def':
                #Def += value
            #elif stat == 'Spd':
                #Spd += value
    #return (f'{Hp}/{Def}/{Atk}/{Spd}/{Mag}')

def get_temp_stats(stats, equips, selected_item, is_adding):
    #current_stats = update_stats(stats, current_equips)
    Hp, Def, Atk, Spd, Mag = stats.split('/')
    Atk = int(Atk)
    Def = int(Def)
    Spd = int(Spd)
    for item in equips:
        for stat, value in item.stats.items():
            if stat == 'Atk':
                Atk += value
            elif stat == 'Def':
                Def += value
            elif stat == 'Spd':
                Spd += value

    for stat, value in selected_item.stats.items():
        if stat == 'Atk':
            if is_adding == 1:
                Atk += value
            else:
                Atk -= value
        elif stat == 'Def':
            if is_adding == 1:
                Atk += value
            else:
                Atk -= value
        elif stat == 'Spd':
            if is_adding == 1:
                Atk += value
            else:
                Atk -= value

    return (f'{Hp}/{Def}/{Atk}/{Spd}/{Mag}')

def backpack(username, lvl, coin, pull, chicky, equip, stats):
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    clock = pygame.time.Clock()
    FPS = 120
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
    #all_equip =[]
    with open('equipment_details.txt', 'r') as file2:
        lines = file2.readlines()
        for line in lines:
            item_details = line.split(",")
            for i in items_list:
                if i in item_details[0]:
                    item_name = (f'{item_details[0]}')
                    item_graphic = (f'{item_details[1]}')
                    item_info = (f'{item_details[2]}\n{item_details[3]}')
                    item_type = (f'{item_details[5]}')
                    item_stat = (f'{item_details[4]}')
                    item = Item(item_graphic, item_type, item_info, item_stat, item_name, 0.65)
                    items.append(item)

            for i in equips_list:
                if i in item_details[0]:
                    equip1_name = (f'{item_details[0]}')
                    equip1_graphic = (f'{item_details[1]}')
                    equip1_info = (f'{item_details[2]}\n{item_details[3]}')
                    equip1_type = (f'{item_details[5]}')
                    equip1_stat = (f'{item_details[4]}')
                    equip1 = Item(equip1_graphic, equip1_type, equip1_info, equip1_stat, equip1_name, 0.65)
                    equips.append(equip1)

            #for i in equipments_list:
                #if i in item_details[0]:
                    #aequip_name = (f'{item_details[0]}')
                    #aequip_graphic = (f'{item_details[1]}')
                    #aequip_info = (f'{item_details[2]}\n{item_details[3]}')
                    #aequip_type = (f'{item_details[5]}')
                    #aequip_stat = (f'{item_details[4]}')
                    #aequip = Item(aequip_graphic, aequip_type, aequip_info, aequip_stat, aequip_name, 0.65)
                    #all_equip.append(aequip)

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
                        temp_stats = get_temp_stats(stats, equips, selected_item, 1)
                        break

                for slot in equip_slots:
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        selected_item.rect.x = pos_mouse[0] + offset_x
                        selected_item.rect.y = pos_mouse[1] + offset_y
                        slot.item = None
                        temp_stats = get_temp_stats(stats, equips, selected_item, 0)
                        break

                #if back_button.check_input(pos_mouse):
                    #lobby(username, lvl, coin, pull, chicky, equip, stats)

            elif event.type == pygame.MOUSEMOTION:
                if selected_item:
                    selected_item.rect.x = pos_mouse[0] + offset_x
                    selected_item.rect.y = pos_mouse[1] + offset_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_item != None:
                    for slot in backpack_slots:
                        if (slot.rect.collidepoint(pos_mouse)) and (slot.item is None):
                            slot.item = selected_item
                            if selected_item in items:
                                selected_item = None
                                offset_x, offset_y = None, None
                                temp_stats = stats
                                backpack(username, lvl, coin, pull, chicky, equip, temp_stats)
                                break
                            elif selected_item in equips:
                                equips.remove(selected_item)
                                items.append(selected_item)
                                selected_item = None
                                offset_x, offset_y = None, None
                                backpack(username, lvl, coin, pull, chicky, equip, temp_stats)
                                break

                    for slot in equip_slots:
                        if (slot.rect.collidepoint(pos_mouse)) and (slot.item is None):
                            same_type_item = next((equip for equip in equips if equip.type == selected_item.type), None)
                            if same_type_item:
                                # Revert to original state
                                for slot in backpack_slots:
                                    if slot.item is None:
                                        slot.item = selected_item
                                        selected_item = None
                                        temp_stats = stats
                                        backpack(username, lvl, coin, pull, chicky, equip, temp_stats)
                                        break
                            else:
                                items.remove(selected_item)
                                equips.append(selected_item)
                                eequipp = str(f'{selected_item.name}')
                                slot.item = selected_item
                                selected_item = None
                                offset_x, offset_y = None, None
                                e = update_equip(username, eequipp)
                                backpack(username, lvl, coin, pull, chicky, e, temp_stats)
                                break

                    if selected_item:
                            for slot in backpack_slots:
                                if slot.item is None:
                                    slot.item = selected_item
                                    selected_item = None
                                    offset_x, offset_y = None, None

        # Draw slots
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
            nHp,nDef,nAtk,nSpd,nMag = temp_stats.split('/')
            new_default = Info(250, 150, (f'Hp={nHp}\nDef={nDef}\nAtk={nAtk}\nSpd={nSpd}'))
            new_default.draw_info(screen)
            info = Info(50, 335, selected_item.info)
            info.draw_info(screen)
            #backpack(username, lvl, coin, pull, chicky, equip, temp_stats)

        pygame.display.flip()
        clock.tick(FPS)

        pygame.display.update()

if __name__ == "__main__":
    # Sample data for testing
    username = "my"
    lvl = 1
    coin = 100
    pull = 0
    chicky = 0
    equip = "no/"
    stats = "100/0/10/10/0"
    backpack(username, lvl, coin, pull, chicky, equip, stats)
