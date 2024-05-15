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

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Slot(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.item = None

    def draw(self, surface):
        pygame.draw.rect(surface, 'white', self.rect, 2)
        if self.item:
            surface.blit(self.item.image, self.rect)