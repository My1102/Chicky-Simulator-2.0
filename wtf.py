import pygame,random

pygame.init()

#game window

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 450

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("Dragging and Dropping")

active_box = None
boxes = []
for i in range(5):
    x = random.randint(50,700)
    y = random.randint(50, 350)
    w = random.randint(35,75)
    h = random.randint(35,65)
    box = pygame.Rect(x,y,w,h)
    boxes.append(box)

run = True
while run:
    screen.fill("turquoise1")

    for box in boxes:
        pygame.draw.rect(screen,"purple",box)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                for num,box in enumerate(boxes):
                    if box.collidepoint(event.pos):
                        active_box = num
        if event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                active_box = None
        if event.type == pygame.MOUSEMOTION:
            if active_box != None:
                boxes[active_box].move_ip(event.rel)
        
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()