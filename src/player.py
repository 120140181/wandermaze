import pygame
import os

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, tile_size):
        super().__init__()
        self.tile_size = tile_size
        self.x = x * tile_size
        self.y = y * tile_size
        self.speed = 2
        self.direction = 'down'
        self.anim_index = 0
        self.anim_timer = 0
        self.anim_delay = 100  # in milliseconds

        self.load_images()
        self.image = self.animations[self.direction][0]
        self.rect = self.image.get_rect(topleft=(self.x, self.y))

    def load_images(self):
        base_path = "assets/images/Characters"
        directions = ['down', 'up', 'left', 'right']
        files = {
            'down': 'Knight_10_Walk_Down.png',
            'up': 'Knight_10_Walk_Up.png',
            'left': 'Knight_10_Walk_Left.png',
            'right': 'Knight_10_Walk_Right.png',
        }

        self.animations = {}

        for dir in directions:
            sheet = pygame.image.load(os.path.join(base_path, files[dir])).convert_alpha()
            frames = []
            for i in range(4):
                frame = sheet.subsurface((i * self.tile_size, 0, self.tile_size, self.tile_size))
                frames.append(frame)
            self.animations[dir] = frames

    def handle_input(self, keys):
        moved = False
        if keys[pygame.K_LEFT]:
            self.x -= self.speed
            self.direction = 'left'
            moved = True
        elif keys[pygame.K_RIGHT]:
            self.x += self.speed
            self.direction = 'right'
            moved = True
        elif keys[pygame.K_UP]:
            self.y -= self.speed
            self.direction = 'up'
            moved = True
        elif keys[pygame.K_DOWN]:
            self.y += self.speed
            self.direction = 'down'
            moved = True

        self.rect.topleft = (self.x, self.y)

        # Animasi hanya aktif jika bergerak
        now = pygame.time.get_ticks()
        if moved:
            if now - self.anim_timer > self.anim_delay:
                self.anim_timer = now
                self.anim_index = (self.anim_index + 1) % len(self.animations[self.direction])
        else:
            self.anim_index = 0  # diam = frame 0

        self.image = self.animations[self.direction][self.anim_index]

    def draw(self, surface):
        surface.blit(self.image, (self.x, self.y))
