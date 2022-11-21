import pygame

class Hero:
    def __init__(self, x, y, v_speed, h_speed, pic):
        self.x = x
        self.y = y
        self.v_speed = v_speed
        self.h_speed = h_speed
        self.pic = pic
        # self.can_jump = False

    def update(self):
        if keystate[pygame.K_RIGHT] == True:
            self.x = self.x + self.h_speed
        elif keystate[pygame.K_LEFT] == True:
            self.x = self.x - self.h_speed
        self.v_speed = self.v_speed + g
        self.y = self.y + self.v_speed
        if self.y >= ground:
            self.v_speed = 0
            self.y = ground    

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.v_speed = -20
            if event.type == pygame.QUIT:
                run = False


pygame.init()
 
fps = 60
clock = pygame.time.Clock()
 
# game settings
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
block_size = 64
g = 2
ground = 400

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
    
    keystate = pygame.key.get_pressed()
    hero.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    screen.blit(hero.pic, (hero.x, hero.y))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()