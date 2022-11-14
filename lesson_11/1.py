import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()

# game settings
block_size = 64

width, height = 640, 800
screen = pygame.display.set_mode((width, height))

snowman = pygame.image.load("SnowMan1_right.png")
snowman = pygame.transform.scale(snowman, (block_size, block_size))

hero_x = 50
hero_y = 50
h_speed = 4
v_speed = 0
g = 2
ground = 700
can_jump = False

run = True
# Game loop.
while run:
    screen.fill((50, 210, 190))
    keystate = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and can_jump == True:
                v_speed = v_speed - 25
                can_jump = False

    if keystate[pygame.K_RIGHT] == True:
        hero_x = hero_x + h_speed
    if keystate[pygame.K_LEFT] == True:
        hero_x = hero_x - h_speed
    if hero_x > width:
        hero_x = -block_size
    elif hero_x < -block_size:
        hero_x = width

    v_speed = v_speed + g
    hero_y = hero_y + v_speed
    if hero_y >= ground:
        hero_y = ground
        v_speed = 0
        can_jump = True
    # if hero_y > height:
    #     hero_y = -block_size
    screen.blit(snowman, (hero_x, hero_y))
    pygame.display.flip()
    clock.tick(fps)
pygame.quit()