import pygame
 
pygame.init()
 
fps = 60
clock = pygame.time.Clock()

# game settings
block_size = 64

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

snowman = pygame.image.load("SnowMan1_right.png")
snowman = pygame.transform.scale(snowman, (block_size, block_size))

hero_x = 50
hero_y = 50

run = True
# Game loop.
while run:
    screen.fill((50, 210, 190))
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if hero_x > width:
        hero_x = -block_size
    else:
        hero_x = hero_x + 4
    screen.blit(snowman, (hero_x, hero_y))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()