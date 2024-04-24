# modify from 2 button tutoraial
import pygame

class Button():
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
        
