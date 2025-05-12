import pygame
import os

TILE_SIZE = 32
ANIMATION_SPEED = 0.60  # Semakin kecil, semakin cepat

class Player(pygame.sprite.Sprite):
    def __init__(self, assets_dir, start_pos=(5 * TILE_SIZE, 5 * TILE_SIZE)):
        super().__init__()
        self.images = {
            "down": self.load_direction_images(os.path.join(assets_dir, "Knight_10_Walk_Down.png")),
            "up": self.load_direction_images(os.path.join(assets_dir, "Knight_10_Walk_Up.png")),
            "left": self.load_direction_images(os.path.join(assets_dir, "Knight_10_Walk_Left.png")),
            "right": self.load_direction_images(os.path.join(assets_dir, "Knight_10_Walk_Right.png")),
        }

        self.direction = "down"
        self.frame_index = 0
        self.image = self.images[self.direction][int(self.frame_index)]
        self.rect = self.image.get_rect(topleft=start_pos)

        self.speed = 2

    def load_direction_images(self, path):
        sheet = pygame.image.load(path).convert_alpha()
        frames = []
        for i in range(sheet.get_width() // TILE_SIZE):
            frame = sheet.subsurface((i * TILE_SIZE, 0, TILE_SIZE, TILE_SIZE))
            frames.append(frame)
        return frames

    def update(self, keys):
        dx = dy = 0

        if keys[pygame.K_LEFT]:
            dx = -self.speed
            self.direction = "left"
        elif keys[pygame.K_RIGHT]:
            dx = self.speed
            self.direction = "right"
        elif keys[pygame.K_UP]:
            dy = -self.speed
            self.direction = "up"
        elif keys[pygame.K_DOWN]:
            dy = self.speed
            self.direction = "down"

        # Perbarui posisi
        self.rect.x += dx
        self.rect.y += dy

        # Animasi jika bergerak
        if dx != 0 or dy != 0:
            self.frame_index += ANIMATION_SPEED
            if self.frame_index >= len(self.images[self.direction]):
                self.frame_index = 0
        else:
            self.frame_index = 0  # reset ke frame awal saat diam

        self.image = self.images[self.direction][int(self.frame_index)]
