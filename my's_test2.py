import pygame
import sys
from backpack import Item, Slot, Info

pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 900, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Inventory System')

# Colors
WHITE = (255, 255, 255)

# Frame rate
clock = pygame.time.Clock()
FPS = 60

INVENTORY_ROWS = 5
INVENTORY_COLS = 3
SLOT_SIZE = 64
inventory_slots = []

# Create inventory slots
for row in range(INVENTORY_ROWS):
    for col in range(INVENTORY_COLS):
        x = 20 + col * (SLOT_SIZE + 10)
        y = 20 + row * (SLOT_SIZE + 10)
        inventory_slots.append(Slot(x, y, SLOT_SIZE, SLOT_SIZE))

# Create equip slots
equip_slots = {
    "sword": Slot(500, 20, SLOT_SIZE, SLOT_SIZE),
    "shield": Slot(500, 100, SLOT_SIZE, SLOT_SIZE),
    "helmet": Slot(600, 20, SLOT_SIZE, SLOT_SIZE),
    "armor": Slot(600, 100, SLOT_SIZE, SLOT_SIZE),
    "shoes": Slot(550, 180, SLOT_SIZE, SLOT_SIZE)
}

def display_info(surface, text, x, y):
    font = pygame.font.Font(None, 36)
    info_text = font.render(text, True, WHITE)
    surface.blit(info_text, (x, y))

items = [
    Item('Sword', 'graphic/sword.png', 'A sharp blade.', 0.4),
    Item('Shield', 'graphic/shield.png', 'A sturdy shield.', 0.4),
    Item('Helmet', 'graphic/helmet.png', 'A good helmet.', 0.4),
    Item('Armor', 'graphic/armor.png', 'A good armor.', 0.4),
    Item('Shoes', 'graphic/noob leg.png', 'A good shoes.', 0.4)
    # Add more items here
]

# Assign sample items to inventory slots
for i, item in enumerate(items):
    inventory_slots[i].item = item

def main():
    selected_item = None
    draging_item = None
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for slot in inventory_slots + list(equip_slots.values()):
                    for num, item in enumerate(items):
                        if slot.rect.collidepoint(pos) and slot.item:
                            selected_item = slot.item
                            draging_item = num
                            slot.item = None
                            break
                    
            elif event.type == pygame.MOUSEBUTTONUP:
                if selected_item:
                    pos = pygame.mouse.get_pos()
                    for slot in inventory_slots + list(equip_slots.values()):
                        if slot.rect.collidepoint(pos) and slot.item is None:
                            slot.item = selected_item
                            selected_item = None
                            draging_item = None
                            break
                    if selected_item:
                        for slot in inventory_slots:
                            if slot.item is None:
                                slot.item = selected_item
                                selected_item = None
                                break

        screen.fill('black')  # Clear the screen

        # Draw inventory slots and items
        for slot in inventory_slots:
            slot.draw(screen)
        
        # Draw equip slots and items
        for slot in equip_slots.values():
            slot.draw(screen)

        # Display item info
        if selected_item:
            display_info(screen, selected_item.info, 10, HEIGHT - 50)

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()