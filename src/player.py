import pygame
from utils import split_spritesheet

TILE_SIZE = 32

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spritesheet):
        super().__init__()
        self.frames = split_spritesheet(spritesheet, TILE_SIZE, TILE_SIZE)
        self.image = self.frames[0]
        self.rect = self.image.get_rect(topleft=(x, y))

        self.pos = pygame.Vector2(x, y)
        self.speed = 2
        self.direction = pygame.Vector2(0, 0)

        self.reversed = False
        self.reversed_timer = 0
        self.checkpoint = self.pos.copy()

    def update(self, keys, dt):
        self.direction.x = 0
        self.direction.y = 0

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1

        if self.reversed:
            self.direction *= -1
            self.reversed_timer -= dt
            if self.reversed_timer <= 0:
                self.reversed = False

        self.pos += self.direction * self.speed
        self.rect.topleft = self.pos

    def teleport_to_start(self):
        self.pos = pygame.Vector2(0, 0)
        self.rect.topleft = self.pos

    def reverse_controls(self, temporary=False):
        self.reversed = True
        if temporary:
            self.reversed_timer = 3000  # in milliseconds

    def set_checkpoint(self, pos):
        self.checkpoint = pygame.Vector2(pos)

    def reset_to_checkpoint(self):
        self.pos = self.checkpoint.copy()
        self.rect.topleft = self.pos
