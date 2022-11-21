import pygame

class Hero:
    def __init__(self, x, y, v_speed, h_speed, pic):
        self.x = x
        self.y = y
        self.v_speed = v_speed
        self.h_speed = h_speed
        self.pic = pic

    def update(self):
        self.x = self.x + self.h_speed


pygame.init()
 
fps = 60
clock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
block_size = 64

snowman = pygame.image.load("SnowMan1_right.png")
snowman = pygame.transform.scale(snowman, (block_size, block_size))
enemy = pygame.image.load("stay_right.png")
enemy = pygame.transform.scale(enemy, (block_size, block_size))
block = pygame.image.load("mario_block.png")
block = pygame.transform.scale(block, (block_size, block_size))

hero = Hero(50, 50, 0, 1, snowman)

run = True
# Game loop.
while run:
    screen.fill((100, 255, 255))
    
    hero.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(hero.pic, (hero.x, hero.y))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()