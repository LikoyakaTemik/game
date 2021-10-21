import pygame
pygame.init()
SIZE = (1500, 1500)
PINK = (255, 100, 160)
FPS = 60
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()
pudge = pygame.image.load("pudge.png")
x = y = 500
speed = 10
move_up = False
move_down = False
move_left = False
move_right = False
move_speed = False
is_game_on = True
move_slow = False
while(is_game_on):
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            is_game_on = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up = True
            if event.key == pygame.K_s:
                move_down = True
            if event.key == pygame.K_a:
                move_left = True
            if event.key == pygame.K_d:
                move_right = True
            if event.key == pygame.K_LSHIFT:
                move_speed = True
            if event.key == pygame.K_q:
                move_slow = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                move_up = False
            if event.key == pygame.K_s:
                move_down = False
            if event.key == pygame.K_a:
                move_left = False
            if event.key == pygame.K_d:
                move_right = False
            if event.key == pygame.K_LSHIFT:
                move_speed = False
            if event.key == pygame.K_q:
                move_slow = False
    if move_up == True:
        if(y - speed >= 400):
            y -= speed
    if move_down == True:
        if (y + speed <= 780):
            y += speed
    if move_right == True:
        if(x + speed <= 900):
            x += speed
    if move_left == True:
        if(x - speed >= 0):
            x -= speed
    if move_speed == True:
        speed = speed + 1
    if move_slow == True:
        if(speed - 1 > 0):
            speed = speed - 1

    sc.fill(PINK)
    sc.blit(pudge, (x, y))
    pygame.display.flip()
    clock.tick(FPS)

