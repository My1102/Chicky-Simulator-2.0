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
class Slot:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None
    
    def draw(self, screen):
        if self.item:
            screen.blit(self.item.image, self.rect.topleft)
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)

class Item:
    def __init__(self, graphic, item_type, info, scale):
        self.image = pygame.image.load(graphic)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.type = item_type
        self.info = info
        self.stats = self.parse_stats(info)

    def parse_stats(self, info):
        stats = {}
        lines = info.split('\n')
        for line in lines:
            if '=' in line:
                key, value = line.split('=')
                stats[key.strip()] = int(value.strip())
        return stats

class Button:
    def __init__(self, image_path, x, y, scale, text):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.text = text
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        font = pygame.font.Font(FONT_PATH, 36)
        text_surface = font.render(self.text, True, WHITE)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def check_input(self, pos_mouse):
        return self.rect.collidepoint(pos_mouse)

class Info:
    def __init__(self, x, y, text):
        self.x = x
        self.y = y
        self.text = text
    
    def draw_info(self, screen):
        font = pygame.font.Font(FONT_PATH, 24)
        lines = self.text.split('\n')
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, WHITE)
            screen.blit(text_surface, (self.x, self.y + i * 30))

class Lock:
    def __init__(self, image_path, x, y, scale):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect(center=(x, y))
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

# Utility Functions
def load_user_backpack(username):
    with open('user_backpack.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            user_backpack = line.strip().split(", ")
            if user_backpack[0] == username:
                return user_backpack[2].split('/')
    return []

def load_item_details(items_list):
    items = []
    with open('equipment_details.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            item_details = line.strip().split(",")
            for item_name in items_list:
                if item_name == item_details[0]:
                    item_graphic = item_details[1]
                    item_info = f'{item_details[2]}\n{item_details[3]}'
                    item_type = item_details[5]
                    item = Item(item_graphic, item_type, item_info, 0.65)
                    items.append(item)
    return items

def create_slots(rows, cols, x_offset, y_offset, slot_size, x_gap, y_gap):
    slots = []
    for row in range(rows):
        for col in range(cols):
            x = x_offset + col * (slot_size + x_gap)
            y = y_offset + row * (slot_size + y_gap)
            slots.append(Slot(x, y, slot_size, slot_size))
    return slots

def draw_ui(screen, coin, stats, backpack_slots, equip_slots, selected_item):
    screen.fill((0, 0, 0))  # Clear screen with black
    pygame.display.set_caption('Chicky Simulator - Backpack')

    # Static Elements
    backpack_text = pygame.font.Font(FONT_PATH, 100).render('Backpack', True, WHITE)
    backpack_text_rect = backpack_text.get_rect(center=(450, 80))
    screen.blit(backpack_text, backpack_text_rect)

    coin_logo = Lock('graphic/manycoin.png', 700, 80, 0.3)
    coin_logo.draw(screen)

    coin_text = pygame.font.Font(FONT_PATH, 50).render(f'{coin}', True, WHITE)
    coin_text_rect = coin_text.get_rect(center=(780, 80))
    screen.blit(coin_text, coin_text_rect)

    backpack_surface = pygame.Surface((420, 550))
    backpack_surface.fill('white')
    backpack_surface.set_alpha(150)
    backpack_surface_rect = backpack_surface.get_rect(center=(670, 410))
    screen.blit(backpack_surface, backpack_surface_rect)

    equip_surface = pygame.Surface((420, 550))
    equip_surface.fill('white')
    equip_surface.set_alpha(150)
    equip_surface_rect = equip_surface.get_rect(center=(230, 410))
    screen.blit(equip_surface, equip_surface_rect)

    back_button = Button('graphic/botton1.png', 100, 80, 0.6, "<<")
    back_button.draw(screen)

    # Draw slots
    for slot in backpack_slots:
        slot.draw(screen)
    
    for slot in equip_slots:
        slot.draw(screen)

    # Draw selected item
    if selected_item:
        screen.blit(selected_item.image, selected_item.rect.topleft)
        info = Info(50, 335, selected_item.info)
        info.draw_info(screen)

    # Draw stats
    Hp, Def, Atk, Spd, Mag = stats.split('/')
    default_info = Info(50, 150, f'Hp={Hp}\nDef={Def}\nAtk={Atk}\nSpd={Spd}')
    default_info.draw_info(screen)
    
    pygame.display.flip()

def update_stats(base_stats, equips):
    Hp, Def, Atk, Spd, Mag = [int(stat) for stat in base_stats.split('/')]
    for item in equips:
        for stat, value in item.stats.items():
            if stat == 'Hp':
                Hp += value
            elif stat == 'Def':
                Def += value
            elif stat == 'Atk':
                Atk += value
            elif stat == 'Spd':
                Spd += value
            elif stat == 'Mag':
                Mag += value
    return f"{Hp}/{Def}/{Atk}/{Spd}/{Mag}"

def backpack(username, lvl, coin, pull, chicky, equip, stats):
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    clock = pygame.time.Clock()

    selected_item = None
    offset_x, offset_y = None, None

    backpack_slots = create_slots(BACKPACK_ROWS, BACKPACK_COLS, BACKPACK_X_OFFSET, BACKPACK_Y_OFFSET, SLOT_SIZE, SLOT_X_GAP, SLOT_Y_GAP)
    equip_slots = [Slot(x, y, SLOT_SIZE, SLOT_SIZE) for x, y in EQUIP_SLOT_COORDS]

    equipments_list = load_user_backpack(username)
    items_list = [item for item in equipments_list if item not in equip.split('/')]
    equips_list = [item for item in equipments_list if item in equip.split('/')]

    items = load_item_details(items_list)
    equips = load_item_details(equips_list)

    for i, item in enumerate(items):
        if i < len(backpack_slots):
            backpack_slots[i].item = item

    for n, equip1 in enumerate(equips):
        if n < len(equip_slots):
            equip_slots[n].item = equip1

    while True:
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
                        slot.item = None
                        items.remove(selected_item)
                        break

                for slot in equip_slots:
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        slot.item = None
                        equips.remove(selected_item)
                        break

                #if back_button.check_input(pos_mouse):
                    # Call the lobby function here
                    #pass

            elif event.type == pygame.MOUSEMOTION and selected_item:
                selected_item.rect.x = pos_mouse[0] + offset_x
                selected_item.rect.y = pos_mouse[1] + offset_y

            elif event.type == pygame.MOUSEBUTTONUP and selected_item:
                for slot in backpack_slots + equip_slots:
                    if slot.rect.collidepoint(pos_mouse) and not slot.item:
                        slot.item = selected_item
                        if slot in equip_slots:
                            equips.append(selected_item)
                        else:
                            items.append(selected_item)
                        selected_item = None
                        offset_x, offset_y = None, None
                        stats = update_stats(stats, equips)
                        break

        draw_ui(screen, coin, stats, backpack_slots, equip_slots, selected_item)
        clock.tick(FPS)

if __name__ == "__main__":
    # Sample data for testing
    username = "my"
    lvl = 1
    coin = 100
    pull = 0
    chicky = 0
    equip = "axe/shield3/helmet3"
    stats = "100/50/30/20/10"
    backpack(username, lvl, coin, pull, chicky, equip, stats)
