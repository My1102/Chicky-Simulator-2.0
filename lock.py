# modify from button library
import pygame

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