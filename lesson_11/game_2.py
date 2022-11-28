import pygame
import time
 
pygame.init()

class Figure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = (225, 212, 100)

    def update(self):
        self.y += block_size


fps = 60
clock = pygame.time.Clock()
 
width, height = 320, 480
screen = pygame.display.set_mode((width, height))

#game settings
block_size = 32
margin = block_size * 0
figure_types = {"type_1": []}
shapes = [
    [(0, 0), (0, 1), (1, 1), (1, 2)],
    [(0, 0), (0, 1), (1, 0), (1, 1)],
    [(0, 0), (0, 1), (0, 2), (0, 3)],
]

figure = Figure(3 * block_size, 64)
new_figure = False
busy_coords = []
start = time.time()
run = True
# Game loop.
while run:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if new_figure:
        figure = Figure(3 * block_size, 64)
        shape = [(0, 0), (0, 1), (1, 0), (1, 1)]
        new_figure = False
    if time.time() - start > 0.1:
        figure.update()
        start = time.time()
    for t in shape:
        pygame.draw.rect(screen, figure.color, (figure.x + t[0] * block_size, figure.y + t[1] * block_size, block_size, block_size))
    for t in shape:
        if figure.y // block_size + t[1] == height // block_size - 1:
            new_busy_coords = [(figure.x + c[0] * block_size, figure.y + c[1] * block_size) for c in shape]
            busy_coords.extend(new_busy_coords)
            new_figure = True
            break
    for c in busy_coords:
        pygame.draw.rect(screen, (0, 0, 0), (c[0], c[1], block_size, block_size))
    for i in range(height // block_size):
        pygame.draw.line(screen, (0, 0, 0), (margin, i * block_size), (width - margin, i * block_size))
    for i in range(margin // block_size, (width - margin) // block_size + 1):
        pygame.draw.line(screen, (0, 0, 0), (i * block_size, 0), (i * block_size, height))
    pygame.display.flip()
    clock.tick(fps)
         
         
pygame.quit()