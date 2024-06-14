import pygame

class Item():
    def __init__(self, graphic, item_type, info, stats, name, scale):
        self.image = pygame.image.load(graphic)
        self.image = pygame.transform.scale(self.image, (int(self.image.get_width() * scale), int(self.image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.type = item_type
        self.info = info
        self.name = name

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None

    def draw(self, screen):
        pygame.draw.rect(screen, 'black', self.rect, 4)
        if self.item:
            screen.blit(self.item.image, self.rect)

class Info():
    def __init__(self, x, y, info):
        self.info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 45).render(info, True, 'black')
        self.pos_x = x
        self.pos_y = y

    def draw_info(self, screen):
        screen.blit(self.info, (self.pos_x, self.pos_y))
        