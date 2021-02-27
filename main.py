import pygame
import random

pygame.init()
screen_width, screen_height = 700, 700
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Car Game")
running = True
player_color = (0, 200, 70)
enemy_color = (200, 70, 0)
x, y = screen_width / 2.25, screen_height-140
car_width, car_height = 70, 140
tyre_width, tyre_height = 20, 25
black = (40, 40, 40)
accelerating = 0
speed, acc = 0, 0.01
right, left = False, False
max_distance = 300
turn_speed = 0.7
en_x, en_y = [], []
en_speed = 0.25
num_en = 3
blacklist = []
for i in range(3):
    if i == 0:
        en_x.append(50)
    elif i == 1:
        en_x.append(300)
    elif i == 2:
        en_x.append(550)
    en_y.append(random.randint(-200, -50))

def game():
    global x, y, right, left, accelerating, speed, acc, max_distance, turn_speed, en_speed, num_en, screen_height, screen_width, start, running
    if accelerating == 1:
        if y >= screen_height - max_distance:
            y -= speed
        speed += acc

    if right == True:
        x += turn_speed
    if left == True:
        x -= turn_speed


    for i in range(num_en):
        en_y[i] += en_speed
        if en_y[i] >= 200 and i not in blacklist:
            en_x.append(en_x[i])
            en_y.append(random.randint(-200, -50))
            num_en += 1
            blacklist.append(i)

while running:
    screen.fill((140, 140, 140))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or event.key == pygame.K_UP:
                accelerating = 1
            elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                accelerating = -1
            elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                right = True
            elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                left = True
        if event.type == pygame.KEYUP:
            accelerating = 0
            right, left = False, False

    # drawing the player car
    player = pygame.draw.rect(screen, player_color, (x, y, car_width, car_height))

    pygame.draw.rect(screen, black, (x - tyre_width, y + 10, tyre_width, tyre_height))
    pygame.draw.rect(screen, black, (x + car_width, y + 10, tyre_width, tyre_height))
    pygame.draw.rect(screen, black, (x - tyre_width, y + car_height - tyre_height, tyre_width, tyre_height))
    pygame.draw.rect(screen, black, (x + car_width, y + car_height - tyre_height, tyre_width, tyre_height))

    # drawing enemy cars
    for i in range(num_en):
        en_rect = pygame.draw.rect(screen, enemy_color, (en_x[i], en_y[i], car_width, car_height))
        pygame.draw.rect(screen, black, (en_x[i] - tyre_width, en_y[i], tyre_width, tyre_height))
        pygame.draw.rect(screen, black, (en_x[i] + car_width, en_y[i], tyre_width, tyre_height))
        pygame.draw.rect(screen, black, (en_x[i] - tyre_width, en_y[i] + car_height - tyre_height - 10, tyre_width, tyre_height))
        pygame.draw.rect(screen, black, (en_x[i] + car_width, en_y[i] + car_height - tyre_height - 10, tyre_width, tyre_height))

    # game over
        if player.colliderect(en_rect) == True:
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                font = pygame.font.Font('freesansbold.ttf', 70)
                text = font.render("Game Over!", True, (255, 0, 0), (0, 0, 0))
                textRect = text.get_rect()
                textRect.center = (screen_width / 2, screen_height / 2)
                screen.blit(text, textRect)
                pygame.display.flip()

    game()
    pygame.display.flip()

pygame.quit()
