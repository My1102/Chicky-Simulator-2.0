import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, name, image_path, info, scale):
        super().__init__()
        self.name = name
        image = pygame.image.load(image_path)
        width, height = image.get_size()
        self.image = pygame.transform.scale(image, (int(width*scale), int(height*scale)))
        self.rect = self.image.get_rect()
        self.info = info

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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
        self.info = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(info, True, 'black')
        self.pos_x = x
        self.pos_y = y
        # self.info_rect = self.info.get_rect(center=(self.pos_x, self.pos_y))

    def draw(self, screen):
        screen.blit(self.info, (self.pos_x, self.pos_y))