import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Inventory System")

class Item:
    def __init__(self, name, description, image, item_type):
        self.name = name
        self.description = description
        self.image = pygame.image.load(image)
        self.type = item_type  # e.g., "sword", "shield", "helmet", "armor", "shoes"
        self.rect = self.image.get_rect()

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

def draw_inventory(screen, inventory, selected_item=None):
    x, y = 50, 50
    for item in inventory.items:
        screen.blit(item.image, (x, y))
        if item == selected_item:
            pygame.draw.rect(screen, (255, 255, 0), (x, y, 64, 64), 3)  # Highlight selected item
        x += 70  # Move to the next slot

def draw_item_info(screen, item):
    font = pygame.font.Font(None, 36)
    text = font.render(item.name, True, (255, 255, 255))
    screen.blit(text, (50, 500))
    description = font.render(item.description, True, (255, 255, 255))
    screen.blit(description, (50, 540))

class EquipSlot:
    def __init__(self, x, y, item_type):
        self.rect = pygame.Rect(x, y, 64, 64)
        self.item = None
        self.type = item_type

# Define equip slots
equip_slots = {
    "sword": EquipSlot(700, 50, "sword"),
    "shield": EquipSlot(700, 130, "shield"),
    "helmet": EquipSlot(700, 210, "helmet"),
    "armor": EquipSlot(700, 290, "armor"),
    "shoes": EquipSlot(700, 370, "shoes")
}

selected_item = None
dragging_item = None
offset_x = 0
offset_y = 0

def handle_mouse_event(event, inventory):
    global selected_item, dragging_item, offset_x, offset_y
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = 50, 50
        for item in inventory.items:
            item.rect.topleft = (x, y)
            if item.rect.collidepoint(event.pos):
                selected_item = item
                dragging_item = item
                offset_x = item.rect.x - event.pos[0]
                offset_y = item.rect.y - event.pos[1]
            x += 70
    elif event.type == pygame.MOUSEBUTTONUP:
        if dragging_item:
            for slot in equip_slots.values():
                if slot.rect.collidepoint(event.pos) and slot.type == dragging_item.type:
                    slot.item = dragging_item
                    inventory.remove_item(dragging_item)
            dragging_item = None
    elif event.type == pygame.MOUSEMOTION:
        if dragging_item:
            dragging_item.rect.x = event.pos[0] + offset_x
            dragging_item.rect.y = event.pos

# Load images
sword_image = "graphic/sword.png"
shield_image = "graphic/shield.png"
item_type1 = 'sword'
item_type2 = 'shield'

# Create items
sword = Item("Sword", "A sharp blade.", sword_image, item_type1)
shield = Item("Shield", "A sturdy shield.", shield_image, item_type1)

# Create an inventory and add items
inventory = Inventory()
inventory.add_item(sword)
inventory.add_item(shield)

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handle_mouse_event(event, inventory)

    screen.fill((30, 30, 30))  # Fill the screen with a dark color
    draw_inventory(screen, inventory, selected_item)
    if selected_item:
        draw_item_info(screen, selected_item)
    pygame.display.flip()

pygame.quit()
sys.exit()