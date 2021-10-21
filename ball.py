import pygame

pygame.init()

SIZE = (700, 500)
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
sc = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

x_r = y_r = 250
r = 20
speed_x = 5
speed_y = 5
x_p = 200
y_p = 400
w_p = 100
h_p = 50
left = False
right = False

is_going = True
while is_going:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_going = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                left = True
            if event.key == pygame.K_a:
                right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                left = False
            if event.key == pygame.K_a:
                right = False

    if left and x_p + w_p <= SIZE[0]:
        x_p += 5
    if right and x_p >= 0:
        x_p -= 5

    x_r += speed_x
    y_r += speed_y
    if x_r - r <= 0 or x_r + r >= SIZE[0]:
        speed_x = -speed_x
    if y_r - r <= 0 or y_r + r >= SIZE[1]:
        speed_y = -speed_y
    if x_r >= x_p and x_r <= x_p + w_p and y_r < y_p and x_r + r >= x_p and x_r - r <= x_p + w_p and y_r + r >= y_p and y_r + r <= y_p + h_p / 2:
        speed_y = -speed_y
    if x_r >= x_p and x_r <= x_p + w_p and y_r > y_p and x_r + r >= x_p and x_r - r <= x_p + w_p and y_r + r <= y_p + h_p and y_r + r >= y_p + h_p / 2:
        speed_y = -speed_y
    #if y_r > y_p and x_r + r <= x_p + w_p:
     #   speed_x = -speed_x
    #if y_r > y_p and x_r + r >= x_p:
      #  speed_x = -speed_x
    sc.fill(WHITE)
    pygame.draw.circle(sc, BLACK, (x_r, y_r), r)
    pygame.draw.rect(sc, BLACK, (x_p, y_p, w_p, h_p))
    pygame.display.flip()
    clock.tick(FPS)