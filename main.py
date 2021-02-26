import pygame
pygame.init()
screen_width, screen_height = 700, 700
screen = pygame.display.set_mode((screen_width, screen_height))
running = True
player_color = (0, 200, 70)
x, y = screen_width/2.25, screen_height
tyre_width, tyre_height = 20, 25
black = (40, 40, 40)
accelerating = 0
speed, acc = 0, 0.01
right, left = False, False
max_distance = 150
turn_speed = 1

def game():
	global x, y, right, left, accelerating, speed, acc, max_distance, turn_speed
	if accelerating == 1:
		if y >= screen_height-max_distance:
			y -= speed
		speed += acc
	elif accelerating == -1:
		if y >= screen_height-max_distance:
			y -= speed
		if speed > 0:
			speed -= acc
	elif accelerating == 0:
		if y >= screen_height-max_distance:
			y -= speed
		if speed > 0:
			speed -= acc/2
			
	if right == True:
		x += turn_speed
	if left == True:
		x -= turn_speed

while running:
	screen.fill((140, 140, 140))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				accelerating = 1
			elif event.key == pygame.K_s:
				accelerating = -1
			elif event.key == pygame.K_d:
				right = True
			elif event.key == pygame.K_a:
				left = True
		if event.type == pygame.KEYUP:
			accelerating = 0
			right, left = False, False

	#drawing the car
	pygame.draw.rect(screen, player_color, (x, y, 70, 140))
	
	pygame.draw.rect(screen, black,(x-tyre_width, y+10, tyre_width, tyre_height))
	pygame.draw.rect(screen, black, (x+70, y+10, tyre_width, tyre_height))
	pygame.draw.rect(screen, black, (x-tyre_width, y+140-tyre_height, tyre_width, tyre_height))
	pygame.draw.rect(screen, black, (x+70, y+140-tyre_height, tyre_width, tyre_height))
	
	game()
	pygame.display.flip()
	
pygame.quit()
