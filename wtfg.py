import pygame
import sys

class Slot:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect, 2)
        if self.item:
            screen.blit(self.item.image, self.rect.topleft)

class Item:
    def __init__(self, image_path, info, scale):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.info = info

class Button:
    def __init__(self, image_path, x, y, scale, text):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect(center=(x, y))
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.text_surf = self.font.render(text, True, 'white')
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
        screen.blit(self.text_surf, self.text_rect.topleft)

    def check_input(self, pos):
        return self.rect.collidepoint(pos)

class Info:
    def __init__(self, x, y, info_text):
        self.x = x
        self.y = y
        self.info_text = info_text
        self.font = pygame.font.Font(None, 36)

    def draw_info(self, screen):
        lines = self.info_text.split('\n')
        for i, line in enumerate(lines):
            text_surf = self.font.render(line, True, 'white')
            screen.blit(text_surf, (self.x, self.y + i * 40))

def backpack(username, lvl, coin, pull):
    pygame.init()
    screen = pygame.display.set_mode((900, 700))
    clock = pygame.time.Clock()

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
        for line in lines:
            user_backpack = line.strip().split(", ")
            if user_backpack[0] == username:
                equipment_list = user_backpack[2].split('/')
                break
    print(f"Equipment List for {username}: {equipment_list}")

    items = []
    with open('equipment_details.txt', 'r') as file2:
        lines = file2.readlines()
        for line in lines:
            item_details = line.strip().split(", ")
            if item_details[0] in equipment_list:
                item_graphic = (f'{item_details[1]}')
                item_info = (f'{item_details[2]}\n{item_details[3]}')
                item = Item(item_graphic, item_info, 0.65)
                items.append(item)

    for i, item in enumerate(items):
        if i < len(backpack_slots):
            backpack_slots[i].item = item

    while True:
        screen.fill((0, 0, 0))
        pygame.display.set_caption('Chicky Simulator - Backpack')

        backpack_text = pygame.font.Font(None, 100).render('Backpack', True, 'white')
        backpack_text_rect = backpack_text.get_rect(center=(450, 80))
        screen.blit(backpack_text, backpack_text_rect)

        coinlogo = pygame.image.load('graphic/manycoin.png')
        coinlogo = pygame.transform.scale(coinlogo, (int(coinlogo.get_width() * 0.3), int(coinlogo.get_height() * 0.3)))
        screen.blit(coinlogo, (700, 80))

        coin_text = pygame.font.Font(None, 50).render(f'{coin}', True, 'white')
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

        pos_mouse = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                for slot in backpack_slots + list(equip_slots.values()):
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        selected_item.rect.x = pos_mouse[0] + offset_x
                        selected_item.rect.y = pos_mouse[1] + offset_y
                        slot.item = None
                        break

                if back_button.check_input(pos_mouse):
                    return # Replace with call to your lobby function: lobby(username, lvl, coin, pull)

            elif event.type == pygame.MOUSEMOTION:
                if selected_item:
                    selected_item.rect.x = pos_mouse[0] + offset_x
                    selected_item.rect.y = pos_mouse[1] + offset_y

            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_item:
                    for slot in backpack_slots + list(equip_slots.values()):
                        if slot.rect.collidepoint(pos_mouse) and slot.item is None:
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

        if selected_item:
            screen.blit(selected_item.image, selected_item.rect.topleft)
            info = Info(50, 320, selected_item.info)
            info.draw_info(screen)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    backpack('my', 1, 100, 1)  # Example call to the backpack function