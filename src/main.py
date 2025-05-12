import pygame
from level import Level

pygame.init()

WIDTH, HEIGHT = 640, 480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
CLOCK = pygame.time.Clock()

level = Level()

running = True
while running:
    CLOCK.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    level.update(keys)
    level.draw(SCREEN)
    pygame.display.flip()

pygame.quit()