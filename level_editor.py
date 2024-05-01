import pygame
import pickle

from os import path


pygame.init()

clock = pygame.time.Clock()
fps = 60

#game window
tile_size = 35
cols = 20
margin = 100
screen_width = tile_size * cols
screen_height = (tile_size * cols) + margin

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Level Editor')


#load images

bg_img = pygame.image.load('graphic/map.jpg')
bg_img = pygame.transform.scale(bg_img, (screen_width, screen_height - margin))
block_img = pygame.image.load('graphic/block.png')

mon1_img = pygame.image.load('graphic/monster1.png')
mon2_img = pygame.image.load('graphic/monster2.png')
mon3_img = pygame.image.load('graphic/monster3.png')
# platform_x_img = pygame.image.load('img/platform_x.png')
# platform_y_img = pygame.image.load('img/platform_y.png')
# lava_img = pygame.image.load('img/lava.png')
coin_img = pygame.image.load('graphic/coin.png')
exit_img = pygame.image.load('graphic/bananacat.png')
save_img = pygame.image.load('graphic/84297.png')
save_img = pygame.transform.scale(save_img,(50,50))
load_img = pygame.image.load('graphic/load.png')
load_img = pygame.transform.scale(load_img,(50,50))


#define game variables
clicked = False
level = 1

#define colours
white = (255, 255, 255)
green = (144, 201, 120)
darkgreen = (0,100,0)

font = pygame.font.SysFont('Futura', 24)

#create empty tile list
world_data = []
for row in range(20):
	r = [0] * 20
	world_data.append(r)

#create boundary
for tile in range(0, 20):
	world_data[19][tile] = 1
	world_data[0][tile] = 1
	world_data[tile][0] = 1
	world_data[tile][19] = 1

#function for outputting text onto the screen
def draw_text(text, font, text_col, x, y):
	img = font.render(text, True, text_col)
	screen.blit(img, (x, y))

def draw_grid():
	for c in range(21):
		#vertical lines
		pygame.draw.line(screen, darkgreen, (c * tile_size, 0), (c * tile_size, screen_height - margin))
		#horizontal lines
		pygame.draw.line(screen, darkgreen, (0, c * tile_size), (screen_width, c * tile_size))


def draw_world():
	for row in range(20):
		for col in range(20):
			if world_data[row][col] > 0:
				if world_data[row][col] == 1:
					#blocks
					img = pygame.transform.scale(block_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))
				if world_data[row][col] == 2:
					img = pygame.transform.scale(coin_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size ))
				if world_data[row][col] == 3:
					img = pygame.transform.scale(mon1_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size ))
				if world_data[row][col] == 4:
					img = pygame.transform.scale(mon2_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size ))
				if world_data[row][col] == 5:
					img = pygame.transform.scale(mon3_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size ))
				if world_data[row][col] == 6:
					#exit
					img = pygame.transform.scale(exit_img, (tile_size, tile_size))
					screen.blit(img, (col * tile_size, row * tile_size))

#load and save buttons
class Button():
	def __init__(self, x, y, image):
		self.image = image
		self.rect = self.image.get_rect()
		self.rect.topleft = (x, y)
		self.clicked = False

	def draw(self):
		action = False

		#get mouse position
		pos = pygame.mouse.get_pos()

		#check mouseover and clicked conditions
		if self.rect.collidepoint(pos):
			if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
				action = True
				self.clicked = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.clicked = False

		#draw button
		screen.blit(self.image, (self.rect.x, self.rect.y))

		return action
	
save_button = Button(screen_width // 2 - 150, screen_height - 80, save_img)
load_button = Button(screen_width // 2 + 50, screen_height - 80, load_img)

#main game loop
run = True
while run:

	clock.tick(fps)

	#draw background
	screen.fill(green)
	screen.blit(bg_img, (0, 0))
	# screen.blit(sun_img, (tile_size * 2, tile_size * 2))

	#load and save level
	if save_button.draw():
		#save level data
		pickle_out = open(f'level{level}_data', 'wb')
		pickle.dump(world_data, pickle_out)
		pickle_out.close()
	if load_button.draw():
		#load in level data
		if path.exists(f'level{level}_data'):
			pickle_in = open(f'level{level}_data', 'rb')
			world_data = pickle.load(pickle_in)


	#show the grid and draw the level tiles
	draw_grid()
	draw_world()


	#text showing current level
	draw_text(f'Level: {level}', font, white, tile_size, screen_height - 60)
	draw_text('Press UP or DOWN to change level', font, white, tile_size, screen_height - 40)

	#event handler
	for event in pygame.event.get():
		#quit game
		if event.type == pygame.QUIT:
			run = False
		#mouseclicks to change tiles
		if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
			clicked = True
			pos = pygame.mouse.get_pos()
			x = pos[0] // tile_size
			y = pos[1] // tile_size
			#check that the coordinates are within the tile area
			if x < 20 and y < 20:
				#update tile value
				if pygame.mouse.get_pressed()[0] == 1:
					world_data[y][x] += 1
					if world_data[y][x] > 8:
						world_data[y][x] = 0
				elif pygame.mouse.get_pressed()[2] == 1:
					world_data[y][x] -= 1
					if world_data[y][x] < 0:
						world_data[y][x] = 8
		if event.type == pygame.MOUSEBUTTONUP:
			clicked = False
		#up and down key presses to change level number
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				level += 1
			elif event.key == pygame.K_DOWN and level > 1:
				level -= 1

	#update game display window
	pygame.display.update()

pygame.quit()