# modify from button library
# time = steps
import pygame

class Ranking():
    # set the parameter
    def __init__(self, y, place, username, time):
        self.pos_y = y
        self.place = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(place, True, 'black')
        self.place_rect = (150, self.pos_y)
        self.name = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(username, True, 'black')
        self.name_rect = (230, self.pos_y)
        self.time = pygame.font.Font("ThaleahFat/ThaleahFat.ttf", 50).render(f'{time} steps', True, 'black')
        self.time_rect = (550, self.pos_y)

    # use to display
    def show(self, screen):
        screen.blit(self.place, self.place_rect)
        screen.blit(self.name, self.name_rect)
        screen.blit(self.time, self.time_rect)
