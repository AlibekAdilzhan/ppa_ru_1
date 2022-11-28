import pygame
 
pygame.init()
pygame.font.init()
pygame.mixer.init()

# font object..................................
def create_font(t,s=36,c=(255,255,0), b=False,i=False):
    font = pygame.font.SysFont("Arial", s, bold=b, italic=i)
    text = font.render(t, True, c)
    return text
# Text to be rendered with create_font    
game_start_text = create_font("Please, press 's' to start")

fps = 60
clock = pygame.time.Clock()

jump_sound = pygame.mixer.Sound("sound_trampoline.wav")

# game settings
block_size = 64
map = [
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    "................................................................",
    ".............bbb.........................................................",
    "...........bbbbbbbb..bbb........................................",
    "bbbbb bb bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
    "................................................................",
]

width, height = 640, 800
screen = pygame.display.set_mode((width, height))

snowman_right = pygame.image.load("SnowMan1_right.png")
snowman_right = pygame.transform.scale(snowman_right, (block_size, block_size))
snowman_left = pygame.image.load("SnowMan1_left.png")
snowman_left = pygame.transform.scale(snowman_left, (block_size, block_size))
enemy = pygame.image.load("stay_right.png")
enemy = pygame.transform.scale(enemy, (block_size, block_size))
block = pygame.image.load("mario_block.png")
block = pygame.transform.scale(block, (block_size, block_size))

snowman = snowman_right

hero_x = 50
hero_y = 50
hero_x_old = hero_x
hero_y_old = hero_y
enemy_x = 300
enemy_y = 50
enemy_hp = 100
h_speed = 4
h_speed_enemy = 2
v_speed = 0
v_speed_enemy = 0
g = 2
ground = 700
can_jump = False
can_jump_enemy = False
camera_x = 0

hero_rect = pygame.Rect(hero_x, hero_y, 1 * block_size // 3, block_size)
enemy_rect = pygame.Rect(enemy_x, enemy_y, block_size, block_size)
enemy_is_dead = False
rects = []
for i in range(len(map)):
    for j in range(len(map[i])):
        if map[i][j] == "b":
            rect = pygame.Rect(j * block_size, i * block_size, block_size, block_size)
            rects.append(rect)

run = True
game_mod = "start"
run_1 = True
# Game loop.
while True:
    if game_mod == "start":
        music_menu = pygame.mixer.music.load("sound_Jingle_Bells.wav")
        pygame.mixer.music.play(-1)
        while run_1:
            screen.fill((50, 210, 190))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_s:
                        run_1 = False
                        game_mod = "game"
            screen.blit(game_start_text, (150, 200))
            pygame.display.flip()
            clock.tick(fps)
    elif game_mod == "game":  
        music = pygame.mixer.music.load("music_1.ogg")
        pygame.mixer.music.play(-1)
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
                        can_jump_enemy = False
                        pygame.mixer.Sound.play(jump_sound)

            hero_x_old = hero_x
            hero_y_old = hero_y
            if keystate[pygame.K_RIGHT] == True:
                hero_x = hero_x + h_speed
                snowman = snowman_right
            if keystate[pygame.K_LEFT] == True:
                hero_x = hero_x - h_speed
                snowman = snowman_left
            # if hero_x > width:
            #     hero_x = -block_size
            # elif hero_x < -block_size:
            #     hero_x = width
            if hero_x - camera_x >= width * 0.8:
                camera_x = camera_x + h_speed
            elif hero_x - camera_x <= width * 0.1:
                camera_x = camera_x - h_speed
            v_speed = v_speed + g
            v_speed_enemy = v_speed_enemy + g
            hero_y = hero_y + v_speed
            enemy_y = enemy_y + v_speed_enemy
            # if hero_y >= ground:
            #     hero_y = ground
            #     v_speed = 0
            #     can_jump = True
            if enemy_y >= ground:
                enemy_y = ground
                v_speed_enemy = 0
                can_jump_enemy = True
                
            if hero_x > enemy_x:
                enemy_x = enemy_x + h_speed_enemy
            else:
                enemy_x = enemy_x - h_speed_enemy
            hero_rect.x = hero_x
            hero_rect.y = hero_y
            if enemy_hp >= 0:
                enemy_rect.x = enemy_x
                enemy_rect.y = enemy_y
            for rect in rects:
                if hero_rect.colliderect(rect) == True and abs(hero_rect.y - rect.y) <= block_size // 2:
                    hero_x = hero_x_old
                if hero_rect.colliderect(rect) == True:
                    hero_y = rect.y - block_size
                    v_speed = 0
                    can_jump = True
                if enemy_hp >= 0 and enemy_rect.colliderect(rect) == True:
                    enemy_y = rect.y - block_size
                    v_speed_enemy = 0
                    can_jump_enemy = True
            if enemy_hp >= 0 and hero_rect.colliderect(enemy_rect) and enemy_rect.y - hero_rect.y <= block_size and abs(hero_rect.x - enemy_rect.x) < block_size // 3:
                hero_y = enemy_y - block_size
                enemy_hp = enemy_hp - 50 
                v_speed = v_speed - 25
            if hero_y >= 1000:
                hero_y = -block_size
            for i in range(len(map)):
                for j in range(len(map[i])):
                    if map[i][j] == "b":
                        screen.blit(block, (j * block_size - camera_x, i * block_size))
            if enemy_hp >= 0:
                screen.blit(enemy, (enemy_x - camera_x, enemy_y))
            elif enemy_is_dead == False:
                del enemy_rect
                enemy_is_dead = True
                # del enemy_x
                # del enemy_y
                # del enemy_hp
            screen.blit(snowman, (hero_x - camera_x, hero_y))
            pygame.display.flip()
            clock.tick(fps)
        pygame.quit()
    if run == False:
        break