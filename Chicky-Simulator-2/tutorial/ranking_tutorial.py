# this one is from chatgpt

import pygame
import sys
import pygame_gui

pygame.init()

width, height = 900, 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Chicky Simulator')
ranking_image = pygame.image.load('graphic/garden.png')
clock = pygame.time.Clock()
Manager = pygame_gui.UIManager((width, height))
UI_REFRESH_RATE = clock.tick(60) / 1000

# Sample ranking data (score, player_name)
ranking_data = [
    (100, 'Player1'),
    (80, 'Player2'),
    (60, 'Player3'),
    (40, 'Player4'),
    (20, 'Player5'),
]

def draw_ranking():
    screen.blit(ranking_image, (0, 0))

    ranking_surface = pygame.Surface((700, 400))
    ranking_surface.fill('white')

    # Display the ranking data on the surface
    font = pygame.font.Font(None, 36)
    for i, (score, player_name) in enumerate(ranking_data, start=1):
        text = font.render(f'{i}. {player_name}: {score}', True, pygame.Color('black'))
        ranking_surface.blit(text, (20, 20 * i))

    # Calculate the position to center the surface on the screen
    x_pos = (width - ranking_surface.get_width()) / 2
    y_pos = 200
    screen.blit(ranking_surface, (x_pos, y_pos))

def ranking():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            Manager.process_events(event)

        Manager.update(UI_REFRESH_RATE)

        draw_ranking()

        pygame.display.update()

ranking()