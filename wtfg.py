import pygame
import sys

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 700
FPS = 60
SLOT_SIZE = 100
BACKPACK_ROWS, BACKPACK_COLS = 5, 3
BACKGROUND_COLOR = (30, 30, 30)
TEXT_COLOR = (255, 255, 255)

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Inventory System')
clock = pygame.time.Clock()

class Slot:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect, 2)
        if self.item:
            surface.blit(self.item.image, self.rect)

class Item:
    def __init__(self, name, image_path):
        self.name = name
        self.image = pygame.transform.scale(pygame.image.load(image_path), (SLOT_SIZE, SLOT_SIZE))
        self.rect = self.image.get_rect()

def create_slots(rows, cols, start_x, start_y, slot_size, margin_x, margin_y):
    slots = []
    for row in range(rows):
        for col in range(cols):
            x = start_x + col * (slot_size + margin_x)
            y = start_y + row * (slot_size + margin_y)
            slots.append(Slot(x, y, slot_size, slot_size))
    return slots

# Create backpack slots
backpack_slots = create_slots(BACKPACK_ROWS, BACKPACK_COLS, 495, 140, SLOT_SIZE, 25, 10)

# Create equipment slots
equip_slots = {
    "sword": Slot(105, 430, SLOT_SIZE, SLOT_SIZE),
    "shield": Slot(255, 430, SLOT_SIZE, SLOT_SIZE),
    "helmet": Slot(30, 550, SLOT_SIZE, SLOT_SIZE),
    "armor": Slot(180, 550, SLOT_SIZE, SLOT_SIZE),
    "shoes": Slot(330, 550, SLOT_SIZE, SLOT_SIZE)
}

# Create items
items = [
    Item('Sword', 'graphic/sword.png'),
    Item('Shield', 'graphic/shield.png'),
    Item('Helmet', 'graphic/helmet.png'),
    Item('Armor', 'graphic/armor.png'),
    Item('Shoes', 'graphic/noob leg.png')
]

# Place initial items in backpack slots
for i, item in enumerate(items):
    backpack_slots[i].item = item

def draw_text(surface, text, size, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, TEXT_COLOR)
    text_rect = text_surface.get_rect(center=(x, y))
    surface.blit(text_surface, text_rect)

def inventory(username, lvl, coin, pull):
    selected_item = None
    offset_x, offset_y = None, None

    running = True
    while running:
        screen.fill(BACKGROUND_COLOR)
        pos_mouse = pygame.mouse.get_pos()
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for slot in backpack_slots + list(equip_slots.values()):
                    if slot.rect.collidepoint(pos_mouse) and slot.item:
                        selected_item = slot.item
                        #offset_x = pos_mouse[0]
                        #offset_y = pos_mouse[1]
                        offset_x = slot.rect.x - pos_mouse[0]
                        offset_y = slot.rect.y - pos_mouse[1]
                        selected_item.rect.x = pos_mouse[0] + offset_x
                        selected_item.rect.y = pos_mouse[1] + offset_y
                        print(pos_mouse)
                        print(selected_item.rect.x, selected_item.rect.y)
                        slot.item = None
                        break

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
                    if selected_item:  # If item wasn't placed, return it to a backpack slot
                        for slot in backpack_slots:
                            if slot.item is None:
                                slot.item = selected_item
                                selected_item = None
                                offset_x, offset_y = None, None
                                break

        # Draw slots and items
        for slot in backpack_slots:
            slot.draw(screen)
        for slot in equip_slots.values():
            slot.draw(screen)

        # Draw selected item
        if selected_item:
            screen.blit(selected_item.image, selected_item.rect.topleft)

        # Draw UI text
        draw_text(screen, 'Backpack', 50, 670, 80)
        draw_text(screen, 'Equipment', 50, 230, 80)
        draw_text(screen, f'Coins: {coin}', 30, 780, 80)
        draw_text(screen, 'Back', 30, 100, 80)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

# Example usage
inventory('player1', 1, 100, 0)